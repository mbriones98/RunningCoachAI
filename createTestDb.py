import asyncio
import pymongo
import json
from util import decodeMongoDBResponse
import model

mongoClient = pymongo.MongoClient('mongodb://127.0.0.1:27017')

athleteDb = mongoClient["Athlete"]
activityCol = athleteDb["Activities"]

def main():
    with open('testData/activities_1_16_24.json', 'r') as activitiesFile:
        activities = json.load(activitiesFile)

    # iterate through list of activities and only keep fields according to model.py
    for activity in activities:
        unwantedFields = set(activity.keys()) - model.keepActivityFields

        # remove unwanted fields
        for unwantedField in unwantedFields:
            del activity[unwantedField]

    activityCol.delete_many({})
    x = activityCol.insert_many(activities)
    print(x.inserted_ids)

main()
print(decodeMongoDBResponse(activityCol.find()))
