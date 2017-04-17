from bs4 import BeautifulSoup
import urllib.request
from html.parser import HTMLParser
import traceback
import sys
count = 0
def collegeDuniya2(fo1,fo3,headers,urlBaseCd2,negativeWords):
    flag = False
    try:
        temp = None
        for i in range(1,5):
            url = urlBaseCd2 + "/page-"+ str(i)
            req = urllib.request.Request(url, headers=headers)
            res = urllib.request.urlopen(req)
            content = res.read()
            soup = BeautifulSoup(content, "lxml")
            #result5 = soup.find_all("div", {"class":"review_data"})
            result5 = soup.find_all("div", {"class": "review_content"})
            result6 = soup.find_all("span",{"class":"review_date"})
            #for i in result5:
                #fo1.write("{}".format(i.text).strip()+"\n\n")
            if (temp == result5[0].text):
                break
            if(temp == None):
                temp = result5[0].text

            for i,j in zip(result5,result6):
                if i.div:
                    _ = i.div.extract()
                var = i.text.strip("00reportRead More").strip()
                var = var[:-11]
                #fo2.write("{}".format(i.text).strip("00reportRead More").strip() + "\n\n")
                #fo2.write(var+"\n\n")
                if any(word in i.text for word in negativeWords):
                    fo3.write("{}".format(j.text).strip() + "\n" + "{}".format(var) + "\n\n")
                    flag = True
                else:
                    fo1.write("{}".format(j.text).strip() + "\n" + "{}".format(var) + "\n\n")
                global count
                count += 1
            if flag == False:
                fo3.write("No negative review!\n\n")
            #for a,b in zip(result6, result5):
                #fo2.write("{}".format(a.text).strip() + "\n" + "{}".format(b.text).strip() + "\n\n")
    except IndexError:
        print('Error on line {}').format(sys.exc_info()[-1].tb_lineno)
    except Exception as e:
        #print(e)
        traceback.print_exc()
    except HTMLParser as he:
        print(he)
