import sys
from typing import Dict

from fastapi import FastAPI
from app.models.production import Production, ProductionPatch
import bdd_constants
import psycopg2
import app.models
import psycopg2.extras
import app.routers
from app.models.chemical import Chemical, ChemicalPatch
from app.models.unite import Unite
from app.models.engrais import Engrais, EngraisPatch
# import app.routers.crud_chemical
from app.routers.bdd_connection import app
from app.routers import chemical_operations, unite_operations, engrais_operations, production_operations
from app.routers.bdd_connection import app
from fastapi import HTTPException

conn2 = psycopg2.connect(
    dbname="posepython",
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
@app.get('/1.0/unite/{unite_id}')
async def get_one_unite(unite_id: str):
    """
    Get a unique resources contained in the "unite" database's table.
    :param unite_id: the unique identifier of the resource requested. (primary key of the table.)
    :return: A datastructure containing meta-datas based on the endpoint and the resource specified.
    """

    try:
        resource = unite_operations.select_one(cur2, unite_id)

        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "get-one-unite",
            "resource_name": "unite",
            "status_code": 200,
            "data": resource
        }
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "get-one-unite",
            "resource_name": "unite",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.get('/1.0/unite')
async def get_unites():
    """
    Get a collection of all resources contained in the "unite" database's table
    :return: A datastructure containing meta-datas based on the endpoint and the collection of resources.
    """
    try:
        resources = unite_operations.select_all(cur2)
        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "get-unite",
            "resource_name": "unite",
            "status_code": 200,
            "data": resources
        }
        return results
    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "get-unite",
            "resource_name": "unite",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.post('/1.0/unite')
async def create_unite(unite: Unite):
    """
   Add a new resource in the "unite" database's table.
   :param unite: A datastructure representing one resource deserialized from the request body.
   :return: A datastructure containing meta-datas based on the endpoint.
   """

    try:
        unite_operations.post(cur2, unite)

        results = {
            "version": 1.0,
            "request": "create-unite",
            "resource_name": "unite",
            "status_code": 200,
            "data": unite
        }
        conn2.commit()
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "create-unite",
            "resource_name": "unite",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.delete('/1.0/unite/{unite_id}')
async def delete_unite(unite_id: str):
    """
    Delete an existing resource in the "unite" database's table.
    :param unite_id: the unique identifier of the resource to delete. (primary key of the table.)
    :return: A datastructure containing meta-datas based on the endpoint.
    """
    try:
        unite_operations.delete(cur2, unite_id)

        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "delete-unite",
            "resource_name": "unite",
            "status_code": 200,
            "data": "Deletion was done with success."
        }
        conn2.commit()
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "delete-unite",
            "resource_name": "unite",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


# Chemical endpoints
@app.get('/1.0/chemicals', tags=['chemical'])
async def get_chemicals():
    """
    Get a collection of all resources contained in the "elements_chimiques" database's table
    :return: A datastructure containing meta-datas based on the endpoint and the collection of resources.
    """
    try:
        resources = chemical_operations.select_all(cur2)
        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "get-chemicals",
            "resource_name": "chemical",
            "status_code": 200,
            "data": resources
        }
        return results
    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "get-chemicals",
            "resource_name": "chemical",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.get('/1.0/chemicalsFiltered')
async def get_chemicals_filtered(un: str = '%', limit: int = 1000, offset: int = 0, order: str = 'DESC'):
    """
    Get a collection of resources contained in the "elements_chimiques" database's table filtered with query parameters.
    :param un: Unite type for which the element is defined.
    :param limit: Maximum number of element recovered in the database.
    :param offset: Value of the starting offset from which we start recovering resources.
    :param order: name of the field to use for alphabetical sorting of the resources.
    :return: A datastructure containing meta-datas based on the endpoint and the collection of resources.
    """
    try:
        select_script = "SELECT * FROM elements_chimiques " + \
                        "WHERE un LIKE %s " + \
                        "LIMIT %s " \
                        "OFFSET %s"
        cur2.execute(select_script, (un, limit, offset))
        resources = cur2.fetchall()
        print(resources)

        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "get-chemical",
            "resource_name": "chemical",
            "status_code": 200,
            "data": resources
        }
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "get-chemicals",
            "resource_name": "chemical",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.get('/1.0/chemicals/{chemical_id}', tags=['chemical'])
