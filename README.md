# Finances App
View and assign tasks to users

## Usage

* Install and create virtualenv 

```bash
python install virtualenv
virtualenv venv
```

* Activate virtualenv and install dependencies

```bash
for Linux and Mac:
source venv/bin/activate

for Windows
/venv/Scripts/activate

pip install -r requirements.txt
```

* Run Django on your local server

```bash
python manage.py migrate
python manage.py runserver
```

* Open http://127.0.0.1:8000/ in your browser and enter details

![Home page](example_files/home_page.png)

* Upload excel sheet in the following format:

![Excel example](example_files/excel_example.png)

* Once you submit you'll be directed to the chart page

![Chart example](example_files/chart_page.png)

## Solution Explanation

* This web app uses Django.
* Each form uploaded stores the users name, date of birth and file (in the form of the file location) to the Accounting model
![model](example_files/model.png)
* Once the file is uploaded, the data is extracted using [openpyxl](https://openpyxl.readthedocs.io) and saved as a JSON data field to the correspoing model.
![JSON](example_files/json.png)
* The user is then directed to the chart page which graphs all their data using [Chart.js](https://www.chartjs.org/docs/latest/charts/line.html)
