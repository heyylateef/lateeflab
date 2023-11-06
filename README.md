## LateefLab
A small Django website to give back to the community! Currently features a blog app where I post my Django tutorials. I also have a few pages dedicated to the gig work I'm interested in doing for clients (use the contact form if you're interested!).

## Motivation
I wanted to give back to the community that helped build a career! This site (lateeflab.com) is made open-source for all to see, inspect, and clone!

## Tech/framework used

<b>Built with</b>
- [Python 3.8.10](https://www.python.org/)
- [Django 3.2.5](https://www.djangoproject.com/)

## Features
This website includes my blog (lateeflab.com/blog) where I post tutorials for Django web developers. I'm also open to gig work, so I also show visitors some of the gig work I have experience in.


## How to use? (Using cloned database, for testing purposes)
Inside terminal(Mac)/command-line(Windows):
```
cd/YOUR/PROJECT/DIRECTORY/TO/CLONEDREPO
```

Once you changed directory the cloned repo, start the web server by using the following command: manage.py runserver
```
.../YOUR/PROJECT/DIRECTORY/TO/CLONEREPO python manage.py runserver 
```
Inside a web browser, paste the following url: http://127.0.0.1:8000/

## How to use? (Starting fresh, for production)
If you want to clear out the migrations and database then do the following:
1. Delete everything inside of the mediarequestform/migration folder EXCEPT __init__.py
2. Drop the current database (or delete db.sqlite3)
3. Make migrations, inside terminal(Mac)/command-line(Windows):
```
.../YOUR/PROJECT/DIRECTORY/TO/CLONEREPO python manage.py makemigrations
```
4. Apply migrations, inside terminal(Mac)/command-line(Windows):
```
.../YOUR/PROJECT/DIRECTORY/TO/CLONEREPO python manage.py migrate
```
5. (Optional) Create super user, inside terminal(Mac)/command-line(Windows):
```
.../YOUR/PROJECT/DIRECTORY/TO/CLONEREPO python manage.py createsuperuser
```
```
Username: admin
```
```
Email Address: admin@example.com
```
```
Password: **********
Password (again): *********
Superuser created successfully.
```
6. Run the web server
```
.../YOUR/PROJECT/DIRECTORY/TO/CLONEREPO python manage.py runserver 
```

## License
LateefLab

Copyright © 2023 Lateef Adetona

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

MIT © [Lateef Adetona]()