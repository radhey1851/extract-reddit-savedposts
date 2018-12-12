#!/usr/bin/env python
"""
savedposts.py

Extracts saved posts from a reddit account and stores them as a CSV file.

"""


import csv
import sys

import praw
import prawcore
import acc


def login():
    """ to login.

    Logs into Reddit user account with the details given in acc.py.
    Hence add details to acc.py before starting.

    Returns:
        a Reddit class instance if logged in successfully.

    Raises:
        PrawcoreException: If login fails due to improper
         user credentials
    """
    if not acc.client_id or not acc.client_secret or not acc.password or not acc.username:
        print("pls enter details in acc.py")
        sys.exit(1)

    try:
        reddit = praw.Reddit(client_id=acc.client_id,
                             client_secret=acc.client_secret,
                             user_agent="saved posts script",
                             username=acc.username,
                             password=acc.password)
        # to raise any possible exceptions from logging in
        reddit.user.me()
        return reddit
    except prawcore.exceptions.PrawcoreException as e:
        print("Login failed: Pls check user credentials and app details")
        print("error: -------------------------------------------------")
        print(e)
        print("--------------------------------------------------------")
        sys.exit(1)


def write_to_csv(saved, filename='data.csv'):
    """
    to write extracted posts to a csv file

    Args:
        saved (list): List of all saved posts
        filename (str,optional): File to be written into.
            defaults to data.csv

    """
    with open(filename, 'w') as csv_file:
        row = ['URL', 'Title', 'Id', 'Sub']
        writer = csv.writer(csv_file)
        writer.writerow(row)
        for i in saved:
            if not hasattr(i, 'title'):
                i.title = i.link_title
            try:
                row = ['https://reddit.com' + i.permalink, i.title, i.id, i.subreddit]
                writer.writerow(row)
            # hack to fix unicode encoding issue
            except UnicodeEncodeError:
                row = ['https://reddit.com' + i.permalink, i.title.encode('utf-8'),
                       i.id, i.subreddit]
                writer.writerow(row)


def main():
    """ main method"""

    # login to reddit
    reddit = login()
    user = reddit.user

    # get saved posts
    saved = user.me().saved(limit=None)

    # write them to a file
    write_to_csv(saved)

    sys.exit(0)


if __name__ == '__main__':
    main()

