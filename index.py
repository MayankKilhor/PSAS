from flask import Flask, redirect, request, url_for, render_template
import pyowm
import requests
from selenium import webdriver
from getpass import getpass
import xml.etree.ElementTree
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from simple_image_download import simple_image_download as simp
import urllib3

app= Flask(__name__)
http = urllib3.PoolManager()
url = 'http://www.thefamouspeople.com/singers.php'
response = http.request('GET', url)
news={1:{'title':'','link':'','pubDate':''},2:{'title':'','link':'','pubDate':''},3:{'title':'','link':'','pubDate':''},4:{'title':'','link':'','pubDate':''},5:{'title':'','link':'','pubDate':''}}
links={1:news[1]['link'],2:news[2]['link'],3:news[3]['link'],4:news[4]['link']}
soup = BeautifulSoup(response.data)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/task2')
def task2():
    return render_template('task2.html')

@app.route("/task2/result",methods=['POST'])
def task2_results():
    owm=pyowm.OWM('3282e54688306ae3571e778e51429885')
    s = request.form['location']
    observation = owm.weather_at_place(s)
    weather = observation.get_weather()
    temperature=weather.get_temperature('celsius')['temp']
    wind = weather.get_wind()['speed']
    humid = weather.get_humidity()
    status = weather.get_detailed_status() 
    return render_template("task2_result.html",location=s,temp=str(temperature),wind=str(wind),humid=str(humid),status=str(status))

@app.route('/task1')
def task1():
    return render_template('task1.html')

@app.route('/task1',methods=['POST'])
def task1_option():
    option=request.form['option']
    link=request.form['link']
    l=link.split()
    t=len(l)

    if(option=="2"):
        for elements in l:
            elements=['https://www.' + elements + '' for elements in l]
    
    elif(option=="1"):
            for elements in l:
                elements=[elements for elements in l]

    driver = webdriver.Firefox()
    driver.get("https://www.google.com")
    page_number = 1
    for page in elements:
        # open_tab_page(page, page_number)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[page_number])
        driver.get(page)
        page_number +=1
    return render_template('task1_result.html')

@app.route('/task5')
def task5():
    return render_template('task5.html')

@app.route("/task5",methods=['POST'])
def task5_result():
    username=request.form['username']
    password=request.form['password']
    url='https://facebook.com'
    driver = webdriver.Firefox()
    driver.get(url)
    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('pass').send_keys(password)
    #driver.find_element_by_id('loginbutton').click()
    return render_template('task5_result.html')

@app.route("/task3")
def task3():
    return render_template('task3.html')

@app.route("/task3",methods=['POST'])
def task3_result():
    key=request.form['key']
    num=int(request.form['num'])
    response = simp.simple_image_download 
    imageurl1=response().urls(key,num) 
    try:
        response().download(key,num)
        imageurl1=response().urls(key, num)
    except:
        pass
    return render_template('task3_result.html',imageurl=imageurl1)
@app.route('/task4')
def task4():
    news_url = "https://news.google.com/news/rss"  
    xml_page=requests.get(news_url).content
    e= xml.etree.ElementTree.fromstring(xml_page)
    p = 1
    # news={1:{'title':'','link':'','pubDate':''},2:{'title':'','link':'','pubDate':''},3:{'title':'','link':'','pubDate':''},4:{'title':'','link':'','pubDate':''},5:{'title':'','link':'','pubDate':''}}
    for it in e.iter('item'):
        if(p>4):
            break
        if(p==4):
            news[p]['title']=it.find('title').text
            news[p]['link']=it.find('link').text
            news[p]['pubDate']=it.find('pubDate').text
            p=p+1
        else:
            news[p]['title']=it.find('title').text
            news[p]['link']=it.find('link').text
            news[p]['pubDate']=it.find('pubDate').text
            
            p=p+1
    # links={1:news[1]['link'],2:news[2]['link'],3:news[3]['link'],4:news[4]['link'],5:news[5]['link']}
    #Optimisation - 4 , using the msvcrt module to break loop operations
    # according to user input.
    # print('\npress any key to exit: ')
    # char = msvcrt.getch()
    # input()
    
    return render_template('task4.html',news=news,links=links)



if __name__ == "__main__":
    app.run(debug=True)
