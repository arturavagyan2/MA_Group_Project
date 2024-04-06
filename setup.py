# Import required functions
from setuptools import setup, find_packages

# Call setup function
setup(
    author = "Group 6",
    description= "SuRFM is a Python package for conducting RFM (Recency, Frequency, Monetary) analysis of customers. It provides tools for segmenting customers based on their transaction behavior and identifying high-value segments.",
    name = "SuRFM",
    version = "0.1.0",
    packages = find_packages(include = ["SuRFM", "SuRFM.*"]),
    install_requires=[
        'annotated-types',
        'anyio',
        'exceptiongroup',
        'Faker',
        'fastapi',
        'greenlet',
        'idna',
        'numpy',
        'pandas',
        'pydantic',
        'pydantic_core',
        'python-dateutil',
        'pytz',
        'six',
        'sniffio',
        'SQLAlchemy',
        'starlette',
        'typing_extensions',
        'tzdata',
    ]
)