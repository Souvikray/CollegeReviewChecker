import CollegeDuniyaAsb
import CollegeDuniyaAu
import MouthShutAba
import MouthShutAu
import Career360
import ShikshaAsb
import os
import datetime
import sys
import traceback
from fake_useragent import UserAgent
ua = UserAgent()
userAgent = ua.random
negativeWords = ["horrible","bad","worst","illegal","fraud","poor","fake","frustrate"
                ,"politics","shit","outdated","irrelevant","terrible","waste","not worth"
                ,"drama","neglect","fight"]

try:
    if not os.path.exists("C:\\AUReviews"):
        os.makedirs("C:\\AUReviews")
    fo1 = open("C:\\AUReviews\\ReviewLinks.txt", "w")
    fo2 = open("C:\\AUReviews\\ReviewCount.txt", "a")
    fo3 = open("C:\\AUReviews\\NegativeReviews.txt","w")
    # we create a request header to send browser information to the website
    headers = {}
    # we add browser information to the header dictionary
    headers["User-Agent"] = userAgent

    #fo2.write(str(headers))
    urlBaseMs1 = "http://www.mouthshut.com/product-reviews/Alliance-Business-Academy-Bangalore-reviews-925082323"
    fo1.write("MouthShut - Alliance Business Academy\n"+"Review Link: http://www.mouthshut.com/product-reviews/Alliance-Business-Academy-Bangalore-reviews-925082323\n\n")
    fo3.write("MouthShut - Alliance Business Academy\n"+"Review Link: http://www.mouthshut.com/product-reviews/Alliance-Business-Academy-Bangalore-reviews-925082323\n\n")
    MouthShutAba.mouthShut1(fo1,fo3,headers,urlBaseMs1,negativeWords)

    urlBaseMs2 = "http://www.mouthshut.com/product-reviews/Alliance-University-Bangalore-reviews-925865394"
    fo1.write("MouthShut - Alliance University\n"+"Review Link: http://www.mouthshut.com/product-reviews/Alliance-University-Bangalore-reviews-925865394\n\n")
    fo3.write("MouthShut - Alliance University\n"+"Review Link: http://www.mouthshut.com/product-reviews/Alliance-University-Bangalore-reviews-925865394\n\n")
    MouthShutAu.mouthShut2(fo1,fo3,headers,urlBaseMs2,negativeWords)

    urlBc360 = ["http://www.bschool.careers360.com/alliance-school-business-bangalore/student-reviews"
                ,"http://www.bschool.careers360.com/colleges/alliance-university-bangalore/review"]
    fo1.write("Career360\n"+"Review Link: http://www.bschool.careers360.com/alliance-school-business-bangalore/student-reviews\nReview Link: http://www.bschool.careers360.com/colleges/alliance-university-bangalore/review\n\n")
    fo3.write("Career360\n"+"Review Link: http://www.bschool.careers360.com/alliance-school-business-bangalore/student-reviews\nReview Link: http://www.bschool.careers360.com/colleges/alliance-university-bangalore/review\n\n")
    Career360.career360(fo1,fo3,headers,urlBc360,negativeWords)

    urlBaseSh = "http://www.shiksha.com/college/alliance-school-of-business-alliance-university-anekal-bangalore-31938/reviews"
    fo1.write("Shiksha\n"+"Review Link: http://www.shiksha.com/college/alliance-school-of-business-alliance-university-anekal-bangalore-31938/reviews\n\n")
    fo3.write("Shiksha\n"+"Review Link: http://www.shiksha.com/college/alliance-school-of-business-alliance-university-anekal-bangalore-31938/reviews\n\n")
    ShikshaAsb.shiksha(fo1,fo3,headers,urlBaseSh,negativeWords)

    urlBaseCd1 = "http://www.collegedunia.com/college/17136-alliance-school-of-business-alliance-university-bangalore/reviews"
    fo1.write("CollegeDunia - Alliance School of Business\n"+"Review Link: http://collegedunia.com/college/17136-alliance-school-of-business-alliance-university-bangalore/reviews\n\n")
    fo3.write("CollegeDunia - Alliance School of Business\n"+"Review Link: http://collegedunia.com/college/17136-alliance-school-of-business-alliance-university-bangalore/reviews\n\n")
    CollegeDuniyaAsb.collegeDuniya1(fo1,fo3,headers,urlBaseCd1,negativeWords)

    urlBaseCd2 = "http://www.collegedunia.com/university/25591-alliance-university-au-bangalore/reviews"
    fo1.write("CollegeDunia - Alliance University\n"+"Review Link: http://collegedunia.com/university/25591-alliance-university-au-bangalore/reviews\n\n")
    fo3.write("CollegeDunia - Alliance University\n"+"Review Link: http://collegedunia.com/university/25591-alliance-university-au-bangalore/reviews\n\n")
    CollegeDuniyaAu.collegeDuniya2(fo1,fo3,headers,urlBaseCd2,negativeWords)

    count = MouthShutAba.count+MouthShutAu.count+Career360.count+ShikshaAsb.count+CollegeDuniyaAsb.count+CollegeDuniyaAu.count
    #print(count)
    fo2.write("Total Count: "+str(count)+" || "+str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))+"\n")
    fo1.close()
    fo2.close()
    fo3.close()
except IndexError:
    print('Error on line {}').format(sys.exc_info()[-1].tb_lineno)
except Exception as e:
    #print(e)
    traceback.print_exc()
