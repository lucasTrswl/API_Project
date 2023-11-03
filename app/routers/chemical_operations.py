import psycopg2
from fastapi import HTTPException
from psycopg2.extras import DictCursor, DictRow

from app.models.chemical import Chemical, ChemicalPatch
from pydantic import BaseModel

def select_all(cur: DictCursor) -> list[DictRow]:
    print("hello world")
    cur.execute("SELECT * FROM elements_chimiques")
    resources = cur.fetchall()
    if len(resources) == 0:
        raise HTTPException(status_code=404, detail="no resource founded for this key")
    for resource in resources:
        print(resource)
    return resources


def select_one(cur: DictCursor, chemical_id: str) -> DictRow:
    cur.execute("SELECT * FROM elements_chimiques Where code_element = %s", (chemical_id,))
    resource = cur.fetchall()
    if len(resource) == 0:
        raise HTTPException(status_code=404, detail="no resource founded for this key")
    return resource[0]


def put(cur: DictCursor, chemical: Chemical, chemical_id: str):
    # Check if the resource exist in the base before trying to modify it.
    cur.execute("SELECT * FROM elements_chimiques Where code_element = %s", (chemical_id,))
    resource = cur.fetchall()
    if len(resource) == 0:
        raise HTTPException(status_code=404, detail="no resource founded for this key")

    update_script = ('UPDATE elements_chimiques '
                     'SET un = %s, '
                     'libelle_element = %s'
                     'where code_element = %s')
    cur.execute(update_script, (chemical.un, chemical.libelle, chemical_id))


def patch(cur: DictCursor, chemical_patch: ChemicalPatch, chemical_id: str):
    # Check if the resource exist in the base before trying to modify it.
    cur.execute("SELECT * FROM elements_chimiques Where code_element = %s", (chemical_id,))
    resource = cur.fetchall()
    if len(resource) == 0:
        raise HTTPException(status_code=404, detail="no resource founded for this key")

    # If the field un is defined in the patch deserialized, override the value of the database's element.
    if chemical_patch.un is not None:
        cur.execute('UPDATE elements_chimiques '
                    'SET un = %s '
                    'where code_element = %s',
                    (chemical_patch.un, chemical_id))

    # If the field libelle is defined in the patch deserialized, override the value of the database's element.
    if chemical_patch.libelle is not None:
        cur.execute('UPDATE elements_chimiques '
                    'SET libelle_element = %s '
                    'where code_element = %s',
                    (chemical_patch.libelle, chemical_id))


def post(cur: DictCursor, chemical: Chemical):
    # Check if a resource already exist in the base for this key.
    cur.execute("SELECT * FROM elements_chimiques Where code_element = %s", (chemical.code_element,))
    resource = cur.fetchall()
    if len(resource) != 0:
        raise HTTPException(status_code=409, detail="A resource already exist for this key")

    cur.execute("INSERT INTO elements_chimiques(code_element, un, libelle_element) " "VALUES (%s, %s, %s)",
                (chemical.code_element, chemical.un, chemical.libelle,))

    # placeholder to fill database for test
    # cur2.execute("INSERT INTO elements_chimiques VALUES('N', 'mole', 'Azote')")
    # cur2.execute("INSERT INTO elements_chimiques VALUES('P', 'mole', 'Phosphore')")
    # cur2.execute("INSERT INTO elements_chimiques VALUES('Na', 'mole', 'Sodium')")
    # cur2.execute("INSERT INTO elements_chimiques VALUES('N_m', 'milligram', 'Azote')")


def delete(cur: DictCursor, chemical_id: str):
    # Check if the resource exist in the base before trying to modify it.
    cur.execute("SELECT * FROM elements_chimiques Where code_element = %s", (chemical_id,))
    resource = cur.fetchall()
    if len(resource) == 0:
        raise HTTPException(status_code=404, detail="no resource founded for this key")

    delete_script = 'DELETE FROM elements_chimiques WHERE code_element = %s'
    cur.execute(delete_script, chemical_id)


