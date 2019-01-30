#from apscheduler.schedulers.blocking import BlockingScheduler
import os
import site1
import site2
import site3
import site4

def scrapeAll():
       print(os.getcwd())
       sites = open('WebScraper/sites.txt', 'r')

       webPage1 = sites.readlines(1)[0][:-2] # -2 helps clean \n at the end of each line 
       site1.scrapeS1(webPage1)

       webPage2 = sites.readlines(2)[0][:-2]
       site2.scrapeS2(webPage2)

       webPage3 = sites.readlines(3)[0][:-2]
       site3.scrapeS3(webPage3)

       webPage4 = sites.readlines(4)[0]
       site4.scrapeS4(webPage4)

scrapeAll()

print('end')
#scheduler = BlockingScheduler()
#scheduler.add_job(scrapeAll, 'interval', hours=12)
#scheduler.start()