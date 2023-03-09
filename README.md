# Flunky-Map

## Esittely
### Tämä sovellus on osa kurssia "Tietokantasovelus", joka on tietojenkäsittelytieteen harjoitustyökurssi, jossa toteutetaan tietokantaa käyttävä web-sovellus.

Sovellus on tietokantaan perustuva karttasovellus, jolla näytetään flunkyyn soveltuvat pelipaikat. Pelipaikkojen lisäys karttaan tapahtuu käyttäjän antamien parametrien pohjalta. Lisäksi sovelluksessa on forum-palsta, jossa voi esimerkiksi sopia etukäteen flunkyottelusta tai keskustella lajin säännöistä. 

Karttapohjana tulen käyttämään Mapboxin tarjoamaa gl js API-rajapintaa. 

Tulen viemään sovelluksen tuotantoon jaettavaksi useille käyttäjille. Tähän tarkoitukseen tulen todennäköisesti käyttämään fly.io-palvelua.  

# Mikä flunky?

## Flynky
  -	Alun perin Saksasta rantautunut urheilullinen ja seurallinen peli, josta on syntynyt useita pieniä muutoksia sisältäviä variaatioita. Perusidea on kuitenkin hyvin sama, joten jos osaat pelata esimerkiksi pallon kanssa osaat myös pelata frisbeen kanssa.

### Katso esittelyvideo painamalla alla näkyvää kuvaa! (uusi ikkuna avautuu youtubeen)

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YfvTQjoIykY/0.jpg)](https://www.youtube.com/watch?v=YfvTQjoIykY)

## Muuta, kehityksen tila yms.
  - Sovelluksen keskeneräinen versio on testattavissa fly.io:ssa https://flunkymap.fly.dev/
  - Sijannit näkyvät kartalla. Aina sijainnit eivät kuitenkaan ensiyrittämällä lataudu, vaan tämä pitää tehdä päivittämällä sivu uudelleen. 
  - Lomake uuden sijainnin lisäämiseksi toimii *tarpeeksi* hyvin. Aluksi submit-painiketta painamalla käyttäjä saattaa luulla, ettei lähettäminen onnistunut. Käyttäjän pitää kuitenkin odottaa muutamasta sekunnista minuuttiin, että hänet ohjataan "thank you!"-sivulle.  
  - Koodi vaatii vielä runsaasti siistimistä ja kommentointia logiikan ymmärtämiseksi.
