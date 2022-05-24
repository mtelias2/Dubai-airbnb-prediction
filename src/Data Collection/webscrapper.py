#Written by Moutaz Elias
#Scraps housing price and rent data from https://www.propertyfinder.ae/
#and stores it in a csv file
#written using OOP classes and functions


#importing libraries
import requests
from bs4 import BeautifulSoup
import csv
import re
import time
import datetime
import os
import urllib3

class Scrapper:
    def __init__(self,link):
        self.link = link
    
        


