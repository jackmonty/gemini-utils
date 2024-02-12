# gemini-utils

A set of Python scripts to interact with Gemini Pro

## Description

A simple script that allows users to interact with the Gemini Pro models from the command line. Includes ability to send a message along with a query.

The technoloiges used are:

- **Google Gemini Pro.** The large language model provided by Google.
- **Google AI API.** Python library used to interact with Gemini Pro.

## Installation

Download and then enter the repository:

    git clone git@github.com:jackmonty/gemini-utils.git
    cd gemini-utils

Install the requirements in a virtual environment:

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

To create an executable that runs outside of the virtual environment:

    pyinstaller --onefile gemini-chat.py

## Run

Check the command line variables

    python gemini-chat.py -h

Run the script with example providede

    python gemini-chat.py --image image.jpg Write a short, engaging blog post for this picture.

## Credits

- The script and the example are derived from [Gemini API: Quickstart with Python](https://ai.google.dev/tutorials/python_quickstart) from Google AI for Developers site..

