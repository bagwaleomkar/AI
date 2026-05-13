print("===================================")
print(" Welcome to Blinkit Chatbot ")
print("===================================")

name = input("Enter Your Name: ")

print("\nHello", name + "!")
print("Type 'exit' to stop the chatbot.\n")

while True:

    user = input("You: ").lower()

    # Greeting
    if user in ["hi", "hello", "hey"]:

        print("Bot: Hello", name + "! How can I help you?")

    # Order Status
    elif "order" in user:

        order_id = input("Bot: Enter your Order ID: ")

        print("Bot: Your order", order_id, "is out for delivery.")

    # Delivery Time
    elif "delivery" in user:

        print("Bot: Delivery usually takes 10 to 20 minutes.")

    # Payment
    elif "payment" in user:

        print("Bot: We support UPI, Debit Card, Credit Card and Cash on Delivery.")

    # Refund
    elif "refund" in user:

        print("Bot: Refund will be processed within 3 to 5 working days.")

    # Cancel Order
    elif "cancel" in user:

        print("Bot: Your order cancellation request has been submitted.")

    # Contact
    elif "contact" in user or "number" in user:

        print("Bot: Blinkit Customer Care Number: 9876543210")

    # Location
    elif "location" in user or "address" in user:

        print("Bot: Blinkit service is available in major cities.")

    # Thank You
    elif "thank" in user:

        print("Bot: Thank you", name + "! Have a nice day.")

    # Exit
    elif user == "exit":

        print("Bot: Thank you for using Blinkit Chatbot.")
        break

    # Default
    else:

        print("Bot: Sorry! I did not understand.")
