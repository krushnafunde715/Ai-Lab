# Vaccum Cleaner - simple reflex agent

#initial environment of rooms

rooms = {
    "A" : input("Enter initial environment of room A (clean/ dirty): ").lower(),
    "B" : input("Enter initial environment of room B (clean/ dirty): ").lower()
}

#initial location of vaccum cleaner

location = input("Enter initial location of cleaner (A/ B): ").upper()

print("\n Initial environment: ", rooms)

print("\n====Simple reflex agent====\n")

while 'dirty' in rooms.values():

    print("Agent is in room", location)

    print("Current status of room is", rooms[location])

    if(rooms[location] == 'dirty'):

        print("Action : Suck")
        rooms[location] = "clean"
        print("Room is cleaned now")

    else:

        print("Room is already clean")
        print("No need to clean again")

    if(location == 'A'):
        print("Move to room B")
        location = 'B'

    else:
        print("Move to room A")
        location = 'A'

    print("Environment:", rooms)
    print("====================================\n")

#final result

print("Final Environment:", rooms)
print("All rooms are clean now")