from http.client import LineTooLong
from datetime import date, timedelta

class Smeri:
    fm = "Financna Matematika"
    sm = "Splosna Matematika"
    pm = "Pedagoska Matematika"

class Uporabnik:
    def __init__(self, ime, priimek, smer, predmeti) -> None:
        self.ime = ime 
        self.priimek = priimek
        self.predmeti = predmeti
        self.smer = smer

class Predmet:
    def __init__(self, ime, letnik,opravila) -> None:
        self.ime = ime 
        self.opravila = opravila
        self.letnik = letnik

class Opravilo:
    NUJNO = 7
    PRIJAVA = 4

    def __init__(self, ime, rok, opravljen, tip) -> None:
        self.ime = ime
        self.rok = rok
        self.opravljen = opravljen
        self.tip = tip

    def nujno(self):
        dayD = (self.rok.date() - date.today()).days
        return self.NUJNO > dayD


class Datum:
    def __init__(self, leto, mesec, dan) -> None:
        self.leto = int(leto) 
        self.mesec = int(mesec)
        self.dan = int(dan)
    
    def date(self):
        return date(self.leto, self.mesec, self.dan)
    
    def ucenje(self):
        d = self.date() - timedelta(days=-Opravilo.NUJNO)
        return f'{d.day}.{d.month}.{d.year}'

    def prijava(self):
        d = self.date() - timedelta(days=-Opravilo.PRIJAVA)
        return f'{d.day}.{d.month}.{d.year}'