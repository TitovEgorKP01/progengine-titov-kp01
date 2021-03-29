import requests
from bs4 import BeautifulSoup


def find_word_frequency(page, seekingWord):

    countOfSeekingWords = page.text.count(seekingWord)

    return countOfSeekingWords/len(page.text.split()) * 100

def find_tag_frequency(page, seekingTag):

    countOfTag = len(page.find_all(seekingTag))

    return countOfTag / len(page.find_all()) * 100

def find_countOf_links(page):

    countOfLinks = 0

    for item in page.find_all():
        if item.get('href') == None or item.get('href') == "":
            continue
        else:
            countOfLinks += 1  

    return countOfLinks


###########################################################################

inputHtml = input('Enter website link: ')

r = requests.get(inputHtml)

page = BeautifulSoup(r.text, 'html.parser')

###########################################################################

seekingWord = input('Enter word to seek: ')

wordFrequency = find_word_frequency(page, seekingWord)

print(f"- Frequency of word '{seekingWord}' is %.2f %%" % wordFrequency)

###########################################################################

seekingTag = input('Enter tag to seek: ')

tagFrequency = find_tag_frequency(page, seekingTag)

print(f"- Frequency of tag '{seekingTag}' is %.2f %%" % tagFrequency)

###########################################################################

countOfLinks = find_countOf_links(page)

print("- Links: ", countOfLinks)

###########################################################################

print("- Images: ", len(page.find_all('img'))) 

###########################################################################