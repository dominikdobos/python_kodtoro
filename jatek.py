import random
LEHETSEGES_SZINEK = ['P', 'K', 'Z', 'S', 'N', 'L']
KIVALASZTOTT_SZINEK = random.choices(LEHETSEGES_SZINEK, k=4)


def jatek():
    print("-- KÓDTÖRŐ --\n"
          "\tJáték: 'j'\n"
          "\tKilépés: 'k'")

    dontes = input("Akarsz játszani? (j/k): ")

    while not (dontes == 'j' or dontes == 'k'):
        dontes = input("Válassz! (j/k): ")

    if dontes == 'j':
        jatekmenet()
    else:
        exit("Kilépés...")


def jatekmenet():
    print("\nJátékmenet:"
          "\n\t6 szín közül kell választanod 4-et!"
          "\n\t10 kör alatt ki kell találnod a színeket!"
          "\n\tA sorrend fontos!"
          "\n\tLehetséges színek:\n"
          "\t\tP (piros)\n"
          "\t\tK (kék)\n"
          "\t\tZ (zöld)\n"
          "\t\tS (sárga)\n"
          "\t\tN (narancs)\n"
          "\t\tL (lila)\n"
          "\tÍgy add meg a színeket:\n"
          "\t\tPélda: '1. szín: S'\n"
          "\t(A játék közben a 'k' paranccsal kiléphetsz)")

    for i in range(10):
        print(f"\n{i + 1}. kör")
        if ellenorzes(szint()):
            print("\nNyertél!\n"
                  f"A kiválasztott színek {KIVALASZTOTT_SZINEK} voltak.\n")
            jatek()
    print("\nVesztettél!\n"
          f"A kiválasztott színek {KIVALASZTOTT_SZINEK} voltak.\n")
    jatek()


def szint():
    valasztott_szinek = []

    while len(valasztott_szinek) < 4:

        szin = input(f"\t{len(valasztott_szinek)+1}. szín: ")
        while not (szin in LEHETSEGES_SZINEK or szin == 'k'):
            szin = input(f"\tHIBA! {len(valasztott_szinek) + 1}. szín: ")

        if szin == 'k':
            print("Kiléptél...\n"
                  f"A kiválasztott színek {KIVALASZTOTT_SZINEK} voltak.\n")
            jatek()

        if szin in LEHETSEGES_SZINEK:
            valasztott_szinek.append(szin)

    return valasztott_szinek


def ellenorzes(jatekszint):
    nyert = False

    eltalalt_szinek = 0
    eltalalt_helyek = 0
    mar_tippelt_szinek = []
    for i in range(4):
        if jatekszint[i] in KIVALASZTOTT_SZINEK and jatekszint[i] not in mar_tippelt_szinek:
            eltalalt_szinek += 1
            mar_tippelt_szinek.append(jatekszint[i])
        if jatekszint[i] == KIVALASZTOTT_SZINEK[i]:
            eltalalt_helyek += 1

    print("Kör eredménye:\n"
          f"\tEltalált színek: {eltalalt_szinek}.\n"
          f"\tEltalált helyek: {eltalalt_helyek}.")

    if jatekszint == KIVALASZTOTT_SZINEK:
        nyert = True

    return nyert
