import psycopg2
from fastapi import HTTPException
from psycopg2.extras import DictCursor, DictRow

from app.models.engrais import Engrais, EngraisPatch
from pydantic import BaseModel

def select_all(cur: DictCursor) -> list[DictRow]:
    print("hello world")
    cur.execute("SELECT * FROM engrais")
    resources = cur.fetchall()
    if len(resources) == 0:
        raise HTTPException(status_code=404, detail="no resource founded for this key")
    for resource in resources:
        print(resource)
    return resources


def select_one(cur: DictCursor, engrais_id: str) -> DictRow:
    cur.execute("SELECT * FROM engrais Where id_engrais = %s", (engrais_id,))
    resource = cur.fetchall()
    if len(resource) == 0:
        raise HTTPException(status_code=404, detail="no resource founded for this key")
    return resource[0]


def put(cur: DictCursor, engrais: Engrais, engrais_id: str):
    # Check if the resource exist in the base before trying to modify it.
    cur.execute("SELECT * FROM engrais Where id_engrais = %s", (engrais_id,))
    resource = cur.fetchall()
    if len(resource) == 0:
        raise HTTPException(status_code=404, detail="no resource founded for this key")

    update_script = ('UPDATE engrais '
                     'SET un = %s, '
                     'nom_engrais = %s'
                     'where id_engrais = %s')
    cur.execute(update_script, (engrais.un, engrais.nom, engrais_id))


def patch(cur: DictCursor, engrais_patch: EngraisPatch, engrais_id: str):
    # Check if the resource exist in the base before trying to modify it.
    cur.execute("SELECT * FROM engrais Where id_engrais = %s", (engrais_id,))
    resource = cur.fetchall()
    if len(resource) == 0:
        raise HTTPException(status_code=404, detail="no resource founded for this key")

    # If the field un is defined in the patch deserialized, override the value of the database's element.
    if engrais_patch.un is not None:
        cur.execute('UPDATE engrais '
                    'SET un = %s '
                    'where id_engrais = %s',
                    (engrais_patch.un, engrais_id))

    # If the field nom is defined in the patch deserialized, override the value of the database's element.
    if engrais_patch.nom is not None:
        cur.execute('UPDATE engrais '
                    'SET nom_engrais = %s '
                    'where id_engrais = %s',
                    (engrais_patch.nom, engrais_id))


def post(cur: DictCursor, engrais: Engrais):
    cur.execute("INSERT INTO engrais(un, nom_engrais) " "VALUES (%s, %s)",
                (engrais.un, engrais.nom,))

    # placeholder to fill database for test
    # cur2.execute("INSERT INTO engrais VALUES('N', 'mole', 'Azote')")
    # cur2.execute("INSERT INTO engrais VALUES('P', 'mole', 'Phosphore')")
    # cur2.execute("INSERT INTO engrais VALUES('Na', 'mole', 'Sodium')")
    # cur2.execute("INSERT INTO engrais VALUES('N_m', 'milligram', 'Azote')")


def delete(cur: DictCursor, engrais_id: str):
    # Check if the resource exist in the base before trying to modify it.
    cur.execute("SELECT * FROM engrais Where id_engrais = %s", (engrais_id,))
    resource = cur.fetchall()
    if len(resource) == 0:
        raise HTTPException(status_code=404, detail="no resource founded for this key")

    delete_script = 'DELETE FROM engrais WHERE id_engrais = %s'
    cur.execute(delete_script, engrais_id)


