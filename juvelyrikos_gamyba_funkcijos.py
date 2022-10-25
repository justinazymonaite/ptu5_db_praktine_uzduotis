from models import engine, Uzsakymas, Darbuotojas, Uzsakovas, Statusas, Gaminys, GaminioTipas, GaminioKategorija
from sqlalchemy.orm import sessionmaker

session = sessionmaker(engine)()

def spausdinti_uzsakovus():
    print("(ID, vardas, pavarde, gimimo data, adresas, tel. numeris, el. pastas)")
    uzsakovai = session.query(Uzsakovas).all()
    for uzsakovas in uzsakovai:
        print(uzsakovas)

def spausdinti_uzsakymus():
    print("(ID, uzsakovas, uzsakymo data, atidavimo uzsakovui data, atsakingas darbuotojas, statusas, modifikacijos, gaminiai)")
    uzsakymai = session.query(Uzsakymas).all()
    for uzsakymas in uzsakymai:
        print(uzsakymas, uzsakymas.gaminiai)

def spausdinti_darbuotojus():
    print("(ID, vardas, pavarde, asmens kodas, pareigos, tel. numeris, uzsakymai)")
    darbuotojai = session.query(Darbuotojas).all()
    for darbuotojas in darbuotojai:
        print(darbuotojas)

def spausdinti_pasirinkto_darbuotojo_uzsakymus():
    print("----Pasirinkto darbuotojo uzsakymai----")
    print("Pasirinkite, kurio darbuotojo uzsakymus noresite perziureti is siu galimu:")
    spausdinti_darbuotojus()
    try:
        pasirinkto_darbuotojo_id = int(input("Irasykite pasirinkto darbuotojo ID: "))
    except ValueError:
        print("KLAIDA: iveskite skaiciu")
    else:
        pasirinktas_darbuotojas = session.query(Darbuotojas).get(pasirinkto_darbuotojo_id)
        print(f"{pasirinktas_darbuotojas.vardas} {pasirinktas_darbuotojas.pavarde} uzsakymai:")
        for uzsakymas in pasirinktas_darbuotojas.uzsakymai:
            print(uzsakymas, uzsakymas.gaminiai)

def spausdinti_gaminius():
    print("(ID, modelis, tipas, kategorija)")
    gaminiai = session.query(Gaminys).all()
    for gaminys in gaminiai:
        print(gaminys)

def spausdinti_statusus():
    print("(ID, pavadinimas)")
    statusai = session.query(Statusas).all()
    for statusas in statusai:
        print(statusas)

def spausdinti_tipus():
    print("(ID, pavadinimas)")
    tipai = session.query(GaminioTipas).all()
    for tipas in tipai:
        print(tipas)

def spausdinti_kategorijas():  
    print("(ID, pavadinimas)")
    kategorijos = session.query(GaminioKategorija).all()
    for kategorija in kategorijos:
        print(kategorija)

def trinti_objekta(objekto_klase, objekto_id):
    objektas = session.query(objekto_klase).get(objekto_id)
    if objektas:
        session.delete(objektas)
        session.commit()
        print(f"{objekto_klase.__name__} irasas su ID:{objekto_id} sekmingai istrintas")
    else:
        print(f"Klaida: {objekto_klase.__name__} su ID:{objekto_id} neegzistuoja")