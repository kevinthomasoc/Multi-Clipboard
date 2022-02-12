import pyperclip

clipboard = {}
while True:
    action = input("What would you like to do? (Read, Load, or Save)")
    if action.lower() == "read":
        if len(clipboard) < 1:
            print("You have nothing in your clipboard.")
        else:
            for key in clipboard:
                print(key, clipboard[key])
    elif action.lower() == "save":
        message = input("What do you want to save?")
        key = input("What do you want to save it as? (Make sure you remember this!)")
        clipboard[key] = message
        print("It has been saved!")
    elif action.lower() == "load":
        if len(clipboard) < 1:
            print("You have nothing in your clipboard.")
        else:
            key = (input("What key would you like to access?")).lower()
            print(clipboard[key] + " has been copied to your clipboard!")
            pyperclip.copy(clipboard[key])
    else:
        print("Please enter a valid input.")



