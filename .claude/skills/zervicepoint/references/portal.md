# Beställningsportal, katalog och ikoner

Målet är en gemensam ingång för beställningar inom IT, HR, administration, lokaler och andra verksamheter. Felanmälan hör till supportflödet. Portalens övergripande header, sidomeny och systemstyrda favorit-/rekommendationslistor är inte redigerbara i det tillgängliga området. Utforma den egna ytan för att komplettera plattformens innehåll.

## Förstasida och publicering

- Fyra snabba ingångar: Användarkonto, Dator & tillbehör, Mobil & abonnemang, Programvara. Ge användaren en rak huvudfråga och kort beskrivning.
- Komplettera med vanliga beställningar, produktkort i en 3 × 2-grid på bred yta (t.ex. dator, mobil, skärm, headset, nytt konto, abonnemang), informationsblock och väg till orderstatus/support. Länka direkt till bekräftade mål. Skriv inte in pris och tillgänglighet i flera kopior utan ägare.
- Vid portalunderhåll: ”Vi uppdaterar Beställningsportalen. Under tiden kan korta avbrott eller tillfälliga fel förekomma. Om något inte fungerar, vänta ett par minuter och ladda om sidan.” Håll driftinformation daterad och ta bort den när den är inaktuell.
- Kontrollera vilket block och redigerarläge som faktiskt tar emot HTML. Ett tidigare försök visade rå HTML som text; ändrad CSS löser inte det. Börja med en liten testlänk eller ett formaterat stycke i rätt källa/läge. Om inline CSS är allt som tillåts, bygg med stöd för smala ytor och verifiera vilka regler, bilder och SVG som överlever redigeraren. Undvik globala overrides, tredjepartsskript och styling av låsta plattformsdelar.
- Ha tillgängliga länknamn och fokus, tillräcklig kontrast och dekorativ bild med tom alt-text där kortets text redan beskriver målet. Testa tangentbord och zoom. Blå informationspanel kan skilja meddelanden från klickbara kort.

## Ikonsystem

Standardisera kategoriikon + en liten åtgärdsmarkör. Konton: person-outline; nytt: plus; avslut: minus; ändring/behörighet: verktygssymbol. Återanvänd samma semantik över katalogen, med fast placering, optisk storlek, linjetjocklek och marginal. Skilj fotografi/produktbild från kategoriikon och kräv textetikett för betydelse. Det tidigare användandet av Google Fonts Icons är historik; ett nytt sammanhållet bibliotek kan ersätta det.

Ett enkelt Pythonbaserat ikonverktyg var ett föreslaget sidoprojekt. Lämplig funktion: importera redigerbar katalog, matcha bas + markör med stabilt tjänste-ID, granska och åsidosätt förslag, förhandsvisa i realistisk kortstorlek och exportera SVG/PNG + manifest. Uppdatera samma servicepost när modell/namn ändras. Kontrollera bildlicens och plattformens format före massbyte.

## Katalogisering

Spara källfälten namn, identifierare, typ (Service/Link), process och sidor; håll ikonnycklar och markör som tillagd metadata. Matcha inte enbart på titel eller identifierare: det historiska underlaget innehöll samma visningsnamn för olika objekt, återanvänt identifierarvärde mellan länk och tjänst, testposter, tjänster utan katalogsida, modellnamn som ändrats utan att det tekniska ID:t bytts och produkttexter som innehöll tillfälliga lagerbesked. Bekräfta unik identitet och vilket objekt som är aktivt innan batchändring.

Täck konto/behörighet, telefoni/abonnemang, datorer, surfplattor, konferens, skrivare, tillbehör, appar, e-tjänster/blanketter, omorganisation, kontakt/support och gåvor. Exempel på tjänster: nytt/ändra/avsluta konto, gemensam mapp, SITHS, programinstallation, nätverk, funktionsbrevlåda, distributionslista, bokningsbar kalender/resurs, skrivare och passertagg. Systemkatalogen innehåller bland annat Microsoft/Adobe, SEFOS, Lifecare-varianter, Raindance, Insight, Public360, Prorenata, MittVaccin och Phoniro. Verifiera omfattning och aktuell katalog separat.
