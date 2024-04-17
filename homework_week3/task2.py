import urllib.request
import csv
import function.getpagedata

def getdata(url):
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
    titles=root.find_all("div",class_="title")
    #titles=root.find_all("li")
    #print(titles.a.string)
    #titles=root.find_all("a",class_="title")
    with open("article.csv",mode='a',encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        for title in titles:
            if title.a!=None:
                #writer.writerow([title.a.string])#以列表傳入才不會變成一個個字在csv檔被，分開
                #page_url=getdata(title.a['href'])
                result=function.getpagedata.getpagedata("https://www.ptt.cc"+title.a['href'])#[ 0, 0,'Sat Apr 13 19:55:56 2024']
                writer.writerow([title.a.string,result[0],result[1],result[2]])
                #print(result)


    next_page=root.find('a',string="‹ 上頁")#找到標籤裡有‹ 上頁的網址內容
    return next_page['href']#取得下一頁的網址

print("Input the url you want to crawl:")#https://www.ptt.cc/bbs/Lottery/index.html
url=input()
getdata(url)
next_page="https://www.ptt.cc/"+getdata(url)

count=0
while next_page!=None:
    print("Crawling page:"+next_page)
    next_page="https://www.ptt.cc/"+getdata(next_page)#在這裡爬下一頁的內容
    count+=1
    if count==3:
        break
