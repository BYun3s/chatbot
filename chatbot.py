from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# Create a new instance of ChatBot
chatbot = ChatBot('MyChatBot')
# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Train the chatbot with custom data
custom_training_data = [
"What's your name?",
"My name is MyChatBot.",
"How are you?",
"I'm doing well, thank you!",
"Can you tell me a joke?",
"Sure! Why couldn't the bicycle stand up by itself? It was two-tired!",
"Tell me about yourself.",
"I am a chatbot created using ChatterBot."
]
# Train the chatbot with custom data
trainer.train(custom_training_data)
# Example interaction
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("Bot:", response)
    if user_input == "bye":
        break
