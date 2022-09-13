import sys

if len(sys.argv) == 2:
    command = sys.argv[1]
    if command == "save":
        print("save")
    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")
