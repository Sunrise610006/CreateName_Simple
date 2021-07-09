import WordsData
import Lastname
import Name_tool as tool


# 取得姓氏

Lastname_list = Lastname.LastName()


# 取得所有中文字

Firstname_list = WordsData.Words_Data()


# 吉祥姓名筆劃數

Best = [1, 3, 5, 7, 8, 11, 13, 15, 16, 18, 21, 23, 24, 25, 31,
        32, 33, 35, 37, 39, 41, 45, 47, 48, 52, 57, 61, 63, 65, 67, 68, 81]
Better = [6, 17, 26, 27, 29, 30, 38, 49, 51, 55, 58, 71, 73, 75]
Leader = [3, 13, 16, 21, 23, 39, 31, 37, 39, 41, 45, 47]
Richer = [15, 16, 24, 29, 32, 33, 41, 52]
Artist = [13, 14, 18, 26, 29, 33, 35, 38, 48]
Family = [5, 6, 11, 13, 15, 16, 24, 32, 35]
Auspicy = tool.Delete_TheSame(
    Best + Better + Leader + Richer + Artist + Family)


# 創造名字

def Create_Name(Lastname_input, WordCount_input):

    CreateName = str(Lastname_input)

    if len(Lastname_input) == 1:
        FirstName_number = 1
    else:
        FirstName_number = 0

    Total_Strokes = FirstName_number + tool.get_stroke(Lastname_input)
    for t in range(1, WordCount_input):
        Medium = tool.Random(Firstname_list)
        CreateName += Medium
        Total_Strokes += tool.get_stroke(Medium)

    GoodName = False

    while GoodName == False:
        Final_Name = tool.Random(Firstname_list)
        Total_Strokes += tool.get_stroke(Final_Name)
        if Total_Strokes in Auspicy or Total_Strokes % 81 in Auspicy:
            GoodName = True
            CreateName += Final_Name
            Total_Strokes %= 81

    fate = ""

    if Total_Strokes in Best:
        fate += "【大吉】"
    if Total_Strokes in Better:
        fate += "【吉】  "
    if Total_Strokes in Leader:
        fate += "[領導才能]"
    if Total_Strokes in Richer:
        fate += "[榮華富貴]"
    if Total_Strokes in Artist:
        fate += "[藝術天賦]"
    if Total_Strokes in Family:
        fate += "[家庭美滿]"

    return CreateName + fate
