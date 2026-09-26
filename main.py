from export_excel import export_to_excel
from validators import get_case_id
from models.model import case_exists
from crud.claim_crud import (create_claim,
                             view_all_claims,
                             search_claim,
                             approve_claim,
                             reject_claim)
from crud.case_crud import (register_found_item,
                       view_all_cases,
                       search_case,
                       update_case,
                       delete_case)
from ui.ui import show_title,show_main_menu
from ui.claim_ui import show_claim_menu
from ui.case_ui import display_cases,show_case_menu

#---------------MAIN MENU LOGIC ------------------------------------------



def main():
    show_title()

    while True:
        show_main_menu()

        choice=input("\n Enter your choice - ")

        if choice=="1":
            case_management()

        if choice=="2":
           claim_management()

        if choice=="3":
            print("Excel coming soon")
            export_to_excel()


        elif choice=="4":
            print("GoodBye...")
            break

        else:
            print("option not avail yet .")

#-----------------------------------------------------------------------------

def case_management():
    while True:
        show_case_menu()

        choice = input("\nEnter your choice - ")

        if choice == "1":
            register_found_item()

        elif choice == "2":
            cases = view_all_cases()
            display_cases(cases)

        elif choice == "3":
            search_case()

        elif choice == "4":
            update_case()

        elif choice == "5":
            delete_case()

        elif choice == "6":
            break

        else:
            print("Invalid option.")

#------------------------claim management------------------------------------------------

def claim_management():
    while True:
        show_claim_menu()

        choice = input("\nEnter your choice - ")

        if choice == "1":
            print("-------- CREATE CLAIM --------")
            create_claim()

        elif choice == "2":
            view_all_claims()

        elif choice == "3":
            search_claim()
        elif choice == "4":
            print("APPROVE CLAIM")
            approve_claim()

        elif choice == "5":
            print("REJECT CLAIM")
            reject_claim()

        elif choice == "6":
            break

        else:
            print("Invalid option.")



if __name__ == "__main__":
    main()