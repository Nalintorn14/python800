# รับค่า password จากผู้ใช้
# password นั้นแข็งแรงหรือไม่
# password นั้นจะแข็งแรง ถ้าประกอบไปด้วยตัวเลข ตัวอักษร มี '@' อย่างน้อย1ตัว และ ยาวมากกว่า8ตัว

# ตัวอย่างหน้าจอ
# Please input your password: boonchoo 
# Your password is not strong!

# Please input your passwprd: Bo@o15thai
# Your password is strong!

password = input("Please input your password: ")

has_number = any(char.isdigit() for char in password)
has_letter = any(char.isalpha() for char in password)
has_at = "@" in password
is_long = len(password) > 8

if has_number and has_letter and has_at and is_long:
    print("Your password is strong!")
else:
    print("Your password is not strong!")
