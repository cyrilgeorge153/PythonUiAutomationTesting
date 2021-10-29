# PythonUiAutomationTesting

Ui tesing using python selenium and pytest framework.

# Packages needed to run the project

pip install selenium

pip install webdriver-manager

pip install pytest

pip install pytest-order

pip install pytest-xdist

pip install pytest-html

# Prerequsite: Python version3+, Pycharm

# Execution: Download project to local and open terminal or cmd and execute following commands one by one for respective browser

 `pytest -rA -v -m "smoke or regression" -n 5 --alluredir=allure_report test_cases --browsername chrome`
 
 `pytest -rA -v -m "smoke or regression" -n 5 --alluredir=allure_report test_cases --browsername headlesschrome`
 
 `pytest -rA -v -m "smoke and regression" -n 5 --alluredir=allure_report test_cases --browsername chrome`
 
 `pytest -rA -v -m "smoke and regression" -n 5 --alluredir=allure_report test_cases --browsername headlesschrome`
 
 `pytest -rA -v -m "smoke" -n 5 --alluredir=allure_report test_cases --browsername chrome`
 
 `pytest -rA -v -m "smoke" -n 5 --alluredir=allure_report test_cases --browsername headlesschrome`
 
 `pytest -rA -v -m "regression" -n 5 --alluredir=allure_report test_cases --browsername chrome`
 
 `pytest -rA -v -m "regression" -n 5 --alluredir=allure_report test_cases --browsername headlesschrome`
 
 `pytest -rA -v -m "smoke or regression" -n 5 --alluredir=allure_report test_cases --browsername firefox`
 
 `pytest -rA -v -m "smoke or regression" -n 5 --alluredir=allure_report test_cases --browsername headlessfirefox`
 
 `pytest -rA -v -m "smoke and regression" -n 5 --alluredir=allure_report test_cases --browsername firefox`
 
 `pytest -rA -v -m "smoke and regression" -n 5 --alluredir=allure_report test_cases --browsername headlessfirefox`
 
 `pytest -rA -v -m "smoke" -n 5 --alluredir=allure_report test_cases --browsername firefox`
 
 `pytest -rA -v -m "smoke" -n 5 --alluredir=allure_report test_cases --browsername headlessfirefox`
 
 `pytest -rA -v -m "regression" -n 5 --alluredir=allure_report test_cases --browsername firefox`
 
 `pytest -rA -v -m "regression" -n 5 --alluredir=allure_report test_cases --browsername headlessfirefox`
 
 `pytest -rA -v -m "smoke or regression" -n 5 --alluredir=allure_report test_cases --browsername edge`
 
 `pytest -rA -v -m "smoke and regression" -n 5 --alluredir=allure_report test_cases --browsername edge`
 
 `pytest -rA -v -m "smoke" -n 5 --alluredir=allure_report test_cases --browsername edge`
 
 `pytest -rA -v -m "regression" -n 5 --alluredir=allure_report test_cases --browsername edge`
 
 # To view allure report use the following command after executing any one of the command in the above section 
 
 `allure serve .\allure_report`
 
 # Test execution gif

 
 # Reports:PythonUiAutomationTesting\Reports\report.html 
 
 # Html report screenshot
 ![chrome_XLfsYcJ8hf](https://user-images.githubusercontent.com/52770689/137924093-4609b934-a4e9-46e9-ab61-91865d2e4c28.png)
 
