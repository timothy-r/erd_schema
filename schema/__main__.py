import logging

from dependency_injector.wiring import Provide, inject
from simple_ddl_parser import DDLParser

from schema.container import Container

@inject
def main():
    logging.info('main')

    sql = """
CREATE TABLE people
  (
     id       INT,
     birthday DATETIME DEFAULT GETDATE(),
     some_id  INT,
     EMAIL     NVARCHAR(400),
     PRIMARY KEY(ID),
      INDEX EMAIL_IDX  (EMAIL, ASC) VISIBLE
  );

  CREATE UNIQUE INDEX EMAIL_IDX_2 ON people (EMAIL, ASC) VISIBLE;

"""
    parse_results = DDLParser(sql, silent=False).run(json_dump=True)

    print(parse_results)


if __name__ == '__main__':

    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    # TODO: configure the logging
    logging.basicConfig(
        level=logging.DEBUG,
        filename='erd_schema.log',
        filemode='a',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    main()