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

description ="""

API 

## Items

Youcan**readitems**.

## Users

Youwillbeableto:

***Createusers**(_notimplemented_).

***Readusers**(_notimplemented_).
"""

tags_metadata = [
    {
        "name": "unite",
    },
    {
        "name": "chemical",
    },
    {
        "name": "parcelle",
    },
    {
        "name": "engrais",
    },
    {
        "name": "epandre",
    },
    {
        "name": "posseder",
    },
    {
        "name": "production",
    },
    {
        "name": "culture",
    },
]

app = FastAPI(
    title="APIPosépython",
    description=description,
    summary="API de gestion des cultures",
    version="1.0",
    contact={
        "name": "Github",
        "url": "https://github.com/lucasTrswl/API_Project",
    },
    license_info={
        "name": "Trello",
        "url": "https://trello.com/invite/b/OQVA1Pf8/ATTI1ea6df582f6a47f23098ac1984c01ee71BFB4FDB/posepython",
    },
    openapi_tags=tags_metadata
)

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


