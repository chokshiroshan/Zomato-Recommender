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

The script is using selenium for automation and scraping of zomato website. It loads up every page and scrape name,rating and cost for two person of a particular restaurant. It is then saved in table form and sorted by two values i.e rating and cost_for_two.

### Note:
This is not for commercial use because this data is from zomato's website so they can take actions against the user.
