import tkinter as tk
from tkinter import ttk
import random

# Define predefined responses for different user queries
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a chatbot, but I'm here to help.",
    "bye": "Goodbye! Have a great day.",
    "name": "I'm a chatbot. You can call me ChatBot.",
    "age": "I don't have an age. I'm just a program.",
    "help": "Sure, I can help you with general information. What do you want to know?",
    "who created you": "I was created by a team of developers at OpenAI using advanced natural language processing techniques.",
    "what can you do": "I can answer questions, provide information, and have conversations on a wide range of topics.",
    "how do you work": "I work by analyzing text inputs and generating responses using machine learning algorithms.",
    "joke": "Sure, here's one: Why did the scarecrow win an award? Because he was outstanding in his field!",
    "fun fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    "favorite color": "I don't have preferences, but I like all colors equally!",
    "live": "I exist in the digital world, so I don't have a physical location.",
    "life": "The meaning of life is a philosophical question that has many different answers depending on one's beliefs and perspective.",
    "independence": "The United States Declaration of Independence was adopted on July 4, 1776, and most of the delegates signed it on that date.",
    "world war II": "World War II ended on September 2, 1945, with the formal surrender of Japan.",
    "mona Lisa": "The Mona Lisa was painted by the Italian artist Leonardo da Vinci in the early 16th century.",
    "first moon landing": "The first moon landing occurred on July 20, 1969, when NASA's Apollo 11 mission successfully landed astronauts Neil Armstrong and Buzz Aldrin on the moon.",
    "largest recorded earthquake": "The largest recorded earthquake was the 1960 Valdivia earthquake in Chile, with a magnitude of 9.5.",
    "penicillin": "Penicillin, the first antibiotic, was discovered by Scottish bacteriologist Alexander Fleming in 1928.",
    "Hubble Space Telescope launched": "The Hubble Space Telescope was launched on April 24, 1990, aboard the Space Shuttle Discovery.",
    "Chernobyl disaster": "The Chernobyl nuclear disaster occurred on April 26, 1986, in Ukraine, and is considered one of the worst nuclear accidents in history.",
    "titanic disaster": "The Titanic disaster happened on April 15, 1912, when the RMS Titanic, a British passenger liner, struck an iceberg and sank during its maiden voyage. It was one of the deadliest peacetime maritime disasters in history, with the loss of more than 1,500 lives.",
    "bomb": "Hiroshima and Nagasaki were bombed by the United States during World War II. The atomic bomb 'Little Boy' was dropped on Hiroshima on August 6, 1945, and 'Fat Man' was dropped on Nagasaki on August 9, 1945.",
    "sea": "The biggest sea disaster in recorded history occurred during World War II when the German passenger ship Wilhelm Gustloff was torpedoed by a Soviet submarine on January 30, 1945. The ship was overcrowded with German civilians, military personnel, and refugees, resulting in the loss of an estimated 9,000 lives.",
    "cricket": "Certainly! Let me tell you about Sachin Tendulkar, one of the greatest cricketers of all time. Sachin Tendulkar, also known as the 'Little Master' or 'Master Blaster,' is an Indian former international cricketer. He is considered one of the greatest batsmen in the history of cricket. Tendulkar's career spanned 24 years, during which he scored a record 100 international centuries and is the highest run-scorer in both Test and One Day International (ODI) cricket. He retired in 2013 and remains an iconic figure in the world of cricket.",
    "powerful": "The concept of a 'powerful' country can vary depending on different criteria such as military strength, economic influence, political stability, and more. Currently, countries like the United States, China, Russia, and several European nations are often considered powerful due to their significant global influence in various aspects.",
    "topmost company": "Determining the 'topmost' company can depend on various factors like market capitalization, revenue, and industry. Some of the world's largest and most influential companies include Amazon, Apple, Google's parent company Alphabet, Microsoft, and others. These companies are leaders in technology and have a significant global presence.",
    "india": "India is a diverse and culturally rich country located in South Asia. It is known for its rich history, diverse languages, traditions, and stunning landscapes. India is the world's second-most populous country and has a democratic system of government. It is famous for its landmarks like the Taj Mahal, a UNESCO World Heritage site, and the Himalayan mountain range. India is also known for its contributions to art, science, and spirituality, with yoga and meditation originating from the region. It has a diverse cuisine with a wide variety of delicious dishes. India's economy is one of the fastest-growing in the world, and it plays a significant role in global affairs.",
    "south pole": "India made history by becoming the first country to successfully land on the Moon's South Pole. This achievement was accomplished by India's Vikram spacecraft as part of the Chandrayaan-3 mission. The soft landing on the Moon's South Pole was a significant milestone in India's space exploration endeavors and a moment of pride for the country.",
    "default": "I'm sorry, I didn't understand your question. Please ask again.",
    "tell me a fact": "Sure, here's a fun fact: Honey never spoils! Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
    "favorite book": "I don't have personal preferences, but one of the most famous books of all time is 'To Kill a Mockingbird' by Harper Lee. It's a classic novel that explores themes of racism and injustice in the American South.",
    "tell me a joke": "Of course! Here's a joke for you: Why don't scientists trust atoms? Because they make up everything!",
}

