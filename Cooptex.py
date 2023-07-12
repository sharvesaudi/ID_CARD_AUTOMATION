#automation
from selenium import webdriver
import time
import pandas as pd


driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('http://chennairfid.com/cooptex-tirunelveli/admin/manage-employees/')

# Login with admin
passs = driver.find_element("name", "admin_password")
passs.send_keys("Cooptex001")
btn = driver.find_element("name", "login_submit")
btn.click()

# click Batch 23
element = driver.find_element("xpath", "/html/body/center/table/tbody/tr[2]/td[2]/a")
element.click()

# Add new employee
element2 = driver.find_element("xpath", "/html/body/a[2]")
element2.click()

df = pd.read_excel('test_main.xlsx')
# df = open('ID_CARD_AUTOMATION\test_main.xlsx','r')
l = len(df.columns)
r = len(df)

for i in range(r):
    driver.get('http://chennairfid.com/cooptex-tirunelveli/admin/manage-employees/?evnt=new&did=1')
    ele1 = driver.find_element("name", "employee_name")
    ele1.send_keys(str(df.iloc[i][0]))

    ele2 = driver.find_element("name", "employee_designation")
    ele2.send_keys(str(df.iloc[i][1]))

    ele3 = driver.find_element("name", "employee_number")
    ele3.send_keys(str(df.iloc[i][2]))

    ele4 = driver.find_element("name", "employee_mobile")
    if(len(str(df.iloc[i][3]))==3):
        ele4.send_keys("")
    else:
        ele4.send_keys(int(float(str(df.iloc[i][3])))) 

    ele5 = driver.find_element("name", "employee_email")
    ele5.send_keys(str(df.iloc[i][4]))

    ele6 = driver.find_element("name", "pf_number")
    ele6.send_keys(str(df.iloc[i][5]))
 
    ele7 = driver.find_element("name", "blood_group")
    if(len(str(df.iloc[i][6]))==3):
        ele7.send_keys("")
    else:
        ele7.send_keys(str(df.iloc[i][6]))

    ele8 = driver.find_element("name", "address")
    ele8.send_keys(df.iloc[i][7])

    ele9 = driver.find_element("name", "birth_date")
    ele9.send_keys(df.iloc[i][8])

    ele10 = driver.find_element("name", "retirement_date")
    ele10.send_keys(df.iloc[i][9])  

    ele11 = driver.find_element("name", "submit")
    ele11.click()

    print("Uploaded Number: ", i+1," ",str(df.iloc[i][2]))   
