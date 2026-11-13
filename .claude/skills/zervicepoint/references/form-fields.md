# Formulärfält, variabler och urklipps-JSON

Källor: [Building blocks](https://docs.zervicepoint.com/reference/building-blocks/), [terminologi](https://docs.zervicepoint.com/system-overview/terminology/), [snippets](https://docs.zervicepoint.com/reference/snippets/), [datatåget](https://docs.zervicepoint.com/concepts/datatrain/) och release notes, genomgångna 2026-11-13. JSON-strukturen nedan kommer från leverantörens publicerade snippets (byggda i 1.25) och plugin-exempel. Den är observerad, inte ett officiellt schema. Kontrollera alltid mot en färsk export från målversionen.

## Formulärtyper

| Formulär | Används |
| --- | --- |
| Order form | Beställarens formulär. Varje tjänst har minst ett. |
| Approval form | Visas för godkännare. Väljs i Approval-aktiviteten och är som standard samma som orderformuläret. |
| Task form | Visas för den som tilldelats en manuell uppgift (Task). |
| Setup form | Bara i delad process. Fylls i när en tjänst skapas på processen och ger standardvärden till processens variabler. Tillåter textfält, dropdown (även dynamisk), checkbox och textblock. |

Fält bundna till variabler laddas med variabelns aktuella värde när approval- eller taskformuläret öppnas, och skriver tillbaka när uppgiften slutförs. Event 1020 (FailedToUpdateTask) vid godkännande beror ofta på att order- och approvalformulär har olika variabler.

## Fälttyper

| Fält i designern | JSON `type` | Bindning | Viktiga inställningar |
| --- | --- | --- | --- |
| Text field | `InputText` | String/Decimal/Integer | Character limit (1.21), Validation (None/Name/Email/Numerical/Alphanumeric/Custom regex) med meddelande, Default value, Readonly |
| Text area | `InputTextArea` | String | Rows, Validation, Full width |
| Text block | `TextBlockRTF` | (kan bindas) | HTML/RTF-text i `properties.text`. Visa meddelanden med `val('…')`, `show()`/`hide()`. Fungerar i delade processer från 1.23.2345. |
| Drop down list | `DropDown` | String (flerval: `a;b`) | Static/dynamic, Searchable, Multi select, Allow clear, Placeholder, Restricted/Unrestricted, Data source, dynamisk sökfördröjning, klientcache, minsta söklängd. Alternativ har Label, Value, Selected, Cost och Monthly cost. |
| Checkbox | `CheckBox` (enkel), flerval/dynamisk finns | Boolean (enkel), String (flerval) | Kostnad per val, Dynamic bind, Multi select |
| Radio button | (radiolista) | String | Ett val, går inte att avmarkera, ingen datakälla |
| Date & time picker | `DatePicker` | DateTime | Visa datum och/eller tid, Default value, "Default to current date" (1.25.2549), tillåtna/blockerade intervall och veckodagar (1.32.3257), ny datumväljare i 1.35.2 |
| File upload | `InputFile` | File (GUID) | Maxstorlek per fält, högst butikens gräns (1.30.2958). Filen hämtas med `Get-ZPMedia`/`Get-ZPCartFile` eller bifogas i Send e-mail. |
| Hidden field | `InputHidden` | valfri | Bygg resultat i JS, t.ex. sammanfattning eller JSON till ärendesystem |
| Service selector | (servicesökare) | String | Publicerade tjänster filtrerade på Page/Tag, Default Services, flerval |
| Form section | `FormSection` | – | Barnfält i `fieldsViewModel.fields`. Visa rubrik och bakgrund (`chrome`), Align fields by (`direction`), `fullwidth`, Hidden, Line break |
| Button | (knapp) | – | Från 1.26. Kör `onLoad`, `onClick` (motsvarar onChange) och `onSubmit`. |

Gemensamt för alla fält: Identifier (`name`, används av `Z('#…')`), Name (`displayName`, översättningsbar), Description, Long description/infobubbla (1.34.3563, placering valbar från 1.34.4197), BindTo, Required, Readonly, Hidden, Line break och Size. Fält och aktiviteter kan **tillfälligt inaktiveras** (1.30.2958). Ett inaktiverat fält finns inte alls i formuläret, vilket är användbart vid felsökning.

### Dropdown: restricted, unrestricted och dynamisk

- **Static restricted** (standard): alternativ från designern. Signeras och verifieras vid post, så de kan inte manipuleras.
- **Static unrestricted**: alternativ läggs till med `Z().add()`. Värdet kan ändras av användaren i webbläsaren och måste därför valideras i arbetsflödet. Undvik för känsliga val.
- **Dynamisk** (`isDynamicBind: true`, `dataSource`): PowerShell- eller .NET-funktion på ClientWebService. Alltid restricted. `Id` sparas och `Name` visas. Med `GetCategories` blir det en kategoriväljare ovanför. Från 1.34.3563 laddas kategorier bara vid onLoad.
- Första alternativet förväljs om varken Allow clear eller Searchable är aktivt.
- 1.35.3 rättade ett fel där dropdowns inte fylldes med mer än 50 objekt. Kontrollera långa listor, som 178 ZF-koder, i målversionen.

## Layout

`size` är en sträng i exporterna (`"3"`, `"4"`, `"6"` har observerats). Sätt `lineBreak: true` på sista fältet i en rad. På sektioner styr `fullwidth`, `chrome` och `direction` (0 = rad) layouten. Två sektioner kan stå bredvid varandra om `fullwidth` är av. Ett tomt textblock eller `lineBreak` ersätter DOM-hack för radbrytning.

## Variabler

| Typ | Används för | Not |
| --- | --- | --- |
| String | Text, dropdown, flerval (`;`-separerat) | Standard |
| Boolean | Checkbox, villkor | |
| Decimal | Tal | Decimaloperand i villkor kräver WF Manager CU2+. ZerFlow rättat i 1.35.2. |
| Integer | Heltal | Ny typ i 1.35.2. Standardvärde för andra typer än String gäller bara ZerFlow. |
| DateTime | Datumväljare | ZerFlow hanterar ISO 8601. Strängmanipulering av datum kan brytas vid motorbyte. |
| File | Filuppladdning (GUID) | |
| Translation | Text per kultur | Aktiviteten returnerar en hashtable `@{ 'sv-SE' = '…'; 'en-US' = '…' }` |

- Variabler kan **maskas** helt eller delvis (`hideAll`, `hideStartIndex`, `hideLength` m.fl.). Värdet döljs i orderhistorik och Order Manager men finns kvar i databasen. Generera hellre hemligheter i en aktivitet.
- In- och utmarkering (`isInputParameter`, `isOutputParameter`, `isRequired`) används i grouped activities.
- En variabel kan bara tas bort när den inte är bunden. Typ kan inte ändras på bunden variabel (1.34.5139).

### Systemvariabler

`System.Order.Id`, `.CorrelationId` (kundvagn), `.OrderDate`, `.Cost`, `.MonthlyCost`, `.Quantity`; `System.Requester.Email/Name/Username`; `System.Receiver.*` (ändras av Set receiver); `System.ServiceOwner.*`; `System.Process.Id`; `System.Service.Id/Identifier/Name`; `System.Service.Draft` (1.34.3563); `System.Object.Id` (vald rad i tabellåtgärd). Kontextvariabler: `System.Task.*` och `System.Assignee.*` finns bara inom Task-händelser, `System.While.IterationCounter` bara i While och `System.Store.Url` i e-postmallar. Systemvariabler går att läsa men inte skriva.

## Urklipps-JSON (copy/paste, från 1.24.2410/1.25)

Markera fält eller aktiviteter och kopiera med Ctrl+C. Resultatet är JSON som går att klistra in i en annan tjänst, process eller grouped activity. Inklistring skapar variabler och datakällor som saknas. Från 1.34.5200 varnar Zervicepoint vid copy/paste mellan olika produktversioner. Det är tillåtet, men granska och testa resultatet.

```text
Formulär: { "fields": [Field…], "variables": [Variable…] }
          (egna exporter har även clipboardEntityType "form", clipboardSchemaVersion, zervicepointVersion)
Field:    name, displayName{kultur}, description{kultur}, type, size, properties{…},
          required, readonly, hidden, lineBreak, isBound, boundTo,
          onLoad, onChange, onSubmit (JS som sträng), fieldsViewModel.fields[] (barn)
Variable: id/realId, name, displayName, variableType, value, isBound,
          maskning (shouldHide, hideAll, hideStartIndex, hideLength, hideRemaining …),
          isInputParameter, isOutputParameter, isRequired, isSystemVariable, isAssignable
```

Egenskaper per fälttyp, som de förekommer i leverantörens exempel:

- `InputText.properties`: `defaultvalue{kultur}`, `validationtype`, `validationpattern`, `validationmessage{kultur}`. Observerat: `0` = ingen och `5` = egen regex. `1` och `2` förekommer också. Läs av numret i designern innan du sätter det för hand.
- `DropDown.properties`: `dropdownItems[{id, value, label{kultur}, selected, cost, monthlyCost}]`, `isRestricted`, `isSearchable`, `isMultiSelect`, `isDynamicBind`, `dataSource`, `allowClear`, `placeholder{kultur}`, `useClientCache`, `useDynamicDebounce`, `minimumSearchLength`.
- `TextBlockRTF.properties.text{kultur}`. `FormSection.properties`: `direction`, `chrome`, `fullwidth`.

### Tillägg observerade i en verklig export (1.34.5202)

En kundexport från 1.34.5202 (schema 1) innehöll fler nycklar än leverantörens snippets från 1.25:

- **Per fält:** `id` (databas-ID), `isEnabled` (false = tillfälligt inaktiverat fält), `longDescription{kultur}` (HTML för infobubblan), `descriptionPosition`, `selectedJavascriptModalTab` (editorns UI-läge, ofarligt) och `size` med värdena `"1"`–`"6"`. `FormSection.fieldsViewModel` har även `displayContextMenuEnableAction` och `displayContextMenuDisableAction`.
- **`InputText.properties.maxLength`** är en sträng, t.ex. `"12"`. **`InputTextArea.properties.rows`** är ett tal.
- **`DatePicker.properties`:** `defaultvalue`, `selectableDate`, `selectableTime`, `useCurrentDateDefault`, `weekdays` (bitmask; 31 = de fem första dagarna) och `intervals: [{start, end, isAllowed}]`, där start/end är dagar relativt idag (t.ex. `start: 14` = tidigast om 14 dagar). På fältnivå finns dessutom `day_0`–`day_6` med bitvärdena 1, 2, 4 … eller 0. Kontrollera i målversionens datumväljare vilken veckodag `day_0` motsvarar innan du ändrar.
- **`CheckBox.properties`:** `checkboxItems[]` (samma form som dropdownItems), `defaultvalue` (bool), `isMulti` (0/1), `cost`, `monthlyCost`, `isDynamicBind` och `dataSource`. En enkel checkbox binds till Boolean.
- **`validationtype`** följer troligen designerns ordning: 0 None, 1 Name, 2 Email, 3 Numerical, 4 Alphanumeric, 5 Custom (regex i `validationpattern`). Ordningen är härledd ur leverantörens lista och exempel, inte dokumenterad som numrering.
- **Variabler** var slimmade i denna export: `id`, `name`, `displayName`, `description`, `value`, `variableType`, `shouldHide`, `hideLength`, `hideStartIndex`, `isInputParameter`, `isOutputParameter` och `isRequired`. Exporten innehåller bara de variabler formuläret binder. Tjänstens övriga variabler, t.ex. de som arbetsflödet använder, följer inte med.
- **Systemvariablernas typer**, enligt variabelfliken: `System.Order.Id`, `.Cost`, `.MonthlyCost`, `.Quantity`, `System.Process.Id` och `System.Service.Id` är **Decimal**. `System.Order.OrderDate` är DateTime, `System.Service.Name` är Translation och `System.Service.Draft` är Boolean. Övriga är String.

Arbetsflödes-JSON och aktivitetstyper beskrivs i [Arbetsflöden och aktiviteter](workflow-activities.md#urklipps-json-för-arbetsflöden).

### Regler vid hand- eller AI-redigering av export

- Ändra bara det som är beställt. Bevara `id`/`realId`, `boundTo`, kulturnycklar (`en-US`, `sv-SE`), ordning och okända egenskaper.
- JS i `onLoad`/`onChange`/`onSubmit` är JSON-escapad (`\n`, `\"`). Extrahera, syntaxkontrollera och escapa tillbaka. Räkna inte med att editorn rättar trasig JSON.
- En `boundTo` måste matcha en variabel i `variables` eller i målprocessen. Kopiering mellan tjänster kan skapa dubblettvariabler.
- Provider-aktiviteters `methodId` är miljöspecifikt. Efter inklistring i en annan miljö kan aktiviteten behöva bindas om eller uppdateras.
