# รับค่า ชื่อจริง จากผู้ใช้
# เขียน loop เพื่อนับจำนวน "สระที่มีอยู่ในชื่อที่รับมา" นั้นว่ามีจำนวนกี่ตัว

# ตัวอย่างหน้าจอ

# What is your name?: Boonchoo
# Your name have 4 vowels.

#name = input("What is your name?: ")
name = input("What is your name?: ")

vowels = 0

for letter in name:
    if letter == 'a' or letter == 'A':
        vowels = vowels + 1
    if letter == 'e' or letter == 'E':
        vowels = vowels + 1
    if letter == 'i' or letter == 'I':
        vowels = vowels + 1
    if letter == 'o' or letter == 'O':
        vowels = vowels + 1
    if letter == 'u' or letter == 'U':
        vowels = vowels + 1

print("Your name have", vowels, "vowels.")