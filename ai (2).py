import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk  # PIL library for handling images

# Print current working directory
print(f"Current Working Directory: {os.getcwd()}")

# List contents of mock_images directory
if os.path.exists('mock_images'):
    print(f"Contents of 'mock_images': {os.listdir('mock_images')}")
else:
    print("'mock_images' directory does not exist")

# Sample data: user features based on browsing history and their shopping preferences
data = {
    'Age': [25, 45, 35, 50, 23, 40, 33, 38, 48, 21, 30, 27, 31, 29, 24, 55, 44, 28, 37, 41],
    'Clothing_Browsing_Hours': [15, 5, 10, 4, 14, 6, 12, 11, 3, 16, 9, 13, 7, 8, 15, 2, 5, 10, 6, 4],
    'Electronics_Browsing_Hours': [5, 15, 6, 16, 4, 14, 8, 9, 17, 3, 7, 11, 5, 10, 6, 18, 12, 4, 8, 14],
    'Clothing_Purchases': [4, 1, 3, 0, 4, 2, 3, 4, 1, 5, 3, 4, 2, 3, 4, 0, 1, 3, 2, 1],
    'Electronics_Purchases': [1, 4, 2, 5, 0, 3, 1, 2, 5, 0, 2, 3, 1, 2, 1, 6, 4, 1, 3, 4],
    'Preference': ['Clothing', 'Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics', 'Clothing', 'Clothing', 'Electronics', 'Clothing', 'Clothing', 'Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics']
}

df = pd.DataFrame(data)
# Encode the target variable
df['Preference'] = df['Preference'].map({'Clothing': 0, 'Electronics': 1})

# Split the data into features (X) and target (y)
X = df[['Clothing_Browsing_Hours', 'Electronics_Browsing_Hours', 'Clothing_Purchases', 'Electronics_Purchases']]
y = df['Preference']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Gaussian Naive Bayes model
model = GaussianNB()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Classification Report:')
print(report)

# Predefined available items
# Corrected image paths with double backslashes or raw strings
clothing_items = [
    {"name": "T-shirt", "cost": "$20", "image": r"D:\VSPYTHON.python\project\mock_images\tshirt.jpg"},
    {"name": "Jeans", "cost": "$50", "image": r"D:\VSPYTHON.python\project\mock_images\jeans.jpg"},
    {"name": "Jacket", "cost": "$80", "image": r"D:\VSPYTHON.python\project\mock_images\jacket.jpg"},
    {"name": "Sweater", "cost": "$30", "image": r"D:\VSPYTHON.python\project\mock_images\sweater.jpg"},
    {"name": "Dress", "cost": "$60", "image": r"D:\VSPYTHON.python\project\mock_images\dress.jpg"}
]

electronics_items = [
    {"name": "Smartphone", "cost": "$600", "image": r"D:\VSPYTHON.python\project\mock_images\smartphone.jpg"},
    {"name": "Laptop", "cost": "$1200", "image": r"D:\VSPYTHON.python\project\mock_images\laptop.jpg"},
    {"name": "Headphones", "cost": "$150", "image": r"D:\VSPYTHON.python\project\mock_images\headphones.jpg"},
    {"name": "Smartwatch", "cost": "$300", "image": r"D:\VSPYTHON.python\project\mock_images\smartwatch.jpg"},
    {"name": "Camera", "cost": "$800", "image": r"D:\VSPYTHON.python\project\mock_images\camera.jpg"}
]

# Store unrecognized questions
unrecognized_questions = []

def open_chat_window():
    chat_window = tk.Toplevel(root)
    chat_window.title("AI-Powered Virtual Personal Shopping Assistant")
    
    chat_display = scrolledtext.ScrolledText(chat_window, wrap=tk.WORD, width=50, height=20)
    chat_display.pack(pady=10)
    
    user_entry = tk.Entry(chat_window, width=40)
    user_entry.pack(pady=5)
    
    def send_message():
        user_input = user_entry.get().strip().lower()
        chat_display.insert(tk.END, "You: " + user_input + "\n")
        user_entry.delete(0, tk.END)
        
        if user_input in ["hi", "hello"]:
            chat_display.insert(tk.END, "Bot: Hi! How can I assist you today?\n")
        elif user_input in ["i need help"]:
            chat_display.insert(tk.END, "Bot: I can only help you with the problems related to clothing and electronics\n")
        elif user_input in ["i need clothing", "show me clothing", "recommend clothing","clothing"]:
            chat_display.insert(tk.END, "Bot: Here are the available clothing items:\n")
            for item in clothing_items:
                item_button = tk.Button(chat_window, text=item["name"], command=lambda i=item: show_item_details(chat_display, i))
                chat_display.window_create(tk.END, window=item_button)
                chat_display.insert(tk.END, "\n")
        elif user_input in ["electronics","i need electronics", "show me electronics", "recommend electronics"]:
            chat_display.insert(tk.END, "Bot: Here are the available electronics items:\n")
            for item in electronics_items:
                item_button = tk.Button(chat_window, text=item["name"], command=lambda i=item: show_item_details(chat_display, i))
                chat_display.window_create(tk.END, window=item_button)
                chat_display.insert(tk.END, "\n")
        elif user_input in ["what can you do?", "how can you help me?"]:
            chat_display.insert(tk.END, "Bot: I can help you find clothing and electronics. Just ask for recommendations or browse the items you're interested in!\n")
        elif user_input in ["thank you", "thanks"]:
            chat_display.insert(tk.END, "Bot: You're welcome! If you have any more questions, feel free to ask.\n")
        elif user_input in ["goodbye", "bye"]:
            chat_display.insert(tk.END, "Bot: Goodbye! Have a great day!\n")
        else:
            unrecognized_questions.append(user_input)
            chat_display.insert(tk.END, f"Bot: I'm not sure how to respond to '{user_input}'. Please try asking for 'clothing' or 'electronics' recommendations.\n")
            
            # Log unrecognized question to file
            with open('unrecognized_questions.txt', 'a') as f:
                f.write(f"{user_input}\n")

    send_button = tk.Button(chat_window, text="Send", command=send_message)
    send_button.pack()
    
def show_item_details(chat_display, item):
    # Clear previous item details
    chat_display.delete('1.0', tk.END)
    
    # Display item details
    chat_display.insert(tk.END, f"Bot: You clicked on {item['name']}.\n")
    chat_display.insert(tk.END, f"Cost: {item['cost']}\n")
    
    # Load and display image
    image_path = item['image']
    print(f"Loading image from: {image_path}")  # Debugging statement
    try:
        img = Image.open(image_path)
        img = img.resize((150, 150), Image.LANCZOS)  # Using LANCZOS for resizing with anti-aliasing
        photo = ImageTk.PhotoImage(img)
        chat_display.image_create(tk.END, image=photo)
        chat_display.image = photo
        chat_display.image = photo  # Keep a reference to avoid garbage collection
        chat_display.insert(tk.END, "\n")
    except FileNotFoundError:
        chat_display.insert(tk.END, "Image not found.\n")
    except Exception as e:
        chat_display.insert(tk.END, f"Error loading image: {e}\n")

root = tk.Tk()
root.title("Chatbot Launcher")

chatbot_button = tk.Button(root, text="💬", font=("Helvetica", 24), command=open_chat_window)
chatbot_button.pack(pady=20)

root.mainloop()

# Log unrecognized questions
with open('unrecognized_questions.txt', 'w') as f:
    for question in unrecognized_questions:
        f.write(question + '\n')
