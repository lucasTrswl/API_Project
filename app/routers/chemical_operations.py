import psycopg2
from app.models.chemical import Chemical
from pydantic import BaseModel


def toto(cur_):
    print("hello world")
    cur_.execute("SELECT * FROM elements_chimiques")
    for record in cur_.fetchall():
        print(record)
    print(cur_.fetchall())


def create(cur, chemical: Chemical):
    cur.execute("INSERT INTO elements_chimiques(code_element, un, libelle_element) "
                "VALUES (%s, %s, $s)", (chemical.code_element, chemical.un, chemical.libelle)
                )
    return "success"
