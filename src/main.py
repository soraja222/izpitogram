'''
modul, ki zažene aplikacijo
'''

from datetime import date
import db
from domain import *
from bottle import route, run, template, view, redirect, request
import os

#db.napolni() za development želimo podatkovno bazo na začetku napolniti z že ustvarjenimi podatki, ki nam bodo olajšali testiranje
db.load() #na žačetku, če je podatkovna baza že ustvarjena in obstaja v shranjeni datoteki, želimo to datotkeo prebrati in napiolniti podatkovno bazo z temi podatki.

def uporabnik_find(full_name):
    '''
    iščemo uporabnika po njegovem polnem imenu, npr.: Soraja_Sekavcnik
    '''
    imePriimek = full_name.split('_')
    for uporabnik in db.uporabniki:
        if uporabnik.ime == imePriimek[0] and uporabnik.priimek == imePriimek[1]:
            return uporabnik

@route('/uporabniki/<full_name>')
@view('uporabnik')
def uporabnik(full_name):
    '''
    začetna spletna stran trenutnega uporabnika, kjer se nahajajo njegova opravila in predmeti
    '''

    uporabnik = uporabnik_find(full_name) #poiščemo uporabnika v podatkovni bazi
    if uporabnik is None:
        redirect('/') #če uporabnika ne najdemo, trenutnega uporabnika prevežemo na domačo stran

    opravila = [] #za trenutnega uporabnika poiščemo vsa opravila in jih dodamo v ta spisek
    for predmet in uporabnik.predmeti:
        for opravilo in predmet.opravila:
            if opravilo.opravljen not in ['True', True, 1, '1']:
                opravila.append(opravilo)

    now = date.today()
    return {
        'uporabnik': uporabnik, #vrnemo informacije o uporabniku
        'predmeti': uporabnik.predmeti,
        'opravila': opravila,
        'opravilo_action': f'/uporabniki/{full_name}/opravilo', #vrnemo informacijo, kjer lahko uporabnik ustvari opravilo ali predmet
        'predmet_action': f'/uporabniki/{full_name}/predmet',
        'leto': now.year,
        'mesec': now.month,
        'dan': now.day
    }
    
    
@route("/uporabniki", "POST")
@view('uporabnik_submit')
def ustvari_upoabnika():
    '''
    route kje se posredujejo informacije od forme s katero lahko uporabnik ustvari novega uporabnika
    route prikaže spletno stran na koncu, ko se uporabnik shrani v podatkovno bazo
    '''
    info = dict(request.forms)
    db.uporabniki.append(Uporabnik(info['ime'], info['priimek'], info['smer'], []))
    db.save()
    return info


@route("/uporabniki/<full_name>/predmet/<predmet>/opravilo/<opravilo>/opravljen")
def opravilo_opravil(full_name, predmet, opravilo):
    '''
    route, ki se kliče, ko uporabnik opravi opravilo
    route na koncu uporabnika preveže na njegovo domačo stran
    '''
    uporabnik = uporabnik_find(full_name)
    predmet = uporabnik.predmeti[int(predmet)]
    opr = predmet.opravila[int(opravilo)]
    opr.opravljen = True
    db.save()
    redirect(f"/uporabniki/{full_name}")

@route("/uporabniki/<full_name>/predmet", "POST")
@view('predmet_submit')
def ustvari_predmet(full_name):
    '''
    route, kjer se posredujejo informacije, ko uporabnik ustvari nov predmet
    na koncu, ko se predmet shrani, se prikaže spletna stran za potrditev vnosa
    '''
    uporabnik = uporabnik_find(full_name)
    info = dict(request.forms)
    uporabnik.predmeti.append(Predmet(info['ime'], info['letnik'], []))
    db.save()
    info['back'] = f'/uporabniki/{full_name}'
    return info

@route("/uporabniki/<full_name>/opravilo", "POST")
@view('opravilo_submit')
def ustvari_opravilo(full_name):
    '''
    route, kjer se posredujejo informacije, ko uporabnik ustvari novo opravilo
    na koncu, ko se opravilo shrani, se prikaže spletna stran za potrditev vnosa
    '''
    uporabnik = uporabnik_find(full_name)
    info = dict(request.forms)
    index_predmeta = int(info['predmet'])
    uporabnik.predmeti[index_predmeta].opravila.append(Opravilo(info['ime'], Datum(info['leto'], info['mesec'], info['dan']), False, info['tip_obveznosti']))
    db.save()
    info['back'] = f'/uporabniki/{full_name}'
    return info

@route('/')
@view('index')
def index():
    '''
    prikaz domače index strani, kjer so našteti vsi uporabniki
    '''
    return {"uporabniki": db.uporabniki}

run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080))) #tukaj se server požene na portu 8080 ali na portu, ki je posredovan preko sistemske spremenljivke