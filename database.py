import psycopg2
from psycopg2.extras import Json

def get_db_connection():
    conn = psycopg2.connect(
        dbname="rule_engine_db",
        user="username",  # Replace with your database username
        password="password",  # Replace with your database password
        host="localhost" )
    return conn

def save_rule(rule_ast, description):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO rules (rule_ast, description) VALUES (%s, %s)", (Json(rule_ast), description))
    conn.commit()
    cur.close()
    conn.close()

def get_rules():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT rule_ast FROM rules")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
