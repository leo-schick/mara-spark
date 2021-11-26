from mara_pipelines.commands.python import RunFunction
from mara_pipelines.pipelines import Command


def _HadoopMovePartFile(local_path, file_extension: str):
    """
    Internal function moving the single part file from a hadoop path
    to the local path

    Args:
        local_path: the local path where to export
        file_extension: the file extension which to search for
    """
    import pathlib
    import glob
    import shutil
    import sys

    path = pathlib.Path(local_path)

    if not (path / '_SUCCESS').exists():
        # When the _SUCCESS file does not exist the file creation failed
        print(f'Error: _SUCCESS file does not exist in path {str(path.absolute())}', stdout=sys.stderr)
        return False

    files = glob.glob(str(path / f'part-*.{file_extension}'))

    if not files:
        print(f'Error: Could not find any file in folder matching *.{file_extension}', stdout=sys.stderr)
        return False

    if len(files) > 1:
        print(f'Found muliple files in folder matching *.{file_extension}. This function does not support merging serveral files.', stdout=sys.stderr)
        return False

    shutil.move(files[0], str(path.absolute()) + '.tmp')
    shutil.rmtree(str(path.absolute()))
    shutil.move(str(path.absolute()) + '.tmp', str(path.absolute()))

    return True


def HadoopMovePartFile(storage_alias: str, path: str, file_extension: str) -> Command:
    """
    Returns a command which moves the part file into the local path.

    This only works when there is only one part file. Otherwise you will
    have to merge the files e.g. by calling `hdfs dfs -getmerge <hdfsDir> <localFile>`

    Args:
        storage_alias: the storage alias for the local storage
        path: the path to the hadoop folder where spark or  map reduce placed its output
        file_extension: the file extension of the path files to seach for

    Returns>
        A mara command
    """
    from mara_storage import storages
    storage = storages.storage(storage_alias)
    if not isinstance(storage, storages.LocalStorage):
        raise ValueError('Command HadoopMovePartFile only supports storages of type LocalStorage')

    local_path = storage.base_path / path

    return RunFunction(function=_HadoopMovePartFile, args=[local_path, file_extension])
