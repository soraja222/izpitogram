

import db
from bottle import route, run, template, view, redirect

db.load()

@route('/uporabniki/<full_name>')
@view('uporabnik')
def uporabnik(full_name):
    imePriimek = full_name.split('_')
    for uporabnik in db.uporabniki:
        if uporabnik.ime == imePriimek[0] and uporabnik.priimek == imePriimek[1]:
            opravila = []
            for predmet in uporabnik.predmeti:
                for opravilo in predmet.opravila:
                    opravila.append(opravilo)
    
            return {'uporabnik': uporabnik, 'opravila': opravila}
    redirect('/')
    


@route('/')
@view('index')
def index():
    return {"uporabniki": db.uporabniki}

run(host='localhost', port=8080)