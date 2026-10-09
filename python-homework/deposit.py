
def deposit(money):
    balance = 1000.00

    try:
        money = float(money)

        if money <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")

    except ValueError as e:
        print(f"\nเกิดข้อผิดพลาด: {e}")

    else:
        balance += money
        print("\nฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")

    finally:
        print("สิ้นสุดรายการฝากเงิน")


print("ยอดเงินเริ่มต้น: 1000 บาท")
money = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
deposit(money)