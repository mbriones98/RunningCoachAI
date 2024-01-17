import pymongo
import json

mongoClient = pymongo.MongoClient('mongodb://127.0.0.1:27017')

athleteDb = mongoClient["Athlete"]
activityCol = athleteDb["Activities"]

with open('testData/activities_1_16_24.json', 'r') as activitiesFile:
    activities = json.load(activitiesFile)

x = activityCol.insert_many(activities)
print(x.inserted_ids)