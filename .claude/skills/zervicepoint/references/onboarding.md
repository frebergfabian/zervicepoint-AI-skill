# Onboarding

Målet är en långlivad beställning för ny medarbetare. En ansvarig ska kunna uppdatera rolltexter och standardpaket utan att redigera HTML i formulärets JavaScript.

## Profil och regelmodell

- Navigera **Sektor → arbetsplats → titel**. Använd stabila ID:n för organisation, arbetsplats, titel och profil; skilj dem från svenska etiketter. Håll person, anställning och fysisk arbetsplats isär.
- Förslag för upplösning: gemensam grund → sektorsstandard → arbetsplatsens standard → titelprofil → uttryckligen godkända avvikelser. Definiera merge-/ersättningsregler, prioritet, förbud, konfliktutfall, saknad profil och giltighetsperiod innan implementation. Ge inget automatiskt utökat paket vid okänd match.
- Klassificera varje post som obligatorisk, förvald eller valbar; klassificera leveransen separat som automatiserad, synkad, manuell eller villkorad. Spara källa, systemägare/ansvarig funktion, godkännandekrav, profilversion och motivering. Versionssätt rolltexter och regler med granskningsbar publicering.
- Formuläret visar aktuell rekommendation. Servern löser om och validerar beställningen; spara version och ögonblicksbild av det faktiskt beslutade paketet på ordern. Historiska order får inte ändras när en profil redigeras. Avvikelse och extrasystem kräver motivering och vid behov separat godkännare.
- Eget plugin kan erbjuda datakällor för sektor, arbetsplats, titel och profil och en aktivitet för servervalidering/snapshot. Föreslagna namn, inte installerade: `Get-OnboardingSectors`, `Get-OnboardingWorkplaces`, `Get-OnboardingTitles`, `Get-OnboardingProfile`, `Resolve-OnboardingOrder`. Testa kontraktet med syntetiskt exempel under `examples/`.

## Fältkarta

| Avsnitt | Fält och logik att ta ställning till |
| --- | --- |
| Beställare och ansvar | Beställare från system, ansvarig chef, kontaktperson, leveransplats, eventuellt godkännare. |
| Person och anställning | Tilltalsnamn, efternamn, personidentifiering endast där godkänd och nödvändig, anställningsform, start, slut vid tidsbegränsning, återanställning/befintligt konto. |
| Organisation och roll | Sektor, organisatorisk enhet, arbetsplats, titel, extra arbetsplats/titel vid behov, sökbar fakturareferens/ZF där infört. |
| Konto och första inloggning | Konto, e-post, visningsnamn, åtkomst från rätt datum, MFA-registrering, återanvändning eller säker överlämning till beställaren. |
| System och behörigheter | Visa profilens standard och vad som synkas. Separera extra behörigheter, motivering, uppdragsenheter och godkännanden. Kontrollera systemägares regler för särskild åtkomst. |
| Utrustning och telefoni | Dator/Chromebook, skärm, docka/tillbehör, mobil, abonnemang, SIM, återanvändning, leverans/upphämtning, ev. katalogpris. |
| Fysisk åtkomst | Tagg/passerkort, nycklar, vilka lokaler och tillträdesbehov, giltighetsdatum, ansvarig utförare. SITHS vid rollbehov, med egen handläggning. |
| Sammanställning | Vald profil, förval och avvikelser, automatiskt/synkat/manuellt, datum, kostnad där känd, tydligt vem som gör vad. |

Tidigare presentationsformulär var ett fristående exempel med statiska val och villkorad visning för bland annat datum, utbildning, system, SITHS och tagg. Det provisionerade ingenting. Vid ombyggnad: börja med representativa profiler och utförande via strukturerad ärendedata; automatisera stegvis efter provkörning. Komplettera med dag ett, uppföljning, återförsök, ägarskap för manuella steg och överlämning till ändring/avslut av konto.

## Sektor utbildning: nulägesbild att bekräfta

Välj först organisatorisk väg: särskilj central utbildning/CEBH från skolpersonal/pedagogisk omsorg; verifiera koder, titelunderlag och verksamhetsindelning mot aktuell förteckning.

| System | Beskrivet arbetssätt |
| --- | --- |
| Edlevo | Skoladministratörer lägger upp nyanställda lärare. Grunden för flera efterföljande synkar. |
| SchoolSoft | Synk från Edlevo; skolans behörighetsstyrning behöver bekräftas. |
| Google Workspace for Education och Skolon | Synk från Edlevo enligt nulägesbild. |
| Dugga | App via Skolon. |
| Tyra (förskola) | Synk från SchoolSoft enligt nulägesbild. |
| Widgit Online | Manuell hantering av skoladministratör. |
| Skola24 Schema | Manuell samordning med utsedd systemkontakt. |
| ILT | Begreppa, Polylino (F–9), Polyglutt (F) enligt det lämnade underlaget; bekräfta produkt och nivå per roll. |
| Prorenata | Elevhälsoteam; hanteras via ansvarig systemfunktion. |

En synkad post ska beskriva källa, ansvar, beroende och uppföljning, så att workflow inte skapar en dubblett. Lokala kontaktpersoner och verkliga roll- och behörighetsmatriser förvaras i den behöriga verksamhetskällan.
