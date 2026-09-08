from database import get_connection
from models import get_category
from ui import display_cases
from validators import get_required_input,check_date_format

def generate_claim_id():

    connection=get_connection()
    cursor=connection.cursor()

    cursor.execute("select claim_id from claims order by claim_id desc limit 1")

    result=cursor.fetchone()

    cursor.close()
    connection.close()

    if result is None:
        return "CL0001"

    last_claim_id=result[0]
    last_digit=int(last_claim_id[2:])
    new_claim_id=last_digit+1

    return f"CL{new_claim_id:04d}"

#----------------------------- CREATE CLAIM --------------------------------------------------------------------------------------------------

def create_claim():

    category=get_category()

    items=get_items_by_category(category)

    display_cases(items)

    case_id=get_required_input("Enter the Case ID of matching item - ")
    claimant_name=get_required_input("Enter Claimant Name - ")
    claimant_employee_id=get_required_input("Enter Claimant Employee ID - ")
    claim_date=check_date_format()
    claim_description=get_required_input("Claim Description - ")

    claim_data={
        "case_id": case_id,
        "claimant_name":claimant_name,
        "claimant_employee_id":claimant_employee_id,
        "claim_date":claim_date,
        "claim_description":claim_description
    }

    claim_id=save_claim(claim_data)

    print("\n Claim Created Successfully")
    print(f"Claim ID - {claim_id}")


def save_claim(claim_data):
    claim_id=generate_claim_id()

    connection=get_connection()
    cursor=connection.cursor()

    query=""" insert into claims (claim_id, case_id, claimant_name, 
            claimant_employee_id,claim_date, claim_description)
            values (%s, %s, %s, %s, %s, %s)
            """

    values=(
        claim_id,
        claim_data["case_id"],
        claim_data["claimant_name"],
        claim_data["claimant_employee_id"],
        claim_data["claim_date"],
        claim_data["claim_description"]
    )

    cursor.execute(query,values)

    connection.commit()
    connection.close()
    cursor.close()

    return claim_id

#get items by category--------------------------------------------------------------

def get_items_by_category(category):

    connection=get_connection()
    cursor=connection.cursor(dictionary=True)

    query=("select * from found_items where category=%s")

    cursor.execute(query,(category,))

    items=cursor.fetchall()

    cursor.close()
    connection.close()

    return items

