from enum import Enum

import psycopg2
import psycopg2.extras
from fastapi import FastAPI
from pydantic import BaseModel

conn = psycopg2.connect(
    dbname="posepython",
    user="postgres",
    password="postgres",
)

# cursor will return data as dictionary for easier parsing.
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

app = FastAPI()

class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"


class Chemical(BaseModel):
    code_element: str
    un: str
    libelle: str


chemicals = {
    0: Chemical(code_element='1', un='molle', libelle='ça sent bon'),
    1: Chemical(code_element='2', un='molle', libelle='ça sent super bon')
}


