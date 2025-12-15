import time
import random
    
class Config:
    BASE_URL_UI = "https://opensource-demo.orangehrmlive.com/"
    TIMEOUT = 10
    
    ADMIN_USER = "Admin"
    ADMIN_PASS = "admin123"
    
    EMPTY_USER = ""
    INVALID_PASS = "password_salah"
    
    TIMESTAMP = str(int(time.time()))
        
    NEW_ADMIN_USER = f"Riskiwolfgang{TIMESTAMP}"
    NEW_JOB_TITLE = f"QA Lead {TIMESTAMP}"
    
    EMP_FIRST_NAME = "Riski"
    EMP_LAST_NAME = f"Inrahim{TIMESTAMP}"
    EMP_ID = str(random.randint(10000, 99999))
    
    CANDIDATE_FIRST_NAME = "Truno"
    CANDIDATE_LAST_NAME = f" Pambudi{TIMESTAMP}"
    CANDIDATE_EMAIL = f"pambudi{TIMESTAMP}@mail.com"
    CANDIDATE_VACANCY_NAME = f"QA Junior {TIMESTAMP}"
    
    NAME_VACANCY = f"QA Junior {TIMESTAMP}"
    MANAGER_VACANCY = f"{EMP_FIRST_NAME} {EMP_LAST_NAME}"
    POSISI_VACANCY = "2"
    
    BUZZ_POST_TEXT = f"Hello, i have some interesting news for you guys!{TIMESTAMP}"