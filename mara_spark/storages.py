from functools import singledispatch
from mara_storage import storages

from mara_storage import storages


@singledispatch
def spark_storage_config(storage: object) -> [(str, str)]:
    """
    Returns a pyspark config for a mara storage.
    By default we assume no configuration is necessary so the function returns an empty array.
    """
    raise []

@spark_storage_config.register(str)
def __(storage: str):
    return spark_storage_config(storages.storage(storage))



@singledispatch
def spark_storage_path(storage: object, file_name: str) -> str:
    """Returns a pyspark storage path for a path on a mara storage"""
    raise NotImplementedError(f'Please implement storage_path for type "{storage.__class__.__name__}"')

@spark_storage_path.register(str)
def __(storage: str, file_name):
    return spark_storage_path(storages.storage(storage), file_name)

@spark_storage_path.register(storages.LocalStorage)
def __(storage: storages.LocalStorage, file_name: str):
    return str( (storage.base_path / file_name).absolute())

@spark_storage_path.register(storages.AzureStorage)
def __(storage: storages.AzureStorage, file_name: str):
    return f'wasbs://{storage.container_name}@{storage.account_name}.{storage.storage_type}.core.windows.net/{file_name}'