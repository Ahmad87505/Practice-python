# Create a file with some text
with open("example.txt", "w") as f:
    f.write("Hello, world!")

# Read and use seek(), tell()
with open("example.txt", "r") as f:
    print("Current position:", f.tell())  

    # Read 5 characters
    text = f.read(5)
    print("Read text:", text)

    print("Position after reading:", f.tell())

    # Move back to the beginning
    f.seek(0)
    print("Position after seek:", f.tell())

    # Read full line
    print("Full text again:", f.read())
