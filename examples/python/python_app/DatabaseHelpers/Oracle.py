import cx_Oracle
from Utils import log


# Oracle Helper.
# cx_Oralce needs an instant client or something alike to work
# for simple CI config look at the ORACLE_FDW Doc.
@log
class OracleHelper:
    def __init__(self, user, password, host, port, service_name, lib_dir):
        self.logger.info("Initializing OracleHelper...")
        try:
            cx_Oracle.init_oracle_client(lib_dir=lib_dir)
        except Exception as e:
            self.logger.error("Failed to initialize Oracle client library")
            raise e

        self.dsn = cx_Oracle.makedsn(host, port, service_name=service_name)
        self.connection = None

        self.connect(user, password)

    def connect(self, user, password):

        try:
            self.connection = cx_Oracle.connect(user, password, self.dsn)
            self.logger.info("Oracle database connection established.")
        except Exception as e:
            self.logger.error("Failed to connect to Oracle database.")
            raise e

    def execute_query(self, query):

        try:
            with self.connection.cursor() as cursor:
                self.logger.info(f"Executing query.")
                cursor.execute(query,)
                results = cursor.fetchall()
                self.logger.info(f"Query executed successfully. Rows fetched: {len(results)}")
                return results
        except Exception as e:
            self.logger.error(f"Error executing query: {e}")
            raise

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.logger.info("Oracle database connection closed.")
