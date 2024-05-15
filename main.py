import typer
import pandas as pd
import vamstar.data_cleaning as dc

app = typer.Typer()


df = pd.read_csv("test.tsv", sep="\t")


@app.command()
def run_cleaning_process(df):
    """
    Run the data cleaning process
    """
    dc.mean_population_data(df=df)
    typer.echo("TSV file cleaned successfully!")


if __name__ == "__main__":
    app()
