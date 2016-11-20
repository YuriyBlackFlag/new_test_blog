import cx_Oracle
# create a new database if the database doesn't already exist
with cx_Oracle.connect("pyth/123123@127.0.0.1/test") as connection:
# get a cursor object used to execute SQL commands
    c = connection.cursor()
# create the table
# insert dummy data into the table
    c.execute("""INSERT INTO posts(title, post) VALUES('Excellent', 'I\"m excellent.')""")
    c.execute("""INSERT INTO posts VALUES('Okay','I\"m okay.')""")
