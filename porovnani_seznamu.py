
def zapis_stejne(radek): # je-li identifikátor nalezen v obou seznamech, zapíše se mezi nalezené shody
    with open("stejne.csv","a", encoding='utf-8') as mujsoubor:
        print(radek, file=mujsoubor)

def zapis_jen_v_prvnim(radek): # pokud prohledávání nenašlo shodu, zapíšou se nespárované položky prvního seznamu do unikátních uživatelů z prvního seznamu
    with open("prvni.csv","a", encoding='utf-8') as mujsoubor:
        print(radek ,file=mujsoubor)

def zapis_jen_ve_druhem(radek): # po konci prohledávání se zapíšou zbylé položky druhého seznamu do unikátních uživatelů z druhého seznamu
    with open("druhe.csv","a", encoding='utf-8') as mujsoubor:
        print(radek, file=mujsoubor)

try:
    vstup1 = open('jedna.csv',"r", encoding='utf-8')
    soubor1 = []
    for radek in vstup1:
        soubor1.append(radek.strip()) # vložení všech řádků prvního souboru po pole
except:    
    error = 1
try:
    vstup2 = open('dva.csv',"r", encoding='utf-8')
    soubor2 = []
    for radek in vstup2:
        soubor2.append(radek.strip()) # vložení všech řádků druhého souboru po pole
except:    
    error = 1

# odstraneni hlavicky
hlavicka1 = soubor1.pop(0)
hlavicka2 = soubor2.pop(0)

data1 = []
data2 = []

for a in range(len(soubor1)):
    radek = soubor1[a].split(";")
    data1.append(radek[0])
for b in range(len(soubor2)):
    radek = soubor2[b].split(";")
    data2.append(radek[3])

j = 0
stejne = []
for i in range(len(data1)):
    while j < len(data2)-1 and data2[j] < data1[i] or data2[j] == "z":
        j += 1
    if data1[i] == data2[j]:
        stejne.append(soubor1[i])
        data1[i] = "z"
        data2[j] = "z"

zapis_stejne(hlavicka1)
for radek1 in range(len(stejne)):
    zapis_stejne(stejne[radek1])
zapis_jen_v_prvnim(hlavicka1)
for radek2 in range(len(soubor1)):
    if data1[radek2] != "z":
        zapis_jen_v_prvnim(soubor1[radek2])
zapis_jen_ve_druhem(hlavicka2)
for radek3 in range(len(soubor2)):
    if data2[radek3] != "z":
        zapis_jen_ve_druhem(soubor2[radek3])
