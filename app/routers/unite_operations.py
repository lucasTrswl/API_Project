import psycopg2
from fastapi import HTTPException
from psycopg2.extras import DictCursor, DictRow
from app.models.unite import Unite, UnitePatch
from pydantic import BaseModel


def select_all(cur: DictCursor) -> list[DictRow]:
    cur.execute("SELECT * FROM unite")
    resources = cur.fetchall()
    if len(resources) == 0:
        raise HTTPException(status_code=404, detail="no resource founded for this key")
    for resource in resources:
        print(resource)
    return resources


def select_one(cur: DictCursor, unite_id: str) -> DictRow:
    cur.execute("SELECT * FROM unite Where un = %s", (unite_id,))
    resource = cur.fetchall()
    if len(resource) == 0:
        raise HTTPException(status_code=404, detail="no resource founded for this key")
    return resource[0]


def post(cur: DictCursor, unite: Unite):
    # Check if a resource already exist in the base for this key.
    cur.execute("SELECT * FROM unite Where un = %s", (unite.un,))
    resource = cur.fetchall()
    if len(resource) != 0:
        raise HTTPException(status_code=409, detail="A resource already exist for this key")

    cur.execute("INSERT INTO unite(un) " "VALUES (%s)",
                (unite.un,))


def delete(cur: DictCursor, unite_id: str):
    # Check if the resource exist in the base before trying to modify it.
    cur.execute("SELECT * FROM unite Where un = %s", (unite_id,))
    resource = cur.fetchall()
    if len(resource) == 0:
        raise HTTPException(status_code=404, detail="no resource founded for this key")

    delete_script = 'DELETE FROM unite WHERE un = %s'
    cur.execute(delete_script, unite_id)



