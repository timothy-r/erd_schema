import logging
import json
import sys

from dependency_injector.wiring import Provide, inject
from simple_ddl_parser import DDLParser

from schema.command.command import Command

from schema.container import Container

# @inject
def main(command:Command, args:list):
    logging.info(f'main {command} {args}')

    command.execute(source=args[0])

#     sql = """
# CREATE TABLE people
#   (
#      id       INT,
#      birthday DATETIME DEFAULT GETDATE(),
#      some_id  INT,
#      EMAIL     NVARCHAR(400),
#      PRIMARY KEY(ID),
#     # INDEX  EMAIL_IDX(EMAIL) VISIBLE
#   );

#   -- CREATE UNIQUE INDEX EMAIL_IDX_2 ON people (EMAIL, ASC) VISIBLE;

# """
#     parse_results = DDLParser(sql, silent=False).run(json_dump=True, group_by_type=True)

#     parsed = json.loads(parse_results)
#     print(json.dumps(parsed, indent=4))


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
    if len(sys.argv) > 1:
        command_name = sys.argv[1]
    else:
        command_name = 'info'

    if command_name == 'info':
        command = container.info_command()
    else:
        exit()

    main(command, sys.argv[2:])