from app.db.db_index import conn

sql_schema ="""
CREATE TABLE IF NOT EXISTS tasks(
    id SERIAL PRIMARY KEY,
    to_do VARCHAR(100) NOT NULL,
    to_date DATE,
    from_date DATE,
    sussesful BOOLEAN NOT NULL
)
"""

def iniciar_db():
    try:
        cur = conn.cursor()
        cur.execute(sql_schema)
        conn.commit()
        print("Base de datos inicializada correctamente.")
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")