from database import get_connection
from ui import show_update_menu,show_category,display_case
from validators import get_required_input,check_date_format
from claim_crud import create_claim
from models import get_category

#generate case id logic -----------------------------------------------------------
def generate_case_id():

    connection=get_connection()
    cursor=connection.cursor()

    cursor.execute("select case_id from found_items order by case_id desc limit 1")

    result=cursor.fetchone()

    cursor.close()
    connection.close()

    if result is None:
        return "LF0001"

    last_case_id=result[0]
    last_number=int(last_case_id[2:])
    new_number=last_number+1

    return f"LF{new_number:04d}"

# ----------------------------------CREATE FOUND ITEM ----------------------------------------------------------------------------------




#just taking input from user -------------------------------------------------------

def register_found_item():
    print("\nRegister Found Item")

    item_data={
        "category":get_category(),
        "item_name": get_required_input("Item Name :"),
        "brand": input("Brand (optional): "),
        "model": input("Model (optional): "),
        "description": get_required_input("Description :"),
        "found_location": get_required_input("Found Location :"),
        "found_date": check_date_format(),
        "finder_name": get_required_input("Finder Name :"),
        "finder_employee_id": get_required_input("Finder Employee ID :"),
        "storage_location": input("Storage Location (optional): ")
    }

    case_id=create_found_item(item_data)

    print("\n Item registered successfully")
    print(f"Case ID - {case_id} ")

# input logic for create ------------------------------------------------------------------
def create_found_item(item_data):
    case_id=generate_case_id()

    connection=get_connection()
    cursor=connection.cursor()

    query=""" insert into found_items (case_id,category,item_name,brand,model,description,found_location,found_date,finder_name,finder_employee_id,storage_location)
              values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    values=(
        case_id,
        item_data["category"],
        item_data["item_name"],
        item_data["brand"],
        item_data["model"],
        item_data["description"],
        item_data["found_location"],
        item_data["found_date"],
        item_data["finder_name"],
        item_data["finder_employee_id"],
        item_data["storage_location"],
    )

    cursor.execute(query,values)

    connection.commit()
    cursor.close()

    return case_id

    print(f"Item created successfully. Case ID: {case_id}")

#---------------------------------- create operation ends here -------------------------------------------------------------------------------



#----------------------------------------  View All Operation ----------------------------------------------------------------------------------------

def view_all_cases():
    connection=get_connection()
    cursor=connection.cursor(dictionary=True)

    query="select * from found_items order by case_id"

    cursor.execute(query)
    cases=cursor.fetchall()

    cursor.close()
    connection.close()

    return cases

#----------------------------------------  View All Operation ends ------------------------------------------------------------------------------------



#------------------------------------ search operation  ------------------------------------------------------------------------------

def search_by_case_id(case_id):
    connection=get_connection()
    cursor=connection.cursor(dictionary=True)

    query="select * from found_items where case_id=%s"

    cursor.execute(query,(case_id,))

    case=cursor.fetchone()

    cursor.close()
    connection.close()

    return case

#------------------------------------ search operation ends  ------------------------------------------------------------------------------




#------------------------------------ UPDATE operation  -------------------------------------------------------------------------------

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

#get case id to update ------------------------------------

def update_case():
    print("\nUPDATE CASE")

    case_id=input("Enter Case ID - ")

    case=search_by_case_id(case_id)

    if case is None:
            print("Case not Found.")
            return
    
    field=get_update_field()
    new_val=input("Enter new value - ")

    print(f"\nEntered Case ID - {case_id}")
    print("Selected Field To Update -  ",field.upper())
    print(f"Entered New Value - {new_val}")

    update_found_item(case_id,field,new_val)

#update crud operation---------------------------------------
def update_found_item(case_id,field,new_val):
    connection=get_connection()
    cursor=connection.cursor()

    query=f"update found_items set {field}=%s where case_id=%s "
    value=(new_val,case_id)

    cursor.execute(query,value)

    connection.commit()
    cursor.close()
    connection.close()

    print(f"{field.upper()} has been updated to {new_val.upper()}")

#------------------------------------ UPDATE operation Ends -------------------------------------------------------------------------------

#------------------------------------ Delete operation  -------------------------------------------------------------------------------

def delete_case():

    case_id=input("Enter Case Id - ")

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

def delete_found_item(case_id):

    connection=get_connection()
    cursor=connection.cursor()

    query="delete from found_items where case_id=%s"

    cursor.execute(query,(case_id,))

    connection.commit()
    cursor.close()
    connection.close

#------------------------------------ UPDATE operation Ends -------------------------------------------------------------------------------

