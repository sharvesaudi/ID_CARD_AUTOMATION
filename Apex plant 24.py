#automation
from selenium import webdriver
import time
import pandas as pd


driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('http://chennairfid.com/apex24/admin/manage-employees/')

# Login with admin
passs = driver.find_element("name", "admin_password")
passs.send_keys("Apex110")
btn = driver.find_element("name", "login_submit")
btn.click()

# click Batch 23
element = driver.find_element("xpath", "/html/body/center/table/tbody/tr[2]/td[2]/a")
element.click()

# Add new employee
element2 = driver.find_element("xpath", "/html/body/a[2]")
element2.click()

df = pd.read_excel('C:\\My Files\\Coding\\Photo\\test_main.xlsx')
l = len(df.columns)
r = len(df)

for i in range(r):
    driver.get('http://chennairfid.com/apex24/admin/manage-employees/?evnt=new&did=24')
    ele1 = driver.find_element("name", "employee_name")
    ele1.send_keys(str(df.iloc[i][0]))

    ele2 = driver.find_element("name", "employee_number")
    ele2.send_keys(int(str(df.iloc[i][1])))

    ele3 = driver.find_element("name", "employee_mobile")
    ele3.send_keys(str(df.iloc[i][2]))

    ele4 = driver.find_element("name", "employee_status")
    ele4.send_keys(str(df.iloc[i][3])) 

    ele5 = driver.find_element("name", "address")
    ele5.send_keys(str(df.iloc[i][4]))
 
    ele6 = driver.find_element("name", "blood_group")
    if(len(str(df.iloc[i][5]))==3):
        ele6.send_keys("")
    else:
        ele6.send_keys(str(df.iloc[i][5]))

    # ele7 = driver.find_element("name", "contact_person")
    # if(len(str(df.iloc[i][6]))==3):
    #     ele7.send_keys("")
    # else:
    #     ele7.send_keys(str(df.iloc[i][6])) 

    ele8 = driver.find_element("name", "contact_number")
    if(len(str(df.iloc[i][6]))==3):
        ele8.send_keys("")
    else:
        ele8.send_keys(int(float(str(df.iloc[i][6])))) 
    
    # ele9 = driver.find_element("name", "permanent_address")
    # ele9.send_keys(df.iloc[i][8]) 

    ele10 = driver.find_element("name", "birth_date")
    ele10.send_keys(df.iloc[i][7])

    ele11 = driver.find_element("name", "join_date")
    ele11.send_keys(df.iloc[i][8])  

    ele12 = driver.find_element("name", "submit")
    ele12.click()

    print("Uploaded Number: ", i+1," ",str(df.iloc[i][1]))   
