from .models import upwork, dataa, my_table
from .serializers import upworkSerializer
from django.http import JsonResponse
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import Proxy, ProxyType
import threading

# Helper function to perform the scraping for each job
def scrape_job_data(job, limit):
    options = Options()
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("https://www.upwork.com/freelance-jobs/")
    driver.maximize_window()

    search_result_link = []
    sPython = driver.find_element(By.LINK_TEXT, job)
    search_result_link.append(sPython.get_attribute('href'))

    jobdesc = []
    element = []
    driver.get(sPython.get_attribute('href'))
    driver.maximize_window()
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for response in soup.select('div[class="air3-grid-container"] > div > div.job-tile-wrapper > section > div.job-tile-content'):
        title = response.a.get('href')
        element.append({
            'title': title,
        })
    upId = upwork.objects.filter(up_name=job, limit=limit).first()
    count = 0
    for x in element:
        if count < limit:
            full_link = "https://www.upwork.com" + x['title']
            print("fullLink>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",full_link)
            driver.get(full_link)
            driver.maximize_window()
            
            mytb=my_table.objects.all()
            serializer = upworkSerializer(mytb, many=True)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            for response in soup.select('div[class="col-12 cfe-ui-job-details-content"] > header'):
                job_name = response.h1.get_text(strip=True)
                print(job_name)
                job_description = soup.find('div', {'class': 'job-description break mb-0'}).text
                print(job_description)
                skills = soup.findAll('span', class_=['cfe-ui-job-skill up-skill-badge disabled m-0-left m-0-top m-xs-bottom'])
                print(skills)
                
                mytbId = my_table.objects.create(JobName=job_name, JobDescription=job_description, upwork_entry=upId)
                
                for skill in skills:
                    skill = skill.text.replace('\n', '')
                    print(" skills='" + skill + "'")
                    my_result = dataa.objects.filter(data_skills=skill, my_table_entry=mytbId).values()
                    print(my_result)
                    if not my_result:
                        new_data = dataa.objects.create(data_skills=skill , my_table_entry=mytbId)
                

                jobdesc.append({
                    'JobName': job_name,
                    'JobDescription': job_description,
                    'skill': skills
                })
            count += 1
    driver.quit()

def get_data(request):
    if request.method == 'GET':
        up = upwork.objects.all()
        serializer = upworkSerializer(up, many=True)

        jobs_to_scrape = []
        for data in serializer.data:
            job = data['up_name']
            limit = data['limit']
            jobs_to_scrape.append((job, limit))

        threads = []
        for job, limit in jobs_to_scrape:
            thread = threading.Thread(target=scrape_job_data, args=(job, limit))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        return JsonResponse({"message": "Scraping completed!"})





# from .models import upwork, dataa, my_table
# from .serializers import upworkSerializer
# from django.http import JsonResponse
# from selenium import webdriver
# import time
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.proxy import Proxy, ProxyType
# import threading

# # Helper function to perform the scraping for each job
# def scrape_job_data(job, limit):
#     options = Options()
#     driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#     driver.get("https://www.upwork.com/freelance-jobs/")
#     driver.maximize_window()

#     search_result_link = []
#     sPython = driver.find_element(By.LINK_TEXT, job)
#     search_result_link.append(sPython.get_attribute('href'))
#     print('search_result_link----------------------->',search_result_link)

#     jobdesc = []
#     element = []
#     driver.get(sPython.get_attribute('href'))
#     driver.maximize_window()
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     for response in soup.select('section[data-qa-section="job-grid"] > div.container > div.air3-grid-container > div > div.job-tile-wrapper > section > div.job-tile-content'):
#         title = response.a.get('href')
#         element.append({
#             'title': title,
#         })
#     print('element-------------------------->',element)    
#     upId = upwork.objects.filter(up_name=job, limit=limit).first()
#     count = 0
#     for x in element:
#         if count < limit:
#             full_link = "https://www.upwork.com" + x['title']
#             print("fullLink>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",full_link)
#             driver.get(full_link)
#             driver.maximize_window()

#             soup = BeautifulSoup(driver.page_source, "html.parser")
#             for response in soup.select('div[class="col-12 cfe-ui-job-details-content"] > header'):
#                 job_name = response.h1.get_text(strip=True)
#                 job_description = soup.find('div', {'class': 'job-description break mb-0'}).text
#                 skills = soup.findAll('span', class_=['cfe-ui-job-skill up-skill-badge disabled m-0-left m-0-top m-xs-bottom'])
                
#                 mytbId=my_table.objects.filter(upwork_entry=upId.id ,JobName=job_name, JobDescription=job_description).first()
                   
#                 for skill in skills:
#                     skill = skill.text.replace('\n', '')
#                     print(" skills='" + skill + "'")
#                     if mytbId:
#                         my_result = dataa.objects.filter(data_skills=skill).values()
#                         print(my_result)
#                         if not my_result:
#                             new_data = dataa.objects.create(data_skills=skill)
#                 new_rec = my_table.objects.create(JobName=job_name, JobDescription=job_description, upwork_entry=upId)

#                 jobdesc.append({
#                     'JobName': job_name,
#                     'JobDescription': job_description,
#                     'skill': skills
#                 })
#             count += 1
#     driver.quit()

# def get_data(request):
#     if request.method == 'GET':
#         up = upwork.objects.all()
#         serializer = upworkSerializer(up, many=True)

#         jobs_to_scrape = []
#         for data in serializer.data:
#             job = data['up_name']
#             limit = data['limit']
#             jobs_to_scrape.append((job, limit))
#         print('jobs_to_scrape------------------------->',jobs_to_scrape)    

#         threads = []
#         for job, limit in jobs_to_scrape:
#             thread = threading.Thread(target=scrape_job_data, args=(job, limit))
#             thread.start()
#             threads.append(thread)
#         # print('threads---------------------------->',threads)    

#         for thread in threads:
#             thread.join()

#         return JsonResponse({"message": "Done Scraping successfully!!!"})




