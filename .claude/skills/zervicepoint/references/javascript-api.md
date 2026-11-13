# Z()-API: komplett referens för formulär-JavaScript

Sammanställt från leverantörens [JavaScript-referens](https://docs.zervicepoint.com/reference/javascript/), [migreringsguiden till nya UI](https://docs.zervicepoint.com/how-to/how-to-migrate-to-new-ui/), [datakällor](https://docs.zervicepoint.com/tutorials/data-source/) och release notes, genomgånget 2026-11-13. Fulltext och exempel finns lokalt i `docs-cache/reference/javascript.md` efter `python scripts/sync_docs.py`. "Från" anger lägsta version enligt dokumentationen; saknas den är funktionen äldre än 1.10.

## Händelser och scope

| Händelse | Körs | Typisk användning |
| --- | --- | --- |
| `onLoad` | När formuläret laddas (även i approval-/taskformulär). | Utgångsläge, `Z.call` för förifyllnad, definiera delade funktioner (`window.fn = …`). |
| `onChange` | När fältets värde ändras. På knapp (från 1.26) heter den `onClick`. | Synka beroenden, kaskader, villkorad visning/krav. |
| `onSubmit` | Vid beställning, före post. | Slutkontroll, bygga dolda fält (sammanfattning, JSON) som är bundna till variabler. |

- `this` i händelsen är det aktuella fältet som Z-objekt (`this.val()`, `this.clear()`).
- Kod i ett fälts `onLoad` kan definiera globala hjälpfunktioner (`window.updateX = function(){…}`) som andra fält anropar. Leverantörens exempel gör så; håll namnen unika per formulär.
- **Form functions** (från 1.24.2446): återanvändbara JS-klasser lagras i databasen och importeras i "Edit Scripts"-dialogen. Hanteras med `New-/Set-/Get-/Remove-ZPJavaScript`; `New-ZPForm -FormFunction` kopplar klasser till ett formulär. Klasser kan versionshanteras i Git och laddas upp efter test.
- Från 1.34.4197 visar JS-dialogen en tabell över fältens namn, identifierare och bundna variabler. 1.31 gav autocomplete av Z-selektorer.

## Selektorer

| Selektor | Betydelse |
| --- | --- |
| `Z('#Identifier')` | Fält med given identifierare (fältets `name` i JSON). Skiftlägeskänsligt i praktiken – använd exakt namn. |
| `Z('#[type=inputtext]')`, `Z('#[type=checkbox]')`, `Z('#[type=fieldset]')` | Alla fält av en typ. Typnamnen här är klientens typnamn, inte JSON-exportens `type`. |
| `Z('form')` | Formuläret; `.disable()` / `.enable()` spärrar respektive släpper beställningsknappen (från 1.10.1229). Migreringsguiden skriver `Z('form:')`; använd den form som fungerar i målversionen. |
| `Z('all')` | Alla fält (nämns i 1.31 som autocomplete-selektor). |
| `Z('attr:[type=fieldSet]')` | Används i leverantörens `getOrderDetails`-exempel för att iterera över sektioner i nya UI. |

En selektor kan träffa flera fält: getters returnerar då array, setters påverkar alla. `length` ger antal träffar.

## Metoder på fält

| Metod | Gör | Från / not |
| --- | --- | --- |
| `val()` | Hämtar värde (array om flera fält). Dropdown: sparat värde (Id), inte etikett. Checkbox (enkel): boolean. | |
| `val(v)` | Sätter värde. Dropdown med flera värden: `val(['a','b'])`. `val([])` rensar statisk dropdown (1.21.2160). | Dynamisk dropdown kräver att datakällan har `Validate`; annars rensas värdet. |
| `getItem()` | `{ value, text, isSelected }` för valt objekt. För andra fälttyper är `value` = `text`. | Använd `.text` för visningsetikett. |
| `getItems()` | Alla alternativ i dropdown/radiolista som array av objekt enligt ovan. | |
| `isMultiple()` | Sant om fältet är flerval. | Används i leverantörens nya `getOrderDetails`. |
| `add(value, text, isSelected, suppressChange)` | Lägger till alternativ. `suppressChange=true` hindrar onChange. | Fältet måste vara **Unrestricted**. |
| `clear()` | Tömmer fältet/alla alternativ. | |
| `show()` / `hide()` / `toggle([bool])` | Synlighet. | |
| `visible()` | Sant om synligt. | 1.30 |
| `enable()` / `disable()` | Aktiverar/spärrar. Ersätter `readonly` via DOM. | 1.10.1229 |
| `require([bool])` | Sätter krav; utan argument = krävs. | 1.13. Se fallgrop nedan. |
| `valid([bool], [meddelande], [force])` | Markerar giltighet med eget meddelande; `force=true` visar direkt. `valid()` = giltigt. Ett ogiltigt fält stoppar beställningen. | 1.13 |
| `isValid()` | Sant om giltigt. | 1.30 |
| `spin([bool], [meddelande])` | Laddindikator på fältet. | 1.10.1229 |
| `displayName([text])` | Läser/sätter etikett. | |
| `description([text])` | Läser/sätter beskrivning. | |
| `longDescription(...)` | Läser/sätter lång beskrivning (infobubbla). | 1.34.3799 |
| `children()` | Barnfält i en formsektion. | |
| `first()` / `last()` / `get(i)` | Välj ur selektorn. | |
| `filter(fn)` | Ny selektor med fält där `fn` (med `this` = fält) returnerar true. | |
| `each(fn)` | Iterera; `this` = fält, argument = index. | Används i leverantörens exempel. |
| `change(fn)` | Registrera onChange-hanterare (ersätter jQuery-`bind`). Utan argument triggar den onChange. | |
| `submit(fn)` | Registrera/trigga submit-hanterare på fältet (postar inte formuläret). | |
| `getCategories()` / `getCategory()` | Kategorilista resp. vald kategori i dynamisk dropdown med `GetCategories`. | |

## Globala medlemmar

| Medlem | Innehåll |
| --- | --- |
| `Z.call(namn, data, settings)` | Anropar en inventerad webservice-/datakälla på ClientWebService. `data` är nyckel/värde som matchar funktionens parametrar. Returnerar zXHR med `.done(fn(data))`, `.fail(fn)`, `.always(fn)` och `.spin(fältAttSnurra, meddelande, fältAttSpärra)`. Datakällan måste vara tillagd under formulärets **Data sources** i form editorn. |
| `Z.debounce(fn, ms)` | Returnerar funktion som bara körs när den inte anropats på `ms` millisekunder. Bra för sökfält som triggar `Z.call`. |
| `Z.currentUser` | `culture`, `language`, samt i nya UI `email`, `name`, `username`. |
| `Z.currentStore` | `defaultCulture`, `defaultLanguage`. |
| `Z.service` | Aktuell tjänst (1.24.2466): `name` (identifierare), `displayName`, `shortDescription`, `description`, `cost`, `monthlyCost`, `totalCost`, `totalMonthlyCost`, `quantity`, `tags`, `isFavorite`, `isCartCompatible`, `isCountable`, `processUniqueId`, `uniqueId`. Initieras även för tjänster startade från tabell från 1.35.2. |
| `Z.latinize(str)` | Konverterar tecken till latinska motsvarigheter (`ộ → o`). Från 1.34.5200; bra för kontonamn/e-post. Testa svenska tecken (å/ä/ö) i målversionen innan du förlitar dig på resultatet. |

## Z.call – rekommenderat mönster

Leverantörens rekommendation, generaliserad:

1. Läs indata, avbryt tidigt om obligatorisk kontext saknas.
2. `spin(true, '…')` på fältet som triggar.
3. `.done(data)`: `data` är **alltid en array**. Kontrollera `data.length`, läs `data[0].Egenskap`. En sträng som returneras från PowerShell blir `data[0]`.
4. Sätt värden och `valid()` / `valid(false, 'meddelande', true)`.
5. `.fail()`: markera fel tydligt; tyst fel ger tomma fält.
6. `.always()`: `spin(false)`.

Webservicens parametrar `Config`/`Parameters` ligger i ParameterSetName `Hidden` och skickas inte från formuläret; `$config` fylls på servern med bl.a. `currentuser` och `roles`. Se [Datakällor](datasources.md).

## Fallgropar

- **`require(false)` slår inte ut "Required" satt i AdminWeb.** Låt fältet vara icke-obligatoriskt i designern och sätt `require(true)` i `onLoad` om JS ska styra kravet.
- **`add()` kräver Unrestricted dropdown.** Unrestricted-värden kan ändras av användaren i webbläsaren och är inte signerade; validera dem i arbetsflödet. Statiska restricted och dynamiska dropdowns signeras och verifieras vid post.
- **Dynamisk dropdown via `val()`** fungerar bara om datakällan exporterar `Validate`, som ska returnera samma objekt som `Search` skulle ha gjort. Annars rensas värdet.
- **Flerval** binds till variabel som `v1;v2`. I JS är `val()` en array.
- **Dolda fält behåller värden** och skickas om de är bundna. Rensa när en gren väljs bort.
- **Fattade beslut i arbetsflödet** ska inte bygga på formulärdata som användaren kan manipulera (annat än signerade dropdowns). Hämta om data i arbetsflödet.
- **Fönster-load:** `$(window).load` stöds inte i nya UI. Leverantören föreslår polling med `setInterval` tills fältet har värde; föredra `onLoad`/`change` där det räcker.
- **Datakälla med tomt Id** ger objektreferensfel i ClientWebService; filtrera bort `$null` innan `Select-Object`.

## Observerat i verkliga formulär (odokumenterat – verifiera)

- **`Z('#')`** (tom identifierare) används i kundkod för att hämta *alla* fält. Varje element har bland annat `name` och `type` och svarar på Z-metoder. Det är praktiskt för serialisering men inte dokumenterat.
- **Klientens typnamn** skiljer sig från exportens `type`: `fieldSet`, `inputHidden`, `textBlock`, `button`, `checkBox`, `inputDatePicker`, `serviceSelector`, `InputDropdownField`, `dropDownList`, `dynamicDropDownList`, `unrestrictedDropDownList` m.fl. Använd dem bara för filtrering och testa efter uppgradering.
- **Intern komponentstruktur** som `field.component.props.visible`, `.displayName` och `.value` förekommer i kundkod för att läsa synlighet och visningstext. Det är lika ömtåligt som den DOM-åtkomst som togs bort i nya UI. Använd i stället `visible()`, `displayName()`, `getItem().text` och `isMultiple()`.
- **Skiftläge i selektorn:** leverantören anger inte om `Z('#Namn')` är skiftlägeskänslig. Utgå från att den är det, och skriv exakt identifierare. Kontrollera befintlig kod med en ID-lista; `Z('#X').length === 0` avslöjar en felstavning i konsolen.
- **Okända ID:n ger inget fel.** `Z('#finnsInte').val('x')` är tyst. Felstavade fält-ID:n märks därför först när en funktion uteblir.
- **`add()` utan `clear()`** i `onLoad` ger dubbletter när flera fält bygger samma lista, eller när formuläret laddas med befintliga värden (godkännar- eller taskformulär, utkast).
- **Läs inte resultatet av `Z.call` synkront.** Kod efter `Z.call(...)` körs innan `.done()`. Lägg logik som beror på svaret inuti `.done()`.

## Förbjudet i nya UI (DOM-manipulation)

`getElement()`, `get$Element()`, `getContainer()`, `get$Container()`, jQuery (`$(…)`, `jQuery`), `document.query*`, `document.get*`, `document.body` och `$.validator` stöds inte. Varningar loggades från 1.20, och gamla UI togs bort helt i 1.35.2.

| Gammalt mönster | Ersätt med |
| --- | --- |
| Egen laddindikator i DOM | `spin()` |
| Röd ram och felmeddelande via CSS | `valid(false, msg, true)` och `require()` |
| Ändra bredd via CSS | Fältets storlek i designern |
| Injicerad meddelande-`div` | Textblock (RTF) eller readonly-fält som visas/döljs med `show()`/`hide()`/`val()` |
| Radbrytning via injicerad `div` | `lineBreak` på fältet, sektionens "Align fields by" eller ett tomt textblock |
| `attr('readonly')` | `disable()` / `enable()` |
| `css('display','none')` | `hide()` / `show()` |
| Dölja submit-knapp | `Z('form').disable()` |
| `.bind('change', …)` | `Z('#f').change(fn)` |
| `$.validator.addMethod` (t.ex. personnummer) | Egen funktion i `change()` som anropar `valid(ok, msg)` |
| Skrapa formulär till e-post (`getOrderDetailsHtml`) | Iterera sektioner med `Z('attr:[type=fieldSet]')`, `children()`, `visible()`, `isMultiple()`, `getItem(s)()`; skriv resultatet till ett dolt fält i `onSubmit` |

Hitta gamla tjänster med DOM-manipulation via leverantörens SQL-fråga mot `ProcessComponent.Fields` (`OnLoad`/`OnChange`/`OnSubmit` LIKE …), se [how-to](https://docs.zervicepoint.com/how-to/how-to-find-processes-with-dom-manipulations-and-export-to-excel/). Kör bara mot en behörig kopia.

## Mönster ur leverantörens exempel

- **Visa och kräva vid kryss:** i checkboxens onChange: `Z('#mail').val() === true ? Z('#mailAddress').show().require() : Z('#mailAddress').hide().require(false)`. Metoderna kan kedjas.
- **Kaskad med statiska listor** (snippet, 1.25): överordnad onChange gör `clear()` på alla nedströms fält och `add()` för nya val. Beroende fält är Unrestricted, startar med `readonly`/`disable()` och `onLoad: this.clear()`.
- **Godkännarinfo i formulär:** onLoad på "Beställ åt"-dropdown anropar `Get-ZPADManager` och skriver text i ett RTF-block. Saknas chef sätts `valid(false)` på dropdownen för att stoppa beställningen.
- **Svensk personuppgiftsuppslagning** (snippet, kräver Person Lookup SWE): mönsterkontroll av personnummer, `spin`, rensa målfält, `Z.call('Get-ZPPLSEPersonInformation', {SSN})`, fyll fält eller visa fel i RTF-block.
- **Lösenord i formulär:** validera mot AD-policy med regex i fältets Custom validation. Bind till maskerad variabel eller generera lösenordet i en aktivitet. Se [Formulärfält](form-fields.md#variabler).
