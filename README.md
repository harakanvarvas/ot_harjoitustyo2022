## Selkärangattoman aikuistumisen ajankohdan arvioija

Sovellus laskee annettujen lukujen perusteella vaillinaisen muodonvaihdoksen kautta kasvavan
selkärangattoman aikuistumisen ajankohdan viikon tarkkuudella, mikäli laskettu aikuistumisen
ajankohta on yli seitsemän päivän päässä. Lisäksi sovellus ilmoittaa kalenteriviikon, jolla
se laskee aikuistumisen tapahtuvan. Toki on hyvä huomata, että esimerkiksi sukukypsyyden
selkärangaton useimmiten saavuttaa vasta muutama viikko aikuistumisen jälkeen, ja sen laskemiseen
tämä sovellus ei vielä sovellu. Sovellukseen lisätään vielä kalenteri, johon pystyy halutessaan 
lisäämään arvioidun aikuistumisajankohdan ja myös muuttamaan sitä tai poistamaan sen.



### Dokumentaatio
[arkkitehtuuri.md](https://github.com/harakanvarvas/ot_harjoitustyo2022/blob/main/harjoitustyo/dokumentaatio/arkkitehtuuri.md)

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


