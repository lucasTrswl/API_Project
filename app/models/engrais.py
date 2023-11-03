from pydantic import BaseModel


class Engrais(BaseModel):
    """
       A class to see infos about fertilizer.

       ...

       Attributes
       ----------
       id_engrais : str
           Unique identifier of the fertilizer id.

            
       un : str
           unity of the fertilizer

       nom : str
           name of the fertilizer.
       """
    id_engrais: str = None
    un: str
    nom: str


class EngraisPatch(BaseModel):
    
    un: str = None
    nom: str = None
