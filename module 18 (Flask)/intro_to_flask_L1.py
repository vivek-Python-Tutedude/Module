"""
Introduction to Flask

 What is Flask?
o Flask is a micro-framework for building web applications in Python.

o The "micro" in micro-framework means Flask aims to keep the core simple
but extensible. It doesn't include features like a database ORM or form
validation out of the box (unlike Django), but it's easy to integrate third-party
libraries for these functionalities.

o It provides the essentials: URL routing, request handling, and templating.

 Why choose Flask?
o Flexibility: Gives developers more control over component choices (e.g.,
choose your own ORM, authentication library, etc.).

o Lightweight: Smaller codebase, less boilerplate, making it quick to get started
for simpler projects or APIs.

o Simple to learn: Its API is straightforward and intuitive.

o Great for APIs: Often used to build RESTful APIs.

 Key Concepts:
o Werkzeug: A WSGI (Web Server Gateway Interface) utility library that Flask
uses internally for request and response objects.

o Jinja2: The templating engine Flask uses by default for rendering HTML.
"""
from flask import Flask
print("hii")