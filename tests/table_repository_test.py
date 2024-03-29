from unittest import TestCase

from tests.test_fixtures import TestFixtures
from schema.repository.table_repository import TableRepository
from schema.factory.table_factory import TableFactory
from schema.models.table import Table
class TableRepositoryTest(TestCase):

    def setUp(self) -> None:
        super().setUp()
        factory = TableFactory()
        self._repo = TableRepository(table_factory=factory)
        self._fixtures = TestFixtures()

    def test_get_table(self) -> None:
        sql = self._fixtures._get_test_table_sql()

        self._repo.load_from_string(source=sql)

        result = self._repo.get_table('people')

        self.assertIsInstance(result, Table)

    def test_get_table_for_missing_name(self) -> None:
        sql = self._fixtures._get_test_table_sql()

        self._repo.load_from_string(source=sql)

        result = self._repo.get_table('missing')

        self.assertIsNone(result)
