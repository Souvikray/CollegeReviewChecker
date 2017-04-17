from bs4 import BeautifulSoup
import urllib.request
import re
from html.parser import HTMLParser
import sys
count = 0
def shiksha(fo1,fo3,headers,urlBaseSh,negativeWords):
    flag = False
    try:
        temp = None
        for j in range(1,5):
            url = urlBaseSh + "-"+str(j)+"?sort_by=relevance"
            req = urllib.request.Request(url, headers=headers)
            res = urllib.request.urlopen(req)
            content = res.read()
            soup = BeautifulSoup(content, "lxml")
            result3 = soup.find_all("div", {"id": re.compile("fullDescSection_(.*)")})
            result4 = soup.find_all("p", {"class":"hlp-spn r-t"})
            if (temp == result3[0].text):
                break
            if (temp == None):
                temp = result3[0].text

            for a,b in zip(result4,result3):
                if any(word in a.text for word in negativeWords):
                    fo3.write("{}".format(a.text).strip("Posted:").strip()+"\n"+"{}".format(b.text).strip()+"\n\n")
                    flag = True
                else:
                    fo1.write("{}".format(a.text).strip("Posted:").strip() + "\n" + "{}".format(b.text).strip() + "\n\n")
                global count
                count+=1
            if flag == False:
                fo3.write("No negative review!\n\n")
    except IndexError:
        print('Error on line {}').format(sys.exc_info()[-1].tb_lineno)
    except Exception as e:
        print(e)
    except HTMLParser as he:
        print(he)

