Python / Django Test Assignment

Complete all the tasks listed below. 
Create a local Mercurial repository and commit your code into it during development. 
After completing all tasks, compress all files including ‘.hg’ folder into a zip archive and send it back to us.

Task 1 Create a basic django project that would present your name, surname, birthdate, bio, contacts on the main page. 
Data should be stored in the database. 
Use: 
● manage.py syncdb 
● manage.py runserver 
● Open the browser and all data are in, loaded from fixtures 
● Use pip requirements and virtualenv to manage your third party packages dependencies

Task 2 Create middleware that stores all http requests into the database. 
Also, on a separate page show first 10 http requests that are stored by middleware.

Task 3 Create template­context­processor that adds django.settings to the context.

Task 4 Create page with form that allows to edit data, presented on the main page. 
● Add authentication to this page 
● Add ability to upload, view and change photo

Task 5 For birth date on the same page add calendar widget. Create your own django widget.

Task 6 Create template tag that accepts any object 
and renders the link to its admin edit page (e.g {% edit_link request.user %}).

Task 7 Create django management command that prints all project models and the count of objects in every model. 
Also: 
● Duplicate output to STDERR with prefix "error: " 
● Write a bash script which executes your command and saves output of stderr into file. File name should be “.log”

Task 8 Create signal processor that, for every model, creates the db entry about the object creation/editing/deletion.
