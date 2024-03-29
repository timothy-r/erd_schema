from unittest import TestCase
from unittest.mock import MagicMock, patch

from tests.test_fixtures import TestFixtures

# from schema.factory.table_factory import TableFactory
# from schema.repository.table_repository import TableRepository

from schema.models.table import Table
from schema.models.column import Column

from schema.data_model.graph_builder import GraphBuilder

def mocked_repo_get_table_names() -> Table:
    return ['public.user','public.group', 'public.address']


def mocked_repo_get_table(name:str) -> Table:
    if name == 'user':
        cols = {
            'id': Column(
                name='id',
                type='int',
                size=None,
                references='',
                unique=True,
                nullable=False
            ),
            'group_id': Column(
                name='group_id',
                type='int',
                size=None,
                references='',
                unique=False,
                nullable=False
            )
        }
        alter = {
            "columns": [
            {
                "name": "group_id",
                "constraint_name": None,
                "references": {
                    "table": "group",
                    "schema": "public",
                    "on_delete": None,
                    "on_update": None,
                    "deferrable_initially": None,
                    "column": "id"
                }
            }
        ]
        }

        return Table(
            table_name='user',
            schema='public',
            primary_key=['id'],
            columns=cols,
            alter=alter
        )
    elif name == 'group':
        cols = {
            'id': Column(
                name='id',
                type='int',
                size=None,
                references='',
                unique=True,
                nullable=False
            )
        }
        return Table(
            table_name='group',
            schema='public',
            primary_key=['id'],
            columns=cols
        )
    elif name == 'address':
        cols = {
            'id': Column(
                name='id',
                type='int',
                size=None,
                references='',
                unique=True,
                nullable=False
            )
        }
        return Table(
            table_name='address',
            schema='public',
            primary_key=['id'],
            columns=cols
        )


class GraphBuilderTest(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._fixtures = TestFixtures()

        # mock the table repo
        self._mock_repo = MagicMock()


        self._builder = GraphBuilder(table_repo=self._mock_repo)

    def test_read_all_tables(self) -> None:

        self._mock_repo.get_table_names = mocked_repo_get_table_names
        self._mock_repo.get_table = mocked_repo_get_table

        g = self._builder.build(filter=None)
        self.assertEqual(3, len(g.nodes))
        # self.assertTrue('user' in g)

        # print(g)

