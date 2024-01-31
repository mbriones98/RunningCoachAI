import util

mongoClientURL = 'mongodb://127.0.0.1:27017/'

def main():
    activityCol = util.initializeMongoDB(mongoClientURL, "Athlete", "Athlete")
    util.resetMongoDBCollection(activityCol)

main()