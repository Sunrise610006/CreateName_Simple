import Lastname
import CreateName


# 取得姓氏

Lastname_list = Lastname.LastName()


# 使用者輸入姓氏、字數及參考姓名數

Lastname_input = input("請輸入姓氏: ")
while Lastname_input not in Lastname_list:
    Lastname_input = input("姓氏錯誤，請重新輸入姓氏: ")

WordCount_input = int(input("請輸入字數: "))
NameNumber = int(input("請輸入一次要參考的姓名數: "))

for t in range(NameNumber):
    print(CreateName.Create_Name(Lastname_input, WordCount_input-1))