# Update the responses dictionary with additional responses as needed.


# Function to get a response from the chatbot
def get_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if the user input matches any predefined responses
    for key, value in responses.items():
        if key in user_input:
            return value

    # If no matching response is found, return a default response
    return "I'm sorry, I didn't understand your question."

# Function to handle user input and display responses
def chat():
    user_input = user_entry.get()
    response = get_response(user_input)
    chat_history.config(state='normal')
    chat_history.insert(tk.END, f"\nYou: {user_input}\n", 'user')
    chat_history.insert(tk.END, f"\nChatBot: {response}\n", 'bot')
    chat_history.config(state='disabled')
    user_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("ChatBot")

# Create and configure chat history display (with scrolling)
chat_history_frame = ttk.Frame(root)
chat_history_frame.grid(column=0, row=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

chat_history = tk.Text(
    chat_history_frame,
    wrap=tk.WORD,
    state='disabled',
    bg="#ecf0f1",  # Background color
    fg="#333333",  # Text color
    font=("Arial", 12),
)
chat_history.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

chat_scrollbar = ttk.Scrollbar(chat_history_frame, orient=tk.VERTICAL, command=chat_history.yview)
chat_scrollbar.grid(column=1, row=0, sticky=(tk.N, tk.S))
chat_history['yscrollcommand'] = chat_scrollbar.set

# Create user input field and button
user_entry = ttk.Entry(
    root,
    width=40,
    font=("Arial", 12),
)
user_entry.grid(column=0, row=1, padx=10, pady=10, sticky=(tk.W, tk.E))

send_button = ttk.Button(
    root,
    text="Send",
    command=chat,
    style="Accent.TButton",  # Custom button style
)
send_button.grid(column=0, row=2, padx=10, pady=10, sticky=(tk.W, tk.E))

# Define custom button style
# Define custom button style with smaller size
style = ttk.Style()
style.configure(
    "Small.TButton",           # New custom button style name
    foreground="white",       # Text color
    background="#3498db",     # Button color (blue)
    font=("Arial", 10),       # Smaller font size
    padding=(5, 2),           # Smaller padding (horizontal, vertical)
)

# Create the "Send" button with the custom style
# Create the "Send" button with a smaller width
send_button = ttk.Button(
    root,
    text="Send",
    command=chat,
    style="Accent.TButton",  # Use the custom button style
    width=5,                # Set the width to a smaller value
)
send_button.grid(column=0, row=2, padx=10, pady=10, sticky=(tk.W, tk.E))


# Update the colors for a more attractive GUI
root.configure(bg="#34495e")  # Background color of the main window

# Start the GUI main loop
root.mainloop()
