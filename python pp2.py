def greet(name, callback):
    message = f"Hello, {name}!"
    callback(message)

def display_message(msg):
    print(msg)

greet("Alice", display_message)
def process_data(data, callback):
    processed_data = [item * 2 for item in data]
    callback(processed_data)

def print_list(data_list):
    print(f"Processed list: {data_list}")

process_data([1, 2, 3], print_list)

class Button:
    def __init__(self, name):
        self.name = name
        self.on_click = None

    def click(self):
        if self.on_click:
            self.on_click(self.name)

def button_handler(button_name):
    print(f"{button_name} button was clicked!")

my_button = Button("Submit")
my_button.on_click = button_handler
my_button.click()

import time

def fetch_data_async(url, callback):
    print(f"Fetching data from {url}...")
    time.sleep(2)  # Simulate delay
    data = {"url": url, "content": "Some data from server"}
    callback(data)

def handle_fetched_data(data):
    print(f"Data received: {data}")

print("\nStarting async data fetch...")
fetch_data_async("https://api.example.com/data", handle_fetched_data)
print("Async data fetch initiated, continuing with other tasks...")

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x * x, numbers))
print(f"Squared numbers: {squared_numbers}")

def is_even(num):
    return num % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(f"Even numbers: {even_numbers}")