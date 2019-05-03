# Urheilutulosfoorumi: #
Ideana on laatia järjestelmä, jossa säilytetään otteluiden tuloksia, ja jossa käyttäjät voivat
kommentoida ottelua *(ikään kuin keskustelufoorumin lankaa)*. Käyttäjät voivat lisätä ottelutuloksia
antamalla ajan, paikan (tapahtuman nimen, liigan nimen yms.) kilpailevien joukkueiden nimet, sekä tuloksen. Järjestelmän ylläpitäjällä on kyky poistaa valheellisia tuloksia, sekä epäasiallisia kommentteja.

## Toimintoja: ##
* Kirjautuminen ja käyttäjän hallinta
* Kommentin lisääminen
* Ottelun lisääminen
* Kommentin/Ottelun/Käyttäjän poistaminen (*admin*)

### Käyttöohje ###
* Luo uusi käyttäjä kohdasta **create a new account** (aseta itsellesi käyttäjänimi ja salasana)

* Kirjaudu sisään kohdasta **login**

* Postatut ottelut näet painamalla **a list of matches**
  * Jokaisen ottelun kohdalla on painike **See comments** jonka avulla voi siirtyä tarkastelemaan ottelun kommentteja sekä lisäämään oman kommenttisi

* Voit lisätä uuden tuloksen sivustolle kohdasta **Add a new match**
  
* Kun olet kirjautunut sisään, voit tarkastella itse postaamiasi otteluita sekä muuttaa tilisi tietoja, tai poistaa tilisi kohdasta **My account**

* Voit kirjautua ulos kohdasta **logout**, ja etusivulle voit palata painamalla isoa **Urheilutulosfoorumi** -painiketta :^)

    #### Ylläpitäjän ohjeet ####
    (*ohjeissa oletetaan että olet kirjautunut sisään käyttäjällä jonka roolina on **ADMIN***)
    * Voit hallinnoida käyttäjiä etusivun ***Manage users*** kohdan kautta
    
    * Otteluiden poistaminen onnistuu ottelut listaavasta näkymästä (*Add a new match*), ja kommenttien poistaminen onnistuu kommentit listaavasta näkymästä (*See comments*).
    * **Huom!** Käyttäjän poistaminen poistaa myös kaikki käyttäjän postaamat ottelut sekä kommentit. Ottelutuloksen poistaminen poistaa puolestaan myös kaikki otteluun liittyvät kommentit. 

### Asennusohje (for Linux) ###
*Tarvitset koneellesi ainakin python3:n, git:in sekä sqlite3:n*
* Aloita kloonamalla repo koneellesi
* Navigoi lataamasi kansion sisälle
* Luo virtual environment komennolla `python3 -m venv venv`
* Aktivoi kyseinen environment komennolla `source venv/bin/activate`
* Lataa muut vaatimukset komennolla `python3 -m pip install -r requirements.txt`
* Käynnistä sovellus komennolla `python3 run.py`
* Avaa terminaaliin tulostunut osoite selaimessa
* Voit myös tarkastella paikallista tietokantaa sqlite3:n avulla navigoimalla kansion *application* sisälle, ja suorittamalla siellä komennon `sqlite3 matches.db`

* **Huom!** Uuden käyttäjän luominen asettaa käyttäjälle vakiona roolin **PLEB**. Helpoin tapa luoda **ADMIN** roolilla varustettu käyttäjä on asettaa kyseisen käyttäjän tiedot suoraan tietokantaan. Tämä onnistuu paikallisesti avaamalla tietokanta tarkasteluun ylläolevan komennon avulla, ja syöttämällä halutut tiedot suoraan tietokantaan komennolla `INSERT INTO account (username, password, role) VALUES ('haluamasi käyttäjänimi', 'haluamasi salasana', 'ADMIN');`

    #### Sovelluksen siirtäminen pilveen (*Heroku*) ####
    * Jotta saisit sovelluksen toimimaan Herokussa, tulee sinulla olla asennettuna Herokun komentorivin käyttöliittymä (Heroku CLI, ohjeet löydät [täältä.](https://devcenter.heroku.com/articles/heroku-cli) Lisäksi tarvitset tunnukset Heroku-palveluun.)
    
    * Lisää sovellus Herokuun komennolla `heroku config:set HEROKU=1`
    
    * Lisää tietokanta sovelluksen käyttöön komennolla `heroku addons:add heroku-postgresql:hobby-dev`
    
    * Voit tarkastella tietokantaa komentorivin kautta komennolla `heroku pg:psql` (*käytä tätä esim. **ADMIN**-käyttäjän lisäämiseen INSERT INTO -lauseen avulla avulla*).

### Linkkejä: ###
* [Linkki sovellukseen](https://urheilutulosfoorumi.herokuapp.com/ "urheilutulosfoorumi")
* [User Story:t](https://github.com/AlaNeponen/Urheilutulosfoorumi/blob/master/documentation/UserStories.md)
* [Linkki tietokantakaavion hahmotelmaan](https://github.com/AlaNeponen/Urheilutulosfoorumi/blob/master/documentation/tietokantakaavio.md)
* [CREATE TABLE -lauseet](https://github.com/AlaNeponen/Urheilutulosfoorumi/blob/master/documentation/create.md)

#### Testitunnukset sovelluksen kokeilemiseen ####
*(Feel free to create your own account also!)*

* Username: test_user
* Password: tester_01

Admin_user: 
  * Username: admin
  * Password: admin
