# Arbetsflöden och aktiviteter

Källor: [Building blocks – aktiviteter](https://docs.zervicepoint.com/reference/building-blocks/#workflow-editor-built-in-activities), [egna aktiviteter](https://docs.zervicepoint.com/reference/activity/), [datatåget](https://docs.zervicepoint.com/concepts/datatrain/), [orderflöde](https://docs.zervicepoint.com/concepts/orderflow/), [grouped activities](https://docs.zervicepoint.com/adminweb/groupedactivity/), [delad process](https://docs.zervicepoint.com/adminweb/sharedprocess/), [ZerFlow](https://docs.zervicepoint.com/zerflow/breaking-changes/) och [tjänstedesign](https://docs.zervicepoint.com/concepts/servicedesign/). Genomgångna 2026-11-13.

## Orderflödet i korthet

UserWeb sparar ordern i databasen → ProcessSystem plockar upp den → arbetsflödet körs i motorn (Workflow Manager/Service Bus, eller ZerFlow från 1.35) → inbyggda aktiviteter körs av ProcessSystem, PowerShell-/.NET-aktiviteter av ProvisioningSystem. Beställning går att lägga även när motorn ligger nere; ordern köas.

**Datatåget:** fält bundna till variabler fyller orderns variabellista vid submit. Aktiviteter läser variabler via bundna parametrar. En aktivitet ser bara de variabler som är bundna till dess parametrar. Utdata uppdaterar listan: inbyggda aktiviteter via explicit bindning, egna aktiviteter via returnerad hashtable där **nyckel = variabelnamn**. Task- och approvalformulär läser och skriver samma lista.

## Inbyggda aktiviteter

| Aktivitet (JSON `type`) | Kärna |
| --- | --- |
| Approval (`Approval`) | Godkännare: användarens chef (AD `managedBy`), angivna e-postadresser, tjänsteägare eller variabel med `;`-separerade adresser. Parallell eller sekventiell; en eller alla krävs; vid timeout avslå eller godkänn; timeout och påminnelse anges i sekunder om de binds. Resultat (Boolean) kan bindas. Händelser i editorn: On each approval/reject/timeout samt On approval/On reject. I JSON syns de som `Event` med t.ex. `OnForeachApprove`/`OnForeachReject`. Eget formulär och egna e-postmallar. Från 1.35.2 kräver validering att godkännare finns. |
| Task (`Task`) | Manuell uppgift med egna statusar (minst en standard och en som slutför). Due in, "Complete task when due", notifiering och påminnelse, eget taskformulär. OnChange-händelse med `System.Task.*`/`System.Assignee.*`, som måste kopieras till egna variabler för att användas utanför. Statusar kan få färgade knappar (1.34.3987). |
| Set task description | Bara inne i Task OnChange. Uppdaterar kortbeskrivningen. |
| Set receiver | Sätter mottagare (e-post) och uppdaterar `System.Receiver.*`. |
| Send e-mail | To/Cc/Bcc som `;`-lista eller variabel, valfri avsändare, mall eller ämne/brödtext, bilagor från filvariabler och "End workflow on error". |
| Assign (`Assign`) | Bygger text i en variabel. I editorn infogas variabler med `@`; i JSON blir det `{Variabel}` i `body` med `assignedVariables`. |
| Status (`Status`) | Sätter orderns status, med översättningar (`statusTranslations`). |
| Sequence (`Sequence`) | Gruppering. |
| Conditional sequence (`If`) | `expression` av typen `EqualityExpression` med `operand` (t.ex. `notEqual`), `left` och `right`. Then/Else från 1.31.3196. |
| Parallel | Parallella grenar. Från 1.30.3069 får alla aktivitetstyper blandas. Dela inte variabler mellan grenar. |
| While sequence (`While`) | Loopar tills villkoret uppfylls. `iterationDelaySeconds` kan vara statiskt (1.34.5139) eller bundet. `System.While.IterationCounter` börjar på 1. |
| Code (`Code`) | JavaScript i motorn. Parametrar binds till variabler och blir JS-variabler med samma namn. Alla parametrar returneras som standard, eller ett objekt via `return {…}`. Systemvariabler är skrivskyddade. ZerFlow har ny V8-motor, så testa om. |
| Delay | Paus i h/m/s eller bunden till decimal/integer. |
| Add/Update shared list item | Skriver till en Shared List (intern tabell, hanteras även med `*-ZPList*`). |
| End workflow (`Terminate`) | Avslutar arbetsflödet. |

Aktiviteter kan tillfälligt inaktiveras (1.30.2958), vilket fungerar som att ta bort dem. Det är användbart vid test, t.ex. för att stänga av en approval.

## Egna aktiviteter (PowerShell på ProvisioningSystem)

- En exporterad funktion i en modul under providerns `scriptpath` blir en aktivitet. Parametrar i `param()` visas i editorn och `Mandatory` blir obligatoriska.
- **Utdata:** returnera en hashtable. Tillåtna värdetyper är String, Boolean, Decimal, Integer och DateTime. Andra typer får aktiviteten att misslyckas med att returnera data. En nyckel som inte matchar en variabel uppdaterar ingenting. Leverantörens datatågsexempel visar hur `Status` mot variabeln `State` ger ett oväntat resultat i stället för ett tydligt fel.
- **Prefix:** lägg till parametern `$Prefix` och prefixa nycklarna (`Add-PFHashTablePrefix` i PowerFrame) så att aktiviteter inte skriver över varandras `Name`/`Id`. Leverantörens plugins gör så, t.ex. `Prefix = "APPROVERS"` → `APPROVERSMail`.
- **Dolda parametrar:** `$Config` (provider.xml-nycklar och `scriptpath`) och `$Parameters` (hashtable med definierade och "Additional parameters") ska ligga i `ParameterSetName = "Hidden"`. `Get-PFAdditionalParameter` filtrerar fram de extra parametrarna.
- **Ny parameter i befintlig funktion:** aktiviteten måste läggas in på nytt i arbetsflödet, eller uppdateras med "Update provider activities" (1.34.5139).
- **Inventering:** `Restart-Service ProvisioningSystem` eller `Zipper.ZervicePoint.ProvisioningSystem.Service.exe /inventoryonly`. Kolla Zervicepoints händelselogg om aktiviteten inte syns.
- **Felhantering:** returnera status, kod och meddelande i hashtablen och styr flödet med If. `stopOnError` på provideraktiviteten avgör om ett fel stoppar ordern. En order som är "Completed" men orange har haft ett hanterat fel.
- **Tomma värden** vid redigering: avgör om tomt betyder "rensa" eller "rör inte". AD-pluginet har `ClearEmptyValues` på `Set-ZPADUser`.
- **Säkerhet:** fatta inte beslut i arbetsflödet på osignerad formulärdata. Hämta om data i arbetsflödet. Lösenord bör genereras och skickas av en aktivitet, inte passera formuläret.

## Grouped activity

En återanvändbar sekvens med egna variabler och in- och utparametrar. Den får innehålla allt utom Approval och Task. Uppdateringar slår **inte** igenom automatiskt: processen visar "newer version" och uppdateras där, eller via "Linked processes" i den grupperade aktiviteten (med möjlighet att skapa drafts). Push fungerar inte om obligatoriska parametrar har lagts till eller ändrats.

## Delad process

En process (formulär + arbetsflöde) som delas av flera tjänster. Ändringar slår igenom **direkt** i alla länkade tjänster. Pågående order fortsätter på sin version. Setup form ger värden per tjänst, t.ex. AD-grupp, CollectionId eller ArticleId. Per tjänst: kostnad, tagg, sida, ägare och synlighet. Per process: kundvagn, kvantitet, knapptext och dold submit. Typiskt för mjukvaru- och hårdvarukataloger.

## Urklipps-JSON för arbetsflöden

```text
{ "activities": [Activity…], "variables": [Variable…] }
Activity:  id, name, type, isEnabled, properties{translations}, activities[] (barn/händelser)
Provider:  package, module, method, methodId (miljöspecifikt), stopOnError,
           providerParameters[] / allProviderParameters[] / additionalProviderParameters[],
           providerResult{…}
Parameter: name, providerParameterType, required,
           value{ state: "static" | "bound" | "notSet", value, boundTo, boundToId,
                  isBoundToSystemVariable }
Bindbart värde (Approval, Assign, If m.fl.):
           { isBound, value, boundTo, boundToId, isBoundToSystemVariable }
Approval:  connectedFormName, approvalType ("parallel"), required ("one"), onTimeout ("reject"),
           timeout, remindTime (sekunder), assignees[], notifyAssignees, approvalResult,
           templateName, remindTemplate, activities[ { type: "Event",
           event: "OnForeachApprove" | "OnForeachReject" | … } ]
```

I en export från 1.34.5202 har värdeobjekten ingen `hasWarning`/`boundToId`. En parameter med `state: "bound"` kan ändå ha kvar ett gammalt `value` (t.ex. testtext). Det används inte så länge bindningen gäller, men det följer med vid kopiering, så städa det. `providerResult` (Boolean) kan vara obundet medan aktivitetens hashtable-utdata ändå uppdaterar variabler med samma namn.

`methodId` och `boundToId` pekar på databas-ID:n i källmiljön. Kontrollera efter inklistring att varje provideraktivitet hittar rätt metod och att bindningarna pekar på rätt variabler. Varningar visas som `hasWarning`/`displayWarning`.

## ZerFlow (ny arbetsflödesmotor, 1.35+)

- Uppgradering till 1.35 går inte att nedgradera. Motorval per webbkonfiguration: `WorkflowEngine` = `New` | `NewAndLegacy` | `Legacy`.
- **Brytande skillnader:** DateTime följer ISO 8601, så strängmanipulering av datum kan ge annat resultat. Parallel interfolierar grenar, så räkna inte med en viss ordning och dela inte variabler. Code-aktiviteten och all JS-tolkning körs i ny V8. Nya portar (Zebra API, Workflow API) behöver öppnas.
- Standardvärden för andra variabeltyper än String gäller bara ZerFlow.

## Designråd från leverantören

- Analysera hela processen innan automation. Börja gärna med manuella tasks och automatisera stegvis. Dela långa kedjor i separata tjänster eller grouped activities så att delar kan köras om, t.ex. när en kontosynk inte hunnit klart.
- Bestäm vad som händer vid fel: e-post eller ärende. Alternativt skapas ett ärende direkt och uppdateras genom flödet.
- Tänk CRUD: en "skapa"-tjänst brukar behöva "ändra" och "ta bort". Överväg tabellsidor med åtgärder.
- Hellre flera små tjänster, t.ex. "Återställ lösenord", än en allt-i-ett-tjänst. Det ger enklare test, snabbare flöden och bättre sökbarhet.
- Begränsa synlighet med roller. En tjänst utan "Visible for roles" syns för alla inloggade.
