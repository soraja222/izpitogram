'''
domenski modul, kjer se nahajajo vsi domenski elementi
'''

from http.client import LineTooLong
from datetime import date, timedelta

class Smeri:
    '''
    zbirka vseh podprtih smeri, ki jih lahko uporablja uporabnik
    '''

    fm = "Financna Matematika"
    sm = "Splosna Matematika"
    pm = "Pedagoska Matematika"

class Uporabnik:
    '''
    definicija uporabnika
    '''
    def __init__(self, ime, priimek, smer, predmeti):
        self.ime = ime 
        self.priimek = priimek
        self.predmeti = predmeti
        self.smer = smer

class Predmet:
    '''
    definicija predmeta
    '''
    def __init__(self, ime, letnik,opravila):
        self.ime = ime 
        self.opravila = opravila
        self.letnik = letnik

class Opravilo:
    '''
    definicija opravila
    '''
    NUJNO = 7
    PRIJAVA = 4

    def __init__(self, ime, rok, opravljen, tip):
        self.ime = ime
        self.rok = rok
        self.opravljen = opravljen
        self.tip = tip

    def nujno(self):
        '''
        funkcija, ki vrača ali se rok opravila nahaja znotraj nujnega časovnega območja
        '''
        dayD = (self.rok.date() - date.today()).days
        return self.NUJNO > dayD


class Datum:
    '''
    definicija datuma
    '''
    def __init__(self, leto, mesec, dan):
        self.leto = int(leto) 
        self.mesec = int(mesec)
        self.dan = int(dan)
    
    def date(self):
        '''
        vrne notranje informacije v obliki python datuma (datetime.date)
        '''
        return date(self.leto, self.mesec, self.dan)
    
    def ucenje(self):
        '''
        vrne datum, kdaj se mora uporabnik začeti učit v obliki str
        '''
        d = self.date() - timedelta(days=-Opravilo.NUJNO)
        return f'{d.day}.{d.month}.{d.year}'

    def prijava(self):
        '''
         vrne datum, kdaj se mora uporabnik prijaviti na obveznost (v sistemu VIS) v obliki str
        '''
        d = self.date() - timedelta(days=-Opravilo.PRIJAVA)
        return f'{d.day}.{d.month}.{d.year}'