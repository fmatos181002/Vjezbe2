import asyncio, time

async def dohvati_korisnike():
    await asyncio.sleep(3)
    return [
        {'id': 1, 'ime': 'Ivan', 'email': 'florian@example.com'},
        {'id': 2, 'ime': 'Ana', 'email': 'patrik@example.com'},
        {'id': 3, 'ime': 'Marko', 'email': 'slavko@example.com'},
    ]

async def dohvati_proizvode():
    await asyncio.sleep(5)
    return [
        {'id': 101, 'naziv': 'Laptop', 'cijena': 899.99},
        {'id': 102, 'naziv': 'Miš', 'cijena': 19.99},
        {'id': 103, 'naziv': 'Tipkovnica', 'cijena': 49.99},
    ]

async def main():
    korisnici, proizvodi = await asyncio.gather(dohvati_korisnike(), dohvati_proizvode())
    print("Korisnici:", korisnici)
    print("Proizvodi:", proizvodi)

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Vrijeme izvođenja: {t2 - t1:.2f} s")