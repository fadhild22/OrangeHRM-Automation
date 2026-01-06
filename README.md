# 🍊 OrangeHRM Automation Framework

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?style=for-the-badge&logo=selenium)
![Pytest](https://img.shields.io/badge/Pytest-Framework-yellow?style=for-the-badge&logo=pytest)

## 📋 Project Overview
This repository contains a robust and scalable **Test Automation Framework** developed for the [OrangeHRM Demo Website](https://opensource-demo.orangehrmlive.com/). 

## 🧪 Test Scenarios Covered
You can view the detailed manual test cases (Steps, Expected Results, and Test Data) in the spreadsheet below:

👉 [**Klik Disini: Test Case SpreadSheet**](https://docs.google.com/spreadsheets/d/1yLw1urhdShecnJPM9RFXwWDIQmJjo69pTQBGz0IsdC4/edit?usp=sharing)

The framework is built using **Python** and **Selenium WebDriver**, implementing the **Page Object Model (POM)** design pattern to ensure code reusability and maintainability. It is designed to handle dynamic web elements, server latency, and complex test data dependencies.

## ✅ Apa Saja yang Saya Lakukan?
Dalam project ini, saya tidak hanya mengecek "Flow Positif" (Happy Path), tapi juga memastikan website aman dari error melalui "Flow Negatif".

1.  **End-to-End Testing**: Simulasi user asli, mulai dari Login -> Tambah Employee -> Buat User Admin -> Logout.
2.  **Negative Testing**: Sengaja memasukkan password salah atau data duplikat untuk melihat apakah website memblokirnya.
3.  **Handling Loading**: Membuat script "sabar" menunggu jika website sedang lemot supaya tidak timeout.
4.  **Dynamic Data**: Menggunakan data acak (random) agar test bisa dijalankan berkali-kali tanpa error "Data Sudah Ada".

## 🛠️ Tech Stack
* **Language:** Python
* **Web Automation:** Selenium WebDriver
* **Testing Framework:** Pytest

## 📂 Project Structure
```text
OrangeHRM-Automation/
├── pages/                  # Page Object Classes
│   ├── base_page.py        # Wrapper for Selenium methods (Wait, Click, Input)
│   ├── login_page.py       # Locators & Methods for Login
│   ├── dashboard_page.py   # Locators & Methods for Dashboard
│   ├── pim_page.py         # PIM Module logic (Add/Edit/Delete Employee)
│   └── admin_page.py       # Admin Module logic (User Management)
├── test/                   # Test Scripts
│   ├── test_login.py       # Login scenarios
│   ├── test_pim.py         # Employee management scenarios
│   └── test_admin.py       # Admin user management scenarios
├── screenshots/            # Auto-captured screenshots on failure
├── config.py               # Configuration & Data Generators
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

## 💻 Cara Menjalankan Script Ini
Jika kamu ingin mencoba menjalankan script ini di komputer kamu:

1.  Download repository ini (klik tombol **Code** > **Download ZIP**).
2.  Pastikan kamu sudah install **Python** dan **Google Chrome**.
3.  Buka folder project ini di terminal / CMD.
4.  Install library pendukung dengan mengetik:
    ```bash
    pip install -r requirements.txt
    ```
5.  Jalankan testnya dengan perintah:
    ```bash
    pytest test/ -v -s --html=laporan.html
    ```
    *(Nanti akan muncul file `laporan.html` yang berisi hasil test lengkap)*

---
**Dibuat oleh:** [Fadhil Darussalam]
*Project ini dibuat untuk tujuan belajar dan portofolio QA API Automation.*
