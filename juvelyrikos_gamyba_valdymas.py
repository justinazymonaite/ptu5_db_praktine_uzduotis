from juvelyrikos_gamyba_funkcijos import *


while True:
    # pagrindinis meniu
    try:
        ivestis = int(input("Meniu:\
            \n 1 ivesti nauja \
            \n 2 perziureti \
            \n 3 gaminio priskyrimas uzsakymui \
            \n 4 trinti \
            \n 5 iseiti is programos \
            \nPasirinkite: ")
        )
    except ValueError:
        print("KLAIDA: iveskite skaiciu")
    else:
        if ivestis == 5: 
            break
        elif ivestis == 1:
            # 1 submeniu
            while True:
                print("----Ivedimas----")
                try:
                    ivestis1 = int(input("Meniu:\
                        \n 1 ivesti nauja uzsakova \
                        \n 2 ivesti nauja uzsakyma  \
                        \n 3 ivesti nauja darbuotoja  \
                        \n 4 ivesti nauja gamini \
                        \n 5 ivesti nauja statusa \
                        \n 6 ivesti nauja tipa \
                        \n 7 ivesti nauja kategorija \
                        \n 8 grizti i pagrindini meniu \
                        \nPasirinkite: ")
                    )
                except ValueError:
                    print("KLAIDA: iveskite skaiciu")
                else:
                    if ivestis1 == 8:
                        break
                    elif ivestis1 == 1:
                        print("----Naujas uzsakovas----")
                        ivestas_vardas = input("Vardas: ")
                        ivesta_pavarde = input("Pavarde: ")
                        ivesta_gimimo_data = input("Gimimo data: ")
                        ivestas_adresas = input("Adresas: ")
                        ivestas_tel_nr = input("Telefono numeris: ")
                        ivestas_el_pastas = input("El. pastas: ")
                        uzsakovas = Uzsakovas(
                            vardas=ivestas_vardas, 
                            pavarde=ivesta_pavarde, 
                            gimimo_data=ivesta_gimimo_data, adresas=ivestas_adresas,
                            telefono_numeris=ivestas_tel_nr, el_pastas=ivestas_el_pastas
                        )
                        session.add(uzsakovas)
                        session.commit()
                        print(f"Naujas uzsakovas {uzsakovas} sukurtas sekmingai")
                    elif ivestis1 == 2:
                        print("----Naujas uzsakymas----")
                        print("Pasirinkite uzsakova is siu galimu:")
                        spausdinti_uzsakovus()
                        try:
                            pasirinktas_uzsakovas = int(input("Irasykite pasirinkto uzsakovo ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            ivesta_uzsakymo_data = input("Uzsakymo data: ")
                            ivesta_atidavimo_uzsakovui_data = input("Atidavimo uzsakovui data: ")
                            print("Pasirinkite atsakinga darbuotoja is siu galimu:")
                            spausdinti_darbuotojus()
                            try:
                                pasirinktas_darbuotojas = int(input("Irasykite pasirinkto darbuotojo ID: "))
                            except ValueError:
                                print("KLAIDA: iveskite skaiciu")
                            else:
                                print("Pasirinkite uzsakymo statusa is siu galimu:")
                                spausdinti_statusus()
                                try:
                                    pasirinktas_statusas = int(input("Irasykite pasirinkto statuso ID: "))
                                except ValueError:
                                    print("KLAIDA: iveskite skaiciu")
                                else:
                                    ivestos_modifikacijos = input("Iveskite pageidaujamas modifikacijas: ")
                                    uzsakymas = Uzsakymas(
                                        uzsakovas_id=pasirinktas_uzsakovas, 
                                        uzsakymo_data=ivesta_uzsakymo_data, 
                                        atidavimo_uzsakovui_data=ivesta_atidavimo_uzsakovui_data, atsakingas_darbuotojas_id = pasirinktas_darbuotojas,
                                        statusas_id=pasirinktas_statusas,
                                        modifikacijos=ivestos_modifikacijos
                                    )
                                    session.add(uzsakymas)
                                    session.commit()
                                    print(f"Naujas uzsakymas {uzsakymas} sukurtas sekmingai")
                    elif ivestis1 == 3:
                        print("----Naujas darbuotojas----")
                        ivestas_vardas = input("Vardas: ")
                        ivesta_pavarde = input("Pavarde: ")
                        ivesta_asmens_kodas = input("Asmens kodas: ")
                        ivestos_pareigos = input("Pareigos: ")
                        ivestas_tel_nr = input("Telefono numeris: ")
                        darbuotojas = Darbuotojas(
                            vardas=ivestas_vardas, 
                            pavarde=ivesta_pavarde, 
                            asmens_kodas=ivesta_asmens_kodas, pareigos=ivestos_pareigos,
                            telefono_numeris=ivestas_tel_nr
                        )
                        session.add(darbuotojas)
                        session.commit()
                        print(f"Naujas darbuotojas {darbuotojas} sukurtas sekmingai")
                    elif ivestis1 == 4:
                        print("----Naujas gaminys----")
                        ivestas_modelis = input("Modelis: ")
                        print("Pasirinkite gaminio tipa is siu galimu:")
                        spausdinti_tipus()
                        try:
                            pasirinktas_tipas = int(input("Irasykite pasirinkto tipo ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            print("Pasirinkite gaminio kategorija is siu galimu:")
                            spausdinti_kategorijas()
                            try:
                                pasirinkta_kategorija = int(input("Irasykite pasirinktos kategorijos ID: "))
                            except ValueError:
                                print("KLAIDA: iveskite skaiciu")
                            else:
                                gaminys = Gaminys(
                                    modelis=ivestas_modelis, 
                                    tipas_id=pasirinktas_tipas, 
                                    kategorija_id=pasirinkta_kategorija
                                )
                                session.add(gaminys)
                                session.commit()
                                print(f"Naujas gaminys {gaminys} sukurtas sekmingai")
                    elif ivestis1 == 5:
                        print("----Naujas statusas----")
                        ivestas_pavadinimas = input("Pavadinimas: ")
                        statusas = Statusas(pavadinimas=ivestas_pavadinimas)
                        session.add(statusas)
                        session.commit()
                        print(f"Naujas statusas {statusas} sukurtas sekmingai")
                    elif ivestis1 == 6:
                        print("----Naujas gaminio tipas----")
                        ivestas_pavadinimas = input("Pavadinimas: ")
                        tipas = GaminioTipas(pavadinimas=ivestas_pavadinimas)
                        session.add(tipas)
                        session.commit()
                        print(f"Naujas gaminio tipas {tipas} sukurtas sekmingai")
                    elif ivestis1 == 7:
                        print("----Nauja gaminio kategorija----")
                        ivestas_pavadinimas = input("Pavadinimas: ")
                        kategorija = GaminioKategorija(pavadinimas=ivestas_pavadinimas)
                        session.add(kategorija)
                        session.commit()
                        print(f"Nauja gaminio kategorija {kategorija} sukurta sekmingai")
                    else:
                        print("KLAIDA: Blogas pasirinkimas, rinkites is naujo!") 
        elif ivestis == 2:
            # antras submeniu
            while True:
                print("----Perziura----")
                try:
                    ivestis2 = int(input("Meniu:\
                        \n 1 perziureti uzsakovus \
                        \n 2 perziureti uzsakymus  \
                        \n 3 perziureti darbuotojus  \
                        \n 4 perziureti darbuotojo uzsakymus \
                        \n 5 perziureti gaminius \
                        \n 6 perziureti statusus \
                        \n 7 perziureti tipus \
                        \n 8 perziureti kategorijas \
                        \n 9 grizti i pagrindini meniu \
                        \nPasirinkite: ")
                    )
                except ValueError:
                    print("KLAIDA: iveskite skaiciu")
                else:
                    if ivestis2 == 9:
                        break
                    elif ivestis2 == 1:
                        print("----Uzsakovai----")
                        spausdinti_uzsakovus()
                    elif ivestis2 == 2:
                        print("----Uzsakymai----")
                        spausdinti_uzsakymus()
                    elif ivestis2 == 3:
                        print("----Darbuotojai----")
                        spausdinti_darbuotojus()
                    elif ivestis2 == 4:
                        print("----Darbuotojai----")
                        spausdinti_pasirinkto_darbuotojo_uzsakymus()
                    elif ivestis2 == 5:
                        print("----Gaminiai----")
                        spausdinti_gaminius()
                    elif ivestis2 == 6:
                        print("----Statusai----")
                        spausdinti_statusus()
                    elif ivestis2 == 7:
                        print("----Tipai----")
                        spausdinti_tipus()
                    elif ivestis2 == 8:
                        print("----Kategorijos----")
                        spausdinti_kategorijas()
                    else:
                        print("KLAIDA: Blogas pasirinkimas, rinkites is naujo!") 
        elif ivestis == 3:
            # trecias submeniu
            print("----Gaminio priskyrimas uzsakymui----")
            print("Pasirinkite, kuriam uzsakymui noresite priskirti gamini is siu galimu:")
            spausdinti_uzsakymus()
            try:
                pasirinkto_uzsakymo_id = int(input("Irasykite pasirinkto uzsakymo ID: "))
            except ValueError:
                print("KLAIDA: iveskite skaiciu")
            else:
                pasirinktas_uzsakymas = session.query(Uzsakymas).get(pasirinkto_uzsakymo_id)
                print(f"Pasirinkite, kuri gamini noresite priskirti uzsakymui {pasirinktas_uzsakymas} is siu galimu:")
                spausdinti_gaminius()
                try:
                    pasirinkto_gaminio_id = int(input("Irasykite pasirinkto gaminio ID: "))
                except ValueError:
                    print("KLAIDA: iveskite skaiciu")
                else:
                    pasirinktas_gaminys = session.query(Gaminys).get(pasirinkto_gaminio_id)
                    pasirinktas_gaminys.uzsakymai.append(pasirinktas_uzsakymas)
                    session.commit()
                    print(f"Gaminys {pasirinktas_gaminys} sekmingai priskirtas uzsakymui {pasirinktas_uzsakymas}")
        elif ivestis == 4:
            # ketvirtas submeniu
            while True:
                print("----Trynimas----")
                try:
                    ivestis4 = int(input("Meniu:\
                        \n 1 trinti uzsakova \
                        \n 2 trinti uzsakyma  \
                        \n 3 trinti darbuotoja  \
                        \n 4 trinti gamini \
                        \n 5 trinti statusa \
                        \n 6 trinti tipa \
                        \n 7 trinti kategorija \
                        \n 8 grizti i pagrindini meniu \
                        \nPasirinkite: ")
                    )
                except ValueError:
                    print("KLAIDA: iveskite skaiciu")
                else:
                    if ivestis4 == 8:
                        break
                    elif ivestis4 == 1:
                        print("----Trinti uzsakova----")
                        print("Pasirinkite uzsakova is siu galimu:")
                        spausdinti_uzsakovus()
                        try:
                            trinamo_uzsakovo_id = int(input("Irasykite trinamo uzsakovo ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            trinti_objekta(Uzsakovas, trinamo_uzsakovo_id)
                    elif ivestis4 == 2:
                        print("----Trinti uzsakyma----")
                        print("Pasirinkite uzsakyma is siu galimu:")
                        spausdinti_uzsakymus()
                        try:
                            trinamo_uzsakymo_id = int(input("Irasykite trinamo uzsakymo ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            trinti_objekta(Uzsakymas, trinamo_uzsakymo_id)
                    elif ivestis4 == 3:
                        print("----Trinti darbuotoja----")
                        print("Pasirinkite darbuotoja is siu galimu:")
                        spausdinti_darbuotojus()
                        try:
                            trinamo_darbuotojo_id = int(input("Irasykite trinamo darbuotojo ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            trinti_objekta(Darbuotojas, trinamo_darbuotojo_id)
                    elif ivestis4 == 4:
                        print("----Trinti gamini----")
                        print("Pasirinkite gamini is siu galimu:")
                        spausdinti_gaminius()
                        try:
                            trinamo_gaminio_id = int(input("Irasykite trinamo gaminio ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            trinti_objekta(Gaminys, trinamo_gaminio_id)
                    elif ivestis4 == 5:
                        print("----Trinti statusa----")
                        print("Pasirinkite statusa is siu galimu:")
                        spausdinti_statusus()
                        try:
                            trinamo_statuso_id = int(input("Irasykite trinamo statuso ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            trinti_objekta(Statusas, trinamo_statuso_id)
                    elif ivestis4 == 6:
                        print("----Trinti tipa----")
                        print("Pasirinkite tipa is siu galimu:")
                        spausdinti_tipus()
                        try:
                            trinamo_tipo_id = int(input("Irasykite trinamo tipo ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            trinti_objekta(GaminioTipas, trinamo_tipo_id)
                    elif ivestis4 == 7:
                        print("----Trinti kategorija----")
                        print("Pasirinkite kategorija is siu galimu:")
                        spausdinti_kategorijas()
                        try:
                            trinamos_kategorijos_id = int(input("Irasykite trinamos kategorijos ID: "))
                        except ValueError:
                            print("KLAIDA: iveskite skaiciu")
                        else:
                            trinti_objekta(GaminioKategorija, trinamos_kategorijos_id)
                    else:
                        print("KLAIDA: Blogas pasirinkimas, rinkites is naujo!") 
        else:
            print("KLAIDA: Blogas pasirinkimas, rinkites is naujo!")
