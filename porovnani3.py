# pøedpokládá se tabulka s daty, kde rodná èísla jsou v prvním sloupci, maily ve druhém a telefonní èísla ve tøetím
# v tabulce se nesmí stát, že by nìkterá z tìchto hodnot chybìla a souèasnì byla poslední hodnotou v øádku
    # (csv by nezaznamenalo práznou buòku)
# všechna rodná èísla jsou pøevedena do formátu èísla a seøazena od nejmenšího (neèíselné záznamy jsou na konci)

# FUNKCE
def zapis_stejne_partners(radek): # zápis klientù, kteøí jsou v obou zdrojových souborech, ve formátu dat z Partners
    with open("stejne_partners.csv","a", encoding='utf-8') as mujsoubor:
        print(radek, file=mujsoubor)
def zapis_stejne_simplea(radek): # zápis klientù, kteøí jsou v obou zdrojových souborech, ve formátu dat ze Simpley
    with open("stejne_simplea.csv","a", encoding='utf-8') as mujsoubor:
        print(radek, file=mujsoubor)

def zapis_unikatni_partners(radek): # pokud prohledávání nenašlo shodu, zapíšou se nespárované položky Partners seznamu do unikátních uživatelù z Partners
    with open("unikatni_partners.csv","a", encoding='utf-8') as mujsoubor:
        print(radek ,file=mujsoubor)
def zapis_simplea_unikatni(radek): # po konci prohledávání se zapíšou zbylé položky Simplea seznamu do unikátních uživatelù ze Simpley
    with open("unikatni_simplea.csv","a", encoding='utf-8') as mujsoubor:
        print(radek, file=mujsoubor)

# PROGRAM
try: # zkusí vyhledat soubor stejne_partners.csv a naèíst jej
    # když soubor nalezne, naète všechny øádky do pole
    vstup1 = open('partners.csv',"r", encoding='utf-8')
    soubor1 = []
    for radek in vstup1:
        soubor1.append(radek.strip()) # vložení všech øádkù prvního souboru po pole
except: # když soubor nenalezne, ohlásí error 
    error = 1
try: # analogicky pøedchozímu bloku
    vstup2 = open('simplea.csv',"r", encoding='utf-8')
    soubor2 = []
    for radek in vstup2:
        soubor2.append(radek.strip()) # vložení všech øádkù druhého souboru po pole
except:    
    error = 1

# oèištìní dat od hlavièky tabulky
hlavicka1 = soubor1.pop(0)
hlavicka2 = soubor2.pop(0)

# pole pro rodná èísla z obou zdrojù
rc1 = []
rc2 = []

# prochází naètené øádky souborù a vybírá z nich rodná èísla
for a in range(len(soubor1)):
    radek = soubor1[a].split(";") # rozdìlení záznamu celého øádku na jednotlivé položky tabulky
    try: # je-li možné pøevést položku rodného èísla na integer, provede se to kvùli pozdìjšímu porovnávání hodnot
        rc1.append(int(radek[0])) 
    except:
        rc1.append(radek[0])
for b in range(len(soubor2)):
    radek = soubor2[b].split(";")
    try:
        rc2.append(int(radek[0]))
    except:
        rc2.append(radek[0])

# založení polí pro zaznamenání nalezené shody, kvùli dalšímu zpracování dat se shoda bude zaznamenávat dvakrát, vždy ve formátu obou zdrojových souborù
stejne_partners = []
stejne_simplea = []
j = 0 # ukazatel na data Sipmley
for i in range(len(rc1)): # projdeme všechny klienty ze souboru Partners
    while j < len(rc2)-1 and rc2[j] == "z" or rc2[j] < rc1[i]:
        # procházíme data ze Simpley a hledáme shodu
        # kromì jiných výjimek se pro každý prvek z Partners prohledávají data ze Simpley tak dlouho, dokud je aktuální rodné èíslo rc2 menší než rodné èíslo rc1
        j += 1
    # když pøestane platit podmínka pro velikost rc, vyhodnotí se, jestli se rodná èísla rovnají nebo jsou rozdílná
    if rc1[i] == rc2[j]:
        # pokud jsou rodná èísla shodná, zaznamená se shoda do pøipravených polí
        stejne_partners.append(soubor1[i])
        stejne_simplea.append(soubor2[j])
        # shodná rodná èísla se v pùvodních seznamech nahradí "z", které se následnì bude vyhodnocovat na konci tak, že je-li prvek roven "z",
            # byla u tohoto èísla nalezena shoda, jeli však prvkem pøímo rodné èíslo, je toto unikátní mezi obìma datovými soubory
        rc1[i] = "z"
        rc2[j] = "z"

# zápis hlavièek do výstupních souborù
zapis_stejne_partners(hlavicka1)
zapis_stejne_simplea(hlavicka2)
zapis_unikatni_partners(hlavicka1)
zapis_simplea_unikatni(hlavicka2)

# zápis dat do výstupních souborù
for radek1 in range(len(stejne_partners)):
    zapis_stejne_partners(stejne_partners[radek1])
for radek1 in range(len(stejne_simplea)):
    zapis_stejne_simplea(stejne_simplea[radek1])
for radek2 in range(len(soubor1)):
    if rc1[radek2] != "z":
        zapis_unikatni_partners(soubor1[radek2])
for radek3 in range(len(soubor2)):
    if rc2[radek3] != "z":
        zapis_simplea_unikatni(soubor2[radek3])

