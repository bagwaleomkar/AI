print("===================================")
print(" Welcome to RedBus Chatbot ")
print("===================================")

name = input("Enter Your Name: ")

print("\nHello", name + "!")
print("Type 'exit' to stop the chatbot.\n")

while True:

    user = input("You: ").lower()

    # Greeting
    if user in ["hi", "hello", "hey"]:

        print("Bot: Hello", name + "! How can I help you?")

    # Bus Booking
    elif "book" in user or "ticket" in user:

        source = input("Bot: Enter Source City: ")

        destination = input("Bot: Enter Destination City: ")

        print("Bot: Bus ticket booking from", source, "to", destination, "is available.")

    # Bus Timing
    elif "time" in user or "timing" in user:

        print("Bot: Buses are available 24 hours.")

    # Fare
    elif "fare" in user or "price" in user:

        print("Bot: Ticket price starts from Rs. 500.")

    # Cancel Ticket
    elif "cancel" in user:

        print("Bot: Your ticket cancellation request has been submitted.")

    # Refund
    elif "refund" in user:

        print("Bot: Refund will be processed within 5 working days.")

    # Contact
    elif "contact" in user or "number" in user:

        print("Bot: RedBus Customer Care Number: 9876543210")

    # Location
    elif "location" in user or "address" in user:

        print("Bot: RedBus service is available across India.")

    # Thank You
    elif "thank" in user:

        print("Bot: Thank you", name + "! Have a safe journey.")

    # Exit
    elif user == "exit":

        print("Bot: Thank you for using RedBus Chatbot.")
        break

    # Default
    else:

        print("Bot: Sorry! I did not understand your message.")
