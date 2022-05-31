import time

from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

desired_cap = {"appium:deviceName": "Android Emulator",
               "platformName": "Android",
               "appium:appPackage": "com.flipkart.android",
               "appium:appWaitActivity": "com.flipkart.android.activity.FirstLaunchActivity",
               "appium:app": "C:\\Users\\DELL\\Downloads\\Flipkart-7.18.apk"}

driver = webdriver.Remote( "http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout").click()
driver.find_element_by_id("com.flipkart.android:id/select_btn").click()
driver.find_element_by_id("com.flipkart.android:id/tv_right_cta").click()
driver.find_element_by_id("com.flipkart.android:id/phone_input").send_keys("melvinnirmala@gmail.com")
driver.find_element_by_id("com.flipkart.android:id/button").click()
driver.find_element_by_id("com.flipkart.android:id/phone_input").send_keys("Mel@007")
driver.find_element_by_id("com.flipkart.android:id/button").click()
driver.implicitly_wait(30)
driver.find_element_by_id("com.flipkart.android:id/search_widget_textbox").click()
driver.implicitly_wait(30)
driver.find_element_by_id("com.flipkart.android:id/search_autoCompleteTextView").send_keys("iphone13")
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]").click()
driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()
driver.implicitly_wait(30)
#screenshot
s = time.strftime("%Y_%m_%d_%H%M%S")
activityname = driver.current_activity
filename = activityname + s
driver.save_screenshot("/Users/DELL/PycharmProjects/pythonProject/screenshot/" + filename + ".png")
#scrolling
for i in range(5):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(374, 1177)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(374, 446)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    time.sleep(3)
#adding to cart
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.ImageView[1]").click()
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup").click()




