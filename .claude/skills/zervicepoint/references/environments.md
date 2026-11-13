# Testmiljö och installation

| Alternativ | Bra för | Begränsning |
| --- | --- | --- |
| Separat testtjänst i befintlig store | Snabbt kontrollera formulär och layout med syntetiska värden. | Delar instans; byt workflow och integrationer innan provorder. |
| Separat teststore med dedikerad worker | Formulär, roller, providers och hela orderflödet med testdestinationer. | Store och worker är inte en separat lokal plattformsinstallation. Fråga om kostnad och isolering. |
| Full lokal installation | AdminWeb, UserWeb, SQL, arbetsflödesmotor, API och provisioning; även installation, uppgraderingar och plattformskonfiguration. | Kräver media, servermiljö och stöd för rätt versionskombination. |

[On-premises topologier](https://docs.zervicepoint.com/infrastructure/overview/) och [single-server-guide](https://docs.zervicepoint.com/infrastructure/single-server-setup/) beskriver lokal installation. Fullt media hämtas via [Downloads → Media](https://docs.zervicepoint.com/downloads/zervicepoint/), med begäran om åtkomst vid behov; installeraren heter `ZervicePointSetup.exe`. [Worker-paketet](https://docs.zervicepoint.com/onboarding/cloud-onboarding-worker-deployment/) hämtas från AdminWeb i en ansluten store och innehåller inte själva portalen.

I leverantörens [kravlista](https://docs.zervicepoint.com/infrastructure/requirements/) anges 4 kärnor och 16 GB RAM som minimum. Planera Windows Server/IIS, kompatibel SQL Server, DNS, TLS, tjänstekonton och identitetsleverantör. Kontrollera version och support före val av OS, SQL och arbetsflödesmotor. Äldre motor använder Workflow Manager och Service Bus. [ZerFlow-installationen](https://docs.zervicepoint.com/zerflow/ZerFlow-install-guide/) beskriver Zervicepoint 1.35 eller senare samt licensnyckel; [motorvalet](https://docs.zervicepoint.com/zerflow/Engine-selection/) beskriver drift med ny, äldre eller båda motorer. Urklippsversionen bevisar inte aktuell produktionsversion.

Ingen offentlig prislista för lokal testinstans hittades vid kontroll 2026-11-13. Kontrollera kundavtal och be leverantören specificera mediarätt, tillåten testinstans, startkostnad/årsavgift, AD-plugin och arbetsflödesmotor. Avgifter i leverantörens allmänna [villkor](https://zervicepoint.com/terms-of-service/) hänvisar till huvudavtalet. SQL Server Developer är kostnadsfri för icke-produktion enligt [Microsoft](https://www.microsoft.com/en/sql-server/sql-server-downloads); kompatibilitet med vald kombination behöver bekräftas.

Börja med en tom miljö, en exporterad tjänst och syntetisk data. Sätt upp test-AD, en egen worker där det behövs och stubb eller testinstans av TOPdesk; kontrollera att e-post och skrivningar inte kan nå produktionsmål. Testa lookup, order, återkörning och återställning separat. Importera hellre utvalda tjänster än att återställa hela produktionsdatabasen.
