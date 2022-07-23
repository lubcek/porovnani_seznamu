# p�edpokl�d� se tabulka s daty, kde rodn� ��sla jsou v prvn�m sloupci, maily ve druh�m a telefonn� ��sla ve t�et�m
# v tabulce se nesm� st�t, �e by n�kter� z t�chto hodnot chyb�la a sou�asn� byla posledn� hodnotou v ��dku
    # (csv by nezaznamenalo pr�znou bu�ku)
# v�echna rodn� ��sla jsou p�evedena do form�tu ��sla a se�azena od nejmen��ho (ne��seln� z�znamy jsou na konci)

# FUNKCE
def zapis_stejne_partners(radek): # z�pis klient�, kte�� jsou v obou zdrojov�ch souborech, ve form�tu dat z Partners
    with open("stejne_partners.csv","a", encoding='utf-8') as mujsoubor:
        print(radek, file=mujsoubor)
def zapis_stejne_simplea(radek): # z�pis klient�, kte�� jsou v obou zdrojov�ch souborech, ve form�tu dat ze Simpley
    with open("stejne_simplea.csv","a", encoding='utf-8') as mujsoubor:
        print(radek, file=mujsoubor)

def zapis_unikatni_partners(radek): # pokud prohled�v�n� nena�lo shodu, zap�ou se nesp�rovan� polo�ky Partners seznamu do unik�tn�ch u�ivatel� z Partners
    with open("unikatni_partners.csv","a", encoding='utf-8') as mujsoubor:
        print(radek ,file=mujsoubor)
def zapis_simplea_unikatni(radek): # po konci prohled�v�n� se zap�ou zbyl� polo�ky Simplea seznamu do unik�tn�ch u�ivatel� ze Simpley
    with open("unikatni_simplea.csv","a", encoding='utf-8') as mujsoubor:
        print(radek, file=mujsoubor)

# PROGRAM
try: # zkus� vyhledat soubor stejne_partners.csv a na��st jej
    # kdy� soubor nalezne, na�te v�echny ��dky do pole
    vstup1 = open('partners.csv',"r", encoding='utf-8')
    soubor1 = []
    for radek in vstup1:
        soubor1.append(radek.strip()) # vlo�en� v�ech ��dk� prvn�ho souboru po pole
except: # kdy� soubor nenalezne, ohl�s� error 
    error = 1
try: # analogicky p�edchoz�mu bloku
    vstup2 = open('simplea.csv',"r", encoding='utf-8')
    soubor2 = []
    for radek in vstup2:
        soubor2.append(radek.strip()) # vlo�en� v�ech ��dk� druh�ho souboru po pole
except:    
    error = 1

# o�i�t�n� dat od hlavi�ky tabulky
hlavicka1 = soubor1.pop(0)
hlavicka2 = soubor2.pop(0)

# pole pro rodn� ��sla z obou zdroj�
rc1 = []
rc2 = []

# proch�z� na�ten� ��dky soubor� a vyb�r� z nich rodn� ��sla
for a in range(len(soubor1)):
    radek = soubor1[a].split(";") # rozd�len� z�znamu cel�ho ��dku na jednotliv� polo�ky tabulky
    try: # je-li mo�n� p�ev�st polo�ku rodn�ho ��sla na integer, provede se to kv�li pozd�j��mu porovn�v�n� hodnot
        rc1.append(int(radek[0])) 
    except:
        rc1.append(radek[0])
for b in range(len(soubor2)):
    radek = soubor2[b].split(";")
    try:
        rc2.append(int(radek[0]))
    except:
        rc2.append(radek[0])

# zalo�en� pol� pro zaznamen�n� nalezen� shody, kv�li dal��mu zpracov�n� dat se shoda bude zaznamen�vat dvakr�t, v�dy ve form�tu obou zdrojov�ch soubor�
stejne_partners = []
stejne_simplea = []
j = 0 # ukazatel na data Sipmley
for i in range(len(rc1)): # projdeme v�echny klienty ze souboru Partners
    while j < len(rc2)-1 and rc2[j] == "z" or rc2[j] < rc1[i]:
        # proch�z�me data ze Simpley a hled�me shodu
        # krom� jin�ch v�jimek se pro ka�d� prvek z Partners prohled�vaj� data ze Simpley tak dlouho, dokud je aktu�ln� rodn� ��slo rc2 men�� ne� rodn� ��slo rc1
        j += 1
    # kdy� p�estane platit podm�nka pro velikost rc, vyhodnot� se, jestli se rodn� ��sla rovnaj� nebo jsou rozd�ln�
    if rc1[i] == rc2[j]:
        # pokud jsou rodn� ��sla shodn�, zaznamen� se shoda do p�ipraven�ch pol�
        stejne_partners.append(soubor1[i])
        stejne_simplea.append(soubor2[j])
        # shodn� rodn� ��sla se v p�vodn�ch seznamech nahrad� "z", kter� se n�sledn� bude vyhodnocovat na konci tak, �e je-li prvek roven "z",
            # byla u tohoto ��sla nalezena shoda, jeli v�ak prvkem p��mo rodn� ��slo, je toto unik�tn� mezi ob�ma datov�mi soubory
        rc1[i] = "z"
        rc2[j] = "z"

# z�pis hlavi�ek do v�stupn�ch soubor�
zapis_stejne_partners(hlavicka1)
zapis_stejne_simplea(hlavicka2)
zapis_unikatni_partners(hlavicka1)
zapis_simplea_unikatni(hlavicka2)

# z�pis dat do v�stupn�ch soubor�
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

