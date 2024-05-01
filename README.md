# spartamarket_DRF
Converting the previous Django framework into DRF

# 0. ERD(Entity Relationship Diagram)

![스크린샷 2024-05-01 201659](https://github.com/thewon4155/spartamarket_DRF/assets/99013724/fd51e20c-76f4-4e80-add1-07f7acc76043)

Relationships:
User to Product

One-to-Many: A user can post multiple products, but each product is associated with one user.


# 1. Project abstract: (2024.04.29. ~ 2024.05.01.)

a DRF that runs apps of Accounts, Products to host a website that provides item lists for sale.

Basically an extension from the previous Sparta market.



# 2. Software Used:

Main Framework: Django 5.0.4, Python 3.12.1,

djangorestframework 3.15.1, djangorestframework-simplejwt-5.3.1

Verifications: Postman



# 3. Operating Functions:

APP: ACCOUNTS:

### 1. Signup
Endpoint: /api/accounts

Method: POST

Requirements: Username, password, email, name, nickname, birthday

Verification: Ensure that both username and email are unique.

Implementation: Check for uniqueness and save the data to the database.

1-1. Sample of user info

![스크린샷 2024-05-01 193213](https://github.com/thewon4155/spartamarket_DRF/assets/99013724/afba1565-c88e-47f3-b5e8-ff5c569d43bb)

1-2. verification for multiple username, email

![스크린샷 2024-05-01 191635](https://github.com/thewon4155/spartamarket_DRF/assets/99013724/456c4040-f872-48be-a2bf-24c8e25e3c48)


### 2. Login

Endpoint: /api/accounts/login

Method: POST

Requirements: Username, password

Verification: Check for existence of username and correct password in the database.

Implementation: On successful login, provide a token; on failure, return an error message.

2-1. provide token

![스크린샷 2024-05-01 194017](https://github.com/thewon4155/spartamarket_DRF/assets/99013724/6250d9fa-d73c-46a0-9768-5ffcf591f487)


### 3. Profile Check

Endpoint: /api/accounts/<str:username>

Method: GET

Requirements: User must be logged in to access their profile.

Verification: Access allowed only to logged-in users.

Implementation: Convert logged-in user's information into JSON format.


APP: PRODUCTS:

### 1. Register Product

Endpoint: /api/products

Method: POST

Requirements: User must be logged in; title, context, and product picture are required.

Implementation: Create and save a new product post in the database.

1-1. sample product post

![image](https://github.com/thewon4155/spartamarket_DRF/assets/99013724/0dcdb184-d5d6-4422-9532-1993d6abda7b)

1-2. visualizing post

<img width="944" alt="image" src="https://github.com/thewon4155/spartamarket_DRF/assets/99013724/2b6dc2d0-d3cc-4e5b-9807-cd5bdfc2447e">


### 2. Check for Product List

Endpoint: /api/products

Method: GET

Requirements: No login required.

Implementation: Fetch and convert all product listings with pagination to manage the data efficiently.


### 3. Modify Product

Endpoint: /api/products/<int:productId>

Method: PUT

Requirements: User must be logged in and must be the writer of the post.

Verification: Ensure that the requesting user is the original writer of the post.

Implementation: Update product information with the revised content.


### 4. Delete Product

Endpoint: /api/products/<int:productId>

Method: DELETE

Requirements: User must be logged in and must be the writer of the post.

Verification: Ensure that the requesting user is the original writer of the post.

Implementation: Remove the product post from the database.
