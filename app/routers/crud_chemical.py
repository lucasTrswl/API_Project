from enum import Enum
from pydantic import BaseModel
import bdd_connection
from bdd_connection import conn, cur
from app.routers.bdd_connection import app


def selec_all_chems():
    bdd_connection.cur.execute("SELECT * FROM customer")
    for record in cur.fetchall():
        print(record)
        print(record['name'])
    print(cur.fetchall())


def toto(cur_):
    print("hello world")



class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"


#class Chemical(BaseModel):
#    code_element: str
#    un: str
#    libelle: str


#chemicals = {
#    0: Chemical(code_element='1', un='molle', libelle='ça sent bon'),
#    1: Chemical(code_element='2', un='molle', libelle='ça sent super bon')
#}


