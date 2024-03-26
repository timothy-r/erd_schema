import logging

from dependency_injector.wiring import Provide, inject

from schema.container import Container

@inject
def main():
    print('main')
    logging.info('main')


if __name__ == '__main__':

    container = Container()

    main()