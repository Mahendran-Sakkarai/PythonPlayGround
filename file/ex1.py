def read(filename):
    # Read all content
    f = open(filename, "r")
    print(f.read())
    f.close()

def readUsingWith(filename):
    with open(filename, "r") as file:
        print(file.read())

# -------------------   Write Mode   --------------------------
f = open("abc.txt", "w")
print(f)

f.write("line 1\n")
f.write("line 2\n")
f.write("line 3\n")
f.write("line 4\n")
f.write("line 5\n")

f.close()

# -------------------   Read mode   ---------------------------
# Read all content
f = open("abc.txt", "r")
print(f.read())
f.close()

# Read First 10 char
f = open("abc.txt", "r")
print(f.read(10))
f.close()

# Readling First line
f = open("abc.txt", "r")
print(f.readline())
f.close()

# Read numbere of character in first paragraph
f = open("abc.txt", "r")
print(f.readline(2))
f.close()

# Reall all lines in a file seperated
f = open("abc.txt", "r")
print(f.readlines())
f.close()

# Read all lines using loop
f = open("abc.txt", "r")
for line in f:
    print(line)


# ---------------------------   Append   ------------------------
# Append to the file
f = open("abc.txt", "a")
for i in range(10):
    f.write("line " + str(i) + "\n")
f.close()
read("abc.txt")

# Append an array
listItem = []
for i in range(10, 20):
    listItem.append("line " + str(i) + "\n")
f = open("abc.txt", "a")
f.writelines(listItem)
f.close()
read("abc.txt")


# -------------------------   Using With   ----------------------
# Advantage --> No need to use close. It'll close automatically.
# We can do whatever we done before using the with
with open("abc.txt", "r") as file:
    print(file.read())

with open("abc.txt", "a") as file:
    file.write("End of file")

readUsingWith("abc.txt")


# -------------------   Read Memory Efficient    ------------------
with open("abc.txt" , "r") as file:
    for i, line in enumerate(file):
        if i == 5:
            print(line)
        elif i == 10:
            print(line)
        elif i == 11:
            break

