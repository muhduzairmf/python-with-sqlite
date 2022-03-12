import sqlite3

# If we want to use in memory database
# dbconnection = sqlite3.connect(":memory:")

# If we want to use saved database
dbconnection = sqlite3.connect("customer.db")

# Create cursor
c = dbconnection.cursor()

# Create a Table
# c.execute("""CREATE TABLE customers (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     first_name TEXT,
#     last_name TEXT,
#     email TEXT
# )""")

# Insert a record to the table
# c.execute("""INSERT INTO customers(first_name, last_name, email) VALUES(
#     'John',
#     'Doe',
#     'johndoe@email.com'
# )""")
# c.execute("""INSERT INTO customers(first_name, last_name, email) VALUES(
#     'Sara',
#     'Thompson',
#     'sara@email.com'
# )""")
# c.execute("""INSERT INTO customers(first_name, last_name, email) VALUES(
#     'Mark',
#     'Dane',
#     'markdane@email.com'
# )""")

# Insert many records
# many_customers = [
#     ('Michael', 'Smith', 'michaelsmith@email.com'),
#     ('James', 'Bond', 'jamesbond@email.com'),
#     ('Luis', 'Diaz', 'luisdiaz@email.com'),
# ]
# c.executemany("INSERT INTO customers(first_name, last_name, email) VALUES(?,?,?)", many_customers)

# Query data
# c.execute("SELECT * FROM customers")
# one_customer = c.fetchone()
# three_customers = c.fetchmany(3)
# all_customers = c.fetchall()
# print(one_customer)
# print(three_customers)
# print(all_customers)

# Format query result
# print("Customer details: \n")
# for customer in all_customers:
#     print(f"ID: {customer[0]}")
#     print(f"Firstname: {customer[1]}")
#     print(f"Lastname: {customer[2]}")
#     print(f"Email: {customer[3]} \n")

# Use 'WHERE' clauses
# id_num = 5
# c.execute("SELECT * FROM customers WHERE id = ?", str(id_num))
# execute func cannot receive any params other than string
# print(c.fetchone())

# Update records
# c.execute("""
# UPDATE customers SET last_name = 'McThompson'
# WHERE id = 2
# """)

# Delete records
# c.execute("""
# DELETE from customers
# WHERE id = 6
# """)

# Commit all commands
dbconnection.commit()

# Close database connection
dbconnection.close()
