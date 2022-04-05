## Selkärangattoman aikuistumisen ajankohdan arvioija

Tällä hetkellä sovellus arvioi aikuistumisen päivän tarkkuudella. Muutetaan myöhemmin viikon 
tarkkuuteen, sillä tarkkaa päivää on käytännössä mahdotonta arvioida täsmällisesti. Aikuistumisarvio
viikon tarkkuudella antaa todennäköisesti realistisemmat valmiudet varautua viimeiseen nahanluontiin
ja muuttaa esimerkiksi terraario-olosuhteita hyvissä ajoin nahanluontiin sopivaksi.


### Dokumentaatio
[changelog.md](https://github.com/harakanvarvas/ot_harjoitustyo/blob/master/harjoitustyo/dokumentaatio/changelog.md)
[määrittelydokumentti](https://github.com/harakanvarvas/ot_harjoitustyo/blob/master/harjoitustyo/dokumentaatio/vaatimusmaarittely.md)
[tuntikirjanpito](https://github.com/harakanvarvas/ot_harjoitustyo/blob/master/harjoitustyo/dokumentaatio/tyoaikakirjanpito.md)


### Komentorivitoiminnot

##### Sovelluksen käynnistäminen tapahtuu komennolla
```
python3 -m poetry run invoke start
```

##### Testien ajaminen tapahtuu komennolla
```
python3 -m poetry run invoke test
```

##### Testikattavuuden kerääminen ja HTML-tiedoston muodostaminen tapahtuu komennolla
```
python3 -m poetry run invoke coverage-report
```


