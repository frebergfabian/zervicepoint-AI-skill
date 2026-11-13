# Datakällor (dropdown, webservice, tabell)

Källor: [datakällor](https://docs.zervicepoint.com/tutorials/data-source/), [plugin-anatomi](https://docs.zervicepoint.com/plugins/plugins/), [roller och dropdown.xml](https://docs.zervicepoint.com/adminweb/roles/), [CWS-isolering](https://docs.zervicepoint.com/how-to/how-to-implement-client-web-service-isolation/), [CWS-prestanda](https://docs.zervicepoint.com/how-to/how-to-improve-the-performance-of-client-web-service/) och [tabeller](https://docs.zervicepoint.com/adminweb/pages/#table). Genomgångna 2026-11-13. Installation, AD och Exchange beskrivs i [Plugins](plugins.md).

## Var de körs

Datakällor körs på **ClientWebService (CWS)** och inventeras av **ProvisioningSystemInventory** från provider-XML i `C:\Program Files\Zipper\ZervicePoint\ClientWebService\`. Aktiviteter inventeras av ProvisioningSystem från `...\ProvisioningSystem\`. Efter ändring: `Restart-Service ProvisioningSystemInventory`. En datakälla måste dessutom läggas till under formulärets **Data sources** för att `Z.call` ska nå den.

| Typ | Används av | Krav |
| --- | --- | --- |
| Dropdown-datakälla (`DropDown.*`) | Dynamisk dropdown eller checkbox | Modulen exporterar `Search`. Valfritt: `Validate`, `GetDefault`, `GetCategories`. |
| Webservice (`WebService.*`) | `Z.call` i formulär-JS | Valfria funktionsnamn. Parametrarna blir `data`-nycklar. |
| Tabell | Tabellsektion på sida | Returnerar PSObject. Kolumner mappas i AdminWeb och en egenskap markeras som identifierare (`System.Object.Id` i åtgärdstjänsten). |

## Dropdown-funktioner

| Funktion | Körs | Ska returnera |
| --- | --- | --- |
| `Search` | När användaren söker (eller laddar). | Objekt med **`Id`** och **`Name`**. Namnen är skiftlägeskänsliga; utan dem visas inget. |
| `Validate` | När värde sätts via `Z().val()`. | Samma objekt som `Search` skulle ge för värdet. Annars rensas fältet. `$search` kan vara en array. |
| `GetDefault` | Vid formulärladdning. | Förvalda objekt, t.ex. inloggad användare via `$config.currentuser`. |
| `GetCategories` | Vid laddning. | Array av strängar. Vald kategori skickas som `$category` till övriga funktioner. |

Parametrar: `$search`, `$config`, `$category`. Flerval skickas `;`-separerat. Leverantörens idiom för tom sökning med `*` är `$search = $search -replace "\*" -replace '\)\(.*'`. `Id` ska vara unikt och stabilt, t.ex. ObjectGUID, och är det som binds och skickas vidare. `Name` är bara visning. Filtrera bort objekt med tomt `Id`, annars uppstår objektreferensfel i CWS.

## `$config` i datakällor och webservices

| Nyckel | Innehåll |
| --- | --- |
| `currentuser` | Inloggad användares e-post |
| `currentUserLanguage`, `currentUserCulture` | Användarens språk och kultur |
| `currentStoreDefaultLanguage`, `currentStoreDefaultCulture` | Butikens standard |
| `roles` | Inloggad användares Zervicepoint-roller (ArrayList) |
| `scriptpath` och egna nycklar | Från provider-XML:ens `<configuration>` |

Felsök `$config` genom att tillfälligt köra `$config | Export-Clixml <sökväg>` i funktionen. Ta bort det efteråt, eftersom roller och e-post hamnar på disk.

## Webservice

- Parametertyper visas i AdminWeb som string, decimal, datetime eller other. `Mandatory` visas som Required. `$Config` och `$Parameters` i ParameterSetName `Hidden` döljs.
- Utdata har inget formatkrav men kommer alltid till JS som array. En sträng blir `data[0]` och ett objekt kräver egenskapsnamn: `data[0].OutputMessage`.
- Returnera bara det formuläret behöver. Allt som returneras syns i webbläsaren.

## Behörighetsstyrning

- **Inte via formuläret.** Filtrera i datakällan på `$config.roles`, eller med `dropdown.xml` där pluginet stöder det: LDAP-filter, SearchBase och DomainController per rollnyckel, `<default>` för GetDefault och `<output>` för Id/Name-mappning. Variabler som `$search`, `$currentUser.DistinguishedName` och `$config.X` kan användas i värdena.
- Leverantören beskriver två modeller: en tjänst per roll med egen datakälla (enkelt men svårt att underhålla), eller en tjänst med en rollmedveten datakälla (mer jobb, men återanvändbar).
- Dynamiska dropdowns signeras, så användaren kan inte posta ett Id som datakällan inte lämnat ut. Backend ska ändå validera behörighet till målobjektet.

## Drift och prestanda

- **Trådsäkerhet:** funktioner som inte är trådsäkra isoleras med `<add key="webserviceisolation" value="Modul[/Funktion,…]" />` eller `*` i provider-XML (från 1.8.1043). Det kostar prestanda.
- **Prestanda:** CWS-poolens konto ska inte vara lokal admin, eftersom PowerShell då blir långsamt. Ge servern minst två vCPU. Använd IIS Application Initialization (`startMode=AlwaysRunning`, `preloadEnabled`) mot kallstart.
- **Klientsidan:** använd `Use client cache`, minsta söklängd och dynamisk fördröjning på sökbara dropdowns, och `Z.debounce` för egna anrop.
- Undvik `Import-PSSession` i långlivade moduler (känd minnesläcka) och statiska metoder i PowerShell-klasser. Se felsökningsartiklarna i [katalogen](docs-catalog.md#felsökning).

## Minimal struktur för egen datakälla

```text
<plugin>\Data sources\DropDown.Exempel\DropDown.Exempel.psd1   (FunctionsToExport: Search, Validate, GetDefault, GetCategories)
<plugin>\Data sources\DropDown.Exempel\DropDown.Exempel.psm1
<plugin>\Data sources\WebService.Exempel\WebService.Exempel.psd1 (FunctionsToExport: *)
...\ClientWebService\<plugin>.clientwebservice.providers.xml    (scriptpath → "<plugin>\Data sources\")
```

Provider-XML:ens `<provider name>` måste vara unikt. Assembly-typen är `Zipper.ZervicePoint.ProvisioningSystem.PowerShellProvider.PowerShellEngine`. Kontrollera sökvägen till `assemblyFile` på målservern, eftersom leverantörens exempel skiljer sig mellan versioner.
