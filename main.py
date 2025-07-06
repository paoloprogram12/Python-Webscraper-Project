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

recipes = {}

# anchor tag that matches this particular class
anchor_list = soup.find_all("a", attrs={"class": "inline-block mt-4 px-4 py-2 bg-[#d32f2f] text-white rounded-lg hover:bg-[#b71c1c] transition-colors duration-300"})
for anchor in anchor_list:
    res = requests.get(URL_ENDPOINT+anchor["href"])
    soup = BeautifulSoup(res.text)

    recipe_title = soup.h1.text # grabs the name of each recipe
    
    # grabs the image
    recipe_img = soup.img["src"]
    
    # ingredients 
    ing_header = soup.find("h2", attr={"class": "text-3x1 font-bold text-[#4e342e] mb-6 flex items-center"})
    ingredients = ing_header.next_sibling.find_all("span", attrs={"class": "text-[#4e342e] font-medium"})

    recipe_ingredients = []
    for ingredient in ingredients:
        # print(ingredient.text)
        recipe_ingredients.append(ingredient.text)

    recipes[anchor["href"]] = {
        "name": recipe_title,
        "img": recipe_img,
        "ingredients": recipe_ingredients
    }