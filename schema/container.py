from dependency_injector import containers, providers

from schema.repository.table_repository import TableRepository
from schema.factory.table_factory import TableFactory

from schema.command.info_command import InfoCommand
class Container(containers.DeclarativeContainer):

    table_factory = providers.Factory(
        TableFactory
    )

    table_repository = providers.Singleton(
        TableRepository,
        table_factory = table_factory
    )

    info_command = providers.Factory(
        InfoCommand,
        table_repo=table_repository
    )

    commands_dict = providers.Dict(
        info=info_command
    )