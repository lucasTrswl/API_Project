from pydantic import BaseModel
import uuid, date

class Epandre(BaseModel):
    """
       A class to represent spread.

       ...

       Attributes
       ----------
       id_engrais : uuid
            id of the fertilizer to spread

       no_parcelle : int
           Number of the plot.
       date : date
            date of the spread
           
       qte_repandue : int
           quantity spread during the operation.
       """
    id_engrais: uuid
    no_parcelle: int
    date: date
    qte_repandue: int




class EpandrePatch(BaseModel):
     
     no_parcelle: int = None
     date: int = None
     qte_repandue: int = None


