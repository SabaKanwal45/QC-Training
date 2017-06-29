"""
Read Data from Given Url's via threads and then from Retrieved pages
Search given keywords from the Stories headings and return only the
heading of Stories Returned after Searching
pylint Score 10/10
"""
# pylint: disable-msg=C0103
import threading
import urllib2
from BeautifulSoup import BeautifulSoup


class RetrieveStoryHeading(threading.Thread):
    """
    Retreive From given Urls
    """
    def __init__(self, input_url, words):
        """
        initiate threads  that takes an object
        with two attributes an input url from where
        it have to read data
        :param input_url: Source URL of Data
        :param words: keywords to search
        """
        threading.Thread.__init__(self)
        self.url = input_url
        self.keywords = words

    def run(self):
        """
        Read Data from Given URL and store that data in result attribute
        :return: None
        """
        response = urllib2.urlopen(self.url)
        page_source = response.read()
        soup = BeautifulSoup(''.join(page_source))
        matches = soup.findAll('h2', {"class": "headline"})
        for ele in matches:
            not_required = False
            for word in self.keywords:
                if word not in ele.text:
                    not_required = True
                if not not_required:
                    print ele.text

# Enter Keywords to make search for Story Heading
keywords = []
print "Enter Keyword to Make search Of Story Heading such as Daily Report"
keyword = raw_input()
keywords.append(keyword)
while True:
    print "Press 1 to add more Keyword"
    print "Press 2 to make Search"
    read_input = raw_input()
    if read_input == "1":
        print "Enter Keyword"
        keyword = raw_input()
        keywords.append(keyword)
    elif read_input == "2":
        break
    else:
        print "Enter valid Value"
        continue
threads = []
# Url's from where to read data
urls = ["https://www.reddit.com/r/programming/",
        "https://news.ycombinator.com/",
        "https://www.theguardian.com/us/technology",
        "https://www.nytimes.com/section/technology"]
# Create Seperate threads
for url in urls:
    thread = RetrieveStoryHeading(url, keywords)
    threads += [thread]
    thread.start()

for thread in threads:
    thread.join()

