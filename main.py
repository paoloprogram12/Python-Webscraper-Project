import requests
from bs4 import BeautifulSoup 

URL_ENDPOINT = "https://pizza-site-six.vercel.app"

res = requests.get(URL_ENDPOINT+"/recipes") # pulls all data from this website
# print(res) # <Response [200]> means that its a successful http request

# creates a html file of all the data from website
# with open("test.html", 'w', encoding="utf-8") as file:
#     file.write(res.text)

# fed all the res.text into the soup variable
soup = BeautifulSoup(res.text)

# anchor tag that matches this particular class
anchor_list = soup.find_all("a", attrs={"class": "inline-block mt-4 px-4 py-2 bg-[#d32f2f] text-white rounded-lg hover:bg-[#b71c1c] transition-colors duration-300"})
for anchor in anchor_list:
    print(anchor["href"])

