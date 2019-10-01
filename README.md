         Patient Search API
#######################################

Running API Requires:
    - python 3
    - Angular version 7
    - Postgresql 4
    - npm version >= 8
    - pip

Database:
- within the db directory the patients_db_creation.sql script will create the patients_db database, all neccessary tables, relations, and fill them with some mock data

Python:
- install pipenv with 'pip install pipenv' 
- from a command line or terminal navigate to PatientsApi/backed and run the command 'pipenv --three' to create the virtual environment
- then run 'pipenv install' to install the packages listed in the pipfile 
- once all the packages have been installed, from a powershell terminal run the script boostrap.ps1
- you can now call the different API urls, they are:
    * [GET] http://localhost:5000/patient/<int:id>
    * [POST] http://localhost:5000/patient
    * [POST] http://localhost:5000/patient/record
    * [POST] http://localhost:5000/patient/address
    * [POST] http://localhost:5000patient/search
    * [DELETE] http://localhost:5000/patient/<int:id>
- in order to run the unit tests run the command 'nose2' from the backend directory

Angular:
- from a command line or terminal navigate to PatientsApi/www and run 'npm install' 
- then run 'ng serve' and once it finishes building successfully search http://localhost:4200/ in your browser