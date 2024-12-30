# Setting Up the Container: A Practical Guide

Oracle Database 12c introduced the **Multitenant Architecture**, a game-changer for managing multiple databases efficiently. With this architecture, you can create a **Container Database (CDB)** that houses multiple **Pluggable Databases (PDBs)**. Each PDB acts as a self-contained database but shares the same Oracle instance and background processes as the CDB.

## **What Are Pluggable Databases (PDBs)?**

PDBs are like **independent databases** within a single container. They have their own:

- **Data:** Tables, indexes, and other objects.
- **Schemas:** Logical structures for organizing data.
- **Users:** Access controls and permissions.

However, they share the **same Oracle instance** and **background processes**, making them lightweight and efficient.

## **Benefits of Multitenant Architecture**

1. **Resource Efficiency:**  
   By sharing the same instance and processes, PDBs reduce overhead and save resources.
2. **Simplified Management:**  
   You can manage multiple PDBs as a single entity, making tasks like backups, patching, and upgrades easier.
3. **Isolation:**  
   Changes in one PDB don’t affect others, ensuring security and stability.

## **How to Create a PDB**

Creating a PDB is straightforward. Use the `CREATE PLUGGABLE DATABASE` statement in SQL\*Plus or any Oracle SQL tool. Here’s an example:

```sql
CREATE PLUGGABLE DATABASE pdb_name
ADMIN USER pdb_admin IDENTIFIED BY password
FILE_NAME_CONVERT = ('/path/to/source/', '/path/to/destination/');
```

### **What This Does:**

- **`pdb_name`:** The name of your new PDB.
- **`pdb_admin`:** The admin user for the PDB.
- **`password`:** The password for the admin user.
- **`FILE_NAME_CONVERT`:** Maps source file paths to destination paths for the PDB’s data files.

## **Why Use This Approach?**

- **Saves Time:** Automates repetitive tasks and reduces manual errors.
- **Consistency:** Ensures all PDBs are set up the same way.
- **Scalability:** Makes it easy to add more PDBs as your needs grow.

## **Real-World Use Case**

Imagine you’re managing databases for multiple departments (HR, Finance, Sales) in a company. Instead of running separate instances for each, you can:

1. Create a **CDB** as the main container.
2. Add a **PDB** for each department (e.g., `HR_PDB`, `Finance_PDB`, `Sales_PDB`).
3. Manage them all centrally while keeping their data isolated.

## **Next Steps**

1. Check out the scripts in `../example/oracle`.
2. Customize them for your environment.
