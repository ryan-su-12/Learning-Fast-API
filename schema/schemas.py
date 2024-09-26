def individual_serial(todo) -> dict:
    return{
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["desc"],
        "complete": todo["complete"]
    }

def individual_serial(Finances) -> dict:
    return{
        "id": str(Finances["_id"]),
        "name": Finances["name"],
        "job": Finances["job"],
        "salary": Finances["salary"],
        "Yoe": Finances["Yoe"]

    }


def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]



def list_serial(Finances) -> list:
    return [individual_serial(Finance) for Finance in Finances]