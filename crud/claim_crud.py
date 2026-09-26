from models.model import get_category, case_exists, get_items_by_category
from models.claim_model import (save_claim,
                                get_existing_claim_id,
                                get_claim_by_id,
                                get_all_claim,
                                update_claim_status)
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
def view_all_claims():
    claims=get_all_claim()

    display_all_claims(claims)

# <3> SEARCH CLAIM-------------------------------------------------
def search_claim():
    print("\n SEARCH CLAIM ")

    claim_id=get_existing_claim_id()

    claim=get_claim_by_id(claim_id)

    display_claim(claim)

# <4> APPROVE CLAIM-------------------------------------------------
def approve_claim():
    claim_id=get_existing_claim_id()

    claim=get_claim_by_id(claim_id)

    if claim["claim_status"]=="Approved":
        print("\nClaim is already Approved")
        return

    display_claim(claim)

    confirm=input("\nAre you sure you want to APPROVE (y/n) : ")

    if confirm.lower()!="y":
        print("\nApproval Cancel")
        return

    verified_by=get_required_input("Enter Verifier Employee ID ")

    update_claim_status(claim_id,"Approved",verified_by)

    print("\n Claim Approved Successfully")

# <5> REJECT CLAIM-------------------------------------------------
def reject_claim():
    claim_id=get_existing_claim_id()

    claim=get_claim_by_id(claim_id)

    if claim["claim_status"]=="Rejected":
        print("\nClaim is already Rejected")
        return

    display_claim(claim)

    confirm=input("\nAre you sure you want to REJECT claim (y/n) : ")

    if confirm.lower()!="y":
        print("\nRejection Cancelled")
        return

    verified_by=get_required_input("Enter Verifier Employee ID ")

    update_claim_status(claim_id,"Rejected",verified_by)

    print("\n Claim Rejected Successfully")
