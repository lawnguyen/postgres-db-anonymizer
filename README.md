# PostgreSQL Database Anonymizer

Python utility to transform or mask sensitive customer information in a PostgreSQL database for development or testing purposes

## Requirements

- Python 3
- Pip
- PostgreSQL

## Running the Utility

Navigate to this directory.

Fill out the config.yaml file with connection information and desired transformations/masks.

Install dependencies with

### `pip install -r requirements.txt`

Run the utility with

### `python3 main.py`

## Config Sections

All configuration lives in the [./config.yaml](./config.yaml) file. Please be mindful of indentation, as yaml is sensitive to whitespace.

### `database_connection`

Configure the database to be transformed.

> WARNING: DO NOT USE THIS ON YOUR LIVE PRODUCTION DATABASE, these changes are permanent and can't be undone. Make a copy of the production database first and then run this script on the copy.

### `transformations`

Define all of the transformations you want here.

Format:

```yaml
- table: { TABLE_NAME }
  columns:
    - name: { COLUMN_NAME }
      mode: { transform | mask }
      mode_key: { MODE_KEY }
```

Example:

```yaml
- table: customer_log
  columns:
    - name: march_code
      mode: transform
      mode_key: random
    - name: email
      mode: mask
      mode_key: email
    - name: token
      mode: mask
      mode_key: token
```

| Transform Mode Key | Description                                              | Example                                                    |
| ------------------ | -------------------------------------------------------- | ---------------------------------------------------------- |
| email              | Generate an email address (string only).                 | `john.doe@company.com` -> `ng9XNUBJ@gmail.com`             |
| first-name         | Generate a first name (string only).                     | `Lucas` -> `Alice`                                         |
| full-name          | Generate a full name (string only).                      | `Lucas` -> `Alice Smith`                                   |
| phone-number       | Generate a phone number (string only).                   | `1234567890` -> `+91 (123) 456-7890`                       |
| random             | Randomize value but keep the same length (string only).  | `AAA` -> `B7F`                                             |
| random-free        | Generate a random value of random length (string only).  | `AAA` -> `B7F894GHF`                                       |
| number             | Generate a random number between 1 and 1000 (inclusive). | `42` -> `777`                                              |
| address            | Generate a random address (string only).                 | `80 Cross Street, Chennai, Andhra Pradesh - 731318, India` |
| address2           | Generate a random address2 part (string only).           | `2orat86c7Twwp`                                            |
| token              | Generate a random UUID token (string only).              | `4e782055-4f06-45ab-9eeb-cb86fbc82b9d`                     |

| Mask Mode Key | Description                                                                                                      | Example                                                                          |
| ------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| email         | Mask email address by replacing a random number of characters in both the local and domain parts with asterisks. | `john.doe@company.com` -> `j****.d**@c*****y.com`                                |
| first-name    | Mask a first name by replacing all characters except the first one with asterisks.                               | `Lucas` -> `L****`                                                               |
| full-name     | Mask all characters in both the first and last name except for the first character.                              | `Lucas Smith` -> `L**** S****`                                                   |
| phone-number  | Mask all but the last four digits in a phone number.                                                             | `+91 (123) 456-7890` -> `******7890`                                             |
| token         | Mask a token by replacing a random subset of characters in each segment with asterisks.                          | `4e782055-4f06-45ab-9eeb-cb86fbc82b9d` -> `4e782*55-4*06-****-**eb-cb*6*bc**b9*` |
| random        | Mask 50% of the characters in a string with asterisks.                                                           | `foo bar` -> `f*o *a*`                                                           |

### `database_subset`

Reduce the size of your database by taking a subset of larger tables.

Configure the tables you want reduced under `subset_tables` and the `percentage` remaining.

If you don't want to reduce any tables, make sure `subset_tables` is empty, i.e., `subset_tables:`.

For example,

```yaml
percentage: 10
```

and

```yaml
subset_tables:
  - logs
```

will reduce the table named `logs` to 10% of its original size.

The rows deleted are random based on `TABLESAMPLE BERNOULLI`.

> WARNING: Use at your own risk, these changes involve permanently deleting data and can't be undone. Ensure that the tables configured are not referenced as foreign keys in other tables, as relationships are not supported.

Format:

```yaml
database_subset:
  percentage: { SAMPLE_PERCENTAGE }
  subset_tables:
    - { LARGE_TABLE_NAME }
    - { ANOTHER_LARGE_TABLE_NAME }
    - { AND_ANOTHER_LARGE_TABLE_NAME }
```

## Troubleshooting Tips

- Ensure that you have a backup of the database before you run this script
- Ensure that the database connection information is accurate and that the user defined has appropriate permisssions to read, write, create tables, and drop tables in the database
- Ensure that table and column names are spelled correctly in the `config.yaml`
- Ensure that indentation and whitespace is valid in the `config.yaml`
- If there are issues with the transformations because of unique value constraints causing collisions then it should be enough to re-run the script as transformations are generated randomly.

  - (Suggested) The safest option is to re-run the script on a fresh copy instead of re-running it on the same database multiple times because this increase your chances of more collisions

  Example:

  ```bash
  create database new_test_database
  ```

  ```
  psql -U root -d new_test_database < database-copy.sql
  ```

- If any of the tables are really large, you can run a one-off query like so–
  ```
  DELETE FROM order_log
  WHERE id NOT IN (
      SELECT id
      FROM order_log
      ORDER BY created_at DESC
      LIMIT 10000
  );
  ```
