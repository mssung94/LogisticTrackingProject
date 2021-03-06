# JUNESEOK BYUN @juneseokdev.me
import googlegeo as gg
import sqlite3
import requests
from bs4 import BeautifulSoup
import re

cj_add = 'https://www.doortodoor.co.kr/parcel/doortodoor.do?fsp_action=PARC_ACT_002&fsp_cmd=retrieveInvNoACT&invc_no='

def convertTime(x):
    after = re.findall('\d+', x)
    l = len(after)
    text = ''
    for i in range(0, l):
        text = text + after[i]
    return text


def cj_listreturn(x):
    # x is the str
    url = cj_add + x
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    path = soup.find_all(
        title="집배점 정보 팝업"
        )
    date = soup.find_all(
            "td"
        )

    l1 = len(path)
    l2 = len(date)

    if l1==0:
        return [], []

    pathlist = []
    datelist = []
    for k in range(0,l1):
        pathcell = path[k].get_text()
        datecell = convertTime(date[4*(k+1) + 2].get_text())
        pathlist.append(pathcell)
        datelist.append(datecell)

    print("[PASSED] GET PATHLIST", x, ":", pathlist)
    print("[PASSED] GET TIMELINE", x, ":", datelist)
    
    return pathlist, datelist

if __name__ == "__main__":
    a, b = cj_listreturn('617601330752')



