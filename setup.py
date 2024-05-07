# -*- coding: utf-8 -*-
# Import required functions
from setuptools import setup, find_packages

# Read the README file for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# List of required packages
required_packages = [
    'annotated-types', 'anyio', 'exceptiongroup', 'Faker', 'fastapi',
    'greenlet', 'idna', 'numpy', 'pandas', 'pydantic', 'pydantic_core',
    'python-dateutil', 'pytz', 'six', 'sniffio', 'SQLAlchemy', 'starlette',
    'typing_extensions', 'tzdata', 'appnope', 'asttokens', 'certifi',
    'charset-normalizer', 'click', 'comm', 'debugpy', 'decorator', 'executing',
    'h11', 'httptools', 'importlib_metadata', 'ipykernel', 'ipython',
    'jedi', 'jupyter_client', 'jupyter_core', 'matplotlib-inline',
    'nest-asyncio', 'packaging', 'parso', 'pexpect', 'platformdirs',
    'prompt-toolkit', 'psutil', 'ptyprocess', 'pure-eval', 'Pygments',
    'python-dotenv', 'PyYAML', 'pyzmq', 'requests', 'stack-data', 'tornado',
    'traitlets', 'urllib3', 'uvicorn', 'uvloop', 'watchfiles', 'wcwidth',
    'websockets', 'zipp'
]

# Call setup function
setup(
    author="Artur Avagyan, Elen Galoyan, Hrag Sousani, Ina Karapetyan, Khoren Movsisyan",  # noqa: E501
    description="SuRFM is a Python package for conducting RFM (Recency, Frequency, Monetary) analysis of customers. It provides tools for segmenting customers based on their transaction behavior and identifying high-value segments.",  # noqa: E501
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="SuRFM",
    version="0.1.2",
    packages=find_packages(include=["SuRFM", "SuRFM.*"]),
    install_requires=required_packages
)
