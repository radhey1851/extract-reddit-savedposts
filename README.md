Extract Reddit Saved Posts

Requirements:
- python3
- pipenv
- git

Installation:
- install python3, pipenv and git if not already present on the system.
- run the following commands:
    git clone https://github.com/radhey1851/extract-reddit-savedposts.git
    cd extract-reddit-savedposts
    pipenv install

Usage:
- first get client_id and client_secret by creating a reddit script app in the
  user's reddit account.
- copy client_id, client_secret and enter username and password to acc.py
- then run the following command:
    pipenv run python savedposts.py

A data.csv file should appear in the folder.

