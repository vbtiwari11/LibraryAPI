Library Application API

How to run:

1.Clone the project to your local 

2.make sure you have the virtual environment created for new project
python -m venev LibraryAPIVenv
LibraryAPIvene\Scripts\activate

3.run command "pip install -r requirements.txt"
once all reuirements are installed 
run command : cd library_api

4.run command 'py manage.py makemigrations'
  
5.run command 'py manage.py migrate'
   
6.run command 'py manage.py runserver'
you will be prompted to http://127.0.0.1:8000/

7.Change url to http://127.0.0.1:8000/swagger-ui/#/

8.Now you can add the parameters and execute to see the results.
for Student you can use 'S001,S002....' 
for librarian 'L001,L002..'
for Book 'Book 1','Book 2',....
you can modify the api's and check for different conditions
