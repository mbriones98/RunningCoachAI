import json
import pymongo
from bson import json_util
from model import Activity, keepActivityFields

# create a mongoDB client and return collection based on 'collection' param
def initializeMongoDB(mongoClientURL: str, database: str, collection: str):
    mongoClient = pymongo.MongoClient(mongoClientURL)
    athleteDb = mongoClient[database]
    activityCol = athleteDb[collection]

    return activityCol

# decode mongoDB query response via bson library to json/python dict
def decodeMongoDBResponse(dbResponse):
    return json.loads(json_util.dumps(dbResponse))

# clean activity data to only include fields we want
def cleanActivity(activity: Activity):
    unwantedFields = set(activity.keys()) - keepActivityFields

    # remove unwanted fields
    for unwantedField in unwantedFields:
        del activity[unwantedField]

    return activity

# insert data into mongoDB
# TODO: data validation
def insertIntoMongoDB(data: any, activityCol):
    x = activityCol.insert_one(data)
    return x.inserted_id is not None

def printMongoDBCollection(activityCol):
    for activity in activityCol.find():
        print(activity)

# check if athlete exists in mongoDB
def doesAthleteExist(athleteId: int, athleteCol):
    return athleteCol.count_documents(filter={ 'athlete_id': athleteId })
    
# reset mongoDB collection
# NOTE: DELETE ON DEPLOYMENT
def resetMongoDBCollection(activityCol):
    activityCol.delete_many({})

def speedToPace(metersPerSecond: float):
    if metersPerSecond == 0:
        return 0
    else:
        return 26.8224 / metersPerSecond
    
def metersToMiles(meters: float):
    return meters * 0.000621371