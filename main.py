from fastapi import FastAPI
import requests
import random

app = FastAPI()


# Homepage. Directs you to '/facts' page or '/breeds' page, where either you get a cat fact pulled from the
# catfact.ninja 'facts' get request, or a breed from the 'breeds' get request"
# https://catfact.ninja/#/
@app.get("/")
async def root():
    return "Random fact (from a list) generated at '/facts'. Random breed generated at '/breeds'."


# Returns a random cat fact from a list of facts (default length of 10 facts)
@app.get("/facts")
async def root():
    # URL to send an HTTP get request to
    resp = requests.get("https://catfact.ninja/facts").json()

    # response, after .json conversion, is a dictionary containing data of interest under key "data", and facts in their own dictionary under key "fact"
    facts = resp["data"]
    fact = random.choice(facts)["fact"]

    return fact


# Returns a cat breed from a list dictionaries featuring breeds and other information
@app.get("/breeds")
async def root():
    # URL to send an HTTP get request to
    resp = requests.get("https://catfact.ninja/breeds").json()

    # response, after .json conversion, is a dictionary containing data of interest under key "data", and breeds in their own dictionary under key "breed"
    cat_info = resp["data"]
    breed = random.choice(cat_info)["breed"]

    return breed
