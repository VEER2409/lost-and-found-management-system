from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console=Console()
#panel---------------------------------------------------------------------------
def show_title():

    info=Text(justify="center")
    info.append(" LOST & FOUND MANAGEMENT SYSTEM \n",style="bold white")
    info.append(" TCS - Lost Item Tracking & Claim Management ",style="dim")


    console.print(


        Panel(
            info,
            title="RECEPTION DESK",
            border_style="blue"
        )
    )
#main menu----------------------------------------------------------------------

def show_main_menu():
    table=Table(title="Main Menu")

    table.add_column("Option",justify="center" , style="cyan")
    table.add_column("Operation", style="white")

    table.add_row("1","Case Management")
    table.add_row("2","Claim Management")
    table.add_row("3","Export Data To Excel")
    table.add_row("4","EXIT")

    console.print(table)

#show_case menu-------------------------------------------------------------------

def show_case_menu():
    table=Table(title="Case Management")

    table.add_column("Option", justify="center")
    table.add_column("Operations")

    table.add_row("1", "Register Found Item")
    table.add_row("2", "View All Cases")
    table.add_row("3", "Search Case")
    table.add_row("4", "Update Case")
    table.add_row("5", "Delete Case")
    table.add_row("6", "Back")

    console.print(table)


#show claim menu --------------------------------------------------------------------

def show_claim_menu():
    table = Table(title="CLAIM MANAGEMENT")

    table.add_column("Option", justify="center")
    table.add_column("Operation")

    table.add_row("1", "Create Claim")
    table.add_row("2", "View Claim")
    table.add_row("3", "Approve Claim")
    table.add_row("4", "Reject Claim")
    table.add_row("5", "Back")

    console.print(table)

#-------------------------- category menu ---------------------------------
def show_category():
    table=Table(title="SELECT CATEGORY")

    table.add_column("Choice")
    table.add_column("Category")

    table.add_row("1", "Electronics")
    table.add_row("2", "ID / Documents")
    table.add_row("3", "Jewelry")
    table.add_row("4", "Bags & Accessories")
    table.add_row("5", "Clothing")
    table.add_row("6", "Books & Stationery")
    table.add_row("7", "Keys")
    table.add_row("8", "Office Equipment")
    table.add_row("9", "Personal Items")
    table.add_row("10", "Other")

    console.print(table)
#-------------------------- end category menu ---------------------------------

#--------------------------  UPDATE MENU ---------------------------------
def show_update_menu():
    table=Table(title="SELECT UPDATE FIELD")

    table.add_column("Choice")
    table.add_column("UPDATE")

    table.add_row("1", "Category")
    table.add_row("2", "Item Name")
    table.add_row("3", "Brand")
    table.add_row("4", "Model")
    table.add_row("5", "Description")
    table.add_row("6", "Found Location")
    table.add_row("7", "Found Date")
    table.add_row("8", "Finder Name")
    table.add_row("9", "Finder Employee ID")
    table.add_row("10", "Storage Location")


    console.print(table)
#-------------------------- end UPDATE MENU ---------------------------------


#view all---------------------------------------------------------------------------

def display_cases(cases):
    table=Table(title="Found Items",show_lines=True)

    table.add_column("Case ID")
    table.add_column("Category")
    table.add_column("Item")
    table.add_column("Brand")
    table.add_column("Model")
    table.add_column("Description")
    table.add_column("Found Location")
    table.add_column("Finder Name")
    table.add_column("Finder Employee ID")
    table.add_column("Storage Location")
    table.add_column("Status")

    for  case in cases:
        table.add_row(
            case['case_id'],
            case['category'],
            case['item_name'],
            case['brand'],
            case['model'],
            case['description'],
            case['found_location'],
            str(case['found_date']),
            case['finder_name'],
            case['description'],
            case['storage_location'],
            case['status']
        )

    console.print(table)

#search by--------------------------------------------------------------------------------

def display_case(case):
    if case is None:
        return console.print("no case found.")
    
    table=Table(title="Case Details")

    table.add_column("Field")
    table.add_column("Information")

    table.add_row("Case ID", case["case_id"])
    table.add_row("Category", case["category"])
    table.add_row("Item", case["item_name"])
    table.add_row("Brand", case["brand"] or "-")
    table.add_row("Model", case["model"] or "-")
    table.add_row("Description", case["description"])
    table.add_row("Found Location", case["found_location"])
    table.add_row("Found Date", str(case["found_date"]))
    table.add_row("Finder Name", case["finder_name"])
    table.add_row("Finder Employee ID", case["finder_employee_id"])
    table.add_row("Storage Location", case["storage_location"] or "-")
    table.add_row("Status", case["status"])

    console.print(table)





