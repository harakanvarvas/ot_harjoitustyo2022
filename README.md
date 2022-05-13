## Selkärangattoman aikuistumisen ajankohdan arvioija

Sovellus laskee annettujen lukujen perusteella vaillinaisen muodonvaihdoksen kautta kasvavan
selkärangattoman aikuistumisen ajankohdan viikon tarkkuudella, mikäli laskettu aikuistumisen
ajankohta on yli seitsemän päivän päässä. Lisäksi sovellus ilmoittaa kalenteriviikon, jolla
se laskee aikuistumisen tapahtuvan. Sovelluksessa on listamuotoinen kalenteri, joka näyttää
tallennetut tapahtumat. Tapahtumat on järjestetty päivämäärän mukaan pienimmästä suurimpaan.
Kalenteriin on mahdollista tallentaa tapahtumia. Tallennettavan tapahtuman muodon tulisi olla
'DD/MM/YYYY;Nimi (Valinnainen laji)', jotta kalenteri osaa tallentaa tapahtuman oikein. Kalenteriin
liittyy myös hakutoiminto, jolla tapahtumaa voi hakea nimellä, ja lisäksi tapahtuman voi poistaa
ja kalenterin tyhjentää kokonaan. Kalenteri ei tallenna duplikaatteja, eli samalle päivälle 
tismalleen samalla nimellä tallennettavia tapahtumia.

### Esimerkkejä tapahtumien tallentamisesta

Kirjoitettu tekstikenttään kohtaan *Lisää kalenteriin*:

21/12/2022;Kirppu

31/03/2023;Sirkka (Hierodula membranacea)

01/07/2023;Hämähäkki (Dolichothele diamantinensis)


### Dokumentaatio
[arkkitehtuuri.md](https://github.com/harakanvarvas/ot_harjoitustyo2022/blob/main/harjoitustyo/dokumentaatio/arkkitehtuuri.md)

[sekvenssikaavio.md](https://github.com/harakanvarvas/ot_harjoitustyo2022/blob/main/harjoitustyo/dokumentaatio/sekvenssikaavio.md)

[changelog.md](https://github.com/harakanvarvas/ot_harjoitustyo2022/blob/master/harjoitustyo/dokumentaatio/changelog.md)

[määrittelydokumentti](https://github.com/harakanvarvas/ot_harjoitustyo2022/blob/master/harjoitustyo/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito](https://github.com/harakanvarvas/ot_harjoitustyo2022/blob/master/harjoitustyo/dokumentaatio/tyoaikakirjanpito.md)



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

##### Pylint-virheiden tarkistaminen
```
python3 -m poetry run invoke lint
```


