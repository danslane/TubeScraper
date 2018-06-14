# By Bryant Rolfe w/ assist from Dan Lane (2016)
# This script is designed to search YouTube videos via API and download metadata into a .csv file


# Setup

    # Create a virtualenv if not already there
    [sudo] pip install virtualenv
    virtualenv venv
    # activate virtualenv
    source venv/bin/activate
    pip install -r requirements.txt
    # When done...
    deactivate

Next, create a file called "API_KEY.txt" with the contents of the server API
key for the youtube data api (v3) from https://cloud.google.com/console.
    
# Run Tests

    invoke

# Run Main

    ./main.py
