import time
# 인코딩 문제 해결을 위한 2줄 추가 (한글/이모지 깨짐 방지)
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from appium import webdriver
from appium.options.android import UiAutomator2Options

# 1. 설정
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "MyPhone"
# 패키지명 확인하세요
options.app_package = "com.example.nipa3_app"
options.app_activity = "com.example.nipa3_app.LoginActivity"
options.no_reset = True

# 2. 실행
try:
    print("[GitHub Command] Try to open app...")  # 영어로 변경 (안전)
    
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    
    print("SUCCESS! App opened. Waiting 5 sec...") # 영어로 변경
    time.sleep(5)
    
    print("Closing app...") # 영어로 변경
    driver.quit()
    
except Exception as e:
    print(f"FAIL! Error: {e}") # 영어로 변경
    raise e