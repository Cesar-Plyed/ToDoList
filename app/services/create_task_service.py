from ..db.operations import create_task

def create_task_service(task, to_date, from_date):
    task_to_do = {
        "to_do": task,
        "to_date": to_date,
        "from_date": from_date,
        "sussesful": "false"
    }
    
    result, message = create_task(task_to_do)
    return result