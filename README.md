# Mara Spark

A integration for [Apache Spark](https://spark.apache.org/) for the Mara ETL framework.

* Using mara configuration for `pyspark` scripts.

&nbsp;

## Example execution with RunFunction

*Note:* The output of pyspark will be written to the console but not logged to mara in this mode.

&nbsp;
**spark_via_python_function_pipeline.py**
``` py
from mara_pipelines.commands.python import RunFunction
from mara_pipelines.pipelines import Pipeline, Task

def my_pyspark_function(storage_alias: str, read_filename: str, write_filename) -> bool:
    from pyspark.sql.functions import col, lit, sum

    import mara_spark.session
    from mara_spark.storages import spark_storage_path

    spark = mara_spark.session.spark_session()

    df = spark.read.option("header", True) \
        .csv(path=spark_storage_path(storage_alias, file_name=read_filename))

    # do your transformations

    df.write \
        .option("header", True) \
        .csv(path=spark_storage_path(storage_alias, file_name=write_filename), mode='overwrite')

    spark.stop()

    return True


pipeline = Pipeline(
    id="run_spark_via_function",
    description="Sample pipeline executing a python function with pyspark")

pipeline.add(
    Task(id='run_function',
         description="Executes the python function",
         commands=[
             RunFunction(
                 function=my_pyspark_function,
                 args=[
                     # storage alias
                     'data',
                     # read file name
                     "my_input_file.csv",
                     # write file name
                     "my_output_file.csv"
             ])
         ]))
```


## Example execution with ExecutePython

*Note:* The output of pyspark will be written into the mara log from stderr.

&nbsp;
**my_pyspark_script.py**

``` py
from pyspark.sql.functions import col, lit, sum
import sys

from mara_spark.storages import spark_storage_path
import mara_spark.session

# makes sure that the app configuration is loaded
import app.local_setup


if len(sys.argv) < 3 + 1:
    raise Exception(f'You need 3 parameters for this script, {len(sys.argv)} where passed')

storage_alias = sys.argv[1]
read_filename = sys.argv[2]
write_filename = sys.argv[3]

# here your main pyspark code starts

spark = mara_spark.session.spark_session()

df = spark.read.option("header", True) \
    .csv(path=spark_storage_path(storage_alias, file_name=read_filename))

# do your transformations

df.write \
    .option("header", True) \
    .csv(path=spark_storage_path(storage_alias, file_name=write_filename), mode='overwrite')

spark.stop()
```

&nbsp;
**spark_via_python_script_pipeline.py**

``` py
import pathlib

from mara_pipelines.commands.python import ExecutePython
from mara_pipelines.pipelines import Pipeline, Task

pipeline = Pipeline(
    id="run_spark_via_python_script",
    description="Sample pipeline executing a python script with pyspark",
    base_path=pathlib.Path(__file__).parent)

pipeline.add(
    Task(id='exec_python_script',
         description="Executes the python script",
         commands=[
             ExecutePython(
                 file_name='my_pyspark_script.py',
                 args=[
                     # storage alias
                     'data',
                     # read file name
                     "my_input_file.csv",
                     # write file name
                     "my_output_file.csv"
                 ])
         ]))
```
