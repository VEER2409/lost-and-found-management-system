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


# category menu ---------------------------------
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


# format status--------------------------------------------------------------
def format_status(status):

    if not status:
        return "[dim] NO DATA [/dim]"

    if status=="Awaiting Claim":
        return "[bold white]Awaiting Claim[/bold white]"

    if status=="Claimed":
        return "[bold green] Claimed [/bold green]"

    if status=="Pending":
        return "[bold yellow] Pending [/bold yellow]"

    if status=="Approved":
        return "[bold green] Approved [/bold green]"

    if status=="Rejected":
        return "[bold red] Rejected [/bold red]"

    return str(status)
