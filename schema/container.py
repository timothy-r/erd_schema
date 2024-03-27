from dependency_injector import containers, providers

from schema.repository.table_repository import TableRepository
from schema.command.info_command import InfoCommand
class Container(containers.DeclarativeContainer):

    table_repository = providers.Singleton(
        TableRepository
    )

    info_command = providers.Factory(
        InfoCommand,
        table_repo=table_repository
    )