
def spark_app_name():
    """The name displayed in the mara app"""
    return 'Mara Spark'


def spark_master():
    """The spark master url"""
    import socket
    return f'spark://{socket.getfqdn()}:7077'


def spark_additional_config() -> [(str, str)]:
    """
    Additional config settings for spark.

    E.g. when connecting with JDBC to SQL Server you need to set it to
        ['spark.driver.extraClassPath', pathlib.Path.cwd() / '.spark/jars/mssql-jdbc-9.4.0.jre11.jar')]
    """
    return []
