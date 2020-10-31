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








