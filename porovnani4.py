# pøedpokládá se tabulka s daty, kde rodná èísla jsou v prvním sloupci, maily ve druhém a telefonní èísla ve tøetím
# v tabulce se nesmí stát, že by nìkterá z tìchto hodnot chybìla a souèasnì byla poslední hodnotou v øádku
    # (csv by nezaznamenalo práznou buòku)

# FUNKCE
def zapis_stejne_mail(radek): # zapisuje do souboru klienty se shodnými maily
    with open("stejne_mail.csv","a", encoding='utf-8') as mujsoubor:
        print(radek, file=mujsoubor)
def zapis_stejne_telefon(radek): # zapisuje do souboru klienty se shodnými telefonními èísly
    with open("stejne_telefon.csv","a", encoding='utf-8') as mujsoubor:
        print(radek, file=mujsoubor)

def zapis_rozdilne_mail(radek): # zapisuje do souboru klienty s rozdílnými maily (!vèetnì rozdílu ve velikosti písmen!)
    with open("rozdilne_mail.csv","a", encoding='utf-8') as mujsoubor:
        print(radek ,file=mujsoubor)
def zapis_rozdilne_telefon(radek): # zapisuje do souboru klienty s rozdílnými telefonními èísly
    with open("rozdilne_telefon.csv","a", encoding='utf-8') as mujsoubor:
        print(radek, file=mujsoubor)

# PROGRAM
try: # zkusí vyhledat soubor stejne_partners.csv a naèíst jej
    # když soubor nalezne, naète všechny øádky do pole
    vstup1 = open('stejne_partners.csv',"r", encoding='utf-8')
    data_partners = []
    for radek in vstup1:
        data_partners.append(radek.strip())
except: # když soubor nenalezne   
    error = 1
try:
    # analogicky pøedchozímu bloku
    vstup2 = open('stejne_simplea.csv',"r", encoding='utf-8')
    data_simplea = []
    for radek in vstup2:
        data_simplea.append(radek.strip())
except:    
    error = 1

# oèištìní dat od hlavièky tabulky
hlavicka1 = data_partners.pop(0)
hlavicka2 = data_simplea.pop(0)

# založení potøebných polí
rc = [] # rodná èísla (protože jsou již klienti spárovaní mezi obìma zdroji dat a nalezeny shody, rodná èísla jednotlivých øádkù v souèasných zdrojových souborech si odpovídají)
mail1 = [] # maily z Partners
mail2 = [] # maily ze Simpley
telefon1 = [] # telefonní èísla z Partners
telefon2 = [] # telefonní èísla ze Simpley

for a in range(len(data_partners)): # projde prvky pole (øádky zdrojového souboru) a rozdìlí data na rodné èíslo, mail a telefonní èíslo
    radek = data_partners[a].split(";") # rozdìlí prvek pole (øádek z .csv) podle zadaného rozdìlovaèe ';' na jednotlivé položky bunìk
    rc.append(radek[0])
    mail1.append(radek[1])
    telefon1.append(radek[2])
for b in range(len(data_simplea)):
    radek = data_simplea[b].split(";")
    mail2.append(radek[1]) 
    telefon2.append(radek[2])

# pole na zaznamenání nalezených shod nebo rozdílù
stejne_mail = []
rozdilne_mail = []
stejne_telefon = []
rozdilne_telefon = []

for i in range(len(mail1)): # porovnání mailù   
    if mail1[i] == mail2[i]:
        stejne_mail.append(str(rc[i]) + ";" + str(mail1[i]) + ";" + str(mail2[i])) # zápis výsledku ve formátu pro soubor .csv
    else:
        rozdilne_mail.append(str(rc[i]) + ";" + str(mail1[i]) + ";" + str(mail2[i]))
for i in range(len(telefon1)): # porovnání telefonních èísel   
    if telefon1[i] == telefon2[i]:
        stejne_telefon.append(str(rc[i]) + ";" + str(telefon1[i]) + ";" + str(telefon2[i]))
    else:
        rozdilne_telefon.append(str(rc[i]) + ";" + str(telefon1[i]) + ";" + str(telefon2[i]))

# zapsání hlavièek do .csv souborù s výsledky
zapis_stejne_mail("identifikator" + ";" + "mail_partners" + ";" + "mail_simplea")
zapis_rozdilne_mail("identifikator" + ";" + "mail_partners" + ";" + "mail_simplea")
zapis_stejne_telefon("identifikator" + ";" + "telefon_partners" + ";" + "telefon_simplea")
zapis_rozdilne_telefon("identifikator" + ";" + "telefon_partners" + ";" + "telefon_simplea")

# zapsání získaných dat do souborù
for radek1 in range(len(stejne_mail)):
    zapis_stejne_mail(stejne_mail[radek1])
for radek1 in range(len(stejne_telefon)):
    zapis_stejne_telefon(stejne_telefon[radek1])
for radek1 in range(len(rozdilne_mail)):
        zapis_rozdilne_mail(rozdilne_mail[radek1])
for radek1 in range(len(rozdilne_telefon)):
        zapis_rozdilne_telefon(rozdilne_telefon[radek1])