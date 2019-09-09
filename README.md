# Blog API services 
===================  


	Build Web APIs using Django REST framework .

## Requirements
- Python 3.6
- django 1.11
- django-rest-framework 3.10.0
- djangorestframework-jwt 1.11.0


## Installation
```
	pip3 install django==1.11.17
	pip3 install django-filter==1.0.0
	pip3 install djangorestframework==3.10.3
	pip3 install markdown==3.1.1
	pip3 install django-filter==1.0.0
	pip3 install djangorestframework-jwt==1.11.0

```
Access Blog data from your application using the HTTP methods - GET, POST, PUT, PATCH, DELETE

Endpoint |HTTP Method | Method | Result
-- | -- |-- |--
`/api/auth/login/ ` | POST | Login | Login to session 
`/api/auth/logout/ ` | POST | Logout | Logout from session 
`/api/auth/signup/ ` | POST | Signup | Create new User 
`/api/auth/token/ ` | POST | GET | Get JWT token using username and password 
`/api/auth/articles/` | GET | List | Get list of articles
`/api/auth/articles/` | POST | Create | create a new article
`/api/auth/articles/{article_id}/` | GET | Get | Get article by id
`/api/auth/articles/{article_id}/` | PATCH | Update | Update article by id
`/api/auth/articles/{article_id}/` | DELETE | Delete | Delete article by id
`/api/auth/articles/{article_id}/comments/` | GET | Get | Get article comments by  articleid
`/api/auth/articles/{article_id}/comments/` | POST | Create | create article comments by articleid



## Use 
-   Download or Clone the repository and Extract in destination folder
-   cd /articles_api/blog/
-   python3 manage.py makemigrations
-   python3 manage.py migrate
-   python3 manage.py createsuperuser --email python.vinoth@gmail.com --username vinoth
-   python3 manage.py runserver

-   Open http://127.0.0.1:8000/api/auth/login/ and provide user credetials for session authentication
-   Use the following CURL commend to get JWT token :  curl -X POST -d "username=admin&password=*****" http://127.0.0.1:8000/api/auth/token
-   Open http://127.0.0.1:8000/api/auth/signup/ for creating new User
-   Open http://127.0.0.1:8000/api/auth/logout/ for sign out from session
-   Open http://127.0.0.1:8000/api/auth/articles/ for Listing all articles and create a new article
-   Open http://127.0.0.1:8000//api/auth/articles/{article_id}/ for article details, update article and delete article
-   Open http://127.0.0.1:8000//api/auth/articles/{article_id}/comments for list comments under article and create new comments under article


### Note : 

-   Left "rest_framework.renderers" as default to test using browser
-   Only Author can Update or Delete the Article

