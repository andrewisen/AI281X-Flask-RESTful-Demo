# AI281X-Flask-RESTful-Demo

A simple demo for building an API using the extension Flask-RESTful.
The goal is to show the potential for [Undervisningshuset](https://www.akademiskahus.se/vara-kunskapsmiljoer/byggprojekt/vara-byggprojekt/stockholm/undervisningshuset/).

A [Docker](http://docker.com) example is availbe [here](https://github.com/andrewisen/AI281X-Docker-Flask-RESTful-Demo).

## Getting Started

This is a demo showcasing Flask and how it can be used to build an API from scratch.

### Prerequisites

Basic knowledge of programming, API and Python is recommended.
A working Python 3 enviroment is requred.

```
Python 3.4 or newer (Required)
Pip (Recomended)
Flask (Required)
Flask-RESTful (Required)
```

### Installing

Installing Python 3 in your prefered way.
E.g. Homebrew.

Check your Python version.

```
python3 -V
```

Installing Flask in your prefered way.
E.g Via pip

```
pip ...
```

Lorem Ipsum

```
Foo Bar
```

## Deployment - FLASK REST API

CD into working directory.

Simple Flask App. Returns static website with "Hello World".
```
python3 helloWorld.py
localhost:5000
```


Simple Flask REST API. Returns JSON respons with "Hello:World".
```
python3 helloAPI.py
localhost:5000/<app-key>
```

Simple Flask REST API. Requires the API Key. Returns JSON respons with "Hello:World".
```
python3 app.py
localhost:5000/<app-key>
```
## Deployment - KTH Places
**NOTE:** This is not an web-based application. Everything is done in Terminal or CMD.

Returns all rooms in [Undervisningshuset](https://www.akademiskahus.se/vara-kunskapsmiljoer/byggprojekt/vara-byggprojekt/stockholm/undervisningshuset/). Requires an API Key from 
[KTH IT-Support](https://www.kth.se/student/kth-it-support) .

```
python3 helloJSON.py
```

Returns a places in [Undervisningshuset](https://www.akademiskahus.se/vara-kunskapsmiljoer/byggprojekt/vara-byggprojekt/stockholm/undervisningshuset/) based on hard-coded filters.

Open and Edit the Python-file for more information.

**NOTE:** This requires knowledge on how the KTH Places API works!

```
python3 handleJSON.py
```

## Built With

* [Python 3.7](https://www.python.org/downloads/release/python-370/) - The language used
* [Flask](http://flask.pocoo.org) - The microframework used
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) - An extension to Flask 
* [KTH Places](https://www.kth.se/api/places/swagger/) - KTH Places API

## Acknowledgments

* [Melvin L](https://www.youtube.com/watch?v=s_ht4AKnWZg) - Source of inspiration
