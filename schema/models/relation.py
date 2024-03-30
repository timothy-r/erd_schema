from dataclasses import dataclass
from enum import Enum

class RelationType(Enum):
    # ZERO = 0
    ONE = 1
    MANY = 2

    ZERO_OR_ONE = 3
    ZERO_OR_MANY = 4
    ONE_OR_MANY = 5
    ONE_AND_ONLY_ONE = 6

@dataclass(frozen=True)
class Relation:

    from_table: str
    from_col: str
    to_table: str
    to_col: str

    from_type: RelationType
    to_type: RelationType