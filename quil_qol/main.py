import typer
from typing_extensions import Annotated


app = typer.Typer()


@app.command()
def compare(
    string1: Annotated[str, typer.Argument(help="First string to compare")] = "",
    string2: Annotated[str, typer.Argument(help="Second string to compare")] = "",
    file: Annotated[
        bool,
        typer.Option("--file", "-f", help="Compare with the content of a file"),
    ] = False,
):
    """Compare two strings and print the result"""
    if file:
        with open(string2, "r") as f:
            string2 = f.read()
    if string1 == string2:
        if file:
            print("The strings are the same and the file flag is set")
        else:
            print("The strings are the same")
    else:
        print("The strings are different")
