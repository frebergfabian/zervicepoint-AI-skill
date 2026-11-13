# Källor och vidare läsning

## Indexerad leverantörsdokumentation

Hela docs.zervicepoint.com (289 sidor, ca 1,4 miljoner tecken) indexerades 2026-11-13 med `scripts/sync_docs.py`:

- [docs-catalog.md](docs-catalog.md): genererad katalog med varje sidas titel, URL, lokal sökväg och H2/H3-rubriker som sökord. Versionshanterad.
- `docs-cache/`: lokal fulltext som Markdown, en fil per sida, plus `_manifest.json`. Gitignorerad, eftersom texten är leverantörens. Generera med `python scripts/sync_docs.py`.
- Syntetiserade, granskade referenser: [Z()-API](javascript-api.md), [Formulärfält och JSON](form-fields.md), [Arbetsflöden och aktiviteter](workflow-activities.md), [Datakällor](datasources.md), [Plattform och administration](platform-admin.md), [Versioner](versions.md) och [Felsökning](troubleshooting.md).

Kvalitet på källan: leverantörens sidor har platshållare (`reference/placeholder`, "TODO", "Add link…"), stavfel i kodexempel (t.ex. `Propery`) och delvis föråldrade sökvägar och filnamn för provider-XML. Behandla kodexempel som mönster och verifiera mot målversionen. Release notes är den bästa källan för när en funktion kom.

## Prioritering

Prioritera den senaste godkända beställningen, färsk export från rätt miljö och aktuell leverantörsdokumentation. Tidigare beslut och testresultat är värdefulla, men bevisar inte dagens konfiguration eller vad som är driftsatt. Dokumentera källa, datum och version för ändringar i detta underlag. Återanvänd sammanfattningar och länkar framför kopierad dokumentation.

| Ämne | Primära ingångar |
| --- | --- |
| Översikt | [Dokumentationsindex](https://docs.zervicepoint.com/), [systemarkitektur](https://docs.zervicepoint.com/system-overview/components/), [AdminWeb](https://docs.zervicepoint.com/system-overview/adminweb/), [UserWeb](https://docs.zervicepoint.com/system-overview/userweb/) |
| Katalog och administration | [Tjänster](https://docs.zervicepoint.com/adminweb/services/), [sidor](https://docs.zervicepoint.com/adminweb/pages/), [delade processer](https://docs.zervicepoint.com/adminweb/sharedprocess/), [roller](https://docs.zervicepoint.com/adminweb/roles/), [order](https://docs.zervicepoint.com/adminweb/orders/), [e-postmallar](https://docs.zervicepoint.com/adminweb/emailtemplates/) |
| Formulär och automation | [JavaScript](https://docs.zervicepoint.com/reference/javascript/), [kaskadval](https://docs.zervicepoint.com/reference/snippets/form-cascading-dropdown/), [aktiviteter](https://docs.zervicepoint.com/reference/activity/), [datakällor](https://docs.zervicepoint.com/tutorials/data-source/), [onboardingexempel](https://docs.zervicepoint.com/tutorials/onboard-new-colleague/) |
| Plugins | [Anatomi](https://docs.zervicepoint.com/plugins/plugins/), [AD](https://docs.zervicepoint.com/plugins/plugin-active-directory/), [AD-construct](https://docs.zervicepoint.com/plugins/plugin-active-directory-construct-file/), [Exchange](https://docs.zervicepoint.com/plugins/plugin-exchange/), [providers och datakällor](https://docs.zervicepoint.com/adminweb/providers-and-datasources/) |
| API och överföring | [PowerShell](https://docs.zervicepoint.com/how-to/how-to-get-started-with-zervicepoint-powershell-management/), [REST](https://docs.zervicepoint.com/how-to/how-to-get-started-with-rest-api/), [tjänst och process mellan miljöer](https://docs.zervicepoint.com/how-to/how-to-export-and-import-services-with-zervicepoint-powershell-management/), [store-hantering](https://docs.zervicepoint.com/how-to/how-to-create-and-manage-stores-with-zervicepoint-powershell-management/) |
| Drift | [Installationsöversikt](https://docs.zervicepoint.com/infrastructure/overview/), [krav](https://docs.zervicepoint.com/infrastructure/requirements/), [versionshistorik](https://docs.zervicepoint.com/release-notes/release-history/), [felsökningsguide](https://docs.zervicepoint.com/troubleshooting/troubleshooting-guidelines/), [kontakt](https://zervicepoint.com/sv/kontakta-oss/) |

Den första kunskapsbasen utgår från tidigare portal- och onboardingarbete, en granskad formulärexport och ett inklistrat arbetsflöde. Inget komplett eller aktuellt produktionssnapshot finns i repot. Lokala verksamhetsmatriser, avtalsvillkor, full katalog, testprotokoll och driftsstatus behöver verifieras separat.
