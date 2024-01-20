import json
from bson import json_util
import random
import string
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from urllib.parse import urlencode
import requests
import pymongo
from model import WebhookEvent
import util
import coachAi

app = FastAPI()

# TODO: make these two into env vars
client_id = "119636"
client_secret = "e2c415a4bee48f4138df1576720d7c77184b4a93"

rootURL = "http://127.0.0.1:8000/"

mongoClientURL = 'mongodb://127.0.0.1:27017/'

def getRandomStateString():
    return random.choices(string.ascii_lowercase, k=16)

app.mount("/dashboard", StaticFiles(directory="dashboard"), name="dashboard")

@app.get('/', response_class=RedirectResponse)
async def root():
    redirect_uri = f"{rootURL}exchange_token"
    scope = 'activity:read'

    return RedirectResponse('https://www.strava.com/oauth/authorize?' + urlencode({
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": scope,
        "approval_prompt": "force"
    }))

@app.get('/exchange_token')
async def exchange_token(code: str):
    exchangeArgs = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "grant_type": "authorization_code"
    }

    tokenResponse = requests.post(url="https://www.strava.com/oauth/token", json=exchangeArgs)

    try:
        auth = tokenResponse.json()
        response = {
            "refreshToken": auth["refresh_token"],
            "accessToken": auth["access_token"],
            "expiresAt": auth["expires_at"],
            "athleteId": auth["athlete"]["id"]
        }
    except:
        raise HTTPException(status_code=500, detail="Authorization failed.")

    return response

@app.get('/four_week_activities_stats')
async def four_week_activities_stats(athlete_id: int):
    activityCol = util.initializeMongoDB(mongoClientURL, "Athlete", "Activities")

    # query for activities within the last four weeks
    # not sure if this query works yet
    dbResponse = activityCol.find({
        'athlete.id': athlete_id,
        'start_date': {
            '$dateSubtract': { 
                'startDate': "$$NOW",
                'unit': "week", 
                'amount': 4
            }
        }
    }, { 'id': 1 } )

    jsonResponse = util.decodeMongoDBResponse(dbResponse)

    return jsonResponse

@app.get('/most_recent_activity')
async def most_recent_activity(athlete_id: int):
    activityCol = util.initializeMongoDB(mongoClientURL, "Athlete", "Activities")
    
    # query for activity with most recent start date
    dbResponse = activityCol.find({
        'athlete.id': athlete_id
    }, {
        'id': 1
    }
    ) \
        .sort('start_date', pymongo.DESCENDING) \
        .limit(1)

    jsonResponse = util.decodeMongoDBResponse(dbResponse)
    return {"activity_id": jsonResponse[0]["id"]}

@app.get('/athlete_stats')
async def athlete_stats(athlete_id: int, request: Request):
    statEndpoint = f"https://www.strava.com/api/v3/athletes/{athlete_id}/stats"

    authHeader = request.headers["Authorization"]
    if not authHeader:
        raise HTTPException(status_code=401, detail="Authorization header not found.")
    
    athleteCol = util.initializeMongoDB(mongoClientURL, "Athlete", "Athlete")

    if not util.doesAthleteExist(athlete_id, athleteCol):
        accessToken = authHeader.split(" ")[1]

        # TODO: clean this response data up
        athleteStats = requests.get(url=statEndpoint, headers={
            "Authorization": f"Bearer {accessToken}"
        })
        athleteStatsJson = dict(athleteStats.json())
        athleteStatsJson["athlete_id"] = athlete_id

        insertStatus = util.insertIntoMongoDB(athleteStatsJson, athleteCol)

        # util.printMongoDBCollection(athleteCol)
        if not insertStatus:
            raise HTTPException(status_code=500, detail="Failed to insert athlete stats into database.")
    
    dbResponse = athleteCol.find_one({
        'athlete_id': athlete_id
    })

    return util.decodeMongoDBResponse(dbResponse)

@app.get('/activity_feedback')
async def activity_feedback(activity_id: int):
    activityCol = util.initializeMongoDB(mongoClientURL, "Athlete", "Activities")

    # query for activity based on activity_id
    activityData = activityCol.find_one({
        'id': activity_id
    })

    # raise 404 if not found
    if activityData is None:
        raise HTTPException(status_code=404, detail="Activity not found.")
    
    feedback = coachAi.activityFeedback(activityData)

    return {"feedback": feedback}

@app.post('/webhook')
async def webhook(event: WebhookEvent):
    # check the type of strava webhook event
    # if it's a 'create' event:
        # clean activity data
        # store activity data
        # update athlete stats
        # run activity feedback
    print("Webhook event received")
    print(event)
    return