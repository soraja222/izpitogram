from http.client import LineTooLong


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
    def __init__(self, ime, rok, opravljen) -> None:
        self.ime = ime
        self.rok = rok
        self.opravljen = opravljen

class Datum:
    def __init__(self, leto, mesec, dan) -> None:
        self.leto = leto 
        self.mesec = mesec 
        self.dan = dan 