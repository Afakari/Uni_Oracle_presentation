
# SQL*Plus Basics: Connecting and Using Oracle Database

SQL*Plus is a command-line tool for interacting with Oracle Database. Below are some basic commands, connection string syntax, and usage examples.

---

## **1. Connecting to Oracle Database**

### **Connection String Syntax**
To connect to an Oracle Database using SQL*Plus, use the following syntax:

```bash
sqlplus username/password@[//]host[:port][/service_name]
```

- **username:** Your database username (e.g., `sys`, `system`, or a custom user).
- **password:** Your database password.
- **host:** The hostname or IP address of the database server.
- **port:** The port number (default is `1521`).
- **service_name:** The service name of the database (e.g., `orclpdb1.localdomain`).

### **Examples**
1. Connect as `sys` (sysdba):
   ```bash
   sqlplus sys/localdev@localhost:1521/orclpdb1.localdomain as sysdba
   ```

2. Connect as `system`:
   ```bash
   sqlplus system/localdev@localhost:1521/orclpdb1.localdomain
   ```

3. Connect as a regular user:
   ```bash
   sqlplus myuser/mypassword@localhost:1521/orclpdb1.localdomain
   ```

---

## **2. Basic SQL*Plus Commands**

### **Executing SQL Queries**
1. **Select Query:**
   ```sql
   SELECT * FROM TEST;
   ```

2. **Insert Query:**
   ```sql
   INSERT INTO TEST (id, name) VALUES (1, 'John Doe');
   ```

3. **Update Query:**
   ```sql
   UPDATE TEST SET name = 'Jane Doe' WHERE id = 1;
   ```

4. **Delete Query:**
   ```sql
   DELETE FROM TEST WHERE id = 1;
   ```

### **Database Administration**
1. **Show Current User:**
   ```sql
   SHOW USER;
   ```

2. **Describe a Table:**
   ```sql
   DESC employeeTEST;
   ```

3. **List Tables:**
   ```sql
   SELECT table_name FROM user_tables;
   ```

4. **Run a SQL Script:**
   ```sql
   @/path/to/script.sql
   ```

### **Formatting Output**
1. **Set Page Size:**
   ```sql
   SET PAGESIZE 50;
   ```

2. **Set Line Size:**
   ```sql
   SET LINESIZE 100;
   ```

3. **Enable Column Headings:**
   ```sql
   SET HEADING ON;
   ```

4. **Disable Column Headings:**
   ```sql
   SET HEADING OFF;
   ```

### **Exiting SQL*Plus**
1. **Exit SQL*Plus:**
   ```sql
   EXIT;
   ```

2. **Disconnect but Stay in SQL*Plus:**
   ```sql
   DISCONNECT;
   ```


## **3. Using SQL*Plus in Scripts**

### **Run a SQL Script**
To execute a SQL script from the command line:
```bash
sqlplus username/password@host:port/service_name @/path/to/script.sql
```

### **Example Script (`script.sql`):**
```sql
-- script.sql
SELECT * FROM TEST;
EXIT;
```

Run the script:
```bash
sqlplus myuser/mypassword@localhost:1521/orclpdb1.localdomain @script.sql
```


## **4. Common Connection Issues**

### **1. TNS: Could Not Resolve the Connect Identifier**
- Ensure the `service_name` is correct.
- Check if the database is running and accessible.

### **2. ORA-01017: Invalid Username/Password**
- Double-check the username and password.
- Ensure the user has the necessary privileges.

### **3. ORA-12541: TNS: No Listener**
- Ensure the Oracle listener is running on the specified port.
- Verify the `host` and `port` in the connection string.


