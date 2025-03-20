import struct
import pyodbc
from pyodbc import Connection
from azure import identity

def get_conn():
    connection_string = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:MY_HOSTNAME,1433;Database=SCHOOL_STUDENTS;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30"

    credential = identity.DefaultAzureCredential(exclude_interactive_browser_credential=False)
    token_bytes = credential.get_token("https://database.windows.net/.default").token.encode("UTF-16-LE")
    token_struct = struct.pack(f'<I{len(token_bytes)}s', len(token_bytes), token_bytes)
    
    SQL_COPT_SS_ACCESS_TOKEN = 1256  # This connection option is defined by microsoft in msodbcsql.h
    
    conn = pyodbc.connect(connection_string, attrs_before={SQL_COPT_SS_ACCESS_TOKEN: token_struct})
    return conn

# Function defintion ---------------------------------
def get_age_of_user(connection: Connection, name):

    cursor = connection.cursor()
    cursor.execute("SELECT age FROM Students WHERE name = '" + name + "'")

    row = cursor.fetchone()
    return row.age

# End of function definition ---------------------------------


connection = get_conn()
get_age_of_user(connection, "john")