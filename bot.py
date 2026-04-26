import os, sys, time, uuid, requests, subprocess
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.progress import track

console = Console()

# --- CONFIGURATION (APKA NAAM) ---
OWNER = '𝐎𝐖𝐍𝐄𝐑 𝐁𝐄𝐖𝐀𝐅𝐀 𝐋𝐄𝐆𝐄𝐍𝐃'
DEVICE_FILE = '.device_id'
UNIQUE_DEVICE_ID = str(uuid.getnode())

def clear():
    os.system("clear")

def print_stylish_menu():
    clear()
    # Stylish RGB-like color for the name
    owner_text = Text(f"      {OWNER}      ", style="bold white on rgb(200,0,255)")
    
    banner = f"""
[bold rgb(0,255,150)]88""Yb    db    88b 88  dP""b8 Yb  dP 88""Yb    db    8888P 
88__dP   dPYb   88Yb88 dP   `"  YbdP  88__dP   dPYb     dP  
88\"\"\"   dP__Yb  88 Y88 Yb  "88   8P   88""Yb  dP__Yb   dP   
88     dP    Yb 88  Y8  YboodP  dP    88oodP dP    Yb d8888 
[bold white]------------------------------------------------------------
[bold yellow] OWNER NAME : {OWNER}
[bold yellow] TOOL TYPE  : FRESH ID CLONING (2026)
[bold yellow] STATUS     : PREMIUM ACCESS GRANTED
[bold white]------------------------------------------------------------"""
    console.print(banner)
    console.print(Panel(owner_text, title="[bold green]WELCOME LEGEND", subtitle="[bold red]V1.5.0", width=62))

def login():
    console.print("\n[bold cyan][➔] SECURITY CHECK[/bold cyan]")
    user = Prompt.ask("[bold white]Enter Username[/bold white]")
    pwd = Prompt.ask("[bold white]Enter Password[/bold white]", password=True)
    
    # Login Details jo ap ne batai thin
    if user.lower() == "bewafa" and pwd == "legend2026":
        console.print("[bold green][✓] Access Approved! Welcome Bewafa Legend.[/bold green]")
        time.sleep(1)
        return True
    else:
        console.print("[bold red][✗] Wrong Credentials! Try Again.[/bold red]")
        sys.exit()

def crack(id_pass):
    try:
        id, pas = id_pass.split('|')
        # Yahan aapka cloning logic aayega
        time.sleep(0.05) # Speed simulation
        return True
    except:
        return False

def main():
    print_stylish_menu()
    login()
    
    console.print("\n[bold white][1] START FILE CLONING (MIX ID)[/bold white]")
    console.print("[bold white][2] START FILE CLONING (OLD ID)[/bold white]")
    console.print("[bold white][3] CONTACT OWNER (WHATSAPP)[/bold white]")
    console.print("[bold red][0] EXIT TOOL[/bold red]")
    
    opt = Prompt.ask("\n[bold yellow]Select Option[/bold yellow]", choices=["1", "2", "3", "0"])
    
    if opt == "1" or opt == "2":
        file_path = Prompt.ask("\n[bold green]Put Your ID File Path[/bold green]")
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                ids = f.readlines()
            
            console.print(f"[bold cyan][➔] Total IDs Found: {len(ids)}[/bold cyan]")
            console.print(f"[bold cyan][➔] Cloning Speed: Max (30 Threads)[/bold cyan]\n")
            
            with ThreadPoolExecutor(max_workers=30) as exe:
                for item in track(ids, description="[bold magenta]Cloning...[/bold magenta]"):
                    exe.submit(crack, item.strip())
            
            console.print("\n[bold green][✓] Cloning Completed Successfully![/bold green]")
        else:
            console.print("[bold red][!] File Not Found! Check path again.[/bold red]")
            
    elif opt == "3":
        # Yahan aap apna WhatsApp link dal sakte hain
        console.print("[bold green][➔] Redirecting to WhatsApp...[/bold green]")
        time.sleep(1)

if __name__ == '__main__':
    main()
