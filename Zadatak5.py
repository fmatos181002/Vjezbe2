import asyncio

async def secure_data(podaci):
    await asyncio.sleep(3)
    return {
        'prezime': podaci['prezime'],
        'broj_kartice': hash(podaci['broj_kartice']),
        'CVV': hash(podaci['CVV'])
    }

async def main():
    osjetljivi_podaci = [
        {'prezime': 'Matoš', 'broj_kartice': '1234567812345678', 'CVV': '123'},
        {'prezime': 'Šlat', 'broj_kartice': '8765432187654321', 'CVV': '456'},
        {'prezime': 'Brinc', 'broj_kartice': '1111222233334444', 'CVV': '789'}
    ]
    zadaci = [asyncio.create_task(secure_data(podaci)) for podaci in osjetljivi_podaci]
    rezultati = await asyncio.gather(*zadaci)
    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())