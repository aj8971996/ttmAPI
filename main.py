import uvicorn
from api.endpoints import app
from sqlalchemy import inspect, MetaData, Table
from database.database import create_tables, engine
from sqlalchemy.exc import OperationalError

def modify_table_structure(inspector, metadata):
    """
    Modifies existing tables if the schema has changed by adding missing columns and keeping existing data.
    """
    try:
        # Reflect the existing database schema
        metadata.reflect(bind=engine)

        # Loop through each table in the metadata
        for table in metadata.tables.values():
            existing_columns = {col['name'] for col in inspector.get_columns(table.name)}
            model_columns = {col.name for col in table.columns}

            # Add missing columns to the existing table
            missing_columns = model_columns - existing_columns

            if missing_columns:
                print(f"Modifying table '{table.name}' to add missing columns: {missing_columns}")
                with engine.connect() as connection:
                    for col_name in missing_columns:
                        col_type = table.columns[col_name].type
                        alter_stmt = f'ALTER TABLE {table.name} ADD COLUMN {col_name} {col_type}'
                        connection.execute(alter_stmt)
                        print(f"Added column '{col_name}' to table '{table.name}'.")

    except Exception as e:
        print(f"Error while modifying table structures: {e}")
        raise e

def check_tables_and_modify_structure():
    try:
        # Check if tables exist
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        
        metadata = MetaData()

        if tables:
            # Modify tables to match the current schema
            modify_table_structure(inspector, metadata)
        else:
            # Create tables if they do not exist
            create_tables()

        # Tables exist or have been created/modified
        print("Tables exist, have been created, or modified. API is running.")

    except OperationalError as e:
        print(f"Operational error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_tables_and_modify_structure()
    uvicorn.run(app, host="0.0.0.0", port=8000)