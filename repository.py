import psycopg
from psycopg import sql
from transformer import transform_data


def fetch_all_records_id(cur, table):
    # Query the database and obtain data as Python objects.
    return cur.execute(f"SELECT id FROM {table}")


# Update all columns in a table with obfuscated/masked values
def update_table(conn, cur, table, columns):
    print(
        f"Transforming and updating the following columns in all records of table {table}: {', '.join(column['name'] for column in columns)}"
    )

    updated_values = []

    # For each record, build a list of values to update
    records = fetch_all_records_id(cur, table)
    for record in records:
        set_values = {}
        for column in columns:
            # Assign transformed data value
            set_values[column["name"]] = transform_data(column["transform_key"])

        updated_values.append((record[0], set_values))

    # Indexes within updated_values
    idIndex = 0
    columnsIndex = 1

    # Generate the UPDATE query dynamically
    update_query = sql.SQL("UPDATE {} SET {} WHERE id = %s").format(
        sql.Identifier(table),
        sql.SQL(", ").join(
            [
                sql.Identifier(column) + sql.SQL(" = %s")
                for column in updated_values[0][columnsIndex].keys()
            ]
        ),
    )
    print(f"\nQuery: {update_query.as_string(conn)}")

    # Prepare a list of tuples with the updated values and the id
    data = [
        tuple(
            row[columnsIndex][column]
            for column in updated_values[0][columnsIndex].keys()
        )
        + (row[idIndex],)
        for row in updated_values
    ]

    print(f"\nFormat data: {data}")

    # Execute the UPDATE query for each row
    try:
        cur.executemany(update_query, data)
        conn.commit()
    except psycopg.Error as err:
        print("An error has occured:")
        print(err)
