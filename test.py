import base64
import os.path
import time
from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from  selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput



desired_cap = {
  "appium:deviceName": "1365351932001U4",
  "platformName": "Android",
  "appium:appPackage": "com.flipkart.android",
  "appium:appWaitActivity": "com.flipkart.android.activity.FirstLaunchActivity",
  "appium:app": "C:\\Users\\USER\\Downloads\\com.flipkart.android.1500500.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout").click()
driver.implicitly_wait(30)
driver.start_recording_screen()
driver.find_element_by_id("com.flipkart.android:id/select_btn").click()
driver.implicitly_wait(30)
driver.find_element_by_id("com.google.android.gms:id/cancel").click()
driver.find_element_by_id("com.flipkart.android:id/tv_right_cta").click()
driver.implicitly_wait(30)
driver.find_element_by_id("com.flipkart.android:id/phone_input").send_keys("gk2751971@gmail.com")
driver.find_element_by_id("com.flipkart.android:id/button").click()
driver.find_element_by_id("com.flipkart.android:id/phone_input").send_keys("geetha@123")
driver.find_element_by_id("com.flipkart.android:id/button").click()
driver.implicitly_wait(30)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.widget.ImageView").click()
time.sleep(10)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.ImageView").click()
driver.find_element_by_id("com.flipkart.android:id/search_icon").click()
driver.find_element_by_id("com.flipkart.android:id/search_autoCompleteTextView").send_keys("Mobiles")
time.sleep(5)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]").click()
driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()
for i in range(5):
  actions = ActionChains(driver)
  actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
  actions.w3c_actions.pointer_action.move_to_location(363, 1065)
  actions.w3c_actions.pointer_action.pointer_down()
  actions.w3c_actions.pointer_action.move_to_location(375, 273)
  actions.w3c_actions.pointer_action.release()
  actions.perform()
  time.sleep(5)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[1]").click()
time.sleep(5)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView").click()
#driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Back Button']").click()
#time.sleep(4)
#driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView").click()
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup").click()
#driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
video_rawdata = driver.stop_recording_screen()
video_name = driver.current_activity + time.strftime("%y_%m_%d_%H%M%S")
filepath=os.path.join("/Users/USER/PycharmProjects/pythonProject/Screenshot/", video_name + ".mp4")
with open(filepath, "wb") as video:
  video.write(base64.b64decode(video_rawdata))

