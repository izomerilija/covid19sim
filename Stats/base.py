import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="malivesa003",
  database = "corona"
)

kursor = mydb.cursor()

#funkcija za pretvaranje liste u string
def list_to_string(lista):
  string = ""
  for i in lista:
    string += str(i)
    if i != lista[len(lista)-1]:
      string += "v"
  return string

#funkcija za pretvaranje stringa u listu
def string_to_list(string):
  pomstring = ""
  lista = []
  for i in string:
    if i != 'v':
      pomstring += i
    else:
      lista.append(pomstring)
      pomstring = ""
  lista.append(pomstring)
  lista = [int(i) for i in lista]
  return lista 

#funkcija za izvlacenje podatka iz tabele iz baze
def get_case(i):
  kursor.execute("SELECT * FROM coronabase WHERE rb = " + str(i))
  lista = []
  for j in kursor:
    lista = list(j)
  lista[1] = string_to_list(lista[1])
  lista[2] = string_to_list(lista[2])
  lista[3] = string_to_list(lista[3])
  lista[4] = string_to_list(lista[4])
  lista.remove(lista[0])
  return lista

#funkcija za dodavanje u tabelu u bazi
def add_case(zivi,mrtvi,zarazeni,ozdravljeni,krajnje_vreme):
  pom1 = '\'' + list_to_string(zivi) + '\''
  pom2 = '\'' + list_to_string(mrtvi) + '\''
  pom3 = '\'' + list_to_string(zarazeni) + '\''
  pom4 = '\'' + list_to_string(ozdravljeni) + '\''
  kursor.execute("INSERT INTO coronabase(zivi,mrtvi,zarazeni,ozdravljeni,krajnje_vreme) VALUES(" + pom1 + "," + pom2 + "," + pom3 + "," + pom4 + "," + str(krajnje_vreme) + ")")
  mydb.commit()

#testiranje
"""
add_case([600,700,800],[300,350,400],[500,200,0],[500,700,1000],3)
print(get_case(1))
"""

#kod za kreaciju tabele
"""
CREATE TABLE coronabase(
rb INT PRIMARY KEY AUTO_INCREMENT,
zivi TEXT,
mrtvi TEXT,
zarazeni TEXT,
ozdravljeni TEXT,
krajnje_vreme INT
);
"""