import psycopg
import yaml

from repository import reduce_table_size, update_table


def main():
    # Read config file
    with open("config.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)

            user_confirmation1 = input(
                """
                The execution of this script will alter data (as defined in the config as 'transformations') 
                and delete data (as defined in the config as 'database_subset').
                
                These operations are permanent and should never be ran against a production database.
                
                Please confirm that the database connection set up in the config is NOT a production database (yes/no):
                """
            )

            user_confirmation2 = input(
                """
                Please confirm that you have a backup of the target database, 
                should you need to recover or restart the script (yes/no):
                """
            )

            if user_confirmation1 != "yes" or user_confirmation2 != "yes":
                print(
                    "Confirmation not received. No changes have been made. Exiting script."
                )
                quit()

            # Connect to an existing database
            database_connection = config["database_connection"]
            with psycopg.connect(
                f"dbname={database_connection['database_name']} user={database_connection['user']}"
            ) as conn:

                # Open a cursor to perform database operations
                with conn.cursor() as cur:
                    if config["database_subset"]["subset_tables"]:
                        for subset_table in config["database_subset"]["subset_tables"]:
                            reduce_table_size(
                                conn,
                                cur,
                                subset_table,
                                config["database_subset"]["percentage"],
                            )
                    if config["transformations"]:
                        for transformation in config["transformations"]:
                            update_table(
                                conn,
                                cur,
                                transformation["table"],
                                transformation["columns"],
                            )
                    cur.close()
                conn.close()
        except yaml.YAMLError as exc:
            print(exc)


if __name__ == "__main__":
    main()
