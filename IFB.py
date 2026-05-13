print("======================================")
print(" Welcome to IFB Service Centre ")
print("======================================")

name = input("Enter Your Name: ")

print("\nHello", name + "!")
print("How can I help you today?")
print("Type 'exit' to stop.\n")

while True:

    user = input("You: ").lower()

    # Greeting
    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello", name + "! Welcome to IFB Service Centre.")

    # Service Booking
    elif "service" in user or "repair" in user:

        machine = input("Bot: Which machine do you have? (Top Load / Front Load): ")

        problem = input("Bot: Enter the problem: ")

        print("Bot: Your service request has been registered.")
        print("Bot: Machine Type:", machine)
        print("Bot: Problem:", problem)
        print("Bot: Technician will contact you soon.")

    # Complaint
    elif "complaint" in user:

        complaint = input("Bot: Please enter your complaint: ")

        print("Bot: Complaint registered successfully.")

    # Price
    elif "price" in user or "charge" in user:

        print("Bot: Service charges start from Rs. 300.")

    # Location
    elif "location" in user or "address" in user:

        print("Bot: IFB Service Centre, Pune, Maharashtra.")

    # Contact
    elif "contact" in user or "number" in user:

        print("Bot: Contact Number: 9876543210")

    # Timing
    elif "time" in user or "timing" in user:

        print("Bot: Service timing is 9 AM to 6 PM.")

    # Thank You
    elif "thank" in user:

        print("Bot: Thank you", name + "!")

    # Exit
    elif user == "exit":

        print("Bot: Thank you for visiting IFB Service Centre.")
        break

    # Default
    else:

        print("Bot: Sorry! I did not understand your message.")
