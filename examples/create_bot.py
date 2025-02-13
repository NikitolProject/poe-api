import poe
import logging
import sys

# Create a bot and edit its model
poe.logger.setLevel(logging.INFO)
token = sys.argv[1]
client = poe.Client(token)

print(client.bots)
bot_name = input("bot handle name: ")
display_name = input("bot display name: ")
prompt = input("bot prompt: ")
new_bot = client.create_bot(
    bot_name, 
    prompt,
    display_name=display_name,
    base_model="a2"
)
print("new bot created: " + bot_name)

handle = bot_name.lower()
bot_id = client.bots[handle]["defaultBotObject"]["botId"]
edit_result = client.edit_bot(
    bot_id, handle, prompt, 
    base_model="chinchilla", api_key="9c3bUbFXqbGO8atB2CotccmX1oT4mdcc"
) # Switch model to ChatGPT

print("edit status: " + edit_result["status"])

