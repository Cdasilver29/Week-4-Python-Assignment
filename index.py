# 1. File Read & Write Challenge 🖋️

# Open input.txt for reading
f = open("input.txt", "r")
text = f.read()
f.close()

# Modify the text (make uppercase)
modified = text.upper()

# Open output.txt for writing
f = open("output.txt", "w")
f.write(modified)
f.close()

print("The new file has been created successfully")


# 2. Error Handling Lab 🧪

filename = input("Enter filename: ")

try:
    f = open(filename, "r")
    content = f.read()
    f.close()
    print(content)
except FileNotFoundError:
    print("❌ File not found.")
except Exception as e:
    print("❌ Error:", e)

