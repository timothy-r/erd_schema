from dataclasses import dataclass

@dataclass
class Column:
    name: str
    type: str
    size: int
    # when is this set?
    # when there's an explicit references statement for the col?
    references: str
    unique: bool
    nullable: bool
    default: bool
    check: bool