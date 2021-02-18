# BIU-grades-scraping
a small python script to auto scrape BIU inbar system grades and list them as a table.

 <img src="https://i.ibb.co/g9rZRn4/appbiu.png">


# How to use
you can -
* use the pre-released installer for windows-64 ---not working properly at the moment
* use the source code main.py without GUI
* use biugradeGUI.py with GUI
## main.py --without gui
pip-install:
```
pip-install selenium, tabulate
```


enter your id and password lines 7-8 in the code.

download chrome-driver at https://chromedriver.chromium.org/
and place the file location at line 5.
## biugradeGUI.py
just run with python 3.8 or higher  after installing the pip modules :
```
python biugradeGUI.py
```
## chrome-driver
you can download the right chrome-driver for your chrome browser version at https://chromedriver.chromium.org
