from models.model import get_category, case_exists, get_items_by_category
from models.claim_model import (save_claim,
                                get_existing_claim_id,
                                get_claim_by_id,
                                get_all_claim)
from ui.case_ui import display_cases
from ui.claim_ui import display_all_claims,display_claim
from validators import get_required_input, check_date_format

# <1> Create claim---------------------------------------
#GET INFO----------
def create_claim():

    category=get_category()

    items=get_items_by_category(category)

    display_cases(items)

    case_id=case_exists(category)
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


# <2> VIEW ALL CLAIM------------------------------------------------
def view_all_claim():
    claims=get_all_claim()

    display_all_claims(claims)

# <3> SEARCH CLAIM-------------------------------------------------
def search_claim():
    print("\n SEARCH CLAIM ")

    claim_id=get_existing_claim_id()

    claim=get_claim_by_id(claim_id)

    display_claim(claim)
