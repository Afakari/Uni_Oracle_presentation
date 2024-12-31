
# Python Oracle Connection Example

This example demonstrates how to connect to an Oracle Database using Python. The project includes a Docker setup for easy deployment and a Python application with helper modules for database management.

## Project Structure

```
.
├── Dockerfile
├── python_app
│   ├── DatabaseHelpers
│   │   ├── DatabaseManager.py
│   │   ├── __init__.py
│   │   └── Oracle.py
│   ├── main.py
│   ├── .env
│   └── Utils
│       ├── EnvLoader.py
│       ├── __init__.py
│       └── Logger.py
├── requirments.txt
└── setup_Instant_client.sh
```

## Docker Setup

The `Dockerfile` sets up a Python environment with the necessary dependencies and Oracle Instant Client.
> It runs on python3.11-bookworm-slim version of the python container.

## Python Application

The Python application is structured into modules for database management and utilities.

### `main.py`

This is the entry point of the application. It initializes the database connection and performs operations.

### `DatabaseHelpers/`

This directory contains helper modules for managing database connections and operations.

- `DatabaseManager.py`: Manages database connections and queries.
- `Oracle.py`: Contains Oracle-specific database operations.

### `Utils/`

This directory contains utility modules for environment loading and logging.

- `EnvLoader.py`: Loads environment variables.
> This env file is used to keep secrets and provide modularity to the script.
- `Logger.py`: Handles logging for the application.

## Running the Project

1. **Build the Docker Image:**
   ```bash
   docker build -t python-oracle .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run python-oracle
   ```

This setup is a very basic client setup. This image can be later integrated with other tools such as matplot,pandas and steamlit for simple analytics, or like a file importer module.
Just a basic setup example.

