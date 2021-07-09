import bs4
import urllib.request as r


def Words_Data():

    # 常見取名用字表網址

    Thewords_URL = "http://www.name104.com/name-hot.php#.YOJ3lOgzY2w"

    # 獲取常見取名用字表資料

    requests = r.Request(Thewords_URL, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    })

    with r.urlopen(requests) as responses:
        Words_data = responses.read().decode("utf-8")

    Words_Get = bs4.BeautifulSoup(Words_data, "html.parser")
    words = Words_Get.get_text()

    # 取得表格中的資料並保留常用字的部分

    words_list = []
    decision = False

    for w in words:
        w = str(w)
        if w == "怡":
            decision = True
        if (w.isalpha()) == False:
            continue
        if decision == True:
            words_list += w
            if w == "旨":
                decision = False

    return words_list
