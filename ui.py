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
            title=" [bold cyan] RECEPTION DESK [/bold cyan]",
            border_style="cyan",
            padding=(1,4)
        )
    )
#main menu----------------------------------------------------------------------

def show_main_menu():
    table=Table(
        title="\n\n[bold cyan] Main Menu [/bold cyan]",
        show_lines=True
        )

    table.add_column("Option",justify="center" , style="bold cyan")
    table.add_column("Operation", style="white")

    table.add_row("1","[bold green]Case Management [/bold green]")
    table.add_row("2","[bold green]Claim Management [/bold green]")
    table.add_row("3","[bold green]Export Data To Excel [/bold green]")
    table.add_row("4","[bold yellow] EXIT [/bold yellow]")

    console.print(table)

#show_case menu-------------------------------------------------------------------

def show_case_menu():
    table=Table(
        title="\n [bold cyan]Case Management [/bold cyan]",
        show_lines=True
        )

    table.add_column("Option", justify="center",style="bold cyan")
    table.add_column("Operations",style="white")

    table.add_row("1", "[bold green] Register Found Item [/bold green]")
    table.add_row("2", "[bold green] View All Cases[/bold green]")
    table.add_row("3", "[bold green] Search Case [/bold green]")
    table.add_row("4", "[bold green] Update Case [/bold green]")
    table.add_row("5", "[bold red] Delete Case [/bold red]")
    table.add_row("6", "[bold yellow] Back [/bold yellow]")

    console.print(table)


#show claim menu --------------------------------------------------------------------

def show_claim_menu():
    table = Table(
        title="[bold cyan] CLAIM MANAGEMENT [/bold cyan]",
        show_lines=True
        )

    table.add_column("Option", justify="center",style="bold cyan")
    table.add_column("Operation",style="bold white")

    table.add_row("1", "[bold green] Create Claim [/bold green]")
    table.add_row("2", "[bold green] View Claim [/bold green]")
    table.add_row("3", "[bold green] Approve Claim [/bold green]")
    table.add_row("4", "[bold red] Reject Claim [/bold red]")
    table.add_row("5", "[bold yellow] Back [/bold yellow]")

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

def format_status(status):

    if not status:
        return "[dim] NO DATA [/dim]"

    if status=="Awaiting Claim":
        return "[bold yellow]Awaiting Claim[/bold yellow]"

    if status=="Claimed":
        return "[bold green] Claimed [/bold green]"

    if status=="Pending":
        return "[bold blue] Pending [/bold blue]"

    if status=="Rejected":
        return "[bold red] Rejected [/bold red]"

    return str(status)


def display_cases(cases):
    table=Table(title="\n[bold cyan]Found Items [/bold cyan]",show_lines=True)

    table.add_column("[bold bright_cyan] Case ID [/bold bright_cyan]",width=10)
    table.add_column("[bold bright_cyan] Category [/bold bright_cyan]",overflow="fold")
    table.add_column("[bold bright_cyan] Item [/bold bright_cyan]",overflow="fold")
    table.add_column("[bold bright_cyan] Brand [/bold bright_cyan]")
    table.add_column("[bold bright_cyan] Model [/bold bright_cyan]")
    table.add_column("[bold bright_cyan] Description [/bold bright_cyan]")
    table.add_column("[bold bright_cyan] Found Location [/bold bright_cyan]")
    table.add_column("[bold bright_cyan] Finder Name [/bold bright_cyan]")
    table.add_column("[bold bright_cyan] Finder Employee ID [/bold bright_cyan]",width=10)
    table.add_column("[bold bright_cyan] Found Date [/bold bright_cyan]",width=12)
    table.add_column("[bold bright_cyan] Storage Location [/bold bright_cyan]")
    table.add_column("[bold bright_cyan] Status [/bold bright_cyan]",overflow="fold")

    for  case in cases:
        table.add_row(
            f"[bold purple] {case['case_id'] or 'NO DATA'} [/bold purple]",
            f"[dim] {case['category'] or 'NO DATA '}[/dim]",
            f"[dim] {case['item_name'] or 'NO DATA'} [/dim]",
            f"[dim] {case['brand'] or 'NO DATA'} [/dim]",
            f"[dim] {case['model'] or 'NO DATA'} [/dim]",
            f"[dim] {case['description'] or 'NO DATA'} [/dim]",
            f"[dim] {case['found_location'] or 'NO DATA'} [/dim]",
            f"[dim] {case['finder_name'] or 'NO DATA'} [/dim]",
            f"[dim] {case['finder_employee_id'] or 'NO DATA'} [/dim]",
            f"[dim] {case['found_date'] or 'NO DATA'} [/dim]",
            f"[dim] {case['storage_location'] or 'NO DATA'}  [/dim]",
            format_status(case['status'])
        )

    console.print(table)

#search by--------------------------------------------------------------------------------

def display_case(case):
    if case is None:
        return console.print("[bold red] No case found. [/bold red]")
    
    table=Table(title=" [bold cyan] Case Details [/]")

    table.add_column("[bold bright_cyan]Field [/]",style="purple")
    table.add_column("[bold bright_cyan]Information [/]",style="bold green")

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
    table.add_row ("Status",format_status(case['status']))

    console.print(table)





