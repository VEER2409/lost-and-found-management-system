from rich.console import Console
from rich.table import Table
from rich.text import Text

console=Console()
#show claim menu --------------------------------------------------------------------

def show_claim_menu():
    table = Table(
        title="[bold cyan] CLAIM MANAGEMENT [/bold cyan]",
        show_lines=True
        )

    table.add_column("Option", justify="center",style="bold cyan")
    table.add_column("Operation",style="bold white")

    table.add_row("1", "[bold green] Create Claim [/bold green]")
    table.add_row("2", "[bold green] View All Claim [/bold green]")
    table.add_row("3", "[bold green] Search Claim [/bold green]")
    table.add_row("4", "[bold green] Approve Claim [/bold green]")
    table.add_row("5", "[bold red] Reject Claim [/bold red]")
    table.add_row("6", "[bold yellow] Back [/bold yellow]")

    console.print(table)

#display all claims ----------------------------------------------------------------

def display_all_claims(claims):
    if not claims:
        console.print("[bold red] No Claims Found [/bold red]")
        return

    table=Table(
        title="[bold cyan] ALL CLAIMS [/bold cyan]",
        show_lines=True
    )

    table.add_column("Claim ID",style="bold yellow")
    table.add_column("Case ID",style="bold cyan")
    table.add_column("Claimant",style="bold green")
    table.add_column("Employee ID ")
    table.add_column("Claim Date")
    table.add_column("Status",style="bold")

    for claim in claims:
        table.add_row(
            claim["claim_id"],
            claim["case_id"],
            claim["claimant_name"],
            claim["claimant_employee_id"],
            str(claim["claim_date"]),
            claim["claim_status"]
        )

    console.print(table)


#display claim ---------------------------------------------------------------------

def display_claim(claim):
    if not claim:
        console.print("[bold yellow]No claims found.[/bold yellow]")
        return

    table=Table(
        title="\n[bold cyan] CLAIM DETAILS [/bold cyan]"
    )

    table.add_column("Field",style="bold purple")
    table.add_column("Information",style="bold green")

    table.add_row("Claim ID",f"[bold yellow]{claim['claim_id']} [/bold yellow]")
    table.add_row("Case ID",claim["case_id"])
    table.add_row("Claimant Name",claim['claimant_name'])
    table.add_row("Claimant EMP ID",claim['claimant_employee_id'])
    table.add_row("Claim Date",str(claim['claim_date']))
    table.add_row("Claim Description",claim['claim_description'])
    table.add_row("Status",claim['claim_status'])
    table.add_row(
        "Verified By EMP_ID",
        claim['verified_by_employee_id'] or '-'
    )

    console.print(table)
