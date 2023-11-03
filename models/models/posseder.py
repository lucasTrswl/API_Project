from pydantic import BaseModel


class Posseder(BaseModel):
    """
       A class to represent the composition of a fertilizer, 
       with what chemicals.

       ...

       Attributes
       ----------
       no_parcelle : int
           Number of the parcelle.
       surface : int
           
       libelle : str
           name of the production.
       """
    no_parcelle: int
    surface: int
    nom_parcelle: str
    coordonnees: str


class CulturePatch(BaseModel):
    surface: int = None
    nom_parcelle: str = None
    coordonnees: str = None


