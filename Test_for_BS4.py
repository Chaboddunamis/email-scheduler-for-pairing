from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://henryuwakwe.com"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())