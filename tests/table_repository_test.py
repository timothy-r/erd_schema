from unittest import TestCase

from schema.repository.table_repository import TableRepository
from schema.factory.table_factory import TableFactory
from schema.models.table import Table
class TableRepositoryTest(TestCase):

    def setUp(self) -> None:
        super().setUp()
        factory = TableFactory()
        self._repo = TableRepository(table_factory=factory)

    def test_get_table(self) -> None:
        sql = self._get_test_sql()

        self._repo.load_from_string(source=sql)

        result = self._repo.get_table('people')

        self.assertIsInstance(result, Table)

    def test_get_table_for_missing_name(self) -> None:
        sql = self._get_test_sql()

        self._repo.load_from_string(source=sql)

        result = self._repo.get_table('missing')

        self.assertIsNone(result)

    def _get_test_sql(self) -> str:

        return """
        CREATE TABLE people
  (
     id       INT UNIQUE NOT NULL,
     EMAIL     NVARCHAR(400),
     PRIMARY KEY(ID),
     FAMILY_ID INT
  )
    CREATE TABLE car
  (
     id       INT PRIMARY KEY,
     NAME     NVARCHAR(400),
     OWNER_ID INT,
     CONSTRAINT fk_category FOREIGN KEY (OWNER_ID)
                         REFERENCES people(ID)
  )

      CREATE TABLE FAMILY
  (
     id       INT PRIMARY KEY,
     NAME     NVARCHAR(400)
  )

    ALTER TABLE people ADD FOREIGN KEY (FAMILY_ID) REFERENCES FAMILY(ID)
  ;
        """
