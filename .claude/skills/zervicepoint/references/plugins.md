# Plugins och integrationer

## Byggdelar och installation

En datakälla ger formuläret data; en aktivitet utför ett steg i arbetsflödet. Ett plugin grupperar byggdelar för ett system eller en funktion. Zervicepoint beskriver stöd för PowerShell och .NET-baserade providers. Utgå från befintligt plugin och [leverantörens anatomiguide](https://docs.zervicepoint.com/plugins/plugins/) för målversionen.

- Windows-installationer använder normalt `C:\Program Files\Zipper\ZervicePoint\Provider extensions\<Plugin>`. Separera datakällor, aktiviteter och gemensamma moduler. Installera på de noder som faktiskt kör rollerna.
- Provider-XML definierar unikt providernamn, engine/assembly och `scriptpath` samt miljöinställningar via `$config`. ClientWebService-konfigurationen ligger under `ClientWebService`; aktiviteternas under `ProvisioningSystem`. Kontrollera filnamn och roll på målet; äldre dokument och exempel varierar i namngivning.
- ProvisioningSystemInventory inventerar datakällor från ClientWebService-konfiguration; ProvisioningSystem inventerar aktiviteter från sin konfiguration. Kontrollera att rätt modul och funktion syns och att bindningar återkopplas efter import.
- `dropdown.xml` kan styra delegation, sökbas eller domänkontrollant per roll. Det avgränsar formulärets uppslag, men backend behöver egen behörighets- och målvalidering.
- Installera externa beroenden och lägg credential-referenser i avsedd Credential Store i tjänstekontots kontext. Frontend behöver bara läsbehörighet där uppslag krävs; delegera backend precis de skrivåtgärder som behövs i rätt mål. Använd separata testvärden och uppgifter.

## AD

- [AD-pluginets dokumentation](https://docs.zervicepoint.com/plugins/plugin-active-directory/) listar bland annat `Get-ZPADUser`, `Get-ZPADOrganizationalUnit`, `Test-ZPADUser`, `New-ZPADUser`, `Set-ZPADUser` och `Add-ZPADGroupMember`. Formulärens befintliga GET-funktioner visar inte att kontot får skapas. Kontrollera modulversion, förutsättningar och testdelegation.
- Användare/datorer och grupper har olika scheman för `constructs.xml`. För `New-ZPADUser` genereras bland annat SamAccountName, Name/CN och DisplayName med ordnade regler; testa kollisioner, korta namn, tecken och reservnamn. Blacklist kan begränsa genererade värden. Lägg inte in exempelregler från dokumentationen som lokal namnpolicy.
- För grupper beskriver [construct-guiden](https://docs.zervicepoint.com/plugins/plugin-active-directory-construct-file/) separata `constructname`-profiler, regler för unikhet (domän/OU) och eventuell standardsökväg. Verifiera sökväg/format innan ändring; användar- och gruppregler ska inte blandas.
- Implementera återkörning med stabil order- och personkorrelation, upptäckt av tidigare skapad identitet, kontrollerad konflikthantering och tydlig status. Validera mål-OU och grupp-/attributlista på servern. Skapa inget i produktion för att testa formkod. Följ kommunens beslut om åtkomststart och kontoaktivering.

## Exchange

Exchange-pluginets datakällor kan leta upp eller kontrollera brevlådor och adresser. Aktiviteterna omfattar bland annat `Enable-ZPExchangeMailbox`, `Enable-ZPExchangeRemoteMailbox`, `New-ZPExchangeSharedMailbox` och delegering av mailboxbehörighet. Kontrollera om den aktuella miljön använder lokal Exchange, hybrid eller molnflöde; skapa inte både lokal och fjärrbrevlåda av bara farten. Konfigurationen anger bland annat endpoint, domänkontrollant, namn på credential och vid behov standardsökvägar. Säkerställ stödda autentiseringsmetoder i aktuell version.

## TOPdesk

Använd en strukturerad payload med orderkorrelation, status, beslutad profil, godkännanden, beställda poster och kvarvarande manuella moment. Matcha tekniknamn i installerad provider; `New-TDincident` är observerad i en workflow-export, inte ett antagande om en standardmetod för alla kunder. Kontrollera destination, kategorier och operatörsgrupp i test. Granska kvittens och återkörning så en order inte skapar flera ärenden. Ärenden kan visa användarnamn och e-post efter kontoskapning; lämna lösenord och andra starthemligheter utanför payload och loggar.

För andra integrationer: inventera vad som faktiskt finns. Zervicepoints dokumentation innehåller även t.ex. Person Lookup, PDF Automator, Product Catalog, Files & Folders, e-signering och andra systemplugins. Ett system i katalogen (t.ex. SEFOS, Lifecare eller Prorenata) innebär inte att Zervicepoint har ett färdigt plugin eller att kommunen har aktiverat det.
