import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'florian123', 'email': 'florian123@gmail.com'},
    {'korisnicko_ime': 'ana_kristo', 'email': 'akristo@gmail.com'},
    {'korisnicko_ime': 'maja_0310', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'slavko032', 'email': 'slavko032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'florian123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_kristo', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0310', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'slavko032', 'lozinka': 'slavko123'}
]

async def autorizacija(korisnik_iz_baze, lozinka):
    await asyncio.sleep(2)
    ime = korisnik_iz_baze['korisnicko_ime']
    for zapis in baza_lozinka:
        if zapis['korisnicko_ime'] == ime and zapis['lozinka'] == lozinka:
            return f"Korisnik {ime}: Autorizacija uspješna."
    return f"Korisnik {ime}: Autorizacija neuspješna."

async def autentifikacija(korisnik):
    await asyncio.sleep(3)
    for k in baza_korisnika:
        if k['korisnicko_ime'] == korisnik['korisnicko_ime'] and k['email'] == korisnik['email']:
            return await autorizacija(k, korisnik['lozinka'])
    return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen."

async def main():
    korisnik = {'korisnicko_ime': 'florian123', 'email': 'florian123@gmail.com', 'lozinka': 'lozinka123'}
    rezultat = await autentifikacija(korisnik)
    print(rezultat)

asyncio.run(main())