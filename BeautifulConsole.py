from rich import print
from rich.console import Console

console = Console()
console.print('Hello', 'World!', style = 'bold red')

print('Hello, [bold magenta]World[/bold magenta]', ':vampire:', locals())