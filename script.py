import requests
from bs4 import BeautifulSoup
import  pandas as pd

req = requests.get('https://test-scrape-site.onrender.com/people.html')
soup = BeautifulSoup(req.text, 'html.parser')

people = soup.select("ul#people-list li")

structured_data = []

for person in people:
    text = person.getText(separator=" ", strip=True)
    lines = text.split(" ")

    name = person.strong.text
    job = lines[2]
    age = text.split("Age: ")[1].split(" ")[0]
    city = text.split("City: ")[1].split(" ")[0]
    interests = text.split("Interests: ")[1]

    structured_data.append({
        "name": name,
        "job": job,
        "age": age,
        "city": city,
        "interests": interests
    })
df = pd.DataFrame(structured_data)
df.to_excel("people.xlsx", index=False)









