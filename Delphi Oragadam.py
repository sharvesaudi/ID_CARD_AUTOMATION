from selenium import webdriver
import time
import pandas as pd
import xlrd
from datetime import datetime
import math
import numpy

driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('http://chennairfid.com/delphi-oragadam/admin/')

# Login with admin
passs = driver.find_element("name", "admin_password")
passs.send_keys("delphi105")
btn = driver.find_element("name", "login_submit")
btn.click()

# click general
element = driver.find_element("xpath", "/html/body/center/table/tbody/tr[2]/td[2]/a")
element.click()

# Add new employee
element2 = driver.find_element("xpath", "/html/body/a[2]")
element2.click()

df = pd.read_excel('C:\\My Files\\Coding\\Photo\\test.xlsx')
l = len(df.columns)
r = len(df)

for i in range(r):
    driver.get('http://chennairfid.com/delphi-oragadam/admin/manage-employees/?evnt=new&did=1')
    ele1 = driver.find_element("name", "employee_name")
    ele1.send_keys(str(df.iloc[i][0]))

    ele2 = driver.find_element("name", "father_name")
    ele2.send_keys(str(df.iloc[i][1]))

    ele3 = driver.find_element("name", "employee_number")
    ele3.send_keys(str(df.iloc[i][2]))

    ele4 = driver.find_element("name", "cc_number")
    ele4.send_keys(str(df.iloc[i][3])) 

    ele5 = driver.find_element("name", "employee_mobile")
    ele5.send_keys(str(df.iloc[i][4]))
 
    ele6 = driver.find_element("name", "blood_group")
    ele6.send_keys(str(df.iloc[i][5]))

    ele7 = driver.find_element("name", "present_address")
    ele7.send_keys(str(df.iloc[i][6])) 

    ele8 = driver.find_element("name", "permanent_address")
    ele8.send_keys(str(df.iloc[i][7])) 

    ele9 = driver.find_element("name", "birth_date")
    today_date1 = df.iloc[i][8] 
    # .strftime('%d.%m.%Y')
    ele9.send_keys(today_date1)

    ele10 = driver.find_element("name", "join_date")
    today_date2 = df.iloc[i][9]
    # .strftime('%d.%m.%Y')
    ele10.send_keys(today_date2)
    
    ele11 = driver.find_element("name", "issue_date")
    ele11.send_keys(df.iloc[i][10])
    # if(len(str(df.iloc[i][10]))>15):
    #     today_date3 = df.iloc[i][10].strftime('%d.%m.%Y')
    #     ele11.send_keys(today_date3)

    # elif(len(str(df.iloc[i][10]))==3):
    #     ele11.send_keys("") 
    
    ele12 = driver.find_element("name", "submit")
    ele12.click()

    print("Uploaded Number: ", i)   