async def get_one_chemical(chemical_id: str):
    """
    Get a unique resources contained in the "elements_chimiques" database's table.
    :param chemical_id: the unique identifier of the resource requested. (primary key of the table.)
    :return: A datastructure containing meta-datas based on the endpoint and the resource specified.
    """

    try:
        resource = chemical_operations.select_one(cur2, chemical_id)

        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "get-one-chemical",
            "resource_name": "chemical",
            "status_code": 200,
            "data": resource
        }
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "get-one-chemical",
            "resource_name": "chemical",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.post('/1.0/chemical/', tags=['chemical'])
async def create_chemical(chemical: Chemical):
    """
    Add a new resource in the "elements_chimiques" database's table.
    :param chemical: A datastructure representing one resource deserialized from the request body.
    :return: A datastructure containing meta-datas based on the endpoint.
    """

    try:
        chemical_operations.post(cur2, chemical)

        results = {
            "version": 1.0,
            "request": "create-chemical",
            "resource_name": "chemical",
            "status_code": 200,
            "data": chemical
        }
        conn2.commit()
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "create-chemical",
            "resource_name": "chemical",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.put('/1.0/chemical/{chemical_id}', tags=['chemical'])
async def put_chemical(chemical_id: str, chemical: Chemical):
    """
    Override an existing resource in the "elements_chimiques" database's table.
    :param chemical_id: The unique identifier of the resource to update. (primary key of the table.)
    :param chemical: A datastructure representing one resource deserialized from the request body.
    :return: A datastructure containing meta-datas based on the endpoint.
    """
    try:
        chemical_operations.put(cur2, chemical, chemical_id)
        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "put-chemical",
            "resource_name": "chemical",
            "status_code": 200,
            "data": chemical
        }
        conn2.commit()
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "put-chemical",
            "resource_name": "chemical",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.patch('/1.0/chemical/{chemical_id}', tags=['chemical'])
async def patch_chemical(chemical_id: str, chemical_patch: ChemicalPatch):
    """
    Partial Override an existing resource in the "elements_chimiques" database's table by updating fields.
    :param chemical_id: The unique identifier of the resource to update. (primary key of the table.)
    :param chemical_patch: A datastructure representing the properties to override deserialized from the request body.
    :return: A datastructure containing meta-datas based on the endpoint.
    """
    try:
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

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "patch-chemical",
            "resource_name": "chemical",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.delete('/1.0/chemical/{chemical_id}', tags=['chemical'])
async def delete_chemical(chemical_id: str):
    """
    Delete an existing resource in the "elements_chimiques" database's table.
    :param chemical_id: the unique identifier of the resource to delete. (primary key of the table.)
    :return: A datastructure containing meta-datas based on the endpoint.
    """
    try:
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

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "delete-chemical",
            "resource_name": "chemical",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


#Engrais enpoint
@app.get('/1.0/engrais', tags=['engrais'])
async def get_engrais():
    """
    Get a collection of all resources contained in the "engrais" database's table
    :return: A datastructure containing meta-datas based on the endpoint and the collection of resources.
    """
    try:
        resources = engrais_operations.select_all(cur2)
        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "get-engrais",
            "resource_name": "engrais",
            "status_code": 200,
            "data": resources
        }
        return results
    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "get-engrais",
            "resource_name": "engrais",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.get('/1.0/engraisFiltered', tags=['engrais'])
async def get_engrais_filtered(un: str = 'ANY', limit: int = 1000, offset: int = 0, order: str = 'DESC'):
    """
    Get a collection of resources contained in the "engrais" database's table filtered with query parameters.
    :param un: Unite type for which the element is defined.
    :param limit: Maximum number of element recovered in the database.
    :param offset: Value of the starting offset from which we start recovering resources.
    :param order: name of the field to use for alphabetical sorting of the resources.
    :return: A datastructure containing meta-datas based on the endpoint and the collection of resources.
    """
    try:
        select_script = ("SELECT * FROM engrais "
                         "WHERE un = %s "
                         "LIMIT %s "
                         "OFFSET %s")
        cur2.execute(select_script, (un, limit, offset))
        resources = cur2.fetchall()

        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "patch-engrais",
            "resource_name": "engrais",
            "status_code": 200,
            "data": resources
        }
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "get-engrais",
            "resource_name": "engrais",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.get('/1.0/engrais/{engrais_id}', tags=['engrais'])
