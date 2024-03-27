
from schema.models.table import Table

class TableFactory:

    def create(self, data:dict) -> Table:
        table = Table(**data)
        return table