pytest -rA -v -m "smoke or regression" -n 5 --html=Reports\report.html test_cases --browser chrome
REM pytest -rA -v -m "smoke or regression" -n 5 --html=Reports\report.html test_cases --browser firefox
REM pytest -rA -v -m "smoke or regression" -n 5 --html=Reports\report.html test_cases --browser edge