from pydantic import BaseModel


class Production(BaseModel):
    """
       A class to represent production.

       ...

       Attributes
       ----------
       code_production : int
           Unique identifier of the resource.
       un : str
           Unite of measurement used for the production.
       libelle : str
           name of the production.
       """
    code_production: int
    un: str
    nom_production: str



class ProductionPatch(BaseModel):

    un: str = None
    nom_production: str = None
    