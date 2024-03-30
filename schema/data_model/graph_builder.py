import networkx as nx

from schema.repository.table_repository import TableRepository
from schema.models.table import Table
class GraphBuilder:
    """
        from a data set of Tables accessed from the repo
        builds a graph of related tables
        using a filter to control the graphs contents
    """

    def __init__(self, table_repo:TableRepository) -> None:
        self._table_repo = table_repo

    def build(self, filter) -> nx.Graph:

        g = nx.Graph()

        # ignore filter, just build from all available Tables
        for table_name in self._table_repo.get_table_names():
            table = self._table_repo.get_table(name=table_name)
            g.add_node(node_for_adding=table_name, attr={'table': table})

        # add edges - get the references from each table

        # read all the tables into the graph & then add edges

        for node in g.nodes().data():
            # table_name = node[0]
            table:Table = node[1]['attr']['table']
            references = table.get_relations()
            # references are fks to other table - is the relationship one to many or one to one?

        return g