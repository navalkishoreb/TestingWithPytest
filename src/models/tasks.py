from dataclasses import dataclass

@dataclass
class Task():
    summary:str = None
    owner:str = None
    done: bool = False
    _id: str = None
