from turtledemo.penrose import start

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
         started = True
         print("car started ready to go ...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!!")
        else:
            started = False
            print("car stopped !!")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
          """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand that")