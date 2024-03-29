
class TestFixtures:

    def _get_test_table_data(self) -> dict:

        return {
    "table_name": "item",
    "schema": "",
    "primary_key": [
        "ID"
    ],
    "columns": [
        {
            "name": "ID",
            "type": "INT",
            "size": None,
            "references": None,
            "unique": True,
            "nullable": False,
            "default": "",
            "check": ""
        },
        {
            "name": "NAME",
            "type": "NVARCHAR",
            "size": 400,
            "references": "",
            "unique": False,
            "nullable": True,
            "default": "",
            "check": ""
        }
    ],
    "alter": {},
    "checks": [],
    "index": [],
    "partitioned_by": [],
    "constraints": {},
    "tablespace": ""
}