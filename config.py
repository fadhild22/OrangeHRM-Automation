class Config:
    BASE_URL_UI = "https://opensource-demo.orangehrmlive.com/"
    TIMEOUT = 10
    
    ADMIN_USER = "Admin"
    ADMIN_PASS = "admin123"
    
    INVALID_PASS = "password_salah"
    INVALID_USER = "salahuser"
    
    TIMESTAMP = str(int(time.time()))
    
    NEW_ADMIN_USER = f"Riskiwolfgang{TIMESTAMP}"
    NEW_JOB_TITLE = f"QA Lead {TIMESTAMP}"
    
    EMP_FIRST_NAME = "Ahmad"
    EMP_LAST_NAME = f"Dhani_{TIMESTAMP}"
    EMP_ID = str(random.randint(10000, 99999))
    
    CANDIDATE_EMAIL = f"test{TIMESTAMP}@mail.com"
    VACANCY_NAME = f"Vacancy {TIMESTAMP}"
    
    BUZZ_POST_TEXT = f"Automation Test Post {TIMESTAMP} - Hello World!"