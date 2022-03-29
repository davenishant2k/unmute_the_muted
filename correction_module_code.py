from requests import get
from bs4 import BeautifulSoup
import requests

def run_this(query_value):

    query = query_value
    query = '+'.join(query.split())

    url = "https://www.google.com/search?q="+query+"&rlz=1C1CHBF_enIN872IN872&oq=there&aqs=chrome.0.69i59l2j69i57j0i67j0i433j46i67i433j69i60l2.1874j0j1&sourceid=chrome&ie=UTF-8"

    response = get(url)
    # print(response.text[:500])
    
    html_soup = BeautifulSoup(response.text, 'html.parser')
    final_value = html_soup.find(class_= "MUxGbd v0nnCb lyLwlc")
    if final_value is None:
        return "Your Text is correct, which is: "+query_value
    print(type(final_value))
    return "Your Text's corrected output is:"+final_value.a.text