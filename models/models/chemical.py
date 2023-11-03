from pydantic import BaseModel


class Chemical(BaseModel):
    """
       A class to represent chemical element.

       ...

       Attributes
       ----------
       code_element : str
           Unique identifier of the resource.
       un : str
           Unite of measurement used for the chemical.
       libelle : str
           short description for the chemical.
       """
    code_element: str
    un: str
    libelle: str


class ChemicalPatch(BaseModel):
    """
           A class to represent the properties selected for a patch of an existing resource.

           ...

           Attributes
           ----------
           un : str
               Unite of measurement used for the chemical to override.
           libelle : str
               short description for the chemical to override.
           """
    un: str = None
    libelle: str = None
