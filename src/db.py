from datetime import date
from domain import *
import pickle
import os 

uporabniki = []

def napolni():
    global uporabniki

    # Janez
    o1 = Opravilo("Izpit", Datum(2020, 5, 24), False, "Izpit")
    o2 = Opravilo("Izpit", Datum(2020, 7, 24), False, "Izpit")
    p1 = Predmet("Matematika", 1, [o1, o2])
    janez = Uporabnik("Janez", "Novak", Smeri.fm, [p1])
    uporabniki.append(janez)

    # Marko
    o1 = Opravilo("Izpit", Datum(2020, 8, 24), False, "Seminarska naloga")
    o2 = Opravilo("Izpit", Datum(2020, 9, 24), False, "Izpit")
    p1 = Predmet("Fizika", 1, [o1, o2])
    Marko = Uporabnik("Marko", "Novak", Smeri.sm, [p1])
    uporabniki.append(Marko)

def save():
    global uporabniki
    with open('database.bin', 'wb') as file:
        pickle.dump(uporabniki, file)

def load():
    global uporabniki
    if os.path.exists('database.bin'):
        with open('database.bin', 'rb') as file:
            uporabniki = pickle.load(file)
            print(f"Loaded: {len(uporabniki)} users")
    else:
        print("Sorry existing db not found.")
