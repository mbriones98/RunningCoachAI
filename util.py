import json
import pymongo
from bson import json_util

def initializeMongoDB(mongoClientURL: str, database: str, collection: str):
    mongoClient = pymongo.MongoClient(mongoClientURL)
    athleteDb = mongoClient[database]
    activityCol = athleteDb[collection]

    return activityCol

def decodeMongoDBResponse(dbResponse):
    return json.loads(json_util.dumps(dbResponse))

def speedToPace(metersPerSecond: float):
    if metersPerSecond == 0:
        return 0
    else:
        return 26.8224 / metersPerSecond
    
def metersToMiles(meters: float):
    return meters * 0.000621371