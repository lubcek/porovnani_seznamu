# p�edpokl�d� se tabulka s daty, kde rodn� ��sla jsou v prvn�m sloupci, maily ve druh�m a telefonn� ��sla ve t�et�m
# v tabulce se nesm� st�t, �e by n�kter� z t�chto hodnot chyb�la a sou�asn� byla posledn� hodnotou v ��dku
    # (csv by nezaznamenalo pr�znou bu�ku)

# FUNKCE
def zapis_stejne_mail(radek): # zapisuje do souboru klienty se shodn�mi maily
    with open("stejne_mail.csv","a", encoding='utf-8') as mujsoubor:
        print(radek, file=mujsoubor)
def zapis_stejne_telefon(radek): # zapisuje do souboru klienty se shodn�mi telefonn�mi ��sly
    with open("stejne_telefon.csv","a", encoding='utf-8') as mujsoubor:
        print(radek, file=mujsoubor)

def zapis_rozdilne_mail(radek): # zapisuje do souboru klienty s rozd�ln�mi maily (!v�etn� rozd�lu ve velikosti p�smen!)
    with open("rozdilne_mail.csv","a", encoding='utf-8') as mujsoubor:
        print(radek ,file=mujsoubor)
def zapis_rozdilne_telefon(radek): # zapisuje do souboru klienty s rozd�ln�mi telefonn�mi ��sly
    with open("rozdilne_telefon.csv","a", encoding='utf-8') as mujsoubor:
        print(radek, file=mujsoubor)

# PROGRAM
try: # zkus� vyhledat soubor stejne_partners.csv a na��st jej
    # kdy� soubor nalezne, na�te v�echny ��dky do pole
    vstup1 = open('stejne_partners.csv',"r", encoding='utf-8')
    data_partners = []
    for radek in vstup1:
        data_partners.append(radek.strip())
except: # kdy� soubor nenalezne   
    error = 1
try:
    # analogicky p�edchoz�mu bloku
    vstup2 = open('stejne_simplea.csv',"r", encoding='utf-8')
    data_simplea = []
    for radek in vstup2:
        data_simplea.append(radek.strip())
except:    
    error = 1

# o�i�t�n� dat od hlavi�ky tabulky
hlavicka1 = data_partners.pop(0)
hlavicka2 = data_simplea.pop(0)

# zalo�en� pot�ebn�ch pol�
rc = [] # rodn� ��sla (proto�e jsou ji� klienti sp�rovan� mezi ob�ma zdroji dat a nalezeny shody, rodn� ��sla jednotliv�ch ��dk� v sou�asn�ch zdrojov�ch souborech si odpov�daj�)
mail1 = [] # maily z Partners
mail2 = [] # maily ze Simpley
telefon1 = [] # telefonn� ��sla z Partners
telefon2 = [] # telefonn� ��sla ze Simpley

for a in range(len(data_partners)): # projde prvky pole (��dky zdrojov�ho souboru) a rozd�l� data na rodn� ��slo, mail a telefonn� ��slo
    radek = data_partners[a].split(";") # rozd�l� prvek pole (��dek z .csv) podle zadan�ho rozd�lova�e ';' na jednotliv� polo�ky bun�k
    rc.append(radek[0])
    mail1.append(radek[1])
    telefon1.append(radek[2])
for b in range(len(data_simplea)):
    radek = data_simplea[b].split(";")
    mail2.append(radek[1]) 
    telefon2.append(radek[2])

# pole na zaznamen�n� nalezen�ch shod nebo rozd�l�
stejne_mail = []
rozdilne_mail = []
stejne_telefon = []
rozdilne_telefon = []

for i in range(len(mail1)): # porovn�n� mail�   
    if mail1[i] == mail2[i]:
        stejne_mail.append(str(rc[i]) + ";" + str(mail1[i]) + ";" + str(mail2[i])) # z�pis v�sledku ve form�tu pro soubor .csv
    else:
        rozdilne_mail.append(str(rc[i]) + ";" + str(mail1[i]) + ";" + str(mail2[i]))
for i in range(len(telefon1)): # porovn�n� telefonn�ch ��sel   
    if telefon1[i] == telefon2[i]:
        stejne_telefon.append(str(rc[i]) + ";" + str(telefon1[i]) + ";" + str(telefon2[i]))
    else:
        rozdilne_telefon.append(str(rc[i]) + ";" + str(telefon1[i]) + ";" + str(telefon2[i]))

# zaps�n� hlavi�ek do .csv soubor� s v�sledky
zapis_stejne_mail("identifikator" + ";" + "mail_partners" + ";" + "mail_simplea")
zapis_rozdilne_mail("identifikator" + ";" + "mail_partners" + ";" + "mail_simplea")
zapis_stejne_telefon("identifikator" + ";" + "telefon_partners" + ";" + "telefon_simplea")
zapis_rozdilne_telefon("identifikator" + ";" + "telefon_partners" + ";" + "telefon_simplea")

# zaps�n� z�skan�ch dat do soubor�
for radek1 in range(len(stejne_mail)):
    zapis_stejne_mail(stejne_mail[radek1])
for radek1 in range(len(stejne_telefon)):
    zapis_stejne_telefon(stejne_telefon[radek1])
for radek1 in range(len(rozdilne_mail)):
        zapis_rozdilne_mail(rozdilne_mail[radek1])
for radek1 in range(len(rozdilne_telefon)):
        zapis_rozdilne_telefon(rozdilne_telefon[radek1])