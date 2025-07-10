from app.db.db_index import conn

cur = conn.cursor()

def create_task(task):
    if not task["to_do"]:
        return (False, "El nombre es obligatorio")
    try:
        cur.execute("INSERT INTO tasks (to_do, from_date, to_date, sussesful) VALUES (%s, %s, %s, %s)",(task["to_do"], task["from_date"], task["to_date"], task["sussesful"]))
        conn.commit()
        return (True, "Tarea creada correctamente")
    except Exception as e:
        print(f"Error al crear tarea: {e}")
        return (False, "Error al crear tarea")

def get_tasks():
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    return tasks

def delete_task(task_id):
    cur.execute("DELETE FROM tasks WHERE id = %s", (str(task_id),))
    conn.commit()
    return (True, "Tarea eliminada correctamente")

def update_sussesful_task(cliente_id):
    cur.execute("SELECT * FROM tasks WHERE id = %s", (str(cliente_id),))

    cliente = cur.fetchone()
     
    if not cliente[1]:
        return(False, "El id no exixte, intente de nuevo con un id diferente")
    
    cur.execute("UPDATE tasks SET sussesful = %s WHERE id = %s", ("true", cliente_id))

    conn.commit()

    return (True, "Task actualizado correctamente")