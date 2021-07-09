import random


# 刪除重複內容

def Delete_TheSame(AList):
    TheList = list(set(AList))
    return TheList


# 轉換中文字為utf-8的URL

def ChangeToUTF8(AString):
    Theword = str(AString.encode('utf-8'))
    TheList = Theword.replace('\\x', '%')
    return TheList.lstrip("b'").rstrip("'")


# 取得亂數

def Random(Alist):
    random.seed(None)
    return random.choice(Alist)


# 計算筆畫

def get_stroke(words):
    strokes = []
    with open("strokes.txt", 'r') as f:
        for line in f:
            strokes.append(int(line.strip()))

    Theword = ord(words)

    if 13312 <= Theword <= 64045:
        return strokes[Theword-13312]
    elif 131072 <= Theword <= 194998:
        return strokes[Theword-80338]
    else:
        return 0
