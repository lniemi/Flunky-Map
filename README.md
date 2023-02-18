# Flunky- ja kyykkäkartta

## Esittely
### Tämä sovellus on osa kurssia "Tietokantasovelus", joka on tietojenkäsittelytieteen harjoitustyökurssi, jossa toteutetaan tietokantaa käyttävä web-sovellus.

Sovellus on tietokantaan perustuva karttasovellus, jolla näytetään flunkyyn ja kyykkään soveltuvat pelipaikat. Pelipaikkojen lisäys karttaan tapahtuu käyttäjän antamien parametrien pohjalta. Lisäksi sovelluksessa on toiminto, jolla voi sopia etukäteen flunkyottelusta. 

Karttapohjana tulen käyttämään Mapboxin tarjoamaa gl js API-rajapintaa. 

Sovelluksen kehittyessä on tarkoitus myös lisätä edistyneempiä toimintoja, kuten mahdollisesti turnauksen suunnitteleminen tai ottelun lisääminen automaattisesti telegram-botin kanssa, mikäli botti huomaa määrätylle kanavalle tulleen viestin suunnitellusta flunky- tai kyykkäottelusta (Huom. telegrambotti on tärkeyslistassa viimeisimpänä). Myös pelipaikoille tulee kehittää erilaisia ominaisuuksia, kuten mahdollisuus arvostella sijaintia esimerkiksi väljyyden tai ympäristön rauhallisuuden perusteella. 

Tulen viemään sovelluksen tuotantoon jaettavaksi useille käyttäjille. Tähän tarkoitukseen tulen todennäköisesti käyttämään fly.io palvelua tai mahdollisesti olen myös valmis kokeilun nimissä maksamaan herokun palveluista.  

# Mikä kyykkä? Mikä flunky?

## Kyykkä
  - Vuosisatoja vanha karjalainen ulkona pelattava peli. https://fi.wikipedia.org/wiki/Kyykk%C3%A4

## Flynky
  -	Alun perin Saksasta rantautunut urheilullinen ja seurallinen peli, josta on syntynyt useita pieniä muutoksia sisältäviä variaatioita. Perusidea on kuitenkin hyvin sama, joten jos osaat pelata esimerkiksi pallon kanssa osaat myös pelata frisbeen kanssa.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YfvTQjoIykY/0.jpg)](https://www.youtube.com/watch?v=YfvTQjoIykY)

## Muuta, kehityksen tila yms.
  - Sovelluksen keskeneräinen versio on testattavissa fly.io:ssa https://flunkymap.fly.dev/
  - Sijannit näkyvät kartalla
  - Lomake uuden sijainnin lisäämiseksi toimii *tarpeeksi* hyvin tietokoneen selaimella. Mobiiliselaimella lomake ei kuitenkaan mukaudu näytölle ikkunan koon mukaisesti. 
  - Profiilisivu on tekemeättä. 
  - Kuvien näyttäminen ei 'all locations' sivulla onnistu. Kuvat siirtyvät tietokantaan kuitenkin lomakkeen kautta. 
