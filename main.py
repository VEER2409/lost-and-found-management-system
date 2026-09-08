from case_crud import register_found_item,view_all_cases,search_by_case_id,update_case,create_claim,delete_case
from ui import show_title,show_main_menu,display_cases,display_case,show_case_menu,show_claim_menu
from export_excel import export_to_excel

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
            case_id = input("Enter Case ID: ")
            case = search_by_case_id(case_id)
            display_case(case)

        elif choice == "4":
            update_case()

        elif choice == "5":
            print("Delete Case")
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
            create_claim()

        elif choice == "2":
            print("View Claim ")

        elif choice == "3":
            print("Approve Claim ")

        elif choice == "4":
            print("Reject Claim ")

        elif choice == "5":
            break

        else:
            print("Invalid option.")



if __name__ == "__main__":
    main()