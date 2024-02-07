import psycopg
from psycopg import sql
from masker import mask_data
from transformer import transform_data


def fetch_all_records_id(cur, table):
    # Query the database and obtain data as Python objects.
    return cur.execute(f"SELECT id FROM {table}")


def fetch_current_value(conn, table, recordId, columnName):
    select_column_query = sql.SQL("SELECT {} FROM {} WHERE id = %s").format(
        sql.Identifier(columnName),
        sql.Identifier(table),
    )
    with conn.cursor() as cur:
        cur.execute(select_column_query, (recordId,))
        current_value = cur.fetchone()[0]
        cur.close()
        return current_value


"""
Update all columns in a table with transformed/masked values

@param conn - psycopg connection
@param cur = psycopg cursor
@param table = name of table to update
@param columns - list of columns to update and the mode key
@param mode ["transform" | "mask"] - mode of operation to apply to record
"""


def update_table(conn, cur, table, columns):
    print(
        f"Transforming/masking and updating the following columns in all records of table {table}: {', '.join(column['name'] for column in columns)}"
    )

    updated_values = []

    # For each record, build a list of values to update
    records = fetch_all_records_id(cur, table)
    for record in records:
        set_values = {}
        for column in columns:
            mode = column["mode"]
            current_value = fetch_current_value(conn, table, record[0], column["name"])
            # Assign transformed or masked data value
            if mode == "transform":
                set_values[column["name"]] = transform_data(
                    column["mode_key"], current_value
                )
            elif mode == "mask":
                set_values[column["name"]] = mask_data(
                    column["mode_key"], current_value
                )
            else:
                print(f"Error: Unsupported transformation mode: {mode}")
                print("Supported modes are 'transform' | 'mode'")
                return

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
    print(f"Query: {update_query.as_string(conn)}")

    # Prepare a list of tuples with the updated values and the id
    data = [
        tuple(
            row[columnsIndex][column]
            for column in updated_values[0][columnsIndex].keys()
        )
        + (row[idIndex],)
        for row in updated_values
    ]

    # print(f"\nFormat data: {data}")

    # Execute the UPDATE query for each row
    try:
        cur.executemany(update_query, data)
        conn.commit()
        print("Success\n")
    except psycopg.Error as err:
        print("An error has occured:")
        print(err)
