import psycopg2 as ps

con_ = ps.connect(
    dbname="testdb",
    user="testuser",
    password="testdbpass",
    # host="127.0.0.1",
    # port="5432"
    host="db"
)

cr = con_.cursor()

cr.execute('SELECT version();')
print(cr.fetchone())