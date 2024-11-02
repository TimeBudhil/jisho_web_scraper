from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import csv

driver = webdriver.Chrome('/Users/MyUsername/Downloads/chromedriver')

# the link which will be edited according t the word
main_link = "https://jisho.org/word/" # + kanji
search_link = "https://jisho.org/search/" # + search


# returning example sentence as string
def find_example_sent(word):
    new_link = main_link + word
    return word


# returns new word
# verifies the correct writing in the respective database
def search_kanji_word(word):
    new_link = search_link + word
    driver.get(new_link)
    driver.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div/span[2]')

    return word

# returns alternative readings
def find_alt_writings(word):
    new_link = main_link + word
    return word


def find_readings(word):
    new_link = main_link + word
    return word

# returns definition
def find_definition(word):
    new_link = main_link + word
    return word

# SAVES to NEW TSV
def find_one_def(word):
    #modify link
    fields = [word]
    new_link = main_link + word
    
    # append more fields
    
    # mixed-Kanji Word

    # Alternative readings (not doing now)

    # Definition

    # Kanji Reading (hiragana/katakana)

    #Finding Example sentence
    

    #stitch the words together and return as tsv

    return new_link


# get list of words


