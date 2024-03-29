
from schema.repository.table_repository import TableRepository

class GraphBuilder:
    """
        from a data set of Tables accessed from the repo
        builds a graph of related tables
        using a filter to control the graphs contents
    """

    def __init__(self, table_repo:TableRepository) -> None:

        self._table_repo = table_repo

    def build(self, filter):
        pass