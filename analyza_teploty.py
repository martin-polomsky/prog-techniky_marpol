
import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt  # pip install matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# funkcia na generovanie teplot
def generuj():

    try:
        pocet = int(vstup.get())

        if pocet < 50:
            messagebox.showerror("Chyba", "Zadaj aspon 50 hodnot!")
            return

    except ValueError:
        messagebox.showerror("Chyba", "Zadaj cele cislo!")
        return

    # vytvorenie nahodnych teplot
    teploty = []

    for i in range(pocet):
        teplota = round(random.uniform(-10, 40), 2)
        teploty.append(teplota)

    # vypocet novych hodnot podla vzorca
    vypocitane = []

    for t in teploty:
        nova = round(t * 1.05 + 2, 2)
        vypocitane.append(nova)

    # zakladne vypocty
    priemer = sum(teploty) / len(teploty)
    minimum = min(teploty)
    maximum = max(teploty)

    # zoradenie teplot od najmensiej po najvacsiu
    zoradene = sorted(teploty)

    # vypocet zakladnych udajov pre vypocitane hodnoty
    vypocitane_minimum = min(vypocitane)
    vypocitane_maximum = max(vypocitane)

    # priklad vypoctu vzorca
    priklad_vstup = teploty[0]
    priklad_vystup = vypocitane[0]

    # vypis vysledkov
    vysledok.config(
        text=f"""
    Pocet merani: {pocet}

    Priemerna teplota: {priemer:.2f} °C
    Minimalna teplota: {minimum:.2f} °C
    Maximalna teplota: {maximum:.2f} °C

    Najmensich 5 hodnot: {zoradene[:5]}
    Najvacsich 5 hodnot: {zoradene[-5:]}

    VYPOCET PODLA VZORCA

    Vzorec: nova hodnota = teplota × 1.05 + 2

    Priklad:
    {priklad_vstup:.2f} × 1.05 + 2 = {priklad_vystup:.2f}

    Minimalna vypocitana hodnota: {vypocitane_minimum:.2f} °C
    Maximalna vypocitana hodnota: {vypocitane_maximum:.2f} °C
    """
    )

    # vykreslenie grafu
    graf.clear()

    x = range(1, pocet + 1)

    graf.plot(x, teploty, label="Povodne teploty", marker="o")
    graf.plot(x, vypocitane, label="Vypocitane teploty", marker="x")

    graf.set_title("Porovnanie teplot")
    graf.set_xlabel("Cislo merania")
    graf.set_ylabel("Teplota v °C")

    graf.tick_params(axis="both", labelsize=11)

    graf.title.set_fontsize(14)
    graf.xaxis.label.set_fontsize(12)
    graf.yaxis.label.set_fontsize(12)

    graf.legend(fontsize=11)
    graf.grid()

    platno.draw()


# zmena sirky textu podla vysledkoveho ramceka
def zmen_sirku_vysledkov(event):
    vysledok.config(wraplength=max(300, event.width - 50))


# vytvorenie hlavneho okna
okno = tk.Tk()
okno.title("Analyza teploty")
okno.geometry("1000x750")
okno.minsize(850, 650)
okno.configure(bg="#eeeeee")


# nadpis aplikacie
nadpis = tk.Label(
    okno,
    text="ANALYZA TEPLOTY",
    font=("Arial", 20, "bold"),
    bg="#eeeeee"
)
nadpis.pack(pady=15)

zadanie = tk.Label(
    okno,
    text="Zadanie 2 - Python",
    font=("Arial", 11),
    bg="#eeeeee",
    fg="gray"
)
zadanie.pack()

autor = tk.Label(
    okno,
    text="Autor: Martin Polomský",
    font=("Arial", 9),
    bg="#eeeeee",
    fg="gray"
)
autor.pack(anchor="e", padx=30)

# horna cast aplikacie
horna_cast = tk.Frame(okno, bg="#eeeeee")
horna_cast.pack(fill="x", padx=40, pady=15)

# lava strana - vstup
lava_strana = tk.Frame(horna_cast, bg="#eeeeee")
lava_strana.pack(side="left", fill="y", padx=15, pady=10, anchor="center")

vstupny_ramcek = tk.LabelFrame(
    lava_strana,
    text="Vstupne udaje",
    font=("Arial", 12, "bold"),
    bg="#eeeeee",
    padx=10,
    pady=8
)
vstupny_ramcek.pack(anchor="center", expand=True)

popis = tk.Label(
    vstupny_ramcek,
    text="Pocet merani (min. 50):",
    font=("Arial", 12),
    bg="#eeeeee"
)
popis.pack(pady=5)

vstup = tk.Entry(
    vstupny_ramcek,
    font=("Arial", 13),
    width=15,
    justify="center"
)
vstup.insert(0, "50")
vstup.pack(pady=8)

tlacidlo = tk.Button(
    vstupny_ramcek,
    text="Generovat a vypocitat",
    font=("Arial", 12),
    command=generuj,
    bg="#3498db",
    fg="white",
    padx=15,
    pady=8
)
tlacidlo.pack(pady=8)


# prava strana - vysledky
prava_strana = tk.LabelFrame(
    horna_cast,
    text="Vysledky vypoctov",
    font=("Arial", 12, "bold"),
    bg="#eeeeee",
    padx=8,
    pady=5
)
prava_strana.pack(side="left", fill="both", expand=True, padx=20)

vysledok = tk.Label(
    prava_strana,
    text="Tu sa zobrazia vysledky",
    font=("Arial", 13),
    bg="white",
    justify="left",
    anchor="w",
    padx=20,
    pady=15
)
vysledok.pack(fill="both", expand=True)
prava_strana.bind("<Configure>", zmen_sirku_vysledkov)

# vytvorenie grafu
obrazok, graf = plt.subplots(figsize=(8, 4))

obrazok.subplots_adjust(
    left=0.15,
    right=0.85,
    top=0.90,
    bottom=0.15
)

graf_ramka = tk.Frame(okno, bg="#eeeeee")
graf_ramka.pack(fill="both", expand=True, padx=30, pady=10)

platno = FigureCanvasTkAgg(obrazok, master=graf_ramka)
platno.get_tk_widget().pack(fill="both", expand=True)

# zvacsovanie pisma podla velkosti okna
def zmen_velkost(event):

    if event.widget == okno:

        sirka = event.width
        vyska = event.height

        pomer = min(sirka / 1000, vyska / 750)

        if pomer < 0.85:
            pomer = 0.85

        nadpis.config(font=("Arial", int(20 * pomer), "bold"))
        zadanie.config(font=("Arial", int(11 * pomer)))
        autor.config(font=("Arial", int(9 * pomer)))
        popis.config(font=("Arial", int(12 * pomer)))
        vstup.config(font=("Arial", int(13 * pomer)))
        tlacidlo.config(font=("Arial", int(12 * pomer)))
        vysledok.config(font=("Arial", int(9 * pomer)))
        vstupny_ramcek.config(font=("Arial", int(12 * pomer), "bold"))
        prava_strana.config(font=("Arial", int(12 * pomer), "bold"))


okno.bind("<Configure>", zmen_velkost)


# spustenie aplikacie
generuj()
okno.mainloop()
