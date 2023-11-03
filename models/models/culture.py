from pydantic import BaseModel


class Culture(BaseModel):
    """
       A class to represent culture.

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


