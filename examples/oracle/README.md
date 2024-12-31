# Oracle Database Container Setup

A quick guide to setting up an Oracle Database using Docker Compose.

## Docker Compose Configuration

Here’s the `docker-compose.yml` file for setting up the Oracle Database container:

```yaml
services:
  oracle:
    image: docker.arvancloud.ir/wvbirder/database-enterprise:12.2.0.1-slim
    container_name: oracle
    hostname: oracle
    ports:
      - "1521:1521"  # Oracle Database port
      - "5000:5000"  # Additional port (optional)
    environment:
      - ORACLE_PWD=localdev  # Password for the Oracle SYS user
      - ORACLE_CHARACTERSET=AL32UTF8  # Character set for the database
    volumes:
      - oracle_data:/opt/oracle/oradata  # Persistent storage for database files
    networks:
      - monitoring_network  # Custom network for the container
    healthcheck:
      test:
        [
          "CMD",
          "sqlplus",
          "-S",
          "sys/localdev@localhost:1521/orclpdb1.localdomain as sysdba",
          "<",
          "/dev/null",
        ]
      interval: 30s  # Check every 30 seconds
      timeout: 10s  # Timeout for the health check
      retries: 3  # Number of retries before marking as unhealthy
    logging:
      driver: "json-file"
      options:
        max-size: "10m"  # Maximum log file size
        max-file: "3"  # Maximum number of log files
    deploy:
      resources:
        limits:
          cpus: "2"  # CPU limit
          memory: 4G  # Memory limit
        reservations:
          memory: 2G  # Memory reservation

volumes:
  oracle_data:  # Persistent volume for Oracle data

networks:
  monitoring_network:  # Custom network for the container
```

## Key Components

### **Image**
- The image used is `docker.arvancloud.ir/wvbirder/database-enterprise:12.2.0.1-slim`.
> This image does not run init scripts.
> In case of actual use, you need to modify this image and customize it.
- Alternatively, you can use the official image from [GitHub](https://github.com/gvenzl/oci-oracle-xe).


### **Ports**
- `1521:1521`: The default port for Oracle Database connections.
- `5000:5000`: An additional port for other services (optional).

### **Environment Variables**
- `ORACLE_PWD`: Sets the password for the Oracle SYS user.
- `ORACLE_CHARACTERSET`: Configures the character set for the database.

### **Volumes**
- `oracle_data`: Persistent storage for Oracle database files, ensuring data is retained even if the container is restarted.

### **Networks**
- `monitoring_network`: A custom network for the container, allowing it to communicate with other services.

### **Health Check**
- The health check uses `sqlplus` to verify the database is running and accessible.
- It runs every 30 seconds, with a timeout of 10 seconds and 3 retries.

### **Logging**
- Logs are stored in JSON format, with a maximum size of 10 MB per file and up to 3 files.

### **Resource Limits**
- The container is limited to 2 CPUs and 4 GB of memory, with a reservation of 2 GB of memory.

## Running the Container

1. **Start the Container:**
   ```bash
   docker-compose up -d
   ```

2. **Check the Logs:**
   ```bash
   docker logs -f oracle
   ```

3. **Connect to the Database:**
   Use a tool like SQL*Plus or SQL Developer to connect to the database using the following details:
   - **Host:** `localhost`
   - **Port:** `1521`
   - **Service Name:** `orclpdb1.localdomain`
   - **Username:** `sys`
   - **Password:** `localdev`

## Stopping the Container

1. **Stop the Container:**
   ```bash
   docker-compose down
   ```

2. **Remove the Volume (Optional):**
   If you want to delete the persistent data, use:
   ```bash
   docker-compose down -v
   ```

---

This compose can be furthurmore enhanced by adding monitoring services such as oracle_exporter, grafana/prometheus.io,etc...
