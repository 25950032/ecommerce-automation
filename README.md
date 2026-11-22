# E-commerce Test Automation Framework

A web test automation project developed with **Python, Playwright, Pytest, and Allure Reports**, using the Page Object Model (POM) design pattern.

## Project Overview

This framework automates functional tests for the [SauceDemo](https://www.saucedemo.com/) e-commerce application.

It covers essential user workflows, including login validation, product catalog verification, shopping cart operations, and the complete checkout process.

## Technologies Used

- Python
- Playwright
- Pytest
- Pytest-Playwright
- Allure Reports
- Page Object Model (POM)
- Git and GitHub

## Project Structure

```text
ecommerce-automation/
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_checkout.py
│   └── test_prueba.py
│
├── reports/
│   └── allure-results/
│
├── .gitignore
└── README.md
```

## Test Coverage

| Module | Test Cases | Description |
|---|---:|---|
| Login | 3 | Successful and invalid login scenarios |
| Inventory | 4 | Product catalog, product information, add and remove products |
| Checkout | 1 | Complete purchase workflow |
| Auxiliary | 1 | Basic Python validation |
| **Total** | **9** | |

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ecommerce-automation
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install pytest playwright pytest-playwright pytest-html allure-pytest
```

Install Chromium:

```bash
playwright install chromium
```

## Running Tests

Run all tests:

```bash
python -m pytest -v tests/
```

Run a specific test module:

```bash
python -m pytest -v tests/test_login.py
```

## Allure Reports

Generate test results:

```bash
python -m pytest -v tests/ --alluredir=reports/allure-results
```

Open the Allure report:

```bash
allure serve reports/allure-results
```

## Automated Screenshots

The framework includes automatic screenshot capture when a test fails.

Screenshots are saved in:

```text
reports/screenshots/
```

## Test Results

Latest verified full test execution:

- Total test cases: 9
- Passed: 9
- Failed: 0
- Success rate: 100%

## Design Pattern

This framework follows the **Page Object Model (POM)** pattern to separate page interactions from test logic, improving code organization, maintainability, and reusability.

## Author

**QA Automation Portfolio Project**

Developed with Python and Playwright.