import chainlit as cl
from connection import config
from agents import Agent, Runner, function_tool 
import requests


async def api_fetching(query):
    url = f"https://user-api-agent.vercel.app/api/user?search={query}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # convert_string = response.
            return response.json()
        else:
            return {"error": "Failed to fetch products"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {e}"}
    
@function_tool
async def rishta(query):
    return await api_fetching(query)

@function_tool       
async def whatsapp(num:int, name:str, partner):
    url = f"https://api.ultramsg.com/instance132904/messages/chat"
    payload = f"token=l28sbrrb61be7myr&to={num}&body={partner}"
    # payload = payload.encode('utf8').decode('iso-8859-1')
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text
      



# Agent definition
agent = Agent(
    name="Dil ka rishta",
    instructions="""
                    You are Dil Ka Rishta Assistant, a helpful and engaging matchmaking agent.

                    🔹 Your goal is to help users find a life partner in a friendly and respectful way.

                    🔹 When the user asks to find, search, or look for a partner, you MUST immediately call the `rishta` tool — do not answer directly.

                    🔹 Use the user's age and gender to search for the most suitable match. Only match users with a partner of the **opposite gender**.

                    🔹 Always return only ONE matching partner — the one whose age is **closest** to the user's.

                    🔹 You MUST never return the same partner more than once in a row to the same user. If a partner was shown before, exclude them from the next result. Always give fresh results. This is CRITICAL to keep the experience exciting and avoid repetition.

                    🔹 When a matching partner is found and you call the `whatsapp` tool to send details, the partner details MUST be passed as a single, fully formatted, human-readable string — NOT as a JSON object or dictionary.

                    🔹 The message MUST exactly follow this structure (with emojis and line breaks):

                    Assalam o Alaikum [UserName]! 😊  
                    Here is your matching partner:  
                    👤 Name: [PartnerName]  
                    🎓 Qualification: [Qualification]  
                    ❤️ Age: [Age]  
                    🕌 Religion: [Religion]  
                    💼 Passion: [Profession]  

                    Would you like to know more about your partner? 💌  

                    🔹 Never include extra fields or remove any part of this message format.

                    🔹 Be respectful, warm, and brief. Your tone should always be friendly and engaging.

                    🔹 Do not show more than one partner at a time.

                    🔹 Most importantly, ensure variety — show different partners each time. Repeating the same suggestion will make the experience boring, and that must be avoided at all costs.


    """,
    tools=[rishta,whatsapp]
    
)
# Chainlit hook
@cl.on_message
async def handle_message(msg: cl.Message):
    result = await Runner.run(agent, msg.content, run_config=config )
    await cl.Message(content=result.final_output).send()