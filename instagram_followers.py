from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import csv

username=raw_input("Enter your instagram username: ")
password=raw_input("Enter your instagram password: ")



def login(username,password):
    try:
        time.sleep(3)
        driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
        elem=driver.find_element_by_xpath("//input[@name='password']")
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        get_followers_list()
    except Exception as e:
        print 'Following error occured: \n'
        print e



def get_followers_list():
    try:
        driver.get("https://www.instagram.com/%s/"%username)
        time.sleep(3)
        allfoll=driver.find_element_by_xpath("//ul/li[2]/a/span").text.split(',')
        if len(allfoll)>1:
	    allfoll=int(allfoll[0])*(10**len(allfoll[1]))+int(allfoll[1])
        else:
	    allfoll=int(allfoll[0])
        #Prints total number of people your account is following
        print('Followers: ',allfoll)
        time.sleep(2)
        driver.find_element_by_partial_link_text("followers").click()
        time.sleep(3)

    
        ids=set()
        if allfoll>100:
            allfoll=100
        while True:
	    newtags = driver.find_elements_by_xpath("//div[@style='position: relative; z-index: 1;']/div/div[2]/div/div[2]/ul/li/div/div/div/div/a")
	    end=len(newtags)-1
	    last=None
	    for i in range(0,len(newtags)):
		if i==end:
	            last=newtags[i]
		ids.add(newtags[i].text)
            
	    if len(ids)==allfoll:
		break
	    print 'Scanned so far: %r'%len(ids)
	    driver.execute_script("arguments[0].scrollIntoView();",last)
	    time.sleep(1)
        time.sleep(2)
        driver.close()
        csvfile=open("followers.csv",'wt')
        writer=csv.writer(csvfile)
        count=0

        for i in ids:
	    count=count+1
	    csvrow=[]
	    csvrow.append(count)
	    csvrow.append(str(i))
	    writer.writerow(csvrow)

    except Exception as e:
        print 'Following error has occured: \n'
        print e




try:
    print 'Opening browser'
    driver=webdriver.Firefox()
    print 'Browser runnning'
    driver.get("http://www.instagram.com")
    time.sleep(2)
    driver.find_element_by_class_name("_fcn8k").click()
    time.sleep(3)
    #call login function now to login
    login(username,password)

except Exception as e:
    print 'Following error occured: \n'
    print e







