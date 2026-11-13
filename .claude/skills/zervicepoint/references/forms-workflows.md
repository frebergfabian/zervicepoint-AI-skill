# Formulär och arbetsflöden

## Känn igen exporten

| Typ | Fält att kontrollera | Användning |
| --- | --- | --- |
| Urklippsformulär | `fields`, `variables`, `clipboardEntityType: "form"`, `clipboardSchemaVersion`, `zervicepointVersion` | Inklistring i formulärbyggaren. |
| Urklippsarbetsflöde | `activities`, `variables`, `clipboardEntityType: "workflow"` och versionsmetadata | Inklistring i arbetsflödesbyggaren. |
| Tjänst och process | API-objekt, processreferens och pluginberoenden | Flytt mellan stores via Management API enligt leverantörens guide. |

Observerat i ett formulär från `1.34.5202`, schema `1`: `FormSection.fieldsViewModel.fields` innehåller barnfält; gå rekursivt. Fält har bland annat `name`, `type`, `size` (sträng i denna export), `lineBreak`, `properties`, översättningar, `isBound` och `boundTo`. Exempel på typer: `InputHidden`, `FormSection`, `TextBlockRTF`, `InputText`, `DatePicker`, `DropDown`, `CheckBox`, `InputTextArea`. Variabler har eget namn, typ och in-/utmarkering; bind inte genom att gissa från etiketten.

Observerat arbetsflöde: aktivitetstyp `Provider` har metodnamn, paket/modul, miljöberoende `methodId`, `providerParameters`, `providerResult`, `stopOnError` och eventuella barnaktiviteter. Parametrar kan vara statiska, bundna eller ej satta; en systembindning som `System.Order.Id` är inte samma som en egen variabel. Se källexportens faktiska datatyper och schema före ändring. Ett giltigt JSON-dokument bevisar inte att en viss metod finns i målets inventory.

## Z()-JavaScript

Fullständig metodlista, versionskrav och ersättningar för DOM-manipulation finns i [Z()-API](javascript-api.md). Fälttyper och JSON-egenskaper finns i [Formulärfält och JSON](form-fields.md). Nedan följer arbetsregler.

- Läs [JavaScript-referensen](https://docs.zervicepoint.com/reference/javascript/) och [kaskadexemplet](https://docs.zervicepoint.com/reference/snippets/form-cascading-dropdown/). Använd dokumenterade formmetoder framför DOM-selektorer och interna klasser. Kontrollera syntax och beteende för målversionen; återanvänd en redan verifierad anropsform där det går.
- `onLoad` sätter utgångsläge och behöver hantera förifylld data. `onChange` synkar beroenden. `onSubmit` gör slutlig formulärkontroll och bygger vid behov orderdata. Kör delad logik konsekvent och håll koll på eventordning, särskilt när ett fält fylls programmatiskt.
- `Z('#fält')` refererar till formulärets tekniska namn. Kontrollera skillnaden mellan `val()` (sparat värde) och det som visas. Hantera tomt värde, enkelval och multival uttryckligen. Kontrollera vilka metodsignaturer exporten använder för `getItems`, `add`, `require`, `valid`, `show` och `hide`.
- Vid kaskader: återställ beroende val, krav och giltighet när överordnat val ändras. Släpp sena svar för gamla val. Ha tydligt tillstånd för laddning, tomt svar och fel. Anropa inte provider förrän obligatorisk kontext finns. `Z.call` måste matcha registrerad datakälla och dess kontrakt.
- Rendera profilinformation som text eller via en granskad mall med escaping. Placera rollinnehåll som ska underhållas utanför JavaScript. Bekräfta eventuell RTF-/HTML-sanering med ett litet test i byggaren.
- Dolda fält kan behålla gamla värden. Kontrollera kombinationen av rensning, giltighet, krav och serialisering, särskilt när någon byter titel eller avmarkerar ett system. Fältets synlighet skyddar inte serverns orderdata.

## Layout som går att presentera

Gruppera korta fält i par, t.ex. förnamn/efternamn och start/slutdatum; låt långa val, information, fritext och sammanfattning stå på egen rad. För presentationsexporten användes `size: "3"` för par och `"6"` för hela rader, `lineBreak` på sista fältet per rad och `properties.fullwidth` på sektioner. Det är ett utgångsmönster från exporten, inte ett löfte om samma rendering i alla klienter. Kontrollera faktisk bredd på smal och bred yta.

## Verifiera och felsök

1. Ta kopia; gör strukturell diff för rekursiva fält och event. Kontrollera namn, typer, dubbla ID:n och att använda egna bindningar kan lösas i rätt scope.
2. Kör JavaScript-syntaxkontroll på extraherade event; komplettera med testdubbel för `Z()` där beteendet spelar roll. Testa öppning, förifyllnad, byte/återställning, tomma svar, fel, obligatoriskt dolt fält, submit och utgående payload. Testa kalenderdatum och tidszon separat.
3. Provimportera formulär och avsedd process i isolerad testtjänst. Testa rätt roll, olika beställarflöden, workflowstatus, renderingen och faktiskt mottagen payload med testdestinationer. Dokumentera separat från steg 1–2.
4. Vid generiskt orderfel, t.ex. Event 1023 / `UserWeb.FailedToOrderService`, läs detaljer i AdminWeb och korrelera med tid/order. Kontrollera klientvalidering, obundet obligatoriskt intyg, dolda krav, ordervariabler, rättigheter, publicerad version och sedan providerfel. Historiskt kvarstod felet även med ett minimalt arbetsflöde; det stödjer en hypotes om ordersteget, men bevisar ingen grundorsak.
5. Vid interna uppslag som uteblir: särskilj browserns nätverksåtkomst, certifikat/nätverk, worker och providerns sökscope. Om portalen förutsätter tillstånd till lokalt nätverk, verifiera den faktiska browserprompten och policyn; ändra inte tillstånd generellt för andra sajter.

Vid flytt mellan miljöer: [exportera tjänst och process](https://docs.zervicepoint.com/how-to/how-to-export-and-import-services-with-zervicepoint-powershell-management/) och inventera relevanta providermoduler på målet. Verifiera delade processer, listor, behörigheter, konfiguration och integrationer separat.
