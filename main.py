import sys
from typing import Dict

from fastapi import FastAPI
import bdd_constants
import psycopg2
import app.models
import psycopg2.extras
import app.routers
from app.models.chemical import ChemicalPatch
from app.models.unite import Unite
# import app.routers.crud_chemical
from app.routers import chemical_operations
from app.routers.bdd_connection import app, Chemical, chemicals

conn2 = psycopg2.connect(
    dbname="popo",
    user="postgres",
    password="postgres",
)

# cursor will return data as dictionary for easier parsing.
# cur2 = conn2.cursor()
cur2 = conn2.cursor(cursor_factory=psycopg2.extras.DictCursor)
app2 = FastAPI()


# Default endpoint
@app.get('/')
async def root():
    """
    Default root of the API.
    :return: A simple string message.
    """
    return "This is the initial root."


# Unite endpoints.
@app.post('/1.0/unite')
async def create_unite(unite: Unite):
    # cur2.execute("INSERT INTO unite VALUES('V')")

    cur2.execute("INSERT INTO unite(un) " "VALUES (%s)",
                 (unite.un,))
    results = {
        "version": 1.0,
        "request": "create-unite",
        "status_code": 200,
        "data": unite
    }
    conn2.commit()
    return results


# Chemical endpoints
@app.get('/1.0/chemicals')
async def get_chemicals():
    """
    Get a collection of all resources contained in the "elements_chimiques" database's table
    :return: A datastructure containing meta-datas based on the endpoint and the collection of resources.
    """
    resources = chemical_operations.select_all(cur2)
    # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
    results = {
        "version": 1.0,
        "request": "patch-chemical",
        "resource_name": "chemical",
        "status_code": 200,
        "data": resources
    }
    return results


@app.get('/1.0/chemicalsFiltered')
async def get_chemicals_filtered(un: str = 'ANY', limit: int = 1000, offset: int = 0, order: str = 'DESC'):
    """
    Get a collection of resources contained in the "elements_chimiques" database's table filtered with query parameters.
    :param un: Unite type for which the element is defined.
    :param limit: Maximum number of element recovered in the database.
    :param offset: Value of the starting offset from which we start recovering resources.
    :param order: name of the field to use for alphabetical sorting of the resources.
    :return: A datastructure containing meta-datas based on the endpoint and the collection of resources.
    """
    select_script = ("SELECT * FROM elements_chimiques "
                     "WHERE un = %s "
                     "LIMIT %s "
                     "OFFSET %s")
    cur2.execute(select_script, (un, limit, offset))
    resources = cur2.fetchall()

    # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
    results = {
        "version": 1.0,
        "request": "patch-chemical",
        "resource_name": "chemical",
        "status_code": 200,
        "data": resources
    }
    return results


@app.get('/1.0/chemicals/{chemical_id}')
async def get_one_chemical(chemical_id: str):
    """
    Get a unique resources contained in the "elements_chimiques" database's table.
    :param chemical_id: the unique identifier of the resource requested. (primary key of the table.)
    :return: A datastructure containing meta-datas based on the endpoint and the resource specified.
    """
    resource = chemical_operations.select_one(cur2, chemical_id)

    # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
    results = {
        "version": 1.0,
        "request": "patch-chemical",
        "resource_name": "chemical",
        "status_code": 200,
        "data": resource
    }
    return results


@app.post('/1.0/chemical/')
async def create_chemical(chemical: Chemical):
    """
    Add a new resource in the "elements_chimiques" database's table.
    :param chemical: A datastructure representing one resource deserialized from the request body.
    :return: A datastructure containing meta-datas based on the endpoint.
    """
    chemical_operations.post(cur2, chemical)

    results = {
        "version": 1.0,
        "request": "create-chemical",
        "status_code": 200,
        "data": chemical
    }
    conn2.commit()
    return results


@app.put('/1.0/chemical/{chemical_id}')
async def put_chemical(chemical_id: str, chemical: Chemical):
    """
    Override an existing resource in the "elements_chimiques" database's table.
    :param chemical_id: The unique identifier of the resource to update. (primary key of the table.)
    :param chemical: A datastructure representing one resource deserialized from the request body.
    :return: A datastructure containing meta-datas based on the endpoint.
    """
    chemical_operations.put(cur2, chemical, chemical_id)

    # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
    results = {
        "version": 1.0,
        "request": "patch-chemical",
        "resource_name": "chemical",
        "status_code": 200,
        "data": chemical
    }
    conn2.commit()
    return results


@app.patch('/1.0/chemical/{chemical_id}')
async def patch_chemical(chemical_id: str, chemical_patch: ChemicalPatch):
    """
    Partial Override an existing resource in the "elements_chimiques" database's table by updating fields.
    :param chemical_id: The unique identifier of the resource to update. (primary key of the table.)
    :param chemical_patch: A datastructure representing the properties to override deserialized from the request body.
    :return: A datastructure containing meta-datas based on the endpoint.
    """

    chemical_operations.patch(cur2, chemical_patch, chemical_id)

    # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
    results = {
        "version": 1.0,
        "request": "patch-chemical",
        "resource_name": "chemical",
        "status_code": 200,
        "data": chemical_patch
    }
    conn2.commit()
    return results


@app.delete('/1.0/chemical/{chemical_id}')
async def delete_chemical(chemical_id: str):
    """
    Delete an existing resource in the "elements_chimiques" database's table.
    :param chemical_id: the unique identifier of the resource to delete. (primary key of the table.)
    :return: A datastructure containing meta-datas based on the endpoint.
    """
    chemical_operations.delete(cur2, chemical_id)

    # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
    results = {
        "version": 1.0,
        "request": "delete-chemical",
        "resource_name": "chemical",
        "status_code": 200,
        "data": "Deletion was done with success."
    }
    conn2.commit()
    return results


# Press the green button in the gutter to run the script.
def main():
    print("main function call")
    print("main function end")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


if __name__ == '__main__':
    main()
