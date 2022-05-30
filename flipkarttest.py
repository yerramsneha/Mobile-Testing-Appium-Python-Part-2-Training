from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

desired_cap = {
  "appium:deviceName": "Android Emulator",
  "platformName": "Android",
  "appium:appPackage": "com.flipkart.android",
  "appium:appWaitActivity": "com.flipkart.android.activity.FirstLaunchActivity",
  "appium:app": "D:\\Downloads\\Flipkart-7.18.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(30)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageView[1]").click()

driver.find_element_by_id("com.flipkart.android:id/select_btn").click()
driver.find_element_by_id("com.flipkart.android:id/tv_right_cta").click()
driver.find_element_by_id("com.flipkart.android:id/phone_input").send_keys("sivakarthikunnikrishnan@gmail.com")
driver.find_element_by_id("com.flipkart.android:id/button").click()
driver.find_element_by_id("com.flipkart.android:id/phone_input").send_keys("sivakarthik34")
driver.find_element_by_id("com.flipkart.android:id/button").click()

driver.find_element_by_id("com.flipkart.android:id/search_widget_textbox").click()
driver.find_element_by_id("com.flipkart.android:id/search_autoCompleteTextView").send_keys("PD chargers")
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]").click()
driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()
for i in range(4):
  actions = ActionChains(driver)
  actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
  actions.w3c_actions.pointer_action.move_to_location(544, 2002)
  actions.w3c_actions.pointer_action.pointer_down()
  actions.w3c_actions.pointer_action.move_to_location(569, 786)
  actions.w3c_actions.pointer_action.release()
  actions.perform()

driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]").click()
s = time.strftime("%Y_%m_%d_%H%M%S")
activityname = driver.current_activity
filename = activityname + s
driver.save_screenshot("/Users/sivak/PycharmProjects/pythonFlipkart/Screenshot/" + filename + ".png")

driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup").click()
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup").click()

