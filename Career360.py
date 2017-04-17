from bs4 import BeautifulSoup
import urllib.request
from html.parser import HTMLParser
import sys
count = 0
def career360(fo1,fo3,headers,urlBc360,negativeWords):
    flag = False
    try:
        for i in urlBc360:
            # we sent the a request to the website
            req = urllib.request.Request(i, headers=headers)
            # we receive the response from the website
            res = urllib.request.urlopen(req)
            # we read the information and store in 'content' variable
            content = res.read()
            # create a soup object to parse the site
            soup = BeautifulSoup(content, "lxml")
            #print(content)
            result7 = soup.find_all("div", {"class":"description"})
            result8 = soup.find_all("div", {"class":"time"})
            for i,j in zip(result8[::3],result7):
                #print(i.text.strip("<div class=\"time\"> <label>Posted On :</label>").strip("</div>"))
                if any(word in j.text for word in negativeWords):
                    fo3.write("{}".format(i.text).strip("<div class=\"time\"> <label>Posted On :</label>").strip("</div>").strip()+"\n"+"{}".format(j.text).strip()+"\n\n")
                    flag = True
                else:
                    fo1.write("{}".format(i.text).strip("<div class=\"time\"> <label>Posted On :</label>").strip(
                        "</div>").strip() + "\n" + "{}".format(j.text).strip() + "\n\n")
                global count
                count += 1
            if flag == False:
                fo3.write("No negative review!\n\n")
    except IndexError:
        print('Error on line {}').format(sys.exc_info()[-1].tb_lineno)
    except Exception as e:
        print(e)
    except HTMLParser as he:
        print(he)


