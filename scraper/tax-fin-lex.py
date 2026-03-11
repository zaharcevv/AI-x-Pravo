import requests
import json
import time
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO-DB-URI"))
db = client["AIxPravo"]
collection = db["laws"]
try:
    client.admin.command("ping")
    print("MongoDB connected")
except Exception as e:
    print(f"Connection failed: {e}")

client = get_client()

page = 1
pageSize = 4
BASE = "https://www.tax-fin-lex.si/api/v1/"
leg_endpoint = f"legislation?page={page}&pageSize={pageSize}&type=zakon&status=veljaven"
art_endpoint = "legislation/{id}"

rate_lim = 10


headers = {
    "User-Agent": "Mozilla/5.0",
    "accept": "application/json",
    "X-Api-Key": os.getenv("TAX-FIN-LEX-API")
}

resp = requests.get(BASE+leg_endpoint, headers=headers)
data = resp.json()
#print(data)

items = data["data"]["items"]


for item in items:

    id = item["id"]

    if collection.find_one({"id": id}):
        print(f"Skipping {id}, already in db")
        continue

    print("sending get")
    resp = requests.get(BASE+art_endpoint.format(id=id), headers=headers)
    data = resp.json()
    try:
        data = data["data"]

        title = data["title"]
        date = item["validFrom"]
        url = item["url"]

        if "RS" in item["documentMark"]:
            locality = "RS"
        else:
            locality = "EU"


        articles = data["articles"]

        text = ""

        for article in articles:
            text += article["html"]
    except:
        print(data)


    print(date)
    date = datetime.fromisoformat(date)

    print(id)

    print(title)

    print(date)

    print(locality)

    print(url)

    #print(text)

    ## llm + DB insert
    response = summarize_html_content(text, client)
    res_js = json.loads(response)
    summary = res_js["summary"]
    area = res_js["leagal_area"]

    collection.insert_one({
        "id": id, 
        "title": title,
        "date": date,
        "area": area,
        "locality": locality,
        "url": url,
        "summary": summary,
    })


    time.sleep(60 / rate_lim)


