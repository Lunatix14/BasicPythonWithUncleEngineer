class Condo:

    def __init__(self,location,sqrMetre,price):
        self.location = location
        self.sqrMetre = sqrMetre
        self.price = price

    def common_Fee(self):
        fee = 50
        totalfee = self.sqrMetre * fee
        print(f'ค่าส่วนกลางต่อเดือน : {totalfee} บาทค่ะ')
    
    def locate(self):
        if self.location == 'เกียกกาย':
            print('Location อยู่ใกล้ค่ายทหาร ลูกค้าระวังรถถังนะคะ')
        elif self.location == 'สนามหลวง':
            print('โปรดระมัดระวังคนเล่นว่าวค่ะ')
        else:
            print('Prime Location เลยนะคะเนี่ย')

    def promote(self):
        if self.sqrMetre == 25:
            print('ขนาดห้อง 25 ตรม. Promotion ฟรีวัคซีน Sinovac 30 ลังค่ะ')
        elif self.sqrMetre >= 25 and self.sqrMetre <= 34:
            print('ขนาดห้อง 25-34 ตรม. Promotion ฟรีเรือดำน้ำมือสองจากจีน 1 ลำค่ะ')
        else:
            print('Promotion จ่ายเพิ่มแพงขึ้น 2 แสนบาทค่ะ')

    def sale(self):
        budget = int(input('คุณลูกค้ามีงบประมาณเท่าไรคะ? : '))
        if budget > 10000000:
            print('ลูกค้า VIP รับส่วนลด On-Top 5 แสนบาทค่ะ')
        elif budget >= 3000000 and budget <= 10000000:
            print('ลูกค้าได้รับส่วนลด On-Top 2 แสนบาทค่ะ')
        else:
            print('ออกไป๊!!!!!!!!!!')

if __name__ == "__main__":
    condo1 = Condo('เกียกกาย', 34 ,'3,000,000')

print('ข้อมูล Condo1 ค่ะ')
print(f'ทำเล : {condo1.location} | ขนาดห้อง {condo1.sqrMetre} ตรม. | ราคา {condo1.price} บาทค่ะ')
condo1.common_Fee()
condo1.locate()
condo1.promote()
condo1.sale()