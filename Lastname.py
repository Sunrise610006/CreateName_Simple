import Name_tool as tool
import urllib.request
import json


def LastName():

    # 政府資料開放平台-姓氏排名與人數按三階段年齡分的網址

    LastName_URL = "https://od.moi.gov.tw/api/v1/rest/datastore/301000000A-001602-005"

    # 獲取姓氏相關資料

    with urllib.request.urlopen(LastName_URL) as LastName_GetData:
        LastName_data = json.load(LastName_GetData)
    LastName_Message = LastName_data["result"]["records"]

    # 只取姓氏

    lastname = []
    for LastName_list in LastName_Message:
        lastname = lastname + [LastName_list["lastname"]]

    # 將標題('姓氏')及重複者去除

    del lastname[lastname.index('姓氏')]
    lastname = tool.Delete_TheSame(lastname)

    return str(lastname)
