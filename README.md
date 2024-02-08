# TO-DO-APP
### cloning the repository
1. cloning the repository using the following command

       git clone https://github.com/YashMarmat/TO-DO-APP.git    # which link you want to clone

2.Navigate to the project folder

        cd folder_name

3.If you use different database you change the database in your_project/settings.py Databases
     
      'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'Kabila_23',
            'HOST': 'localhost',  # Set to the PostgreSQL server address      # here I am using postges
            'PORT': '5432',    

     
4.Run Database Migrations
         
        python manage.py makemigrations
        python manage.py migrate

5.Start the development server

       python manage.py runserver

## Installing from ZIP Archive
- Download the zip file In github
- Extract the ZIP archive to your desired location on your computer.
- Navigate to the project folder: --Right click on the project folder and 'Copy as path' and paste the path like below

      cd project_path
