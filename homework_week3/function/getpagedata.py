import urllib.request
import csv
def getpagedata(url):
    request=urllib.request.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        'Cookie':"over18=1"#預先回答滿18歲的問題
    })
    with urllib.request.urlopen(request) as cont:
        data1=cont.read().decode("utf-8")

    import bs4 #引進beautifulsoup幫忙解析html
    root=bs4.BeautifulSoup(data1,'html.parser')
    #print(root.li.string)#string=抓取標籤中的文字
    #titles=root.find("div",class_="breakingnews_pc boxTitle boxText")
    time_div=root.find_all("div",class_="article-metaline")
    if time_div:
        for div in time_div:
            span_time=div.find("span", class_="article-meta-tag")
            value_time=div.find("span", class_="article-meta-value")
            if span_time.string=='時間':
                time_value=value_time.string#Sun Apr 14 23:13:46 2024
    else:
        time_value=None
    
    push_div=root.find_all('div',class_="push")
    if push_div:
        Like=0
        Dislike=0
        for divs in push_div:
            span_push=divs.find("span",class_="hl push-tag")
            span_down=divs.find("span",class_="f1 hl push-tag")
            if span_push is not None:
                span_push.string=="推 "
                Like+=1
            elif span_down is not None:
                if span_down.string=="噓 ":
                    Dislike+=1
                else:
                    continue
    else:
        Like=None
        Dislike=None
    return (Like,Dislike,time_value)

#result=getpagedata("https://www.ptt.cc/bbs/Lottery/M.1297610645.A.D19.html")
#print(result[0])

#getpagedata("https://www.ptt.cc/bbs/Lottery/M.1297610645.A.D19.html")