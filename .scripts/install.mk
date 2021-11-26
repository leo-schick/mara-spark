# set variables unless already set earlier
spark-version ?= 3.1.2
spark-hadoop-version ?= 2.7

# the directory of this Makefile
mara-spark-scripts-dir := $(dir $(lastword $(MAKEFILE_LIST)))

# where mara-spark is installed relative to the project root
mara-spark-dir ?= packages/mara-spark

setup-spark: .copy-mara-spark-scripts

install-spark:
# sudo apt install default-jdk scala -y
	wget -nv https://downloads.apache.org/spark/spark-$(spark-version)/spark-$(spark-version)-bin-hadoop$(spark-hadoop-version).tgz
	tar xf spark-$(spark-version)-bin-hadoop$(spark-hadoop-version).tgz
	rm -f spark-$(spark-version)-bin-hadoop$(spark-hadoop-version).tgz

	rm -rf .spark
	mv spark-$(spark-version)-bin-hadoop$(spark-hadoop-version) .spark

	echo export SPARK_HOME=$$(pwd)/.spark >> .venv/bin/activate
	echo export PYSPARK_PYTHON=$$(pwd)/.venv/bin/python3 >> .venv/bin/activate


.install-spark-jdbc-mssql:
	wget -nv https://github.com/microsoft/mssql-jdbc/releases/download/v9.4.0/mssql-jdbc-9.4.0.jre11.jar
	mkdir -p .spark/jars/
	mv mssql-jdbc-9.4.0.jre11.jar .spark/jars/


# copy scripts from mara-spark package to project code
.copy-mara-spark-scripts:
	rsync --archive --recursive --itemize-changes  --delete $(mara-spark-dir)/.scripts/ $(mara-spark-scripts-dir)


.cleanup-spark:
	rm -rf .spark/
