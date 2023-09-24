import typer
from typing_extensions import Annotated


app = typer.Typer()


@app.command()
def compare(
    string1: Annotated[str, typer.Argument(help="First string to compare")],
    string2: Annotated[str, typer.Argument(help="Second string to compare")],
):
    """Compare two strings and print the result"""
    if string1 == string2:
        print("The strings are the same")
    else:
        print("The strings are different")
