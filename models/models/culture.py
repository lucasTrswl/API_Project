from pydantic import BaseModel
import date

class Culture(BaseModel):
    """
       A class to represent culture.

       ...

       Attributes
       ----------
       identifiant_culture : int
           id of the culture
        
       no_parcelle : int
           Number of the plot.
       surface : int
           
       code_production : int
           code of the production.

        date_debut : date
            beginning of the recolt

        date_fin : date
            ending of the recolt

        qte_recoltee : int
            harvested quantity 

       """
    
    
    identifiant_culture: int
    no_parcelle: int
    code_production: int
    date_debut: date
    date_fin: date
    qte_recoltee: int

class CulturePatch(BaseModel):
    no_parcelle: int = None
    code_production: int = None
    date_debut: date = None
    date_fin: date = None
    qte_recoltee: int = None


