import logging
import sys

# from dependency_injector.wiring import Provide, inject

from schema.command.command import Command

from schema.container import Container

# @inject
def main(command:Command, args:list):
    logging.info(f'main executing: {command} with: {args[0]}')

    command.execute(source=args[0])

if __name__ == '__main__':

    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    # TODO: configure the logging
    logging.basicConfig(
        level=logging.DEBUG,
        filename='erd_schema.log',
        filemode='w',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    if len(sys.argv) > 1:
        command_name = sys.argv[1]
    else:
        command_name = 'info'

    # TODO: put this into a dict in the container
    if command_name == 'info':
        command = container.info_command()
    else:
        exit(f'Command name not recognised {command_name}')

    args = sys.argv[2:]
    if len(args) == 0:
        exit('Too few args')

    main(command=command, args=args)