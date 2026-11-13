---
name: zervicepoint
description: Utvecklar och granskar Zervicepoint-tjänster, formulärexporter, Z()-JavaScript, arbetsflöden, PowerShell-plugins och beställningsportaler. Använd för onboarding, Nytt användarkonto, rollprofiler, VoO, IFO, ZF, AD/Exchange/TOPdesk, felsökning, testmiljöer eller portalens innehåll och ikoner.
---

# Zervicepoint

Utgå från användarens aktuella export och uttryckligen godkända ändringar. Arbeta på svenska om inget annat anges. Behåll exakta tekniska fältnamn, variabler och enumvärden där källan kräver det; skilj visningsetikett från sparat värde.

## Läs rätt referens

| När frågan gäller | Läs |
| --- | --- |
| Formulär-JSON, `Z()`, layout, validering, arbetsflöde, import eller Event 1023 | [Formulär och arbetsflöden](references/forms-workflows.md) |
| Onboarding, rollprofiler, fält, utbildning, behörigheter och utrustning | [Onboarding](references/onboarding.md) |
| Nytt användarkonto, VoO, IFO, ZF, Unit4 och leveransstatus | [Nytt användarkonto](references/account-order.md) |
| Eget plugin, provider-konfiguration, AD, Exchange eller TOPdesk | [Plugins och integrationer](references/plugins.md) |
| Förstasida, innehållsblock, katalogstruktur och ikoner | [Portal och katalog](references/portal.md) |
| Installation, teststore, worker, versioner, licens och miljöval | [Testmiljöer](references/environments.md) |
| Dokumentationslänkar, källkritik och versionsstöd | [Källor](references/sources.md) |
| Syntetiskt exempel på rollprofil som underlag för ett eget plugin | [Rollprofilsexempel](examples/role-profile.example.json) och [Onboarding](references/onboarding.md) |

## Arbeta i den här ordningen

1. Identifiera leveransen och miljön. Skilj **formulärets urklipps-JSON**, **arbetsflödets urklipps-JSON**, **tjänst/process via Management API** och **providerkonfiguration på servern**. Låt metadata i källexporten avgöra format, version och beteende.
2. Kartlägg berörda fält, bindningar och händelser. Sök i nästlade sektioner, övriga JavaScript-händelser, villkor och det som faktiskt skickas till nästa system. Om färsk källa saknas: lämna plan, diffskiss eller syntetiskt exempel och ange vad som krävs för säker import.
3. Ändra minsta godkända yta. Bevara övriga ID:n, ordning, kultur, typer, befintliga val och plattformsspecifik metadata. Katalogisera och föreslå större omtag separat från beställd ändring.
4. Verifiera rätt nivå: JSON-struktur, syntax, bindningar och lokalt simulerade scenarier först; separat provimport och körning i Zervicepoint med testintegrationer därefter. Dra ingen slutsats om produktion från en simulerad körning.
5. Redovisa per tjänst eller ärende vad som ändrades, vad som testades, vad som fortfarande är öppet och nästa handgrepp. Påstå aldrig att en ändring är importerad, publicerad eller aktiv i AD/TOPdesk utan bevis från den miljön.

## Hantera data och externa system

- Arbeta med syntetiska testpersoner och konfigurationsplatshållare. Lämna råexporter, ärendebilagor, interna kataloger, driftuppgifter och hemligheter utanför det publika repot.
- Validera rollprofil, tillåtna åtgärder, behörighetsnivå och användarens rätt att beställa på serversidan. Formulärets visning är inte behörighetskontroll.
- Ärendet kan ge beställaren användarnamn, e-postadress och besked om hur första inloggningen går till. Förmedla eventuella starthemligheter via en godkänd separat kanal; lägg dem inte i ärendetext, ordervariabler eller loggar.
- Dokumentera okända pluginversioner, dubbletter, målmappningar och miljöskillnader som öppna frågor. Gissa inte AD-attribut, sökväg, katalog-ID eller API-kontrakt.
- Använd bara den avsedda testmiljön vid exekvering; behandla kopierade workflows som potentiellt skrivande tills deras destinationer har kontrollerats.
