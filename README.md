<div id="top"></div>

# kindle-to-anki

Convert your Amazon Kindle clippings to Anki cards (one deck per book) and easily import them.

Built with Python `3.8` for Anki `2.1.48`.

[![Screencast][screencast]](doc/screencast.gif)

## Getting Started

The following steps will guide you through the process to get a local copy up and running.

### Prerequisites

You must have the following to run the project:

* [Python](https://www.python.org/downloads/) `3.8.1` or above
* [pip](https://pip.pypa.io/en/stable/installation/) `19.2.3` or above
* [Anki](https://apps.ankiweb.net/) `2.1.48` or above

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/aziule/kindle-to-anki.git
   ```
2. [Optional] Create a Python virtual env and activate it
3. Install pip requirements
   ```sh
   make req-install
   # OR
   python -m pip -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage

There are two steps to convert your clippings to Anki cards:

1. Convert your clippings to Anki packages (`*.apkg` files) using this project
2. Import the packages to Anki and reorganise the cards

### 1) Create Anki packages

1. Connect your Amazon Kindle via USB
2. Find the file named "My Clippings.txt" in your Amazon Kindle
3. From the project's root directory, using your terminal, run:
   ```sh
   # Note: replace the path to My Clippings.txt 
   python ./cli.py --clippings=My\ Clippings.txt
   ```
   
The packages will be located in the `gen` directory of the project.

You should see something like this:

[![Step 1 - Convert][step-1-convert]](doc/1_convert.png)

### 2) Import packages in Anki

First, you need to open Anki:

1. Open Anki
2. Create a new profile or choose an existing one
3. Open it

Then, for each book, you will need to repeat the following:

1. Click "Import File"
2. Head to the project directory, under the `gen` folder
3. Select the `*.apkg` file you would like to import and import it
4. Check the database (Tools > Check Database)
5. The cards should be visible in the "Browse" tab

You should see something like this:

[![Step 2 - Import][step-2-import]](doc/2_import.png)

That's it! All your clippings are now in Anki, ready to be further dealt with.

### 3) More information

* By default, Anki will import the cards to the Default deck. If you want to split them per book,
I recommend that you assign them to the deck you desire _before_ importing the next `*.apkg`. Otherwise
it might be tricky to find when the first deck's cards end and when the next one's start.
* You need to check the database after each import. 

<p align="right">(<a href="#top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

## Acknowledgments

* [genanki](https://github.com/kerrickstaley/genanki)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[screencast]: doc/screencast.gif
[step-1-convert]: doc/1_convert.png
[step-2-import]: doc/2_import.png