async def get_one_engrais(engrais_id: str):
    """
    Get a unique resources contained in the "engrais" database's table.
    :param engrais_id: the unique identifier of the resource requested. (primary key of the table.)
    :return: A datastructure containing meta-datas based on the endpoint and the resource specified.
    """

    try:
        resource = engrais_operations.select_one(cur2, engrais_id)

        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "get-one-engrais",
            "resource_name": "engrais",
            "status_code": 200,
            "data": resource
        }
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "get-one-engrais",
            "resource_name": "engrais",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.post('/1.0/engrais/', tags=['engrais'])
async def create_engrais(engrais: Engrais):
    """
    Add a new resource in the "engrais" database's table.
    :param engrais: A datastructure representing one resource deserialized from the request body.
    :return: A datastructure containing meta-datas based on the endpoint.
    """

    try:
        engrais_operations.post(cur2, engrais)

        results = {
            "version": 1.0,
            "request": "create-engrais",
            "status_code": 200,
            "data": engrais
        }
        conn2.commit()
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "create-engrais",
            "resource_name": "engrais",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.put('/1.0/engrais/{engrais_id}', tags=['engrais'])
async def put_engrais(engrais_id: str, engrais: Engrais):
    """
    Override an existing resource in the "engrais" database's table.
    :param engrais_id: The unique identifier of the resource to update. (primary key of the table.)
    :param engrais: A datastructure representing one resource deserialized from the request body.
    :return: A datastructure containing meta-datas based on the endpoint.
    """
    try:
        engrais_operations.put(cur2, engrais, engrais_id)
        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "put-engrais",
            "resource_name": "engrais",
            "status_code": 200,
            "data": engrais
        }
        conn2.commit()
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "put-engrais",
            "resource_name": "engrais",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.patch('/1.0/engrais/{engrais_id}', tags=['engrais'])
async def patch_engrais(engrais_id: str, engrais_patch: EngraisPatch):
    """
    Partial Override an existing resource in the "engrais" database's table by updating fields.
    :param engrais_id: The unique identifier of the resource to update. (primary key of the table.)
    :param engrais_patch: A datastructure representing the properties to override deserialized from the request body.
    :return: A datastructure containing meta-datas based on the endpoint.
    """
    try:
        engrais_operations.patch(cur2, engrais_patch, engrais_id)

        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "patch-engrais",
            "resource_name": "engrais",
            "status_code": 200,
            "data": engrais_patch
        }
        conn2.commit()
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "patch-engrais",
            "resource_name": "engrais",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.delete('/1.0/engrais/{engrais_id}', tags=['engrais'])
async def delete_engrais(engrais_id: str):
    """
    Delete an existing resource in the "engrais" database's table.
    :param engrais_id: the unique identifier of the resource to delete. (primary key of the table.)
    :return: A datastructure containing meta-datas based on the endpoint.
    """
    try:
        engrais_operations.delete(cur2, engrais_id)

        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "delete-engrais",
            "resource_name": "engrais",
            "status_code": 200,
            "data": "Deletion was done with success."
        }
        conn2.commit()
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "delete-engrais",
            "resource_name": "engrais",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results







##################################################################################


## PRODUCTION

##################################################################################




@app.get('/1.0/production')
async def get_production():
    """
    Get a collection of all resources contained in the "production" database's table
    :return: A datastructure containing meta-datas based on the endpoint and the collection of resources.
    """
    try:
        resources = production_operations.select_all(cur2)
        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "get-production",
            "resource_name": "production",
            "status_code": 200,
            "data": resources
        }
        return results
    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "get-production",
            "resource_name": "production",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.get('/1.0/productionFiltered')
