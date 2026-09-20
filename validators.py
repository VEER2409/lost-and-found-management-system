from datetime import datetime
from ui.ui import console
#------------------ CASE FIELD VALIDATORS ---------------------
# <1> validator for other fields------------------------------

def validate_required(value,field_name):
    if not value.strip():
        return False,f"{field_name} cannot be empty "
    return True,""

def get_required_input(field_name):
    while True:
        value=input(f"{field_name}: ")

        valid,message=validate_required(value,field_name)

        if valid:
            return value
        console.print(f"[bold red]{message}[/bold red]")


# <2> validator for date---------------------------------------


def validate_date(date_text):
    try:
        datetime.strptime(date_text,"%Y-%m-%d")
        return True,""
    except ValueError:
       return False , "data must be in YYYY-MM-DD format."


def check_date_format():
    while True:
            found_date = input("Found Date (YYYY-MM-DD): ")

            valid, message = validate_date(found_date)

            if valid:
                return found_date

            console.print(f"[bold red]{message}[/bold red]")

# <3> search case by id no. validation------------------------------

def get_case_id():
    while True:
        case_id=input("Enter Case ID : ")
        valid,message=validate_case_id(case_id)

        if valid:
            return case_id
        console.print(f"[bold red]{message}[/bold red]")

def validate_case_id(case_id):

    case_id = case_id.strip().upper()
    if not case_id.startswith("LF"):
        return False,"Case ID must start with 'LF' "
    if len(case_id) !=6 :
        return False,"Case ID must be in the Format LF0000"
    if not case_id[2:].isdigit():
        return False,"Case ID must contain 4 digits after LF"
    return True,case_id


#------------------ CLAIM FIELD VALIDATORS ---------------------

# <1> get and validate claim_id no.-------------------------------------

def get_claim_id():
    claim_id=input("Enter claim ID")
    valid,result = validate_claim_id(claim_id)

    if valid:
        return result

    console.print(f"[bold red] {result} [/bold red]")

def validate_claim_id(claim_id):
    claim_id=claim_id.strip().upper()

    if not claim_id.startswith("CL"):
        return False,"Claim ID starts with CL"
    if len(claim_id) !=6 :
        return False,"Claim ID must be in format CL0000"
    if not claim_id[2:].isdigit():
        return False,"Claim ID must contain 4 digits after CL "

    return True,claim_id


