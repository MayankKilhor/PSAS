# from flask import Flask

from selenium import webdriver
import os
# from urllib3 import urlopen
from contextlib import closing
import xml.etree.ElementTree
from getpass import getpass
import pyowm
import re
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from google_images_download import google_images_download
import urllib3

from simple_image_download import simple_image_download as simp

http = urllib3.PoolManager()

url = 'http://www.thefamouspeople.com/singers.php'
response = http.request('GET', url)
soup = BeautifulSoup(response.data)
#Optimisation - 1, Using msvcrt module to break down runtime of code in sections
import msvcrt
#User Menu, Input based module selection
print("\n\t\t\t\t\tWelcome to the Python and Selenium toolset\n")
pp=1
while(pp>0):
    print("1. Multiple Link opener")
    print("2. Weather report")
    print("3. Image scraper")
    print("4. News scraper")
    print("5. Facebook login automation\n")
    print("6. Exit\n")
    n=input("Enter your selection: ")
    try:
        n=int(n)
    except:
        print("\nERROR: String input, please try again\n")
        print('\npress any key to continue: ')
        char = msvcrt.getch()
        continue
    #Accessing the Multiple link opener module
    if(n==1):
        k=int(input('With prefix (https://www.) (1) or without (2) ?'))
        s=input('Enter the links to be opened: (separated by spaces): ')
        l=s.split()
        t=len(l)
        #Optimisation - 2, creating list through implicit list iterations
        if(k==2):
            for elements in l:
                elements = ['https://www.' + elements + '' for elements in l]
        elif(k==1):
            for elements in l:
                elements = [elements for elements in l]
        def open_tab_page(page, page_number):
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[page_number])
            driver.get(page)
        # initialise driver
        driver = webdriver.Firefox()
        driver.get("https://www.google.com")
        page_number = 1
        for page in elements:
            open_tab_page(page, page_number)
            page_number +=1
        print('\npress any key to exit: ')
        char = msvcrt.getch()
        print('\n')
    #Accessing the Weather report module
    elif(n==2):
        owm=pyowm.OWM('3282e54688306ae3571e778e51429885')
        s=input('Enter the city to get weather details: ')
        print("\n")
        observation = owm.weather_at_place(s)
        weather = observation.get_weather()
        temperature=weather.get_temperature('celsius')['temp']
        wind = weather.get_wind()['speed']
        humid = weather.get_humidity()
        status = weather.get_detailed_status()
        print('The temperature in '+s+' is '+ str(temperature) + ' degrees celsius')
        print('Wind speeds are '+str(wind)+' m/s')
        print('Humidity is '+str(humid)+' %')
        print('Current status of '+s+' is '+status)
        print('\npress any key to exit: ')
        char = msvcrt.getch()
        print('\n')
    #Accessing the Image scraper module
    elif(n==3):
        #Using OS directory to create folders in working directory
          
  
            # creating object 
        response2 = google_images_download.googleimagesdownload()  
        response = simp.simple_image_download    
            
            
        def downloadimages(query,n): 
            
            arguments = {"keywords": query, 
                        "format": "jpg", 
                        "limit":n, 
                        "print_urls":True, 
                        "size": "medium", 
                        "aspect_ratio":"panoramic"} 
            try: 
                response2.download(arguments) 
                  
                from simple_image_download import simple_image_download as simp

                

                response().download(query, n)

                print(response().urls(query, n))
            # Handling File NotFound Error     
            except FileNotFoundError:  
                arguments = {"keywords": query, 
                            "format": "jpg", 
                            "limit":n, 
                            "print_urls":True,  
                            "size": "medium"} 
                            
                # Providing arguments for the searched query 
                try: 
                    # Downloading the photos based 
                    # on the given arguments 
                    response2.download(arguments)  
                except: 
                    pass
        if __name__ == '__main__':
            word = input("Input key word: ")
            n = int(input("Enter the number of images required: "))
            
            downloadimages(word,n)
            # download_baidu(word,word)
            print('\npress any key to exit: ')
            char = msvcrt.getch()
    #Accessing the News scraper module
    elif(n==4):
        # xml_data = requests.get(news_url).content

        # soup = BeautifulSoup(xml_data, "xml")
        # with closing(requests.get(news_url).content) as page:
        #     xml_page = page.read()
        news_url = "https://news.google.com/news/rss"
        xml_page=requests.get(news_url).content
        print("\nDisplaying the top 5 stories of today:\n")
        e = xml.etree.ElementTree.fromstring(xml_page)
        print(xml_page)
        p = 1
        for it in e.iter('item'):
            if(p>5):
                break
            if(p==5):
                print(it.find('title').text)
                print(it.find('link').text)
                print(it.find('pubDate').text)
                p=p+1
            else:
                print(it.find('title').text)
                print(it.find('link').text)
                print(it.find('pubDate').text)
                print('\n')
                char = msvcrt.getch()
                p=p+1
        #Optimisation - 4 , using the msvcrt module to break loop operations
        # according to user input.
        print('\npress any key to exit: ')
        char = msvcrt.getch()
        input()
    #Accessing the Facebook automated login module
    elif(n==5):
        username=input('Enter username:')
        password=getpass()
        url='https://facebook.com'
        driver = webdriver.Firefox()
        driver.get(url)
        driver.find_element_by_id('email').send_keys(username)
        driver.find_element_by_id('pass').send_keys(password)
        driver.find_element_by_id('loginbutton').click()
        print('\npress any key to exit: ')
        char = msvcrt.getch()
    elif(n==6):
        print("Exitiing!")
        break
    #In case of invalid input
    else:
        print("Invalid input")
        print('\npress any key to continue: ')
        char = msvcrt.getch()
