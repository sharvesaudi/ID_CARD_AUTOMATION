from selenium import webdriver
import time
import pandas as pd


driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('https://idcard.cloud/apex-research-development/admin/ ')

# Login with admin
passs = driver.find_element("name", "admin_password")
passs.send_keys("Apex117")
btn = driver.find_element("name", "login_submit")
btn.click()

# click general
element = driver.find_element("xpath", "/html/body/center/table/tbody/tr[2]/td[2]/a")
element.click()

# Add new employee
element2 = driver.find_element("xpath", "/html/body/a[2]")
element2.click()

df = pd.read_excel('test_main.xlsx')
l = len(df.columns)
r = len(df)

for i in range(r):
    driver.get('https://idcard.cloud/apex-research-development/admin/manage-employees/?evnt=new&did=1')
    ele1 = driver.find_element("name", "employee_name")
    ele1.send_keys(str(df.iloc[i][0]))

    ele2 = driver.find_element("name", "employee_number")
    ele2.send_keys(int(str(df.iloc[i][1])))


    ele4 = driver.find_element("name", "address")
    ele4.send_keys(str(df.iloc[i][2])) 

    ele5 = driver.find_element("name", "emergency_contact")
    ele5.send_keys(str(df.iloc[i][3]))

    ele6 = driver.find_element("name", "blood_group")
    ele6.send_keys(str(df.iloc[i][4]))

    ele12 = driver.find_element("name", "submit")
    ele12.click()

    print("Uploaded Number: ", i+1," ",str(df.iloc[i][1]))   
