from Utils import log
from DatabaseHelpers import DatabaseManager


# Inputs
table_name=''
schema=''

# Database factory
DbFactory = DatabaseManager()
oracle_helper = DbFactory.get_oracle_helper()

# Query to retrieve oracle tables and columns in Postgres format
query=f"""
SELECT
'Hello world' from dual;
"""
oracle_schema_data = oracle_helper.execute_query(query)

print(f'Result: {oracle_schema_data}')
print('-----------------------------------------\n')
