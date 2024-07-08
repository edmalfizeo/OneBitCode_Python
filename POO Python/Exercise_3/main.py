from class_Travel import Travel

tickets = []
places = Travel.get_places()
transports = Travel.get_transports()

while True:
    print("\n1. See Available Destinations")
    print("2. See available Transports")
    print("3. Buy Ticket")
    print("4. Show Travel Details")
    print("5. Exit")

    choose_option = int(input("Choose an option: "))

    if choose_option == 1:
        print("\nAvailable Destinations:")
        for place in places:
            print(place)

    if choose_option == 2:
        print("\nAvailable Transports:")
        for transport in transports:
            print(transport)

    if choose_option == 3:
        try:
            destination = input("Enter the destination: ")
            duration = input("Enter the duration: ")
            transport = input("Enter the transport: ")

            new_ticket = Travel()
            new_ticket.buy_ticket(destination, duration, transport)
            tickets.append(new_ticket)
            print("Ticket bought successfully!")
        except ValueError as e:
            print(e)
            print("Please Insert a valid destination or transport!")

    if choose_option == 4:
        if tickets:
            print("\nYour Tickets:")
            for i, ticket in enumerate(tickets, start=1):
                print(f"\nTicket {i}:")
                print(ticket)
        else:
            print("No tickets bought yet.")

    if choose_option == 5:
        break
