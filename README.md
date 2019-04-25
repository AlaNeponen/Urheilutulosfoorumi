# Urheilutulosfoorumi: #
Ideana on laatia järjestelmä, jossa säilytetään otteluiden tuloksia, ja jossa käyttäjät voivat
kommentoida ottelua *(ikään kuin keskustelufoorumin lankaa)*. Käyttäjät voivat lisätä ottelutuloksia
antamalla ajan, paikan (tapahtuman nimen, liigan nimen yms.) kilpailevien joukkueiden nimet, sekä tuloksen. Järjestelmän ylläpitäjällä on kyky poistaa valheellisia tuloksia, sekä epäasiallisia kommentteja **:^)**.

## Toimintoja: ##
* Kirjautuminen ja käyttäjän hallinta
* Kommentin lisääminen
* Ottelun lisääminen
* Kommentin poistaminen (*admin*)

### Käyttöohje ###
* Luo uusi käyttäjä kohdasta **create a new account** (aseta itsellesi käyttäjänimi ja salasana)

* Kirjaudu sisään kohdasta **login**

* Postatut ottelut näet painamalla **a list of matches**
  * Jokaisen ottelun kohdalla on painike **See comments** jonka avulla voi siirtyä tarkastelemaan ottelun kommentteja sekä lisäämään oman kommenttisi

* Voit lisätä uuden tuloksen sivustolle kohdasta **Add a new match**
  * **Huom!** Päivämäärä tulee tallettaa **täysin** samassa muodossa kuin annettu esimerkki (eli esim. *05 05 2022*) mukaanlukien välilyönnit :^) *(I could maybe update this, yes?)*
  
* Kun olet kirjautunut sisään, voit tarkastella itse postaamiasi otteluita sekä muuttaa tilisi tietoja, tai poistaa tilisi kohdasta **My account**

* Voit kirjautua ulos kohdasta **logout**, ja etusivulle voit palata painamalla isoa **Urheilutulosfoorumi** -painiketta :^)

### Asennusohje (for Linux) ###
*Tarvitset koneellesi ainakin python3:n, git:in sekä sqlite3:n*
* Aloita kloonamalla repo koneellesi *(is safe I promise :-D)*
* Navigoi lataamasi kansion sisälle
* Luo virtual environment komennolla `python3 -m venv venv`
* Aktivoi kyseinen environment komennolla `source venv/bin/activate`
* Lataa muut vaatimukset komennolla `python3 -m pip install -r requirements.txt`
* Käynnistä sovellus komennolla `python3 run.py`
* Avaa terminaaliin tulostunut osoite selaimessa
* Voit myös tarkastella paikallista tietokantaa sqlite3:n avulla navigoimalla kansion *application* sisälle, ja suorittamalla siellä komennon `sqlite3 matches.db`

* **Huom!** Uuden käyttäjän luominen asettaa käyttäjälle vakiona roolin **USER**. Helpoin tapa luoda **ADMIN** roolilla varustettu käyttäjä on asettaa kyseisen käyttäjän tiedot suoraan tietokantaan. Tämä onnistuu paikallisesti avaamalla tietokanta tarkasteluun ylläolevan komennon avulla, ja syöttämällä halutut tiedot suoraan tietokantaan komennolla `INSERT INTO account (username, password, role) VALUES ('haluamasi käyttäjänimi', 'haluamasi salasana', 'ADMIN');`

### Linkkejä: ###
* [Linkki sovellukseen](https://urheilutulosfoorumi.herokuapp.com/ "urheilutulosfoorumi")
* [User Story:t](https://github.com/AlaNeponen/Urheilutulosfoorumi/blob/master/documentation/UserStories.md)
* [Linkki tietokantakaavion hahmotelmaan](https://github.com/AlaNeponen/Urheilutulosfoorumi/blob/master/documentation/Tietokantakaavio.jpg)

#### Testitunnukset sovelluksen kokeilemiseen ####
*(Feel free to create your own account though :^))*

* Username: test_user
* Password: tester_01

Admin_user: 
  * Username: admin
  * Password: admin
