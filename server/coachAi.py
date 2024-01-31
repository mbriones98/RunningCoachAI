from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

llm = Ollama(model="llama2")

def activityFeedback(runningData):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a world class running coach. \
         You MUST keep responses to no more than five sentences. \
         Speak in a friendly, supportive tone. \
         Mention specific metrics that the user can improve on. \
         Also mention specific metrics that the user is doing well on. \
         Do NOT mention that you are a running coach."),

        ("user", "I recently did this activity based on the following JSON activity data: {activityData}\n \
         Please give me feedback.")
    ])

    chain = prompt | llm

    feedback = chain.invoke({
        "activityData": runningData
    })
    
    return feedback