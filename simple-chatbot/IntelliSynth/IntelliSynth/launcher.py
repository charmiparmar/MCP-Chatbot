from rich import print
from core_engine import run_system

if __name__ == "__main__":
    topic = input("Enter your research topic: ")
    print("[bold green]Running IntelliSynth...[/bold green]")
    summary = run_system(topic)
    print("\n[bold cyan]Summary:[/bold cyan]")
    print(summary)
