"""
Introduction to APIs and REST
This chapter lays the groundwork by defining what APIs are and specifically what constitutes
a RESTful API.

1.1 APIs and REST APIs
 What is an API? (Application Programming Interface)

o An API is a set of rules and definitions that allows different software
applications to communicate with each other.

o Think of it like a menu in a restaurant: it tells you what you can order
(available functions) and how to order it (parameters, data format). You don't
need to know how the kitchen prepares the food; you just use the menu.

o Examples: Google Maps API, Twitter API, Payment Gateway APIs.

 What is REST? (Representational State Transfer)
o REST is an architectural style for designing networked applications. It's not a
protocol (like HTTP) but a set of guidelines.

o RESTful APIs are designed to be stateless, client-server, cacheable, and use a
uniform interface (HTTP methods).

o Key Principles of REST:
 Client-Server: Separation of concerns. The client (e.g., web browser,
mobile app) and server (e.g., your Django API) evolve independently.

 Stateless: Each request from client to server must contain all the
information needed to understand the request. The server should not
store any client context between requests.

 Cacheable: Responses can be explicitly or implicitly defined as
cacheable to improve performance.

 Layered System: A client cannot ordinarily tell whether it is
connected directly to the end server or to an intermediary along the
way.

 Uniform Interface: The most critical constraint. It simplifies system
architecture by having a common way to interact with resources. This
involves:

 Resource-based: Data is identified as resources (e.g.,
/products, /users/1).

 Standard HTTP Methods: Use standard HTTP verbs to
perform actions on resources:

 GET: Retrieve (Read) a resource or collection of
resources. (Idempotent & Safe)

 POST: Create a new resource. (Not Idempotent & Not Safe)

 PUT: Update/Replace an existing resource (entirely). (Idempotent)

 PATCH: Partially update an existing resource. (Not
Idempotent)

 DELETE: Remove a resource. (Idempotent)

 Stateless Interactions: No session information is stored on the server.

 Hypermedia as the Engine of Application State
(HATEOAS): Resources should contain links to related
resources, guiding the client on available actions. (Often not
fully implemented in simpler APIs).

 Code on Demand (Optional): Servers can temporarily extend or
customize the functionality of a client by transferring executable code.

 JSON (JavaScript Object Notation):
o The most common data format for REST APIs due to its lightweight nature
and ease of parsing for both humans and machines.

o Looks like Python dictionaries and lists.

"""

"""
API ==> Application Programing Interface
it uses a different services
Allows  one software to communicate with another


REST ==> REpresentational State Transfer
CLIENT --> SERVER
 (HTTP)
Uses HTTP Request Method (get, post) 
Pattern for making API's
## All API's are not REST API's but All REST API's are API's
Example ==> we (cilent) --> Kitchen (server) ==> Waiter (API)
API will return data in the form of XML OR JSON file   
"""