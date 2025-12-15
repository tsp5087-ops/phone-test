import time
import sys
import io
import os
import requests
import subprocess # 윈도우 명령어를 쓰기 위한 도구

# 한글 깨짐 방지
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ---------------------------------------------------------
# [설정] 내 슬랙 주소 (여기에 직접 복사해서 넣으세요!)
# 로컬에서 돌릴 때는 깃허브 금고를 못 쓰니까, 직접 적어야 합니다.
SLACK_URL = "" 
# ---------------------------------------------------------

def send_slack(msg):
    if SLACK_URL:
        try:
            requests.post(SLACK_URL, json={"text": msg})
            print("LOG: 슬랙 알림 전송 완료")
        except Exception as e:
            print(f"WARNING: 전송 실패 - {e}")

print("[투명 감시자] ADB 기술로 화면을 훔쳐봅니다... (방해 안 함)")

try:
    while True:
        # 1. ADB 명령어로 현재 화면 정보 긁어오기 (투명 기술)
        # "dumpsys window"는 폰의 화면 정보를 다 보여주는 명령어입니다.
        result = subprocess.run(
            ['adb', 'shell', 'dumpsys', 'window', 'displays'], 
            capture_output=True, 
            text=True, 
            encoding='utf-8', # 한글 윈도우 호환
            errors='ignore'
        )
        output = result.stdout

        # 2. 화면 이름 찾기 (mCurrentFocus 또는 mFocusedApp)
        # 보통 "패키지명/액티비티명" 형태로 나옵니다.
        if "mCurrentFocus" in output:
            # 텍스트 정리해서 보기 좋게 만듦
            for line in output.splitlines():
                if "mCurrentFocus" in line:
                    print(f"[감시 중] {line.strip()}")
                    
                    # 3. 로그인 성공 화면(MainActivity)이 보이면?
                    if "MainActivity" in line:
                        print("\n🚨 [포착] 로그인 성공 화면 발견!")
                        send_slack("🚀 [CCTV 알림] 깃허브가 로그인을 성공시켰습니다! (MainActivity 진입)")
                        
                        # 알림 보내고 종료하려면 break, 계속 감시하려면 break 지우기
                        print("감시를 종료합니다.")
                        sys.exit() 
                        
        time.sleep(1) # 1초마다 확인

except KeyboardInterrupt:
    print("\n감시를 강제로 종료합니다.")