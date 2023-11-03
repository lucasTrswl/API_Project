from pydantic import BaseModel
import uuid

class Posseder(BaseModel):
    """
       A class to represent the composition of a fertilizer, 
       with what chemicals.

       ...

       Attributes
       ----------
       id_engrais : uuid
           Id of the fertilizer.
       code_element : int
           code of the element
       valeur : str
           value of the of the fertilizer.
       """
    id_engrais: uuid
    code_element: str
    valeur: str


class PossederPatch(BaseModel):
    code_element: str = None
    valeur: str = None


