

import db
from domain import *
from bottle import route, run, template, view, redirect, request
"""
url metode je informacija kaj ho;e uporabnik narediti na routu, POST: ustvariti informacije, PUT: spremeniti informacije, GET: dobiti informacije, DELETE: izbris...
"""
db.load()

def uporabnik_find(full_name):
    imePriimek = full_name.split('_')
    for uporabnik in db.uporabniki:
        if uporabnik.ime == imePriimek[0] and uporabnik.priimek == imePriimek[1]:
            return uporabnik

@route('/uporabniki/<full_name>')
@view('uporabnik')
def uporabnik(full_name):

    uporabnik = uporabnik_find(full_name)
    opravila = []
    for predmet in uporabnik.predmeti:
        for opravilo in predmet.opravila:
            opravila.append(opravilo)


    return {'uporabnik': uporabnik, 'predmeti': uporabnik.predmeti, 'opravila': opravila, 'opravilo_action': f'/uporabniki/{full_name}/opravilo', 'predmet_action': f'/uporabniki/{full_name}/predmet'}
    redirect('/')
    
@route("/uporabniki", "POST")
@view('uporabnik_submit')
def ustvari_upoabnika():
    info = dict(request.forms)
    db.uporabniki.append(Uporabnik(info['ime'], info['priimek'], info['smer'], []))
    db.save()
    return info

    
@route("/uporabniki/<full_name>/predmet", "POST")
@view('predmet_submit')
def ustvari_predmet(full_name):
    uporabnik = uporabnik_find(full_name)
    info = dict(request.forms)
    uporabnik.predmeti.append(Predmet(info['ime'], info['letnik'], []))
    db.save()
    info['back'] = f'/uporabniki/{full_name}'
    return info

@route("/uporabniki/<full_name>/opravilo", "POST")
@view('opravilo_submit')
def ustvari_opravilo(full_name):
    uporabnik = uporabnik_find(full_name)
    info = dict(request.forms)
    index_predmeta = int(info['predmet'])
    uporabnik.predmeti[index_predmeta].opravila.append(Opravilo(info['ime'], info['rok'], False))
    db.save()
    info['back'] = f'/uporabniki/{full_name}'
    return info

@route('/')
@view('index')
def index():
    return {"uporabniki": db.uporabniki}

run(reloader=True, host='localhost', port=8080)