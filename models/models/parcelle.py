from pydantic import BaseModel


class Parcelle(BaseModel):
    """
       A class to represent parcelle.

       ...

       Attributes
       ----------
       no_parcelle : int
           Unique identifier of the resource.
       surface : int
           Unity of alculation for the surface of parcelle.
       nom_parcelle : str
           name of the parcelle.
       coordonnees : str
           coordinates of the parcelle location
       """
    no_parcelle: int
    surface: int
    nom_parcelle: str
    coordonnees: str




class ParcellePatch(BaseModel):
    surface: int = None
    nom_parcelle: str = None
    coordonnees: str = None