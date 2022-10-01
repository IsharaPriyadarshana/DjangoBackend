The Autocompany
---------
This brings a Django backend created for an imaginary company for their e commerce website. 
The backend comprises of a API collection for adding products to a site as well as to Add them to a cart and finally checkout.

**API Collection Functionalities**

Following actions can be performed through the created APIs and please refer the document in the base directory named ***autocompany_api_documentation.pdf*** or use the postman collection named ***Autocompany.postman_collection.json***

* Create a user (Permissions: Anonymous user)
* Login  (Permissions: Anonymous user)
* Logout (Permissions: User)

* Add a products (Permissions: Super user)
* View all exisitng products  (Permissions: User)
* View details of a product (Permissions: User)

* Add item to a cart (Permissions: User)
* View cart (Permissions: User)
* Remove item from cart (Permissions: User)
* Order the current cart (Permissions: User)

* View all orders palced (Permissions: Super user)

How to run the server
---------

Follow the below procedure the start the server <br><br>
**prerequisites:**
* git
* docker
--------------------------------------------
* Checkout the codebase from github by,

* run the following command <br> `docker-compose up`  (Will take a few minutes depending on PC)

