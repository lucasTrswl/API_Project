from pydantic import BaseModel


class Unite(BaseModel):
    """
        A class to represent a unite element.

        ...

        Attributes
        ----------
        un : str
            identifying name for this unit.
        """
    un: str


class UnitePatch(BaseModel):
    """
        A class to represent the properties selected for a patch of an existing resource.

        ...

        Attributes
        ----------
        un : str
            identifying name for this unit.
        """
    un: str = None

