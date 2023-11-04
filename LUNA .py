#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import wikipediaapi
import datetime

# Create a Wikipedia object with a custom user agent
wiki_wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="YourUserAgent/1.0"
)

# Get the current time of day
def get_time_of_day():
    current_time = datetime.datetime.now()
    current_hour = current_time.hour
    if 5 <= current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 17:
        return "afternoon"
    elif 17 <= current_hour < 20:
        return "evening"
    else:
        return "night"

# Function to handle greetings from the user
def handle_greetings(user_response):
    greetings = ["hello", "hi", "hey", "how are you", "whats up","sup"]
    
    if any(greeting in user_response.lower() for greeting in greetings):
        time_of_day = get_time_of_day()
        return f"Good {time_of_day}! I am Luna. How can I assist you today?"

# Function to search Wikipedia and provide a link to the top search result
def search_wikipedia(user_input):
    page = wiki_wiki.page(user_input)
    if page.exists():
        return f"Here's the Wikipedia link: {page.fullurl}"
    else:
        return "I couldn't find a Wikipedia page related to that topic. Can I assist you with something else?"

# Simple chatbot that provides greetings and Wikipedia links based on user input
def chatbot_response(user_input):
    greeting_response = handle_greetings(user_input)
    if greeting_response:
        return greeting_response

    if "morning" in user_input.lower():
        return "Good morning! What can I help you with today?"

    if "how are you" in user_input.lower():
        return "I'm just a computer program, but I'm here to assist you."

    if "what's your name" in user_input.lower():
        return "I'm just a chatbot, so I don't have a name."

    if "bye" in user_input.lower():
        return "Goodbye! Have a great day."

    return search_wikipedia(user_input)

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Luna: Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Luna:", response)

