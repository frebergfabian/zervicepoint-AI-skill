# Versioner: vad som finns från vilken release

Sammanställt ur leverantörens [release notes](https://docs.zervicepoint.com/release-notes/release-history/) (1.20–1.35.3) och funktionsreferensen, genomgånget 2026-11-13. Listan tar med det som påverkar tjänstebygge, formulär och arbetsflöden. Fullständiga noter per version finns i `docs-cache/release-notes/`. **Kontrollera alltid målmiljöns faktiska version** (`zervicepointVersion` i en urklippsexport eller AdminWeb) innan du använder en funktion.

## Senaste läget (2026-11)

| Version | Datum | Viktigt för tjänstebyggare |
| --- | --- | --- |
| 1.35.3 | 2026-11-09 | Rättning: dropdowns visade max 50 objekt, sökbara dynamiska dropdowns kunde ge fel resultat, flerradig text i dropdown, fel vid statusbyte i Approval/Task, `New-ZPVariable` med Integer. |
| 1.35.2 | 2026-10-28 | **ZerFlow-stöd** (ingen väg tillbaka till 1.34). **Gamla UI borttaget helt.** Ny variabeltyp Integer och standardvärden för andra typer än String (bara ZerFlow). Ny datumväljare. Tile-storlek per Service list. Temporära användare. Lista över skickad e-post. Validering kräver tilldelade för Task/Approval. Autocomplete för `Z.latinize()`. `Z.service` initieras för tabellstartade tjänster. ADFS för worker utfasat. |
| 1.34.5203 | 2026-05-25 | Custom domains. |
| 1.34.5202 | 2026-05-20 | Sista major före borttaget gammalt UI. Översättningar flyttas till JSON-filer i nästa major. |
| 1.34.5200 | 2026-04-23 | AdminWeb/UserWeb helt asynkrona. **`Z.latinize()`**. Kommentarer på drafts och växling mellan drafts. **Varning vid copy/paste mellan versioner.** Nya och ändrade fält/aktiviteter markeras. |
| 1.34.5139–5141 | 2025-12 – 2026-02 | Uppdatera provideraktiviteter med ett klick. While-fördröjning kan vara statisk. Variabeltyp kan inte ändras när variabeln är bunden. Tjänsteversion syns i orderdetaljer. Rättningar för grouped activity och kopierade provideraktiviteter. |
| 1.34.5090 | 2025-08-28 | Kopiera bunden variabels namn med klick. Fäll ihop och ut funktioner i JS-editorn. Länk till draft. Egna ordermodaler. |
| 1.34.4197 | 2024-11-08 | **Tabell med namn, identifierare och bindningar i JS-dialogen.** Placering av fältbeskrivning. Filter på tjänstvariabel i Order Manager. |
| 1.34.3987 | 2024-04-12 | OIDC-inloggning. Färgade knappar för task-statusar. Tjänster inbäddade på sidor. Sorteringsindex. Ctrl+S. |
| 1.34.3799 | 2023-10-11 | **`Z('#f').longDescription()`**. Kassera draft. Visa vem som slutförde task/approval. |
| 1.34.3563 | 2023-02-16 | **Lång beskrivning (infobubbla) på fält.** `System.Service.Draft`. Kategoriväljare laddar bara vid onLoad. |
| 1.34.3476 | 2022-11-18 | Rollbaserad REST-behörighet. Provisioning system events. WCAG-förbättringar. |

## Äldre milstolpar (urval)

| Version | Funktion |
| --- | --- |
| 1.6 | `Z.currentUser`, `Z.currentStore` |
| 1.8.1043 | `webserviceisolation` för CWS |
| 1.9 | `.Contains()` i rollregler utfasat → `hasClaim`/`claimIncludes` |
| 1.10.1229 | `Z('form').disable/enable`, `disable()`/`enable()`, `spin()`, `Z.call(...).spin(...)` |
| 1.13 | `valid(...)`, `require(...)` |
| 1.19 | Drafts och tjänsteversioner |
| 1.20 | Grouped activities, Set receiver, Hide submit button, egen knapptext. **Varning vid DOM-manipulation** (`getElement`/`getContainer` m.fl.). |
| 1.21.2160 | Teckengräns på textfält. `Z('#dd').val([])` rensar statisk dropdown. |
| 1.23.2320 / 2345 / 2367 | Kommentar vid publicering. RTF-block i delade processer. `lineBreak` på fält. Nyckelautentisering för ProvisioningSystem och PowerShell-API. |
| 1.24.2410 / 1.25 | **Copy/paste av fält och aktiviteter som JSON** (Ctrl+C/X/V, Ctrl+A/D). |
| 1.24.2446 / 1.25 | **Form functions** (JS-klasser i databasen, `*-ZPJavaScript`, `New-ZPForm -FormFunction`). |
| 1.24.2466 / 1.25 | **`Z.service`** |
| 1.25 | Länkar som ser ut som tjänster. Leverantörens snippets byggda i denna version. |
| 1.25.2549 | DateTime "Default to current date". Visa variabelanvändning. |
| 1.26.2592 | **Knappar i formulär** (`onClick`) |
| 1.29.2822 | REST API |
| 1.30.2958 | **`isValid()`, `visible()`**. Max filstorlek per fält och butik. **Tillfälligt inaktivera aktiviteter och fält.** |
| 1.30.3069 | Parallel får blanda alla aktivitetstyper |
| 1.30.3118 | Kortbeskrivning i Approval. Task-variabler i e-postmallar. |
| 1.31.3196 | Then/Else i Conditional. Plugins-vy. Ny datakällsväljare. Autocomplete av Z-selektorer. API-order kan fylla readonly-fält. |
| 1.32.3257 | Datumintervall och veckodagar i datumväljaren. Microsoft Graph i stället för Azure AD Graph. |
| 1.33.3327 | Egna färger och banner. Hybridautentisering för API. |

## Praktiska följder

- En miljö på 1.34.5202, den version det granskade formulärunderlaget i detta repo kom från, stöder enligt noterna `longDescription()`, `isValid()`/`visible()`, `Z.service` och `Z.latinize()`. Den saknar Integer-variabler, ZerFlow-specifika standardvärden och 1.35-rättningen för dropdowns med fler än 50 objekt.
- Vid uppgradering till 1.35: inventera DOM-manipulation (gamla UI är borta), testa Code-aktiviteter (ny V8), datumhantering (ISO 8601) och Parallel-ordning (ZerFlow). Se [Arbetsflöden](workflow-activities.md#zerflow-ny-arbetsflödesmotor-135).
