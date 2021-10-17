import genanki
import hashlib
import math
from datetime import datetime

def create_model():
    return genanki.Model(
        int(datetime.utcnow().timestamp()),
        'kindle-to-anki model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[{
            'name': 'imported-card',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        }],
    )

def create_decks(model, clippings):
    decks = {}

    for clipping in clippings:
        md5 = hashlib.md5(clipping.book_name.encode('utf-8'))
        id = math.trunc(int(md5.hexdigest(), 16) / 1e+32)

        if id not in decks:
            decks[id] = genanki.Deck(
                id,
                clipping.book_name
            )

        note = genanki.Note(
            model=model,
            fields=['', clipping.contents]
        )
        decks[id].add_note(note)

    print("{} decks created".format(len(decks)))
    return decks

def create_package(output, decks):
    for id, deck in decks.items():
        genanki.Package(deck).write_to_file("{}/{}.apkg".format(output, deck.name))
        print("Anki pkg created: {}".format("{}/{}.apkg".format(output, deck.name)))

    print("All decks successfully exported")