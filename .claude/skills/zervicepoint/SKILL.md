---
name: zervicepoint
description: Utvecklar och granskar Zervicepoint-tjänster, formulärexporter, Z()-JavaScript, arbetsflöden, datakällor, PowerShell-plugins och beställningsportaler, med indexerad leverantörsdokumentation (docs.zervicepoint.com). Använd för formulärfält, Z.call, aktiviteter, ZerFlow, versionskrav, roller, REST/PowerShell-API, onboarding, Nytt användarkonto, rollprofiler, VoO, IFO, ZF, AD/Exchange/TOPdesk, felsökning, testmiljöer eller portalens innehåll och ikoner.
---

# Zervicepoint

Utgå från användarens aktuella export och uttryckligen godkända ändringar. Arbeta på svenska om inget annat anges. Behåll exakta tekniska fältnamn, variabler och enumvärden där källan kräver det; skilj visningsetikett från sparat värde.

## Läs rätt referens

| När frågan gäller | Läs |
| --- | --- |
| Arbetssätt för formulärexport, layout, verifiering, import eller Event 1023 | [Formulär och arbetsflöden](references/forms-workflows.md) |
| `Z()`-metoder, `Z.call`, `Z.service`, händelser, förbjuden DOM-manipulation | [Z()-API](references/javascript-api.md) |
| Fälttyper, inställningar, variabeltyper, systemvariabler, urklipps-JSON för formulär | [Formulärfält och JSON](references/form-fields.md) |
| Inbyggda aktiviteter, egna PowerShell-aktiviteter, grouped activity, delad process, workflow-JSON, ZerFlow | [Arbetsflöden och aktiviteter](references/workflow-activities.md) |
| Dropdown-datakällor, webservices, tabeller, `$config`, rollfiltrering, CWS-drift | [Datakällor](references/datasources.md) |
| Tjänster, drafts/versioner, roller, sidor/tabeller, PowerShell- och REST-API | [Plattform och administration](references/platform-admin.md) |
| Vilken version en funktion kräver, nyheter och brytande ändringar | [Versioner](references/versions.md) |
| Felmeddelanden, händelse-ID och kända problem | [Felsökning](references/troubleshooting.md) |
| Hitta rätt sida i leverantörens dokumentation (alla 289 sidor) | [Dokumentationskatalog](references/docs-catalog.md) och fulltext i `docs-cache/` |
| Onboarding, rollprofiler, fält, utbildning, behörigheter och utrustning | [Onboarding](references/onboarding.md) |
| Nytt användarkonto, VoO, IFO, ZF, Unit4 och leveransstatus | [Nytt användarkonto](references/account-order.md) |
| Eget plugin, provider-konfiguration, AD, Exchange eller TOPdesk | [Plugins och integrationer](references/plugins.md) |
| Förstasida, innehållsblock, katalogstruktur och ikoner | [Portal och katalog](references/portal.md) |
| Installation, teststore, worker, versioner, licens och miljöval | [Testmiljöer](references/environments.md) |
| Dokumentationslänkar, källkritik och versionsstöd | [Källor](references/sources.md) |
| Syntetiskt exempel på rollprofil som underlag för ett eget plugin | [Rollprofilsexempel](examples/role-profile.example.json) och [Onboarding](references/onboarding.md) |

## Slå upp i leverantörens dokumentation

Ämnesreferenserna ovan är en granskad syntes av docs.zervicepoint.com (genomgången 2026-11-13). För exakta detaljer, kodexempel eller ämnen som inte täcks: sök i den lokala fulltextspegeln `docs-cache/` (Grep efter metodnamn, felkod eller rubrik) och använd [katalogen](references/docs-catalog.md) för att hitta rätt sida. Saknas `docs-cache/`, eller behövs färsk dokumentation, kör `python scripts/sync_docs.py` från repots rot. Spegeln är leverantörens upphovsrättsskyddade text och committas inte. Citera sparsamt och länka till originalsidan. Ange versionskrav när svaret beror på en funktion; dokumentationen beskriver senaste versionen, som inte behöver vara målmiljöns.

## Arbeta i den här ordningen

1. Identifiera leveransen och miljön. Skilj **formulärets urklipps-JSON**, **arbetsflödets urklipps-JSON**, **tjänst/process via Management API** och **providerkonfiguration på servern**. Låt metadata i källexporten avgöra format, version och beteende.
2. Kartlägg berörda fält, bindningar och händelser. Sök i nästlade sektioner, övriga JavaScript-händelser, villkor och det som faktiskt skickas till nästa system. Om färsk källa saknas: lämna plan, diffskiss eller syntetiskt exempel och ange vad som krävs för säker import.
3. Ändra minsta godkända yta. Bevara övriga ID:n, ordning, kultur, typer, befintliga val och plattformsspecifik metadata. Katalogisera och föreslå större omtag separat från beställd ändring.
4. Verifiera rätt nivå: JSON-struktur, syntax, bindningar och lokalt simulerade scenarier först; separat provimport och körning i Zervicepoint med testintegrationer därefter. Dra ingen slutsats om produktion från en simulerad körning.
5. Redovisa per tjänst eller ärende vad som ändrades, vad som testades, vad som fortfarande är öppet och nästa handgrepp. Påstå aldrig att en ändring är importerad, publicerad eller aktiv i AD/TOPdesk utan bevis från den miljön.

## Hantera data och externa system

- Organisationsspecifika ID:n (TOPdesk-GUID:er, tjänst- och sid-ID:n, butiksadress, behörighetsmatriser) hör hemma i en privat överbyggnadsskill eller i den gitignorerade mappen `private/`, aldrig i detta repo. Finns en sådan skill installerad, läs den också.
- Arbeta med syntetiska testpersoner och konfigurationsplatshållare. Lämna råexporter, ärendebilagor, interna kataloger, driftuppgifter och hemligheter utanför det publika repot.
- Validera rollprofil, tillåtna åtgärder, behörighetsnivå och användarens rätt att beställa på serversidan. Formulärets visning är inte behörighetskontroll.
- Ärendet kan ge beställaren användarnamn, e-postadress och besked om hur första inloggningen går till. Förmedla eventuella starthemligheter via en godkänd separat kanal; lägg dem inte i ärendetext, ordervariabler eller loggar.
- Dokumentera okända pluginversioner, dubbletter, målmappningar och miljöskillnader som öppna frågor. Gissa inte AD-attribut, sökväg, katalog-ID eller API-kontrakt.
- Använd bara den avsedda testmiljön vid exekvering; behandla kopierade workflows som potentiellt skrivande tills deras destinationer har kontrollerats.
