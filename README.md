<img style="height: auto; width: auto;" src="mdn.png" alt="Hello">
<h1>Django Web Framework (Python)</h1>

-----

I continued working on this tutorial 26.02.23

First create .env file

`
SECRET_KEY=<Your_secret_key>
`

`
DEBUG=<False/True>
`

Deploy locally
1. >`python3 -m venv venv`
2. >`pip install -r req.txt `
3. >`python manage.py makemigrations`
4. >`python manage.py migrate`
5. >`python manage.py runserver`

To create super user for admin pane
- `python manage.py createsuperuser`

[Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
