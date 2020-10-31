# Lifestyle Redesigned - Testing details

[Main README.md file](README.md)

[View website on Heroku](https://code-institute-milestone4.herokuapp.com/)

## Automated Testing

### Validation Services
The following validation services and linter were used to check the validity of the website code.

- [W3C Markup Validation](https://validator.w3.org/) was used to validate HTML. 

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS.

- Pep8 flake extension command flake8 was used to check the Python.

## User Stories Testing

**As a visitor to Lifestyle Redesigned, I expect/want/need:**

- Immediately know what the site is for and what are the different features/things I can do on the site.

The call of action and carousel fulfils this need on the homepage.

- Enjoy navigating the site. Be able to navigate it with ease and not feel frustrated by inconsistencies or a lack of buttons.

Buttons have been placed on most pages pre-emptively addressing where the user may want to go next. On a few pages such as the signin page I was not able to add buttons due to timeboxing.

- Have something beautiful yet not overwhelming to look at, in order to inspire me to purchase services.

Basic styling and a monochromatic color scheme with a hint of color was added in order to create a sophisticated feel.

- Be able to search for what I need immediately, without too much navigation and without having to read through too much information.

The site has very few pages and is functional and to the point, so it is easy for the user to immediately navigate to the service they are looking for.

- As someone who has a busy life and may not have a larger device or may be on the go, I want to be able to search for things easily on my phone or tablet.

The site uses bootstrap to be responsive on smaller screen sizes.

- As someone with either a lower budget or a lot of money to invest, I want to be able to sort through services based on what price point best suits me.

Sort filter for pricing has been added to products pages.

- As a user of the site, I would like to be able to contact the creator of the site easily and quickly if I encounter any issues.

Email of developer is located in the footer on every page.

- As a user of the site, I would like to be able to pay for my purchases through a secure payment system.

Secure stripe payment has been implemented using django.

- As a user of the site, I would like to be able to login and logout of the site so that my purchases are securely tracked somewhere.

Login functionality has been added with django allauth package.

- As a user of the site, when I put something into the cart I'd like the option to remove it or look at it before committing to purchasing.

Unfortunately due to time constraints this was not implemented. See README and features left to implement.

- As a user of the site, I would like my emails and passwords to be secure.

Djangos builtin allauth system provides security, but in future I would like to add further security to the site.

### Business Stories Testing

- As a business owner, I would like visitors to be able to see my listing ASAP so that I can quickly generate traffic.

There are very few pages on the site, so the user immediately can see the different listings and services.

- As a business owner, I would like to be able to contact the creator of the site easily in case I encounter any problems. 

Email address at bottom of page allows for immediate contact.

- As a business owner, I would like an easy to use interface that I can navigate within a few clicks.

The site is very functional and so a person is able to find what they need with minimum effort. 

- As a business owner, I would like the platform that I advertise on to be aesthetically pleasing and inspire my potential customers to use my services.

Unfortunately this need was not entirely met. Styling was minimal due to time constraints.


## Manual Testing

Manual testing was done throughout the project using print statements and pages were checked whenever something new was added. 

Features on all pages were tested by myself and other friends.

## Defensive Design (known issue)

Unfortunately as this is an MVP, it was not possible to implement defensive design and fully test every page in terms of potential errors eg user type additional thing into url. Page not found was not created and activity that does not conform to the general flow of the page was not addressed ie if the user does not necessarily follow the if statements. In future, I would like to make the site more rigid.

However, it is currently built in a way that it addresses the basic flow in the wireframe in the README file without a massive focus on potential error. The site was built in the space of a month while the developer was still learning django, therefore most time was spent learning the material whilst building and so many areas were not addressed.

## Known issues

* Footer does not stick to the bottom of the page.

* Media queries in css do not work on smaller screen size.

* Due to a change in the pathnames during deployment, I was unable to connect the heroku app with the media files and so images cannot be displayed. As a quick fix, I have manually uploaded them but in future I will fix this.

* Images also cannot be displayed in database. I tried to implement this feature in the models but ran into many errors and therefore chose to do it later due to time constraint issues.




