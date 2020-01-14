# Get the relevent web pages
import os,datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
# Construct && Preparations
debug = 0
def __getTime():
    now_time = datetime.datetime.now()
    return now_time.strftime("%H:%M:%S")
def pPT(): #pPT: print Process Time
    return '[' + __getTime() + ']'
def lpr(str): #lpr: log print
    if (debug == 0) print(pPT(),str)
def refresh_Resources(debugOptions = 0):
    global debug
    debug = debugOptions
    lpr("Begin to do the Configurations.")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options = chrome_options)
    login_url = r"http://jwc.bjtu.edu.cn/login_introduce_s.html"
    desti_url = r"https://dean.bjtu.edu.cn/course_selection/courseselect/list_arrange/"
    lpr("Configurations Complete.")
    lpr("Open the Login Page.")
    driver.get(login_url)
    usernameInput = driver.find_element_by_name('TextBoxUserName')
    passwordInput = driver.find_element_by_name('TextBoxPassword')
    LoginButton = driver.find_element_by_name('ButtonLogin')
    usernameInput.send_keys('19211423')
    passwordInput.send_keys('jkw6766034')
    LoginButton.click()
    lpr("Complete the Login.")
    lpr("Open the Manage Page.")
    wait = WebDriverWait(driver,30)
    goto_manage = wait.until(lambda x: x.find_element_by_partial_link_text("新教务系统[师生]"))
    window = driver.current_window_handle
    goto_manage.click()
    sleep(5)
    lpr("Adjust the browser's pages.")
    all_handles = driver.window_handles
    new_window = all_handles[-1]
    driver.switch_to.window(window)
    driver.close()
    driver.switch_to.window(new_window)
    lpr("Get into the Lessons' Display Page.")
    driver.get(desti_url)
    goto_manage = wait.until(lambda x: x.find_element_by_name("submit"))
    goto_manage.click()
    lpr("Begin to download pages.")
    print("\n")
    cnt = 1
    root = ".\\resources\\"
    while (1):
        file_place = root + str(cnt) + ".html"
        with open(file_place,"w",encoding = "utf-8") as f:
            f.write(driver.page_source)
        print("[Finished] Download",driver.current_url,"into the file",file_place)
        cnt = cnt + 1
        try:
            next_page = driver.find_element_by_partial_link_text("下一页")
            next_page.click()
        except:
            quit()
refresh_Resources()
