# Arbeta vidare med Zervicepoint-skillen

- Redigera `.claude/skills/zervicepoint/SKILL.md` och direkt länkade ämnesreferenser. Håll kärnfilen kort och gör djup kunskap sökbar per ämne.
- Läs [Codex-överlämningen](docs/codex-handoff.md) innan en större import eller syntes. Analysera underlaget i en avskild arbetsyta; använd aldrig en publik commit för råmaterial.
- Bevara skillnaden mellan dokumenterad produktfunktion, observerad konfiguration, godkänt krav, förslag, lokalt testad kod och verifierad drift. Ange versions- och miljögränser.
- Publicera bara generaliserad, granskad kunskap och syntetiska exempel. Lämna verkliga personuppgifter, organisations- och behörighetsmatriser, interna ärendelänkar/ID:n, serverkonfiguration och hemligheter utanför repot. Använd en uttryckligen vald behörighetsstyrd plats om interna referenser behövs.
- Kontrollera frontmatter, relativa länkar, exempeldata och diff före commit. Ingen driftsättning, beställning eller AD-/TOPdesk-skrivning är en del av att uppdatera denna skill.
- Leverantörsdokumentationen speglas med `python scripts/sync_docs.py`. Committa aldrig `docs-cache/`; uppdatera `references/docs-catalog.md` genom att köra skriptet och synka de handskrivna referenserna (`javascript-api.md`, `form-fields.md`, `workflow-activities.md`, `datasources.md`, `platform-admin.md`, `versions.md`, `troubleshooting.md`) när release notes visar ändringar.
