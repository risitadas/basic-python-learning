'''

Requests Module For HTTP Requests

What is HTTP?
HTTP stands for the 'Hypertext Transfer Protocol,'.
It is a set of protocols that are designed to enable communication between clients and servers.
Between clients and servers, it works as a request-response protocol.
To request a response from the server, we can request data from the server or submit data to be processed to the server.

What Is Requests Module?
The response data depends on our type of request.

Install Python Requests:-

pip install requests
import requests


Built-in methods in the request module:-

get()
syntax :- requests.get(URL, params={key: value}, args)

URL: this is the URL of the website where we want to send the request.

Params: this is a dictionary or a list of tuples used to send a query string.

Args: It is optional. It can be any named arguments offered by the get method.

put( ):
 It is used to send a put request to a variable.
 It is usually used to update or completely change the resources of a specific URL.

delete( ):
Delete is used to delete the specific resource specified by URL.

head( ):
The head method returns a header for a specific resource.

post( ):
Post requests take with it the data to the server to update it with.

patch( ):
The patch is used to send patch requests. It is used to apply partial modifications to a resource.
It carries with it the instructions for the modification.


'''

import requests
r = requests.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2")
print(r.text)
print(r.status_code)


# url = "www.something.com"
# data = {
#     'p1' : 1,
#     'p2' : 5
# }
# r2 = requests.post(url = url, data= data)
