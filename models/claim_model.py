from database import get_connection
from validators import get_claim_id
from ui.ui import console

#------------------------------ generate claim id -------------------------------
def generate_claim_id():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "select claim_id from claims order by claim_id desc limit 1"
    )

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result is None:
        return "CL0001"

    last_claim_id = result[0]
    last_digit = int(last_claim_id[2:])
    new_claim_id = last_digit + 1

    return f"CL{new_claim_id:04d}"


#------------------- claim id exist or not ---------------------------

def get_existing_claim_id():
    while True:
        claim_id=get_claim_id()

        if claim_id_exists(claim_id):
            return claim_id

        console.print(f"[bold red]Claim ID does not exist.[/bold red]")

def claim_id_exists(claim_id):
    connection=get_connection()
    cursor=connection.cursor()

    query="select claim_id from claims where claim_id=%s"

    cursor.execute(query,(claim_id,))

    result=cursor.fetchone()

    cursor.close()
    connection.close()

    return result is not None


# <1> operation 1 create claim -----------------------------------
def save_claim(claim_data):
    claim_id = generate_claim_id()

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        insert into claims
        (claim_id, case_id, claimant_name,
         claimant_employee_id, claim_date, claim_description)
        values (%s, %s, %s, %s, %s, %s)
    """

    values = (
        claim_id,
        claim_data["case_id"],
        claim_data["claimant_name"],
        claim_data["claimant_employee_id"],
        claim_data["claim_date"],
        claim_data["claim_description"]
    )

    cursor.execute(query, values)

    connection.commit()
    cursor.close()
    connection.close()

    return claim_id

# <2> operation 2 View all claim -------------------------------------

def get_all_claim():
    connection=get_connection()
    cursor=connection.cursor(dictionary=True)

    query="select * from claims order by claim_id"

    cursor.execute(query)

    result=cursor.fetchall()

    cursor.close()
    connection.close()

    return result

# <3> operation 3 SEARCH claim -------------------------------------

def get_claim_by_id(claim_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = "select * from claims where claim_id=%s"

    cursor.execute(query, (claim_id,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result


