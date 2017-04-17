from bs4 import BeautifulSoup
import urllib.request
import re
from html.parser import HTMLParser
import sys
count = 0
def mouthShut2(fo1,fo3,headers,urlBaseMs2,negativeWords):
    flag = False
    try:
        temp = None
        for i in range(1,5):
            url = urlBaseMs2 + "-page-"+ str(i)
            req = urllib.request.Request(url, headers=headers)
            res = urllib.request.urlopen(req)
            content = res.read()

            soup = BeautifulSoup(content, "lxml")
            result1 = soup.find_all("span", {"id": re.compile("(.*)lblDateTime")})
            result2 = soup.find_all("div", {"class": "more reviewdata"})
            #for i in result5:
                #fo1.write("{}".format(i.text).strip()+"\n\n")
            if (temp == result2[0].text):
                break
            if(temp == None):
                temp = result2[0].text
            for i,j in zip(result1,result2):
                if any(word in j.text for word in negativeWords):
                    fo3.write("{}".format(i.text).strip() + "\n" + "{}".format(j.text).strip() + "\n\n")
                    flag = True
                else:
                    fo1.write("{}".format(i.text).strip() + "\n" + "{}".format(j.text).strip() + "\n\n")
                global count
                count += 1
            if flag == False:
                fo3.write("No negative review!\n\n")
    except IndexError:
        print("Error on line {}").format(sys.exc_info()[-1].tb_lineno)
    except Exception as e:
        print(e)
    except HTMLParser as he:
        print(he)

