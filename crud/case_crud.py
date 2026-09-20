from database import get_connection
from validators import get_required_input, check_date_format
from models.model import get_category,case_exists
from models.case_model import (create_found_item,
                               update_found_item,
                               delete_found_item,
                               search_by_case_id)
from ui.case_ui import show_update_menu,display_case

# <1> taking input from user -------------------------------------------------------

def register_found_item():
    print("\nRegister Found Item")

    item_data={
        "category":get_category(),
        "item_name": get_required_input("Item Name "),
        "brand": input("Brand (optional): "),
        "model": input("Model (optional): "),
        "description": get_required_input("Description "),
        "found_location": get_required_input("Found Location "),
        "found_date": check_date_format(),
        "finder_name": get_required_input("Finder Name "),
        "finder_employee_id": get_required_input("Finder Employee ID "),
        "storage_location": input("Storage Location (optional): ")
    }

    case_id=create_found_item(item_data)

    print("\n Item registered successfully")
    print(f"Case ID - {case_id} ")


# <2>  View All Operation ----------------------------------------------------------------------------------------

def view_all_cases():
    connection=get_connection()
    cursor=connection.cursor(dictionary=True)

    query="select * from found_items order by case_id"

    cursor.execute(query)
    cases=cursor.fetchall()

    cursor.close()
    connection.close()

    return cases


# <3>  Search  Operation ----------------------------------------------------------------------------------------

def search_case():
    print("\nSEARCH CASE")

    case_id = case_exists()

    case = search_by_case_id(case_id)

    display_case(case)


# <4> UPDATE operation  -------------------------------------------------------------------------------

#update menu selection--------------------------------------

def get_update_field():
    fields={
        "1": "category",
        "2": "item_name",
        "3": "brand",
        "4": "model",
        "5": "description",
        "6": "found_location",
        "7": "found_date",
        "8": "finder_name",
        "9": "finder_employee_id",
        "10": "storage_location"
    }

    while True:
        show_update_menu()
        choice=input("Enter your choice to update - ")

        if choice in fields:
            return fields[choice]
        
        print("Invalid choice. Please select a field from the menu.")

def update_case():
    print("\nUPDATE CASE")

    case_id = case_exists()

    case = search_by_case_id(case_id)

    if case is None:
        print("Case not Found.")
        return

    field = get_update_field()
    new_val = input("Enter new value - ")

    print(f"\nEntered Case ID - {case_id}")
    print("Selected Field To Update - ", field.upper())
    print(f"Entered New Value - {new_val}")

    update_found_item(case_id, field, new_val)

# <5> Delete operation  -------------------------------------------------------------------------------

def delete_case():

    case_id=case_exists()

    case=search_by_case_id(case_id)

    if case is None:
        print("Case not Found.")
        return

    display_case(case)

    confirm=input("Are you sure you want to delete case ? (y/n)")

    if confirm.lower()=="y":
        delete_found_item(case_id)
        print("Case deleted successfully ")
    else:
        print("Delete cancelled ")
