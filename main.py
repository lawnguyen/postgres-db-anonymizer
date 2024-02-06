import psycopg
import yaml

from repository import update_table


def main():
    # Read config file
    with open("config.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)

            # Connect to an existing database
            database_connection = config["database_connection"]
            with psycopg.connect(
                f"dbname={database_connection['database_name']} user={database_connection['user']}"
            ) as conn:

                # Open a cursor to perform database operations
                with conn.cursor() as cur:
                    for transformation in config["transformations"]:
                        update_table(
                            conn,
                            cur,
                            transformation["table"],
                            transformation["columns"],
                            "transform",
                        )
                    for mask in config["masks"]:
                        update_table(conn, cur, mask["table"], mask["columns"], "mask")
                conn.close()
        except yaml.YAMLError as exc:
            print(exc)


if __name__ == "__main__":
    main()
