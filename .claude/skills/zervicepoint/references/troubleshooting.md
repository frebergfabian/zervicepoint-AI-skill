# Felsökning: index över leverantörens kunskapsbas

Leverantören har 55 felsökningsartiklar. Hela listan med länkar finns i [katalogen](docs-catalog.md#felsökning), och fulltexten i `docs-cache/troubleshooting/`. Här är de vanligaste för tjänstebyggare. Genomgånget 2026-11-13.

## Grundordning (leverantörens riktlinjer)

1. Kontrollera att tjänsterna kör: ProcessSystem, Provisioning System, Provisioning Service Inventory, IIS, samt Service Bus och Workflow Manager eller ZerFlow. Starta om ProcessSystem, ProvisioningSystem och ProvisioningSystemInventory vid köade order.
2. Läs **Event Viewer**. Nästan allt loggas där med order-ID. Service Bus och Workflow Manager har egna loggar.
3. Orderfel syns i Order Manager (AdminWeb) och i händelseloggen.
4. Formulärfel: öppna formuläret med F12 → Console och ladda om, eller sök i dropdownen.
5. Användaren saknar tjänst eller dropdown-träff: kontrollera roller. De uppdateras vid ny inloggning.

## Händelse-ID som ofta dyker upp

Alla Zervicepoint-händelser har unika ID:n, se [listan](https://docs.zervicepoint.com/troubleshooting/zervicepoint-unique-event-ids/) eller `docs-cache/troubleshooting/zervicepoint-unique-event-ids.md`.

| ID | Namn | Vanlig orsak |
| --- | --- | --- |
| 1020 | FailedToUpdateTask | Godkännare kan inte godkänna. Kontrollera att order- och approvalformulär har samma variabler, rätta och starta om med senaste version. |
| 1023 | FailedToOrderService (UserWeb) | Generiskt beställningsfel. Läs detaljer och korrelera tid och användare. Se felsökningsordningen i [Formulär och arbetsflöden](forms-workflows.md#verifiera-och-felsök). |
| 18/19 | SecuritySystemRoleManagerFailedToExecute(Main)Rule | Fel i rollregel-JS. |

## Kända problem per område

| Symptom | Artikel (sökväg i `docs-cache/troubleshooting/`) | Kärna |
| --- | --- | --- |
| Dynamisk dropdown ger objektreferensfel | `empty-results-in-dynamic-drop-down-causes-object-reference-error` | Filtrera bort objekt med tomt `Id` före `Select-Object`. |
| Datum från datumfält går inte att konvertera i aktivitet | `datetime-objects-not-working-correctly` | Tjänstekontots regionformat (t.ex. sv-FI) bryter formatet `MM/dd/yyyy HH:mm:ss`. Byt till ett kompatibelt format som sv-SE. Med ZerFlow gäller ISO 8601. |
| Workflow-validering misslyckas med decimal i villkor | `workflow-validation-failed-when-using-conditional-sequence` | Workflow Manager RTM saknar Int64. Kräver CU2+. |
| Stora arbetsflöden validerar inte | `workflow-validation-fail-with-large-workflows`, `workflow-validation-failed-with-large-workflows` | Dela upp, t.ex. med grouped activities eller separata tjänster. |
| Provider med flera Additional parameters startar men slutförs inte | `provider-with-multiple-additional-parameters-start-but-don-t-complete` | |
| Egen provideraktivitet fastnar i Started | `workflow-stops-with-custom-provider-activity-in-started-state` | |
| CWS-anrop avbryts eller slutar svara | `client-web-service-calls-gets-aborted`, `client-web-service-stops-responding`, `client-web-service-is-not-configured-or-certificates-have-expired` | Timeout, prestanda och certifikat. Se [Datakällor](datasources.md#drift-och-prestanda). |
| Ej trådsäkra cmdlets | `use-retry-functionality-when-working-with-powershell-cmdlets-that-are-not-thread-safe` | Retry eller `webserviceisolation`. |
| Snapins laddar inte i dropdowns och webservices | `why-certain-powershell-snapins-do-not-load-properly-in-drop-downs-and-webservices` | |
| Minnesläcka i ProvisioningSystem | `import-pssession-causes-memory-leak-in-provisioning-system` | Undvik `Import-PSSession` i moduler. |
| Statiska metoder i PS-klasser | `using-static-methods-in-powershell-classes-in-modules-used-by-zervicepoint-can-cause-issues` | |
| Order fastnar i Queued | `orders-are-not-processed-and-are-stuck-in-queued-state`, `a-specific-service-stays-in-queued`, `wfutil-for-cleaning-inactive-workflows`, `orders-stuck-in-queued-state-or-distributed-transaction-manager-msdtc-errors-in-the-event-viewer` | |
| Provisioning-jobb misslyckas varje timme | `provisioning-job-fails-but-repeats-every-hour` | |
| PowerShell Management: Unauthorized, Bad request, timeout | `unauthorized-when-trying-to-use-zervicepoint-powershell-management`, `bad-request-exception-from-zppsmgmt-commands`, `timeout-exception-when-using-get-zpservice-in-zervicepoint-powershell-management` | |

Worker i molnvarianten: [worker-hjälpen](https://docs.zervicepoint.com/onboarding/cloud-onboarding-worker-help/) täcker saknade aktiviteter och datakällor samt dropdowns som inte svarar (DNS, signeringscertifikat, privat nyckel).
