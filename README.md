# Zervicepoint AI-skill

Ett första kunskapsunderlag för Claude Code och vidare analys i Codex. Det omfattar formulär och arbetsflöden, onboarding, kontobeställning, AD/Exchange/TOPdesk, testmiljöer samt portal och ikonstandard.

[Öppna SKILL.md](.claude/skills/zervicepoint/SKILL.md) för instruktioner och ämnesindex. Referenserna skiljer mellan dokumenterad plattformsfunktion, lokala observationer, projektbeslut och förslag. Ingen integration eller publicering i Zervicepoint sker när skillen används.

Leverantörens dokumentation på docs.zervicepoint.com är indexerad: [katalogen](.claude/skills/zervicepoint/references/docs-catalog.md) listar alla sidor med rubriker, och ämnesreferenserna sammanfattar JavaScript-API, fält, aktiviteter, datakällor, plattform, versioner och felsökning. Hämta den lokala fulltextspegeln, eller uppdatera den efter nya releaser, med:

```bash
python scripts/sync_docs.py
```

Spegeln hamnar i `.claude/skills/zervicepoint/docs-cache/`, som är gitignorerad eftersom texten är leverantörens. Skriptet kräver bara Python 3 och nätåtkomst.

Kör Claude Code från repots rot och anropa `/zervicepoint`. För ett annat projekt, kopiera hela `.claude/skills/zervicepoint/` till projektets motsvarande katalog. Se [Claude Codes dokumentation](https://code.claude.com/docs/en/skills).

För nästa datagenomgång: börja i [AGENTS.md](AGENTS.md) och använd [uppdragsunderlaget](docs/codex-handoff.md). Repot är publikt; exemplen är syntetiska och råmaterial ska hållas i en separat behörighetsstyrd arbetsyta.
