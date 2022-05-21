import os
import time

from rich.box import HEAVY
from rich.panel import Panel
from rich.console import Console

console = Console()

def startup():
    console.print(Panel("[#43A3F9]Windows PowerShell Plus", expand=False, border_style="#0468C2", box=HEAVY), justify="center")
    command_line_loop()

def command_line_loop():
    try:
        while True:
            os.system('powershell "' + console.input('\n[#82BAED]' + os.getcwd().replace("\\", " » ") + ': ') + '"')
    finally:
        command_line_loop()

startup()

