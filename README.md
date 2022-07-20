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

![LmkGTdMsAS](https://user-images.githubusercontent.com/52770689/139401453-976ba5c3-c77f-40ab-8262-85d3cec9e02b.gif)
 
 # Allure report screenshots
 
![image](https://user-images.githubusercontent.com/52770689/139401838-3bf37da2-a0ed-4367-94ec-21c81c5287f6.png)
![image](https://user-images.githubusercontent.com/52770689/139401985-19ec382f-aebd-46aa-a9d6-417e8f6b7ed9.png)

If you find this repository useful, don't forget to give it a ⭐ on GitHub.

 
