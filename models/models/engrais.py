from pydantic import BaseModel


class Engrais(BaseModel):
    """
       A class to see infos about fertilizer.

       ...

       Attributes
       ----------
       id_engrais : int
           Unique identifier of the fertilizer id.

            
       un : str
           unity of the fertilizer

       nom_engrais : str
           name of the fertilizer.
       """
    id_engrais: int
    un: str
    nom_engrais: str


class EngraisPatch(BaseModel):
    
    un: str = None
    nom_engrais: str = None


