import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Wechat_Moment():
  def __init__(self):
    self.desired_caps = {}
    self.desired_caps['platformName'] = 'Android'
    self.desired_caps['deviceName'] = '913eea43'
    self.desired_caps['platformVersion'] = '6.0.1'
    self.desired_caps['appPackage'] = 'com.tencent.mm'
    self.desired_caps['appActivity'] = '.ui.LauncherUI'


    self.start_x = 300
    self.start_y = 800
    self.enf_x = 300
    self.end_y = 300

    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
    self.wait = WebDriverWait(self.driver,300)
    print('微信启动...')


  def login(self):
    login_btn = self.wait.until(EC.element_to_be_clickable((By.ID,'com.tencent.mm:id/ene')))
    login_btn.click()
    phone = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//android.widget.EditText[@resource-id='com.tencent.mm:id/m7']")))
    phone.click()
    phone.send_keys("your username")
    next_page = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//android.widget.Button[@resource-id='com.tencent.mm:id/b2f']")))
    next_page.click()
    password = self.wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.LinearLayout[@resource-id='com.tencent.mm:id/doa']/android.widget.EditText[1]")))
    password.click()
    password.send_keys("your password")
    login = self.wait.until(EC.element_to_be_clickable((By.ID,'com.tencent.mm:id/b2f')))
    login.click()
    no_btn = self.wait.until(EC.element_to_be_clickable((By.ID,'com.tencent.mm:id/b48')))
    no_btn.click()
    print('登录成功')


  def find(self):
    search_btn = self.wait.until(EC.element_to_be_clickable((By.ID,'com.tencent.mm:id/r_')))
    time.sleep(5)
    search_btn.click()
    serarch_input = self.wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.EditText[@resource-id='com.tencent.mm:id/m7']")))
    serarch_input.set_text('houser_chiu')
    print('搜索醉夜歌')
    houser_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//android.widget.RelativeLayout[@resource-id='com.tencent.mm:id/c6t']/android.widget.LinearLayout[2]")))
    houser_btn.click()
    menu_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//android.widget.LinearLayout[@resource-id='com.tencent.mm:id/dl3' and @content-desc='个人相册,共3张']/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]")))
    menu_btn.click()
    print('进入朋友圈...')


  def get_data(self):
    while True:
      items = self.wait.until(EC.presence_of_all_elements_located((By.ID,'com.tencent.mm:id/ezu')))
      self.driver.swipe(self.start_x,self.start_y,self.enf_x,self.end_y,2000)
      for item in items:
        moment_text = item.find_element_by_id("com.tencent.mm:id/pi").get_attribute('text')
        day_text = item.find_element_by_id("com.tencent.mm:id/f5p").get_attribute('text')
        month_text = item.find_element_by_id("com.tencent.mm:id/f5q").get_attribute('text')
        print('抓取到醉夜歌朋友圈数据：%s' %moment_text)
        print('抓取到醉夜歌发布时间：%s月%s日' %(month_text,day_text))


if __name__ == '__main__':
  wc_moment = Wechat_Moment()
  wc_moment.login()
  wc_moment.find()
  wc_moment.get_data()




