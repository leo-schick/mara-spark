
def spark_app_name():
    """
    The name displayed in the mara app.
    
    It is possible to extend the name when building the spark session.
    If used, this here is the prefix to the mara app name
    """
    return 'Mara'


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
