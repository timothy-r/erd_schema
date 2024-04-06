import logging
import sys

from dependency_injector.wiring import Provide, inject

from schema.command.command import Command
from schema.repository.table_repository import TableRepository

from schema.container import Container

@inject
def main(
    command:Command,
    args:list,
    table_repo:TableRepository = Provide[Container.table_repository],
    graph_builder = Provide[Container.graph_builder]
    ):

    source = args[0]

    logging.info(f'main executing: {command} with: {source}')

    """
        1: read source into the table repo
        2: construct the data model, using the filter (optional)
        3: execute command on the data model
    """
    logging.info(f'Reading {source}')

    with open(source, 'r', encoding='utf-8') as fh:
        contents = fh.read()
        table_repo.load_from_string(source=contents)

        filter = None
        graph = graph_builder.build(filter=filter)

        command.execute()

if __name__ == '__main__':

    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    # TODO: configure the logging
    logging.basicConfig(
        level=logging.DEBUG,
        # filename='erd_schema.log',
        # filemode='w',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    if len(sys.argv) > 1:
        command_name = sys.argv[1]
    else:
        exit('No command specified')

    commands_dict = container.commands_dict()

    if command_name in commands_dict:
        command = commands_dict[command_name]
    else:
        exit(f'Command name not recognised {command_name}')

    args = sys.argv[2:]

    if len(args) == 0:
        exit('Too few args')

    main(
        command=command,
        # table_repo=container.table_repository(),
        args=args
    )