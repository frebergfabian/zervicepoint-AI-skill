# Plattform: tjänster, versioner, roller, sidor och API

Källor: AdminWeb-avsnitten ([tjänster](https://docs.zervicepoint.com/adminweb/services/), [delad process](https://docs.zervicepoint.com/adminweb/sharedprocess/), [roller](https://docs.zervicepoint.com/adminweb/roles/), [sidor](https://docs.zervicepoint.com/adminweb/pages/)), [drafts och versioner](https://docs.zervicepoint.com/how-to/how-to-work-with-draft/), [copy/paste mellan versioner](https://docs.zervicepoint.com/how-to/how-to-work-with-copied-service-and-process-json/), [arkitektur](https://docs.zervicepoint.com/system-overview/components/) och how-to-guiderna för PowerShell och REST. Genomgångna 2026-11-13.

## Komponenter

| Komponent | Roll |
| --- | --- |
| UserWeb | Portal för beställare, godkännare och utförare (IIS) |
| AdminWeb | Administration: tjänster, processer, roller, sidor och order |
| ClientWebService (CWS) | Kör datakällor och webservices åt formulären |
| ProvisioningSystemInventory | Inventerar datakällor |
| ProvisioningSystem | Inventerar och kör aktiviteter (PowerShell/.NET) |
| ProcessSystem (+ Process System Web) | Lägger och styr order och kör inbyggda aktiviteter |
| Motor | Workflow Manager + Service Bus (äldre) eller ZerFlow (1.35+) |
| SQL Server | Data, logiskt separerat per **store** (multitenant) |

I molnvarianten är **worker** samlingsnamnet för CWS, ProvisioningSystem och ProvisioningSystemInventory. Den installeras på kundens Windows Server och kräver DNS-post och TLS-certifikat för CWS samt token- och datasigneringscertifikat. Om en dropdown eller webservice inte svarar: kontrollera DNS, signeringscertifikat och den privata nyckeln först. Se [worker-hjälpen](https://docs.zervicepoint.com/onboarding/cloud-onboarding-worker-help/) och [Testmiljöer](environments.md).

## Tjänst

- **Catalog info:** identifierare, namn, kort och lång beskrivning, bild (rekommenderat PNG 720×480), kostnad och månadskostnad (läggs i `System.Order.Cost`/`MonthlyCost`), kvantitet, kundvagn, egen knapptext, Recommended, dölj galleri, dölj submit, sidor, taggar, ägare (`System.ServiceOwner.*`) och **Visible for roles**.
- Tom "Visible for roles" betyder synlig för alla inloggade.
- **Länkar** kan se ut som tjänster (1.25). Tjänster kan bäddas in på sidor (1.34.3987).

## Drafts och versioner (1.19+)

- **Save & Publish** skapar en ny publicerad version. Gamla versioner listas under Catalog info och kan öppnas och publiceras igen. Kommentar vid publicering från 1.23.2320 och vid draft från 1.34.5200.
- **Save as draft** skapar en parallell version. Den publicerade påverkas inte. Testa via "Show draft" i UserWeb. Rollerna **StoreAdministrator** och **ServiceReviewer** ser och kan beställa drafts. Draft kan kasseras (1.34.3799), och man kan växla mellan flera drafts (1.34.5200).
- **Save as copy** ger ny tjänst med ny identifierare, utan versionshistorik.
- Pågående order fortsätter på den version de startade med. Delade processer slår igenom direkt i alla länkade tjänster, så använd draft där.
- Kopiering av formulär och arbetsflöden mellan **olika** produktversioner är tillåten men inte garanterad, och från 1.34.5200 visas en varning. Mellan instanser med samma version är det säkert.

## Roller

- Tilldelas vid inloggning utifrån **regler** på token-claims (ADFS/Azure AD/OIDC) och **direkta medlemskap** (e-post, främst för test).
- Regel-JS: `return user.hasClaim('Group', 'Gruppnamn');`, kombinerbart med `||`/`&&`. `return true;` ger alla inloggade. `.Contains()` är utfasat sedan 1.9; använd `hasClaim`/`claimIncludes`.
- Roller styr synlighet för tjänster och sidor, filtrering i datakällor (`$config.roles`) och AdminWeb-behörighet.
- Systemroller: ApiStoreAdministrator, ArticleAdmin, OrderAdmin, PageAdmin, ProcessAdmin, RoleAdmin, ServiceAdmin (bara delade tjänster), ServiceReviewer (drafts), StoreAdministrator, TagAdmin och TranslationAdmin.
- Rollmedlemskap uppdateras vid ny inloggning. Logga ut och in efter regeländring.

## Sidor

Hierarkiska, med egen synlighet per roll. Sektionstyper: **Text block** (även instruktioner och iframes), **Service list** (tjänster på sidan, valfritt även undersidor, och tile-storlek från 1.35.2) och **Table** (data från datakälla, kolumner och åtgärder). Tabellåtgärder: *Action* med kryssruta per rad och en order per rad, *Edit action* som körs vid radklick (en default) och *New action* som genväg under tabellen. Tjänsten får radens identifierare i `System.Object.Id`.

## E-post, uppgifter och order

- E-postmallar använder `{Variabelnamn}` och språkversioner. Mottagarens profilspråk avgör. `System.Store.Url` finns i mallar.
- Order Manager (OrderAdmin) visar steg, variabler och fel samt omstart och terminering. Fel loggas även i Windows Event Log med order-ID. Skickad e-post listas från 1.35.2.
- Temporära användare med begränsad åtkomst finns från 1.35.2.

## Programmatisk hantering

- **PowerShell Management** (`ZervicePoint.WebApi.PowerShell`): `Get/New/Set/Remove-ZPService`, `*-ZPProcess`, `New-ZPForm`, `New-ZPField`, `New-ZPVariable`, `New-ZPActivity`, `*-ZPJavaScript` (form functions), `*-ZPList*` (shared lists), `Get-ZPOrder`, `New-ZPOrder`, `Get-ZPOrderParameter`, `Set-ZPOrderState`, `Get-ZPTask`, `Set-ZPTaskStatus`, `Get-ZPMedia`, `Get-ZPCartFile`, `*-ZPStore`, `New-ZPRole`/`Get-ZPRole`, `Set-ZPKeyCredential` m.fl. Autentisering med ADFS eller nyckel (1.23.2367+).
- Tjänst och process flyttas mellan miljöer enligt [export/import-guiden](https://docs.zervicepoint.com/how-to/how-to-export-and-import-services-with-zervicepoint-powershell-management/), och kopieras enligt [copy-guiden](https://docs.zervicepoint.com/how-to/how-to-make-a-copy-of-a-service-with-zervicepoint-powershell-management/).
- **REST API** (1.29+): resurser som `/api/Service`, `/api/Process`, `/api/Order`, `/api/Media`, `/api/Profile` och `/api/Delegation`. Rollbaserad behörighet, API-användare och OIDC/hybridautentisering har tillkommit i 1.33–1.34. Order via API kan fylla readonly-fält (1.31), eftersom formulär-JS inte körs vid API-beställning. Exempel: [REST kom igång](https://docs.zervicepoint.com/how-to/how-to-get-started-with-rest-api/), [lägg order](https://docs.zervicepoint.com/how-to/how-to-place-order-with-rest-api/), [filuppladdning](https://docs.zervicepoint.com/how-to/how-to-file-upload-api/).
- **Provisioning system events** (1.34.3476): prenumeration på händelser, se [how-to](https://docs.zervicepoint.com/how-to/how-to-subscribe-to-provisioning-system-events/).
- **GDPR:** [radera personuppgifter](https://docs.zervicepoint.com/how-to/how-to-erase-personally-identifiable-information-in-accordance-with-gdpr/). **Före driftstart:** [rensa testorder](https://docs.zervicepoint.com/how-to/how-to-clear-test-orders-from-a-zervicepoint-installation-before-go-live/).

API-anrop som skapar, beställer eller raderar är skrivande. Kör dem bara mot avsedd testbutik och med uttryckligt godkännande.
