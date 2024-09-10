# import chat_flow
from chat_flow import ChatFlow

# create a chat flow object
chat_flow = ChatFlow()
def gen_idea_loop():
    while True:
        # generate an idea
        idea = chat_flow.chat("generate an idea for a product that solves the problem of people who are too busy to cook")
        print(idea)
        idea_check = chat_flow.chat(f"check if the idea is feasible and if it is reply with 'STOP'")
        print(idea_check)
        if idea_check == "stop":
            break
gen_idea_loop()
