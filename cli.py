import click
import os.path
import src.clipping
import src.anki

@click.command()
@click.option("--clippings", default="", help="path to My Clippings.txt file")
def import_clippings(clippings):
    if not os.path.isfile(clippings):
        raise click.ClickException("Clippings file not found")

    try:
        print("=== Parse Clippings.txt")
        clippings = src.clipping.parse(clippings)
        print("Done")
        print("=== Create Anki resources")
        model = src.anki.create_model()
        decks = src.anki.create_decks(model, clippings)
        src.anki.create_package("./gen", decks)
        print("Done")
    except:
        print("failed to import clippings:", sys.exc_info()[0])

if __name__ == "__main__":
    import_clippings()