
from datetime import date
import db
from domain import *
from bottle import route, run, template, view, redirect, request
import os

#db.napolni()
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
    if uporabnik is None:
        redirect('/')

    opravila = []
    for predmet in uporabnik.predmeti:
        for opravilo in predmet.opravila:
            if opravilo.opravljen not in ['True', True, 1, '1']:
                opravila.append(opravilo)

    now = date.today()
    return {
        'uporabnik': uporabnik,
        'predmeti': uporabnik.predmeti,
        'opravila': opravila,
        'opravilo_action': f'/uporabniki/{full_name}/opravilo',
        'predmet_action': f'/uporabniki/{full_name}/predmet',
        'leto': now.year,
        'mesec': now.month,
        'dan': now.day
    }
    
    
@route("/uporabniki", "POST")
@view('uporabnik_submit')
def ustvari_upoabnika():
    info = dict(request.forms)
    db.uporabniki.append(Uporabnik(info['ime'], info['priimek'], info['smer'], []))
    db.save()
    return info


@route("/uporabniki/<full_name>/predmet/<predmet>/opravilo/<opravilo>/opravljen")
def opravilo_opravil(full_name, predmet, opravilo):
    uporabnik = uporabnik_find(full_name)
    predmet = uporabnik.predmeti[int(predmet)]
    opr = predmet.opravila[int(opravilo)]
    opr.opravljen = True
    db.save()
    redirect(f"/uporabniki/{full_name}")

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
    uporabnik.predmeti[index_predmeta].opravila.append(Opravilo(info['ime'], Datum(info['leto'], info['mesec'], info['dan']), False, info['tip_obveznosti']))
    db.save()
    info['back'] = f'/uporabniki/{full_name}'
    return info

@route('/')
@view('index')
def index():
    return {"uporabniki": db.uporabniki}

run(reloader=True, host='localhost', port=os.environ.get('PORT', 8080))