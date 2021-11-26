from pyspark.conf import SparkConf
from pyspark.sql import SparkSession

from . import config


def build_config() -> SparkConf:
    """Builds the pyspark config"""
    conf = SparkConf()
    conf.setAppName(config.spark_app_name())
    conf.setMaster(config.spark_master())
    for key, value in config.spark_additional_config() or []:
        conf.set(key, value)
    return conf


def spark_session() -> SparkSession:
    """Get or creates the Mara Spark session"""
    return SparkSession.builder \
        .config(conf=build_config()) \
        .getOrCreate()
