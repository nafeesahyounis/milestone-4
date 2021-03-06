# .lifestyle redesigned

Lifestyle Redesigned has been designed by developer Nafeesah Younis as a final project for the CodeInstitute Full Stack Development Course.

It is an Ecommerce Site that takes inspiration from the TV show 'Queer Eye', and essentially it offers the user the option to buy both packages and individual services geared at revamping their overall image, whether it be for the purpose of dating or a job.

*Important Note*

Due to time constraints, this ecommerce site was developed as an MVP and therefore is lacking in many features as will be discussed further in the docs.

The User Has the option to purchase either a pre-made package or individual services. 

- Life coaches - mind & motivation

- Stylist + shopping trip - Grooming and fashion 

- Interior Designer

- Professional Photoshoot 



## Table of Contents
1. [UX](#ux)
    - [Goals](#goals)
        - [Visitor Goals](#visitor-goals)
        - [Business Goals](#business-goals)
        - [Solo Traveller Handbook Goals](#solo-traveller-handbook-goals)
    - [User Stories](#user-stories)
        - [Visitor Stories](#visitor-stories)
        - [Business Stories](#business-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
3. [Information Architecture](#information-architecture)
4. [Technologies Used](#technologies-used)
5. [Deployment](#deployment)
6. [Testing](#testing)
7. [Credits](#credits)

# UX

## Goals

### Visitor Goals

The target audience for lifestyle redesigned is adults looking for a one-stop ecommerce site where they can have their lifestyle service related needs met. Lifestyle redesigned acts as a connecting point for consumers and professionals in one of the main categories. Consumers can use the site to book their consultations and access a database of a variety of different professionals to choose from.

The user goals are:

- To have a database where they can quickly and easily find professionals in one of the four service fields: home design, personal styling, fitness & life coaching.

- To be able to easily purchase their first consultation without having to search through lots of different websites.

- To contribute to a growing lifestyle service industry.

Lifestyle redesigned is a great way to address these needs because:

- Currently it is very difficult to find a collection of lifestyle services. Usually the professional has just their own website and you have to contact them personally to book.

- The design of the site is very simple and functional, so it's easy to find what you need and purchase your first consultation.

- At the moment the site is very simple, but later there will be additional features such as a calendar.

### Business Goals

The target businesses for this site are consultants in the four areas of personal trainers, interior designers, stylists and life coaches. This will act as a platform for them to advertise themselves and their business and book more clients.

### Business User Goals

Business user goals are:

- A functional, clean and appealing-to-the eye site upon which I can advertise my business.

- For the end user to easily be able to find my listings through searching via the category.

- For the end user to have a clear overview of what we offer and our pricing.

Lifestyle Redesigned currently caters towards this in the following ways:

- The site has a simple and intuitive colour scheme and design, so it is easy to navigate and find what the user is looking for.

- There is a carousel and a call of action on the homepage, which immediately tells the user what services are available.

- Businesses are able to display all their information on the 'listings page' so that the user can have a better idea of their services.

- There is also a sort filter so the pricing of businesses is clear from the get-go.

### Lifestyle Redesigned Goals

- To provide a clean, clear site where the end user can access lifestyle services in one place.

- To provide a platform for businesses and freelancers to advertise their services.

- As a developer, this was my first time working with Django. My goal was to get familiar enough with the language to build a payment system and various smaller apps and combine them with Front-end.

- Although this is a student project, in the future I would like to expand on the functionality so that there is a separate login system and set of features for businesses to go in and perform CRUD applications so that it can be used as an advertising platform.

## User Stories

### Visitor Stories

As someone who is visiting Lifestyle Redesigned, I want to:

- Immediately know what the site is for and what are the different features/things I can do on the site.

- Enjoy navigating the site. Be able to navigate it with ease and not feel frustrated by inconsistencies or a lack of buttons.

- Have something beautiful yet not overwhelming to look at, in order to inspire me to purchase services.

- Be able to search for what I need immediately, without too much navigation and without having to read through too much information.

- As someone who has a busy life and may not have a larger device or may be on the go, I want to be able to search for things easily on my phone or tablet.

- As someone with either a lower budget or a lot of money to invest, I want to be able to sort through services based on what price point best suits me.

- As a user of the site, I would like to be able to contact the creator of the site easily and quickly if I encounter any issues.

- As a user of the site, I would like to be able to pay for my purchases through a secure payment system.

- As a user of the site, I would like to be able to login and logout of the site so that my purchases are securely tracked somewhere.

- As a user of the site, when I put something into the cart I'd like the option to remove it or look at it before committing to purchasing.

- As a user of the site, I would like my emails and passwords to be secure.

### Business Stories

As a business owner:

- As a business owner, I would like visitors to be able to see my listing ASAP so that I can quickly generate traffic.

- As a business owner, I would like to be able to contact the creator of the site easily in case I encounter any problems. 

- As a business owner, I would like an easy to use interface that I can navigate within a few clicks.

- As a business owner, I would like the platform that I advertise on to be aesthetically pleasing and inspire my potential customers to use my services.

## Design Choices

Lifestyle redesigned has a very minimal and functional design. It was built on a time constraint, so the goal was functionality and pleasant user experience rather than anything too flamboyant.

### Fonts

The main headers of the site use Merriweather & the secondary font is Playfair. These fonts were chosen after doing some research on the most popular web design fonts of the year [awards](https://www.awwwards.com/20-best-web-fonts-from-google-web-fonts-and-font-face.html).

### Colors

A lot of white space was used in this particular project to create a clean feel. It was modelled off of research on other ecommerce sites, where color is often minimal and focus is on products. #ae877e was used for the navbar to create some warmth to the overall monochromatic feel of the site.





## Wireframes

Wireframing was done using the Figma tool. As the product is an MVP and there were 4 weeks to both learn django and complete the project, basic wireframing was done aimed at this goal:

[wireframes](https://www.figma.com/file/Xkc2s9HvJ3Mo6EZavRIGYc/eCommerce-%2F-Nafeesah?node-id=0%3A1)

# Features
## Existing Features

* Navbar

The navbar is on each page and on smaller screens it turns into a hamburger menu on the left hand corner of the screen.

The following items are present on the navbar when the user is not logged in:

- Home

- Shop (dropdown menu)

- Login

- Register

- Shopping cart in left corner

When the user is logged in, the following items are visible:

- Home

- Shop (dropdown)

- Logout

- Shopping cart in left corner

* Footer

Due to time constraints on the project, the footer was kept very simple and displays basic contact information and the name of the developer as well as Copywright info.

I would have liked to better refine and design the footer, but the project had a very strict timeline and so priority was given to the Python backend.

There are also issues with the footer that are discussed in the testing md file.

### Home Page

* Carousel

There is a carousel that shows the main services offered on the site with images. This is in order to create a more appealing user experience and immediately draw the users eye.

* Call to Action/About

There is a brief summary of the purpose of the ecommerce site under the carousel. This is in order to clearly define the purpose of the site to the user without requiring further searching.

* Shopping button

There is a button that takes the user immediately to the products page as this provides more options for navigation and a better user experience.

### Home Page

* Category buttons

The five main categories are listed at the top of the page and user can select which category they want to view, and from there get the results filtered accordingly. 

* Sort filters

There are three filters on each page, price from high to low, price from low to high and highest rated. This allows for the user to sort the services and provides a better ux.

* Breadcrumb menu

There is a breadcrumb menu at the top of the page that the user can click to either be redirected back to the home page, to the category page, or to reload the existing category they are on. 

* Products list

Products are displayed with name and description as well as price and rating. Note: unfortunately due to time constraints and some last minute issues, images were not successfully loaded. See testing.md for further details.

### Listing Detail Page

* Product details

The listing detail page has a product description & name and price of the product. Unfortunately images were not successfully added (see testing.md).

* Buttons

There is an add to cart and a view cart button on the listing page. 

* Breadcrumb menu

For ease of navigation, there is a breadcrumb menu at the top of the page so that user can navigate back to categories.

### Category pages

* Breadcrumb menu

For ease of navigation, there is a breadcrumb menu at the top of the page so that user can navigate back to home.

* Names of categories

Categories are listed for user to go to whichever service they want.

### Register Page

This template is from djangos inbuilt allauth.

* Form 

There is a registration form on this page which adds the users info into the database.


### Login Page

There are form fields on this page that check user email and password. This template is from djangos inbuilt allauth.

### Logout Page

* Buttons

The logout page is from the allauth template. It has two buttons, one that allows the user to logout and one that directs back to the homepage.

### Cart Page

* Table of products

On the cart page, there is a list of products that have been added with prices in the form of a table.

* Buttons

There is a return to products page for better navigation

### Checkout Page

* Progress Indicator

There is a progress indicator to give the user feedback on how much of the checkout process they have left.

* Form

The Order form takes the details of the user and stores them in the database.

* Card payment

There is a stripe payment system and a card payment field. 

### Checkout Success Page

* Progress Indicator

There is a progress indicator to give the user feedback that they have completed their order.

* Buttons

There are some buttons that lead the user back to the shop for better ux.

## Features left to Implement

There are a lot of features I would have liked to implement in this project. However, the time was very tight and it was important to keep it minimal and purposeful.

* Images 

Unfortunately there was a last minute issue with the images that would have delayed submission, and so they were not added to the database.

* Total cost calculator

At the moment, user can only add and pay for one item. I would like to modify this so that they can pay for everything at once.

* Remove product from cart

Due to time constraints, it was not possible to create a button to remove items from cart which significantly impacts the ux of the site.

* Search Bar 

In future, I would like to add a search bar at the top to filter for services.

* User Profile

It would be good to have a place to store user orders and also allow users to review their products. 

* Wishlist

I would like to add a feature where the user can favourite the items they like in order to buy them later if they are logged in.

* Blog app

In future I would like to add an additional app where businesses can have blog posts to further advertise their services.

* Business features

In future, I would like to have a separate system for business users where they can go in and modify their listings and their listing details and then submit them to be later reviewed by the main site admin. 

This will make the platform better for advertising.

* Javascript form authentication

I would like to add more modals and form authentication and feedback on the frontend using javascript as this would provide better ux.

## Information Architecture

### Database Choice

The Django framework works with SQL database. In development, I used the inbuilt sqlite and then in production and for deployment I used postgres as that's built into heroku.

#### Models

* Product Model

- the Product model takes the foreign key of the category model.

| Name |  | length | Field Type |
--- | --- | --- | ---
Category| max_length=254 | ForeignKey
Sku | max_length=254 | CharField
Name | max_length = 254 | CharField
Description | / | TextField
Price | max_digits=6 | DecimalField
Rating |  max_digits = 6 | DecimalField

* Category Model

| Name |  | length | Field Type |
--- | --- | --- | ---
name| max_length=254 | Charfield
friendly_name | max_length=254 | CharField

* Order Model

| Name |  | length | Field Type |
--- | --- | --- | ---
first_name | max_length=254 | CharField
last_name | max_length=254 | CharField
email | /| emailField
address | max_length = 250 | CharField
postal_code | max_digits= 20| Charfield
city | max_digits= 100| Charfield
created | /| DateTimeField
updated | /| DateTimeField
paid | /| BooleanField

* OrderItem Model

| Name |  | length | Field Type |
--- | --- | --- | ---

order | / | ForeignKey
product | / | ForeignKey
quantity | / | PositiveIntegerField
total_cost | / | DecimalField

# Technologies Used

* [GitHub](https://github.com/) - Was used to remotely store the code online.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - This was used for the main markup of the site.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - This was used was for styling.
- [jQuery 3.4.0](https://code.jquery.com/jquery/) was used for the main javascript functionality.
- Bootstrap was used as the framework for the layout.
- [Heroku](https://www.heroku.com) - The app has been hosted on heroku.
- [Python 3.6.7](https://www.python.org/) - was the backend language used for this project.
- Django was used to build the app.


# Testing 

Testing information can be found in separate [TESTING.md](TESTING.md) file


# Deployment

## How to run this project locally

In order to run this project on your idea, you firstly need to have these tools:
    - An IDE like [Visual Studio Code](https://code.visualstudio.com/)

The following three things need to be installed on your machine:
    - [PIP](https://pip.pypa.io/en/stable/installing/)
    - [Python 3](https://www.python.org/downloads/)
    - [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

You must have a free account with the following two services:
    - [Stripe](https://dashboard.stripe.com/register)
    - [AWS](https://aws.amazon.com/) and [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)


### Instructions
- Firstly, you need to save the github repo https://github.com/nafeesahyounis/milestone-4 . You can do this through clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
    ```
    git clone https://github.com/nafeesahyounis/milestone-4
    ```

- The next step is to open your IDE and a terminal session in the unzip folder or cd to the correct location.

- You will need a virtual environment for the Python interpreter, such assumes

    python -m .venv venv
    ```  
_NOTE: The `python` part of this command and the ones in other steps below assumes  you are working with a windows operating system. Your Python command may differ, such as `python3` or `py`_

- Then you must activate .venv with the command:
    ```
    .venv\Scripts\activate 
    ```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._


- You can install the necessary modules with this command: 
    ```
    pip -r requirements.txt.
    ```

And then set up environment variables like so:


    ```json
    "terminal.integrated.env.windows": {
        "HOSTNAME": "<enter hostname here>",
        "DEV": "1",
        "SECRET_KEY": "<enter key here>",
        "STRIPE_PUBLISHABLE": "<enter key here>",
        "STRIPE_SECRET": "<enter key here>",
        "EMAILJS_USER_ID": "<enter key here>",
        "STRIPE_SUCCESS_URL": "<enter url here>",
        "STRIPE_CANCEL_URL": "<enter url here>",
        "AWS_ACCESS_KEY_ID": "<enter key here>",
        "AWS_SECRET_ACCESS_KEY": "<enter key here>",
        "AWS_STORAGE_BUCKET_NAME": "<enter bucket name here>",
    }
    ```

    - If using an IDE that includes a `bashrc` file, open this file and enter all the environment variables listed above using the following format: 
    ```
    HOSTNAME="<enter key here>"
    ```
    - `HOSTNAME` should be the local address for the site when running within your own IDE.
    - `DEV` environment variable is set only within the development environment, it does not exist in the deployed version, making it possible to have different settings for the two environments. For example setting DEBUG to True only when working in development and not on the deployed site.


- Then, you need to migrate the models in the admin panel to make your database template like so:

    python manage.py migrate
    ```

- The next step is to make a superuser in order to be able to use the admin panel

    python manage.py createsuperuser
    ```

- You can now run the program locally with the following command: 
    ```
    python manage.py runserver
    ```

- Once the program is running, go to the local link provided and add `/admin` to the end of the ur. Here log in with your superuser account and create instances of ShippingDestination and Product within the new database.

- Once instances of these items exist in your database your local site will run as expected.


## Heroku Deployment

These are the steps to deploy lifestyle redesigned to heroku.

- First, make a `requirements.txt` file with the command in the terminal `pip freeze > requirements.txt`.

- Then, make a `Procfile` with command in the terminal `echo web: python app.py > Procfile`.

- Thirdly, use `git add` and `git commit` so that the new requirements will go into the Procfile and then git push as otherwise it won't work in Heroku.

- Make a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. 

- Go to the heroku dashboard of your new application and click 'Deploy' > Deployment Method and choose github.

-  Link your github repo with your heroku app.

- Then go to the heroku dashboard and open your config vars and set up the following variables:


| Key | Value |
--- | ---
AWS_ACCESS_KEY_ID | `<your secret key>`
AWS_SECRET_ACCESS_KEY | `<your secret key>`
AWS_STORAGE_BUCKET_NAME | `<your AWS S3 bucket name>`
DATABASE_URL | `<your postgres database url>`
EMAIL_HOST_PASS | `<your heroku app hostname>`
SECRET_KEY | `<your secret key>`
STRIPE_PUBLIC_KEY | `<your secret key>`
STRIPE_SECRET-KEY | `<your secret key>`

- Go to the command line of your local IDE, and do the following:
    - Enter the heroku postGres shell 
    - Migrate the database models 
    - Create your superuser account in your new database
    
     Instructions on how to do these steps can be found in the [heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql).

- Then go to your dashboard in heroku and click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".

- After the build is completed, you can click on View App.

- You can now add /admin to the end of the url and login as a superuser.

- the site should now run as expected.



# Credits

- Checkout and cart code was taken largely from codeinstitute boutique ado project due to time constraints.

- Images were taken from Pexels.




