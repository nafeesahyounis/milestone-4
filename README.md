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

