def write_mylife():
    with open("interactive_file_writer/my_life.txt", "w") as f:
        while True:
            line = input("Enter line: ")
            f.write(line + "\n")
            
            more = input("Are there more lines y/n? ")
            if more.lower() == 'n':
                break

write_mylife()