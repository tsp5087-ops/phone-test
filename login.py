import time
import sys
import io
# 요소를 찾기 위한 필수 도구
from appium.webdriver.common.appiumby import AppiumBy

# 윈도우 터미널 한글 깨짐 방지
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from appium import webdriver
from appium.options.android import UiAutomator2Options

# 1. 설정
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "MyPhone"
options.app_package = "com.example.nipa3_app"
options.app_activity = "com.example.nipa3_app.LoginActivity"
options.no_reset = True

# 2. 실행
try:
    print("[GitHub Command] Try to open app...")
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    
    print("App opened. Waiting 3 sec...")
    time.sleep(3) 

    # ==========================================
    # 로그인 동작 시작
    # ==========================================

    # (1) 아이디 입력 (찾아오신 ID 사용)
    # com.example.nipa3_app:id/idEdit
    id_input = driver.find_element(AppiumBy.ID, "com.example.nipa3_app:id/idEdit")
    id_input.clear()            # 기존 글자 지우기
    id_input.send_keys("ttatest03")  # 실제 비밀번호 입력
    print("LOG: ID entered.")

    # (2) 비밀번호 입력
    # com.example.nipa3_app:id/passwordEdit
    pw_input = driver.find_element(AppiumBy.ID, "com.example.nipa3_app:id/passwordEdit")
    pw_input.clear()
    pw_input.send_keys("ttatest03!")  # 실제 비밀번호 입력
    print("LOG: Password entered.")

    # (3) 로그인 버튼 클릭
    # com.example.nipa3_app:id/loginButton
    login_btn = driver.find_element(AppiumBy.ID, "com.example.nipa3_app:id/loginButton")
    login_btn.click()
    print("LOG: Login button clicked!")

    # ==========================================

    print("Waiting 5 sec to check result...")
    time.sleep(5)
    
    print("Closing app...")
    driver.quit()
    
except Exception as e:
    print(f"FAIL! Error: {e}")
    raise e