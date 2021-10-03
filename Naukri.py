import requests
import csv
from datetime import *
import json
import time

#Sraping Proagram for Naukri        
#We have searched for PythonDeveloper and have scraped first 10pages and extracted data in csv format
#Some fix needs to be done

dat= date.today()
with open('Naukri_PythonDev_'+str(dat)+'.csv','a',newline='',encoding='UTF-8') as fp:
    writer=csv.writer(fp)
    writer.writerow(['PageNumber','Record_no','Current_page_Record','Website','Job_Title','Company','Job_Description','Required_Skills','Details1','Details2','Posted','Url'])

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'application/json',
    'appid': '109',
    'systemid': '109'
}

recordno = 0
for x in range(1, 11):
    print(f'---------Page{x}---------')
    print(f'Overall_Record_Number: {recordno}')
    time.sleep(5)
    url=f'https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword=python%20developer&pageNo={x}&sort=r&k=python%20developer&seoKey=python-developer-jobs-4&src=jobsearchDesk&latLong=&sid=16244011297972720_1'
    r = requests.get(url, headers=headers, timeout=30)
    print(r.status_code)
    data = json.loads(r.text)
    for i, item in enumerate(data['jobDetails']):
        global exp,exp1
        recordno=recordno+1
        print(f'Overall_Record_Number: {recordno}')
        i = i + 1
        print(f'Current_page_RecordNumber:{i}')
        try:
            name = (item['title'])
        except:
            name=''
        try:
            companyname = (item['companyName'])
        except:
            companyname=''
        try:
            jobdescription = (item['jobDescription'])
        except:
            jobdescription=''
        try:
            posted = (item['footerPlaceholderLabel'])
        except:
            posted=''
        try:
            joburl = (item['jdURL'])
        except:
            joburl=''
        try:
            tag = (item['tagsAndSkills'])
        except:
            tag=''
        finalurl = f'https://www.naukri.com{joburl}'
        print(f'JobTitle: {name}')
        print(f'Name of the company: {companyname}')
        print(f'Description: {jobdescription}')
        print(f'Skilled Required: {tag}')
        for holder in (item['placeholders']):
            try:
                exp = (holder['label'])
            except:
                exp=''
            try:
                exp1 = (holder['type'])
            except:
                exp1=''
            print(f'More details: {exp},{exp1}')
        print(finalurl)
        print(f'Job Posted: {posted}')

        with open('Naukri_PythonDev_' + str(dat) + '.csv', 'a', newline='', encoding='UTF-8') as fp:
            writer = csv.writer(fp)
            writer.writerow([x, recordno,i,'naukri.com', name,companyname,jobdescription,tag,exp,exp1,posted,finalurl])

print('-------------------Task_Complete------------------')
