from Utils import EnvLoader,log
from DatabaseHelpers.Oracle import OracleHelper


# Database Instance manager
# A wrapper around helpers for easier init.
# Instance Handling

@log
class DatabaseManager:
    def __init__(self, env_path=".env"):

        self.env = EnvLoader(env_path)
        self.oracle_instance = None
        self.postgres_instance = None

    def get_oracle_helper(self):

        if not self.oracle_instance: 
            self.oracle_instance = OracleHelper(
                user=self.env.get("ORACLE_USER"),
                password=self.env.get("ORACLE_PASSWORD"),
                host=self.env.get("ORACLE_HOST"),
                port=self.env.get("ORACLE_PORT"),
                service_name=self.env.get("ORACLE_SERVICE"),
                lib_dir=self.env.get("ORACLE_LIB_DIR")
            )
        return self.oracle_instance

