from pydantic import BaseModel


class Parcelle(BaseModel):
    """
       A class to represent plot.

       ...

       Attributes
       ----------
       no_parcelle : int
           Unique identifier of the resource.
       surface : int
           Unity of calculation for the surface of plot.
       nom_parcelle : str
           name of the plot.
       coordonnees : str
           coordinates of the plot location
       """
    no_parcelle: int
    surface: int
    nom_parcelle: str
    coordonnees: str




class ParcellePatch(BaseModel):
    surface: int = None
    nom_parcelle: str = None
    coordonnees: str = None