async def get_production_filtered(un: str = 'ANY', limit: int = 1000, offset: int = 0, order: str = 'DESC'):
    """
    Get a collection of resources contained in the "production" database's table filtered with query parameters.
    :param un: Unite type for which the element is defined.
    :param limit: Maximum number of element recovered in the database.
    :param offset: Value of the starting offset from which we start recovering resources.
    :param order: name of the field to use for alphabetical sorting of the resources.
    :return: A datastructure containing meta-datas based on the endpoint and the collection of resources.
    """
    try:
        select_script = ("SELECT * FROM production "
                         "WHERE un = %s "
                         "LIMIT %s "
                         "OFFSET %s")
        cur2.execute(select_script, (un, limit, offset))
        resources = cur2.fetchall()

        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "patch-production",
            "resource_name": "production",
            "status_code": 200,
            "data": resources
        }
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "get-production",
            "resource_name": "production",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.get('/1.0/production/{production_id}')
async def get_one_production(production_id: str):
    """
    Get a unique resources contained in the "production" database's table.
    :param production_id: the unique identifier of the resource requested. (primary key of the table.)
    :return: A datastructure containing meta-datas based on the endpoint and the resource specified.
    """

    try:
        resource = production_operations.select_one(cur2, production_id)

        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "get-one-production",
            "resource_name": "production",
            "status_code": 200,
            "data": resource
        }
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "get-one-production",
            "resource_name": "production",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.post('/1.0/production/')
async def create_production(production: Production):
    """
    Add a new resource in the "production" database's table.
    :param production: A datastructure representing one resource deserialized from the request body.
    :return: A datastructure containing meta-datas based on the endpoint.
    """

    try:
        production_operations.post(cur2, production)

        results = {
            "version": 1.0,
            "request": "create-production",
            "status_code": 200,
            "data": production
        }
        conn2.commit()
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "create-production",
            "resource_name": "production",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.put('/1.0/production/{production_id}')
async def put_production(production_id: str, production: Production):
    """
    Override an existing resource in the "production" database's table.
    :param production_id: The unique identifier of the resource to update. (primary key of the table.)
    :param production: A datastructure representing one resource deserialized from the request body.
    :return: A datastructure containing meta-datas based on the endpoint.
    """
    try:
        production_operations.put(cur2, production, production_id)
        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "put-production",
            "resource_name": "production",
            "status_code": 200,
            "data": production
        }
        conn2.commit()
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "put-production",
            "resource_name": "production",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.patch('/1.0/production/{production_id}')
async def patch_production(production_id: str, production_patch: ProductionPatch):
    """
    Partial Override an existing resource in the "production" database's table by updating fields.
    :param production_id: The unique identifier of the resource to update. (primary key of the table.)
    :param production_patch: A datastructure representing the properties to override deserialized from the request body.
    :return: A datastructure containing meta-datas based on the endpoint.
    """
    try:
        production_operations.patch(cur2, production_patch, production_id)

        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "patch-production",
            "resource_name": "production",
            "status_code": 200,
            "data": production_patch
        }
        conn2.commit()
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "patch-production",
            "resource_name": "production",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results


@app.delete('/1.0/production/{production_id}')
async def delete_production(production_id: str):
    """
    Delete an existing resource in the "elements_chimiques" database's table.
    :param production_id: the unique identifier of the resource to delete. (primary key of the table.)
    :return: A datastructure containing meta-datas based on the endpoint.
    """
    try:
        production_operations.delete(cur2, production_id)

        # Datastructure to return containing the resource(s) and additional datas about the API's endpoint.
        results = {
            "version": 1.0,
            "request": "delete-production",
            "resource_name": "production",
            "status_code": 200,
            "data": "Deletion was done with success."
        }
        conn2.commit()
        return results

    except HTTPException as e:
        results = {
            "version": 1.0,
            "request": "delete-production",
            "resource_name": "production",
            "status_code": e.status_code,
            "data": e.detail
        }
        return results






































# Press the green button in the gutter to run the script.
def main():
    print("main function call")
    print("main function end")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/




if __name__ == '__main__':
    main()
