from setuptools import setup, find_packages
import re


def get_long_description():
    with open('README.md') as f:
        return re.sub('!\[(.*?)\]\(docs/(.*?)\)',
                      r'![\1](https://github.com/mara/mara-spark/raw/master/docs/\2)', f.read())


setup(
    name='mara-spark',
    version='0.1.0',

    description='Lets you use pyspark scripts in mara',

    long_description=get_long_description(),
    long_description_content_type='text/markdown',

    url='https://github.com/mara/mara-spark',

    install_requires=[
        'mara-storage>=1.0.0',
        'mara-db>=4.6.1',
        'mara-page>=1.5.2',
        'mara-pipelines>=3.2.0', # NOTE: expect that 3.3.0 will have the mara_storage 1.0.0 as requirement
        'pyspark==3.1.2' # NOTE: version is fixed here!
    ],

    python_requires='>=3.6',

    packages=find_packages(),

    author='Mara contributors',
    license='MIT',
)