
# Modules

import math
import random
import rich
from time import sleep
from rich.console import Console
from loguru import logger

# Default Variebles

console = Console()

# Logic

name = """
██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░░░░░░░██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗░░░░░░██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║
██║░░██║██║░░██║██║░░╚═╝█████═╝░█████╗░░██████╔╝█████╗██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║
██║░░██║██║░░██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗╚════╝██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║
██████╔╝╚█████╔╝╚█████╔╝██║░╚██╗███████╗██║░░██║░░░░░░██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░░░░╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝
"""

console.print(name, style="bold blue")

def fac(n):
    if not n and n < 0 and n == '':
        logger.error('Number is not defined')
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)

try:
    num = int(console.input('[bold yellow]Enter number: [/bold yellow]'))
    with console.status('[bold green]Learning...[/bold green]') as status:
        sleep(1)
        console.print(f"\nFactorial: [bold green]{fac(num)}[/bold green]\n", style="yellow")
except EOFError as e:
    print(end="")
