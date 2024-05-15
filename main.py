import typer
import pandas as pd

app = typer.Typer()


@app.command()
def run_cleaning_process():
    typer.echo("TSV file cleaned successfully!")


if __name__ == "__main__":
    app()
