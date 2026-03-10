# QA Automation Portfolio - Playwright + Python

![Python](https://img.shields.io/badge/python-3.11-blue)
![Pytest](https://img.shields.io/badge/pytest-6.x-green)
![Playwright](https://img.shields.io/badge/playwright-1.x-purple)
![Build Status](https://img.shields.io/github/actions/workflow/status/YOUR_USERNAME/YOUR_REPO/python-tests.yml?branch=main)

This project is a **QA Automation portfolio** built with **Python, Playwright, and Pytest**.  
It demonstrates automated web testing on [SauceDemo](https://www.saucedemo.com/), including **login scenarios, cart actions, and logout**.

---

## 🎯 Project Goal

- Showcase **QA Automation skills** using Python and Playwright.  
- Implement clean, maintainable automated tests with **Page Objects**.  
- Provide a professional **portfolio-ready project**.

---

## 📂 Project Structure

```
qa-automation-playwright/
│
├── tests/                  
│   ├── test_login.py       # Positive and negative login tests
│   ├── test_cart.py        # Add to Cart test
│   └── test_logout.py      # Logout test
├── pages/                  
│   ├── login_page.py       # LoginPage class
│   ├── products_page.py    # ProductsPage class
│   └── home_page.py        # HomePage class (Logout)
└── .venv/                  
```

- `tests/` → all automated test scripts  
- `pages/` → **Page Objects** for reusability and clean structure  
- `.venv/` → Python virtual environment  

---

## ⚙️ Environment Setup

1. Create a project in **PyCharm** using a **venv**.  
2. Install required packages:

```bash
pip install playwright pytest
playwright install
```

3. Ensure **pytest** is installed in PyCharm:  
   - Preferences → Project → Python Interpreter → install `pytest` if missing  

4. **Run tests using pytest**, not by running the script directly.

---

## 📝 Implemented Tests

### ✅ Login Positive Test

- Username: `standard_user`  
- Password: `secret_sauce`  
- Validates successful login and redirects to inventory page.  

### ❌ Login Negative Test

- Username: `invalid_user`  
- Password: `wrong_password`  
- Captures the error message:  
  `"Username and password do not match any user"`  
- Verifies the error is displayed correctly.

### 🛒 Add to Cart Test

- Adds "Sauce Labs Backpack" to the cart.  
- Verifies that the cart count badge shows `1`.  
- Uses **ProductsPage Page Object**.

### 🔑 Logout Test

- Logs in with standard user.  
- Opens menu and clicks logout.  
- Verifies that the URL returns to login page `/`.  
- Uses **HomePage Page Object**.

---

## ▶️ How to Run the Tests

1. Right-click the **`tests`** folder → **Run 'pytest in tests'**  
2. The **Chromium browser** will open visibly (`headless=False`).  
3. The tests execute in order:
   - Login positive and negative  
   - Add to cart  
   - Logout  
4. Test results appear in PyCharm console.

> ⚠️ Do **not** run test files directly — the browser won’t open.

---

## 💡 Applied Best Practices

- **Page Objects** → clean, reusable code  
- **Positive & negative tests** → basic QA coverage  
- **Delays (`time.sleep()`)** → visually track test flow  
- **Pytest** → professional test execution  
- Tests are **small, focused, and assertive** for readability.

---

## 📌 Next Steps for Portfolio

- Add **Remove from Cart** test  
- Add **Checkout flow** (end-to-end)  
- Generate **HTML test reports**  
- Version control with **GitHub**, frequent commits  
- Add **GitHub Actions workflow** with badge for CI status

---

## 💻 Technologies Used

- Python 3.x  
- Playwright  
- Pytest  
- PyCharm IDE  
- Chromium (via Playwright)

---

## 📊 Expected Results

- Browser opens visibly for each test  
- Login, Add to Cart, and Logout flow executes successfully  
- Console shows test passes, e.g.:

```
tests/test_login.py ..                                           [50%]
tests/test_cart.py .                                            [75%]
tests/test_logout.py .                                          [100%]

============================== 4 passed in 12.34s ============================
```

- Clean, maintainable code ready for **portfolio presentation**