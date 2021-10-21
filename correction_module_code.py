from requests import get
from bs4 import BeautifulSoup
import requests

def run_this(query_value):

    query = query_value
    query = '+'.join(query.split())
    print("corrected text:")
    url = "https://www.google.com/search?q="+query+"&rlz=1C1CHBF_enIN872IN872&oq=there&aqs=chrome.0.69i59l2j69i57j0i67j0i433j46i67i433j69i60l2.1874j0j1&sourceid=chrome&ie=UTF-8"

    response = get(url)
    # print(response.text[:500])

    html_soup = BeautifulSoup(response.text, 'html.parser')
    final_value = html_soup.find(class_= "MUxGbd v0nnCb lyLwlc").a.text
    # print(final_value)
    return final_value