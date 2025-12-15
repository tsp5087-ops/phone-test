# 파일명: simple_start.py
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options

# 1. 설정
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "MyPhone"
# 아까 찾으신 정확한 패키지명
options.app_package = "com.example.nipa3_app"
options.app_activity = "com.example.nipa3_app.LoginActivity"
options.no_reset = True

# 2. 실행
try:
    print("🚀 [GitHub 명령] 앱 실행을 시도합니다...")
    # 내 컴퓨터(로컬)의 Appium에 연결
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    
    print("✅ 앱이 켜졌습니다! 5초간 대기...")
    time.sleep(5)
    
    print("👋 앱을 종료합니다.")
    driver.quit()
    
except Exception as e:
    print(f"❌ 실패! 원인: {e}")
    # 깃허브가 실패를 알 수 있게 에러를 다시 던짐
    raise e