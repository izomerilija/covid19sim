import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="malivesa003",
  database = "corona"
)

kursor = mydb.cursor()

#funkcija za izvlacenje podatka iz tabele iz baze
def get_case(i):
  kursor.execute("SELECT * FROM coronabase WHERE rb = " + str(i))
  for j in kursor:
    return j

#funkcija za dodavanje u tabelu u bazi
def add_case(zivi,mrtvi,zarazeni,ozdravljeni,krajnje_vreme):
  kursor.execute("INSERT INTO coronabase(zivi,mrtvi,zarazeni,ozdravljeni,krajnje_vreme) VALUES(" + str(zivi) + "," + str(mrtvi) + "," + str(zarazeni) + "," + str(ozdravljeni) + "," + str(krajnje_vreme) + ")")
  mydb.commit()

#testiranje
"""
add_case(600,300,0,1000,234)
print(get_case(1))
"""

#kod za kreaciju tabele
"""
CREATE TABLE coronabase(
rb INT PRIMARY KEY AUTO_INCREMENT,
zivi INT,
mrtvi INT,
zarazeni INT,
ozdravljeni INT,
krajnje_vreme INT
);
"""