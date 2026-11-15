import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]
    await asyncio.gather(*timers)

asyncio.run(main())

"""
Objašnjenje kako radi event loop u ovom primjeru

1. asyncio.run(main()) napravi event loop i pokrene main()

2. u main() se s create_task naprave 3 taska (Timer 1, 2 i 3). oni su sad zakazani
   (pending), znači čekaju u redu ali se još ništa ne ispisuje

3. main() dođe do await asyncio.gather(*timers) i tu stane (suspended) dok sva 3
   taska ne završe. time vraća kontrolu event loopu i loop krene izvršavat taskove

4. t = 0s - loop pokreće taskove jedan po jedan (u jednom trenutku radi samo jedan):
   - Timer 1 ispiše "3 sekundi preostalo..." i dođe do await asyncio.sleep(1) pa stane
   - Timer 2 ispiše "5 sekundi preostalo..." i stane
   - Timer 3 ispiše "7 sekundi preostalo..." i stane
   sad sva 3 čekaju i loop čeka da prođe 1 sekunda

5. t = 1s, 2s - kad prođe sleep(1) loop ih budi istim redom. svaki nastavi točno
   di je stao, ispiše sljedeću poruku i opet stane na sleep

6. t = 3s - Timer 1 je gotov, ispiše "Vrijeme je isteklo!" i završi (done)

7. t = 5s - Timer 2 isto završi

8. t = 7s - završi i Timer 3

9. kad su sva 3 gotova, gather završi, main() se nastavi i završi, a asyncio.run()
   zatvori event loop

Sve skupa traje oko 7 sekundi (koliko traje najduži timer), a ne 3 + 5 + 7 = 15s,
jer timeri čekaju u isto vrijeme a ne jedan za drugim

Stanja taska: pending -> running -> suspended -> running ... -> done
"""