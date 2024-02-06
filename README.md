# PostgreSQL Database Anonymizer

Python utility to transform or mask sensitive customer information in a PostgreSQL database

## Requirements

- Python 3
- Pip
- PostgreSQL

## Config Sections

All configuration lives in the [./config.yaml](./config.yaml) file. Please be mindful of indentation, as yaml is sensitive to whitespace.

### `database_connection`

Configure the database to be transformed.

> WARNING: DO NOT USE THIS ON YOUR LIVE PRODUCTION DATABASE, Make a copy of the production database first and then run this script on the copy

### `transformations`

TODO

### `masks`

TODO

### `database_subset`

TODO

## Running the Utility

Navigate to this directory.

Fill out the config.yaml file with connection information and desired transformations/masks.

Install dependencies with

### `pip install -r requirements.txt`

Run the utility with

### `python3 main.py`
