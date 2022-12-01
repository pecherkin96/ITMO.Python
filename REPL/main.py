import commands
print("Command ('loc', 'zip', 'dist', 'end')")
command = ""
while command != "end":
    command = input().lower()
    if command == "loc":
        commands.write_loc()
    elif command == "zip":
        commands.zip()
    elif command == "dist":
        commands.dist()
    else:
        print("Invalid command, ignoring")
print("Done")
