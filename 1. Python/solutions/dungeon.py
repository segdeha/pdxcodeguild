"""
This is a-maze-ing Maze. You start it by calling the main function.
Exiting the program is always an option with 'exit'.
"""

def main():
    print("Welcome to the A-Maze-ing Maze! I dare you to escape!")

    current_room = room0()

    while current_room != exit:
        current_room = current_room()

    current_room()


def process_user_movement(description, doors):
    """
    This is the process_user_movement function that will
       handle a user's inpt.

    Args:
        doors: A description of the current room
        description: dictionary with door:location sets
    """
    # Print the description of the current room
    print(description)

    # Print the available doors
    print("You see doors to the ", end="")
    print(*list(doors.keys()), sep=", ")

    # Prompt the user for what doors they want
    choice = ""

    # Do things based on their response
    while choice.lower() != "exit":
        choice = input("Which way you would like to go? >> ")

        # Valid response: Go to the correct location
        if choice.lower() in doors:
            return doors[choice.lower()]
        elif choice.lower() == "exit":
            print("Too tough for you, eh? Good-bye, then.")
            return exit
        # Invalid response: Ask them again
        else:
            print("I'm sorry, I didn't understand.")


def room0():
    # description
    description = "This room is very small. You barely fit here. You're like Alice in that crazy-tiny-room thing."
    # doors
    # where those doors Go
    doors = {"east": room2, "west": room1}

    return process_user_movement(description, doors)


def room1():
    # description
    description = "This room is HUGE, but there is a tiny door to the south."
    # doors
    # where those doors Go
    doors = {"south": room3, "east": room0}

    return process_user_movement(description, doors)


def room2():
    # description
    description = "This room is boring, there really isn't anything here"
    # doors
    # where those doors Go
    doors = {"west": room0}

    return process_user_movement(description, doors)


def room3():
    # description
    description = "There are three doors here. They all look so inviting."
    # doors
    # where those doors Go
    doors = {"north": room1, "east": room6, "south": room4}

    return process_user_movement(description, doors)


def room4():
    # description
    description = "There are two doors here. They all look so inviting."
    # doors
    # where those doors Go
    doors = {"north": room3, "east": room5}

    return process_user_movement(description, doors)


def room5():
    # description
    description = "There is a giant lever in the middle of the room. It does nothing. "
    # doors
    # where those doors Go
    doors = {"west": room4}

    return process_user_movement(description, doors)


def room6():
    description = "Hey you found the exit!!"
    # doors
    # where those doors Go
    doors = {"exit": exit}

    return process_user_movement(description, doors)


if __name__ == '__main__':
    main()
