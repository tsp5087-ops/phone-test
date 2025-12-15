import time
import sys
import io
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from appium.options.android import UiAutomator2Options

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1. 설정
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "MyPhone"
options.app_package = "com.example.nipa3_app"
options.app_activity = "com.example.nipa3_app.LoginActivity"

# [핵심 수정] False로 변경 -> 앱 켤 때마다 강제 초기화 (무조건 로그인 화면 뜸)
options.no_reset = False 

try:
    print("[GitHub Command] Try to open app...")
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    
    # [수정] 초기화하면 로딩이 길어질 수 있으니 10초 대기
    print("App opened. Waiting 10 sec for loading...")
    time.sleep(10) 

    # (1) 아이디 입력
    print("LOG: Finding ID field...")
    id_input = driver.find_element(AppiumBy.ID, "com.example.nipa3_app:id/idEdit")
    id_input.clear()
    id_input.send_keys("ttatest03")
    print("LOG: ID entered.")

    # (2) 비밀번호 입력
    print("LOG: Finding Password field...")
    pw_input = driver.find_element(AppiumBy.ID, "com.example.nipa3_app:id/passwordEdit")
    pw_input.clear()
    pw_input.send_keys("ttatest03!")
    print("LOG: Password entered.")

    # (3) 로그인 버튼 클릭
    print("LOG: Finding Login button...")
    login_btn = driver.find_element(AppiumBy.ID, "com.example.nipa3_app:id/loginButton")
    login_btn.click()
    print("LOG: Login button clicked!")

    print("Waiting 5 sec...")
    time.sleep(5)
    
    print("Closing app...")
    driver.quit()
    
except Exception as e:
    print(f"FAIL! Error: {e}")
    raise e