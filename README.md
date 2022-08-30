# Izpitogram

Projektna naloga pri predmetu Uvod v Programiranje.

Gre za spletno beležko opravil na faksu, ki je namenjena študentom za lažjo organizacijo dela čez študijsko leto. 
Uporabnik se lahko prijavi v sklopu treh znanih študijskih smeri univerzitetne stopnje študija matematike na FMF.
Nato lahko dodaja predmete na svojem obstoječem urniku ter tem predmetom dodaja tri tipe opravil: izpit, seminarska 
naloga in ustni zagovor. Ko je dodano opravilo s svojim rokom izvrštve, se v seznam opravil poleg le-tega dodata 
tudi dva druga pomembna datuma: kdaj bi se bilo dobro začet učit (7 dni pred iztekom roka) za dodano obveznost 
ter opomin za prijavo v sistemu VIS (4 dni pred iztekom roka). Da je bolj očitno katera opravila se bližajo, ima 
Izpitogram dodatno funkcijo, ki bližajoča se opravila (rok je oddaljen 7 dni ali manj) obarva na rdeče. Ko študent 
opravi določeno obveznost, jo lahko s seznama opravil odstrani z klikom na gumb 'OK'.

# Zagon programa

```
# pip -> python installation packager (instalira zunanje knjiznice)
pip install -r requirements.txt
python src/main.py
```

Podatkovna baza se pri vsaki spremembi shranjuje v database.bin. 
Ta datoteka se ustvari s python knjižnico pickle.

Le-ta te bo preusmeril na spletni vmesnik na [lokalnem naslovu](http://localhost:8080).
