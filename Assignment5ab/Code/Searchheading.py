from threading import Thread
import urllib2
from BeautifulSoup import BeautifulSoup
encoding="utf-8"
# coding=utf-8
threads = [None] * 4
results = [None] * 4
def read_from_URL(url,results,i):
    """
    Function that takes URL and Retrieve
    Data from that Url Using Threads
    """
    print url[i]
    response = urllib2.urlopen(url[i])
    page_source=response.read()
    results[i]=page_source
url=["https://www.reddit.com/r/programming/","https://news.ycombinator.com/","https://www.theguardian.com/us/technology","https://www.nytimes.com/section/technology"]
# Create threads to read pages from different Url at same time
for i in range(len(threads)):
    threads[i] = Thread(target=read_from_URL, args=(url, results, i))
    threads[i].start()

# Join Threads
for i in range(len(threads)):
    threads[i].join()
#
keywords=[]
print "Enter Keyword to Make search Of Story Heading such as Uber"
keyword=raw_input()
keywords.append(keyword)
while True:
    print "Press 1 to add more Keyword"
    print "Press 2 to make Search"
    read_input=raw_input()
    if(read_input=="1"):
        print "Enter Keyword"
        keyword=raw_input()
        keywords.append(keyword)
    elif(read_input=="2"):
        break;
    else:
        print "Enter valid Value"
        continue
soup = BeautifulSoup(''.join(results[3]))# coding=utf-8

matches = soup.findAll('h2',{ "class" : "headline" })
for ele in matches:
    not_required=False
    for keyword in keywords:
        if(keyword not in ele.text):
            not_required=True
        if not(not_required):
            print ele.text.encode('utf-8')
