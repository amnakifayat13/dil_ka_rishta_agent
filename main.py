import chainlit as cl
from connection import config
from data import UserData , partners_context, AllPartners
from agents import Agent, Runner, function_tool , RunContextWrapper
import requests



# async def partner_info(ctx: RunContextWrapper[AllPartners], age):
#     for partner in ctx.context.partners:
#         if partner.age >= age:
#             return partner.info
        
#     return "no partner found"
async def api_fetching(query):
    url = f"https://user-api-agent.vercel.app/api/user?search={query}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch products"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {e}"}

       
# async def whatsapp(num:int, name:str, partner, query):
#     url = f"https://api.ultramsg.com/instance132904/messages/chat"
#     payload = f"token=l28sbrrb61be7myr&to={num}&body=Hi {name}, your matching partner is {partner}"
#     payload = payload.encode('utf8').decode('iso-8859-1')
#     headers = {'content-type': 'application/x-www-form-urlencoded'}
#     response = requests.request("POST", url, data=payload, headers=headers)
#     return response.text
      
@function_tool
async def rishta(ctx: RunContextWrapper[AllPartners], num: str, name: str, age: int, query):

    # matched_user = ctx.context.partners  
   
    # return await whatsapp(num, name, matched_user)
    return await api_fetching(query)


# Agent definition
agent = Agent[AllPartners](
    name="Dil ka rishta",
    instructions="""
    You are Dil Ka Rishta Assistant, a helpful matchmaking agent.

If the user asks to find, search, or look for a partner, immediately call the tool rishta.

Use the user's age and gender to search for the most suitable match.

Always match the user with a partner of the opposite gender.

Among all potential matches, return the one with the closest age to the user from the available data.

Do not answer directly — always call the tool rishta to perform the match.

Be brief, warm, and respectful in your responses.

Never suggest more than one match at a time.

    
    """,
    tools=[rishta]
    
)
# Chainlit hook
@cl.on_message
async def handle_message(msg: cl.Message):
    result = await Runner.run(agent, msg.content, run_config=config , context=partners_context )
    await cl.Message(content=result.final_output).send()
