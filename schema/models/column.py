from dataclasses import dataclass

@dataclass(frozen=True)
class Column:
    name: str
    type: str

    # part of type
    size: int = None
    # when is this set?
    # when there's an explicit references statement for the col?
    references: str = ''
    unique: bool = False
    nullable: bool = True
    default: str = ''
    check: str = ''