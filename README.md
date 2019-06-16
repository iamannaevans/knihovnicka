# twisto-knihovnicka
Sbirka zajimavych knih a sledovani kdo si co aktualne vypujcil

Anno, resim nasledujici problem: mam sbirku zajimavych papirovych knizek,
ktere jsou pro me velice cenne. Moji kamaradi si ode mne radi tyto knihy pujcuji,
bohuzel vsak ne na kazdeho je spoleh a stava se, ze mi vypujcenou knihu nevrati.
Takova situace je pro me vzdy velmi neprijemna, a proto jsem si rekl,
ze by bylo fajn mit misto, kde budu svoji sbirku a vypujcky spravovat.

Maly webik se mi jevi jako uplne nejlepsi varianta.
Webovy framework Django a databaze PostgresQL budou idealnimi pomocniky.

Chtel bych evidovat uplne zakladni informace o titulech a autorech
(autor, nazev publikace, rok publikace, neco co by te napadlo jeste?)
Chtel bych umet zobrazit vsechny svoje knizky, vsechny od jednoho autora,
vsechny aktualne vypujcene.
Strohy detail knihy a zda je aktualne v me knihovnicce, nebo v kapse u kamarada.
Kdyz si nekdo knizku vypujci, tak chci vedet, kdy mi ji vrati. Bylo by fajn vedet,
kdo si knizku pujcoval, abychom se o ni mohli napr. u pivu nekdy pobavit.

#### 🍒
Pokud bych dokazal vyhledavat dle nazvu knihy, byl bych uplne stastny :)

#### Technicke detaily
domnivam se, ze na vsechny 'how to' otazky ti da odpoved tento uvodni tutorial
https://docs.djangoproject.com/en/2.2/intro/ ,
pokud bych se vsak mylil, nevahej a ptej se, rad ti pomuzu.

Django ti nedovoli vytvorit projekt do existujiciho adresare,
proto doporucuji vytvorit zvlast a pote nastavit git origin a pull'nout si.

https://github.com/strelnikov/twisto-knihovnicka-anna.git

Ostatnim vecem se meze nekladou, ponechavam to plne v tve rezii.
Frontend/grafiku resit neni potreba.


Hodne zdaru a tesim se na vysledek.
Dmitrij

---

## Install

###### Python
1. Download [Python 3](https://www.python.org/downloads/)
2. Install
3. Check you installed Python correctly by pasting the following code into shell
```shell
python -V
```

###### PostgreSQL database
1. Download [PostgreSQL](https://www.postgresql.org/)
2. Install
3. Open PgAdmin
4. Create a new database
  - Name: postgres
  - Password: postgres

###### Clone repository
1. Open shell and paste the following code
```shell
git clone https://github.com/strelnikov/twisto-knihovnicka-anna.git
cd twisto-knihovnicka-anna
```

###### Virtual environment
1. Create a virtual environment by pasting the following code into shell
```shell
python -m venv venv
```
2. Activate virtual environment by pasting following code into shell (Windows)
```shell
venv\Scripts\activate
```
or macOS
```shell
$ source venv/bin/activate
```

###### Requirements
1. Paste the following code to shell
```shell
pip install -r requirements.txt
```

## Initialize
###### Migrate
1. Paste the following code into shell
```shell
python manage.py migrate
```

###### Create superuser
1. Paste the following code into shell
```shell
python manage.py createsuperuser
```
2. Follow the instructions in shell


## Import initial data (optional)
1. Paste the following code into shell
```shell
python manage.py loaddata data.json
```

## Run

###### Run Server
1. Paste the following code into shell
```shell
python manage.py runserver
```
2. Open the link the console displays
3. Add '/admin' to the url
4. Log in with your superuser
5. Add data to your database
