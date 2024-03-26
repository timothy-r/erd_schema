from unittest import TestCase

from schema.repository.table_repository import TableRepository

class TableRepositoryTest(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._repo = TableRepository()

    def test_get_table(self) -> None:
        sql = """
        CREATE TABLE people
  (
     id       INT UNIQUE NOT NULL,
     EMAIL     NVARCHAR(400),
     PRIMARY KEY(ID),
  );
        """
        self._repo.load_from_string(source=sql)

        result = self._repo.get_table('people')

        self.assertIsInstance(result, dict)

