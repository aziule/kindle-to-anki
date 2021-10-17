clipping_delimitor = "=========="
idx_book_name = 0
idx_contents = 3

class Clipping:
    def __init__(self, book_name, contents):
        self.book_name = book_name
        self.contents = contents

def parse(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()

    clippings = []

    is_new = True
    raw_data = []

    books = {}

    for line in lines:
        line = line.strip()

        if line != clipping_delimitor:
            is_new = False
            raw_data.append(line)
            continue

        book_name = raw_data[idx_book_name].encode('ascii', 'ignore').decode('utf-8')
        clipping = Clipping(book_name, raw_data[idx_contents])
        clippings.append(clipping)

        books[book_name] = True
        is_new = True
        raw_data = []

    print("{} clippings found in {} books".format(len(clippings), len(books)))

    return clippings
