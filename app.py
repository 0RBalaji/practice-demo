import os
import psycopg2 as ps

DB_HOST = os.environ.get("DB_HOST", "localhost")       # default to service name
DB_PORT = int(os.environ.get("DB_PORT", 5432))
DB_NAME = os.environ.get("DB_NAME", "testdb")
DB_USER = os.environ.get("DB_USER", "testuser")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "testpass")

con_ = ps.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cr = con_.cursor()

cr.execute('SELECT version();')
print(cr.fetchone())