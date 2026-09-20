from database import get_connection
from validators import get_case_id
from ui.ui import show_category,console

# <1> category selection------------------------------------------

def get_category():
    categories={
        "1": "Electronics",
        "2": "ID / Documents",
        "3": "Jewelry",
        "4": "Bags & Accessories",
        "5": "Clothing",
        "6": "Books & Stationery",
        "7": "Keys",
        "8": "Office Equipment",
        "9": "Personal Items",
        "10": "Other"
    }

    while True:
        show_category()
        choice=input("Enter your choice - ")

        if choice in categories:
            return categories[choice]
        print("Invalid choice. Please select a category from the menu. ")

# <2> get items by category -----------------------------

def get_items_by_category(category):

    connection=get_connection()
    cursor=connection.cursor(dictionary=True)

    query=("select * from found_items where category=%s")

    cursor.execute(query,(category,))

    items=cursor.fetchall()

    cursor.close()
    connection.close()

    return items

# <3> case id exists -----------------------------------------

def check_case_exists(case_id):
    connection=get_connection()
    cursor=connection.cursor()

    query="select case_id from found_items where case_id=%s"

    cursor.execute(query, (case_id,))

    result=cursor.fetchone()

    cursor.close()
    connection.close()

    return result is not None

def case_exists(category=None):
    while True:
        case_id=get_case_id()

        if category is None:

           if check_case_exists(case_id):
               return case_id
        else:
            if case_matches_category(case_id,category):
                return case_id

        console.print(f"[bold red]Case  ID {case_id} does not exist.[/bold red]")

# <4> case matches category-------------------------------------------

def case_matches_category(case_id,category):

    connection=get_connection()
    cursor=connection.cursor()

    query="select case_id from found_items where case_id=%s and category=%s "

    cursor.execute(query,(case_id,category))
    result=cursor.fetchone()

    cursor.close()
    connection.close()

    return result is not None

