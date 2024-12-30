import os
from dotenv import load_dotenv


# Wrapper Around load_dot_env
class EnvLoader:
    def __init__(self, env_path=".env"):
        if not os.path.exists(env_path):
            raise FileNotFoundError(f"{env_path} file not found.")
        load_dotenv(env_path)  

    def get(self, key, default=None):
        return os.getenv(key, default)
