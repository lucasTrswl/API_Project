from enum import Enum
from pydantic import BaseModel


class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"


class Chemical(BaseModel):
    code_element: str
    un: str
    libelle: str


chemicals = {
    0: Chemical(code_element='1', un='molle', libelle='ça sent bon'),
    1: Chemical(code_element='2', un='molle', libelle='ça sent super bon')
}
