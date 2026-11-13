# Nytt användarkonto: lägesbild och regressionspunkter

Det här är utvecklingshistorik från chatt, formexport och lokala kontroller; använd färsk export och de godkända ärendespecifikationerna som källa för nästa ändring. Den senast granskade formulärkopian är från 2026-11-04, urklippsschema 1, Zervicepoint `1.34.5202`. Den aktuella produktionsversionen och driftstatusen är inte fastställda här.

| Område | Känt från lokalt arbete | Återstår att verifiera |
| --- | --- | --- |
| IFO: struktur i AD | Organisationsbilagan beskrev namn och upplevd felmappning kring myndighetskontor kontra utförarenhet. Den räckte inte för att härleda faktiska OU-flyttar. Ingen AD-struktur ändrades i formulärleveransen. | Läs behörigt avgränsad AD-export; jämför nuvarande namn, parent och mål, separat från etiketterna i formuläret. Godkänn varje flytt. |
| IFO: behörighetslogik | Tidigare analys skiljer enhetsstyrda Lifecare-val från titelstyrda undantag såsom gruppchef och familjerättssekreterare. En borttagen visningstitel kan behöva leva kvar som dataurval. | Stäm av aktuella värden med systemägaren och med färsk export. Här finns ingen komplett behörighetsmatris. |
| VoO: Avgiftshandläggare | Den befintliga titelstyrda informationsrutan uppdaterades med Lifecare-roller, dataurval, handläggarregister och Procapita VoO Avgifter från specifikationen. Källans upprepade rollrad bevarades. | Importera i test, välj titel, kontrollera informationsblock och byte till annan titel. Kopiera inte behörighetslistan från en äldre chatt. |
| VoO: bredare titeluppdatering | `ddTitelVoo` uppdaterar `#information`. Senare VoO-kopia innehåller tio beskrivningar och nio preciserade titelval enligt lokalt testunderlag. Samma avsnitt berör bland annat anmälans enhetsval och Unit4 som tillval. | Kontrollera bas- och varianttitlar, onLoad/onChange, att byten rensar gammal visning samt att tillval och enheter bara krävs när de är relevanta. |
| ZF: nytt konto | `fakturareferensZF` i `fsFaktureringZF`: sökbart obligatoriskt val i den aktiva utvecklingsvarianten, 178 alternativ i verifierad kopia. Etikett = verksamhet + kod; värde = kod. Lokal simulering kontrollerade att ZF nådde ärendedatan. Det godkända omtaget behöll listan inbäddad. | Provimport, verifiera verklig TOPdesk-payload, tidpunkt för införande och vilket AD-attribut backend ska skriva. Den dolda förberedelsevarianten är en separat kopia; välj en införandevariant. |
| ZF: ändra konto och befintliga konton | Krav på ZF även vid ändring; bulkimport till befintliga konton är ett separat uppdrag. | Implementera och verifiera ändringstjänstens egen bindning och AD-skrivning när mål och tidpunkt är bekräftade. |
| Datum och tillval | Lokalt arbete omfattar villkorat slutdatum för timvikarie/visstid, kalenderdagsjämförelse mot startdatum och villkorade systemavsnitt. Unit4 har eget krav på enhetsval när attest valts. | Testa byte av anställningsform, tidszon, omvända datum, förifyllda val, avmarkering och submit. |

## Kända gränssnitt i formuläret

- `ddSektor` och `ddAvd` är organisationsval; använd faktisk organisationskälla och behåll värde/etikett isär. Tidigare analys pekade ut `Get-SektorKund`/CSV som källa; kontrollera namnet och aktuellt kontrakt på målet.
- `ddTitelVoo` har `onLoad` och `onChange`; följ båda vägarna vid ändring. `information` är en `TextBlockRTF` i den granskade kopian. Lokalisera andra referenser innan fält eller rollalternativ döps om.
- `ddSystembehorighet` styr separata systemsektioner. `unit4Enheter` beror på aktiverat Unit4 och attest; kontrollera det sparade värdet på tillvalet.
- `topdeskRequest` är ett bundet dolt fält med `onSubmit`; inspektera hur det och `objectJson` byggs. Kontrollera att testvärdet skickas hela vägen istället för att bara synas i formuläret.

## Vad arbetsflödeskopian visar

Inklistrad workflow-export visar `Topdesk / Activity.Topdesk / New-TDincident` och därefter en statusaktivitet. Exempel på bindningar: `requestString` ← `topdeskRequest`, `objectJson` ← motsvarande variabel, datum från `dtStartDatum`/`dtAvslutDatum` och korrelation med `System.Order.Id`. Det finns ingen AD-skapande aktivitet i den kopian.

Två granskningspunkter, inte godkända kodändringar: statussteget refererar `TDincidentNumber` medan provider-resultatet var obundet i exporten; verifiera om någon annan mekanism tilldelar värdet. En anpassad TOPdesk-parameter hade samtidigt provtext och datumbindning i representationen; kontrollera verklig parametersemantik i provider och testärende.

Skilj lokalt ändrad kod, lokalt testade event, import och faktisk integration. Varken verifierad AD-skrivning, verkligt testärende eller publicering är styrkt av de lokala kontrollerna.
