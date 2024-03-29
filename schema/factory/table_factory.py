from schema.models.table import Table
from schema.models.column import Column
class TableFactory:

    def create(self, data:dict) -> Table:

        columns = {}
        for col in data['columns']:
            columns[col['name']] = Column(**col)

        data['columns'] = columns
        table = Table(**data)
        return table