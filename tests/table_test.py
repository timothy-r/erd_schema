from unittest import TestCase

from tests.test_fixtures import TestFixtures
from schema.factory.table_factory import TableFactory

from schema.models.table import Table
from schema.models.column import Column
from schema.models.relation import Relation, RelationType
class TableTest(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._factory = TableFactory()
        self._fixtures = TestFixtures()


    def test_table_properties_are_immutable(self) -> None:
        data = self._fixtures.get_test_table_data()

        table:Table = self._factory.create(data=data)

        with self.assertRaises(Exception) as context:
            table.table_name = 'new_table'

        with self.assertRaises(Exception) as context:
            table.schema = 'new_schema'

    def test_table_full_name_with_schema(self) -> None:
        data = self._fixtures.get_test_table_data()
        data["schema"] = 'new_schema'
        full_name = f'{data["schema"]}.{data["table_name"]}'

        table:Table = self._factory.create(data=data)
        self.assertEqual(full_name, table.full_name)

    def test_table_full_name_no_schema(self) -> None:

        data = self._fixtures.get_test_table_data()
        data["schema"] = ''
        full_name = data["table_name"]

        table:Table = self._factory.create(data=data)
        self.assertEqual(full_name, table.full_name)

    def test_get_references(self) -> None:
        data = self._fixtures.get_test_table_data_with_relations()

        table:Table = self._factory.create(data=data)

        expected_relation_count = 1
        expected_from_table = table.full_name
        expected_from_col = 'group_id'
        expected_from_type = RelationType.MANY

        expected_to_table = 'public.group'
        expected_to_col = 'id'
        expected_to_type = RelationType.ONE

        relations:tuple = table.get_relations()

        self.assertTrue(expected_relation_count == len(relations))
        relation:Relation = relations[0]

        self.assertEqual(expected_from_table, relation.from_table)
        self.assertEqual(expected_from_col, relation.from_col)
        self.assertEqual(expected_from_type, relation.from_type)

        self.assertEqual(expected_to_table, relation.to_table)
        self.assertEqual(expected_to_col, relation.to_col)
        self.assertEqual(expected_to_type, relation.to_type)

    def test_has_relation(self) -> None:
        data = self._fixtures.get_test_table_data_with_relations()

        table:Table = self._factory.create(data=data)

        self.assertTrue(table.has_relation('public.group'))
        self.assertFalse(table.has_relation('public.missing'))
        self.assertFalse(table.has_relation('group'))