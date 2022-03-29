# Instrumenta

<img src="docs/mockups/mockups.png">

<hr>

## Welcome to my Site [Instrumenta](https://instrumenta.herokuapp.com/)!

<br>

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-
refresh-toc -->

# Table of Content

1. [Project goals](#project-goals)

2. [User experience](#user-experience)

    1. [Target audience](#target-audience)

    2. [User stories](#user-stories)

    3. [Design](#design)

    4. [Technical design](#technical-design)

        1. [Wireframes](#wireframes)

        2. [Database diagram](#database-diagram)

3. [Features](#features)

4. [Technologies used](#technologies-used)

    1. [Languages](#languages)

    2. [Libraries and programs](#libraries-and-programs)

5. [Testing](#testing)

    1. [HTML](#html)

    2. [CSS](#css)

    3. [Python](#python)

    4. [Javascript](#javascript)

    5. [Accessibility](#accessibility)

    6. [Performance](#performance)

    7. [Further testing](#further-testing)

    8. [Testing user stories](#testing-user-stories)

6. [Bugs](#bugs)

7. [Deployment](#deployment)

8. [Credit](#credit)

    1. [Acknowledgement](#acknowledgement)

## Project goals

* The goal of this project is for the site owner to practice Django and implement a working ecommerce site.

## User experience

### Target audience

* This site is targeted towards musicians and beginners.

### User stories

#### Site Visitor

1. As a Site Visitor I can see pictures of instruments when I enter the page so that I know what kind of page I am on.

2. As a Site Visitor I can see music instrument categories so I can find the products I am interested in.

3. As a Site Visitor I can scroll thru a list of products so that I can find the product I want.

4. As a Site Visitor I can click on a product and see information about the product so I can get a better view of the product.

5. As a Site Visitor I can sort products so I can find the product I want.

6. As a Site Visitor I can search for products so I can find the relevant one for me.

7. As a Site Visitor I can add products to a bag so I can see everything I have added.

8. As a Site Visitor I can Update and Delete products in bag so I can Remove products I dont want.

9. As a Site Visitor I can add products to a bag so that I can buy them

10. As a Site Visitor I can buy a product so I can get the product I want.

11. As a Site Visitor I can get an email confirmation so I can feel confident the purchase is ok.

12. As a Site Visitor I can view an order confirmation so I can feel confident everything is ok.

13. As a Site Visitor I can browse the site and get notifications messages so I can know if things are working or not.

14. As a Site Visitor I can click on a button so that I can get to the top of the page quickly.

15. As a Site Visitor I can read reviews so that I can see which products customers are happy with.

16. As a Site Visitor I can create an account so that I can have personal info saved.

#### Site User

17. As a Site User I can log in to my account so that I can save my personal info.

18. As a Site User I can add a product to a wishlist so that I can keep track of products I want.

19. As a Site User I can delete a product from a wishlist so that I can remove products I dont want.

20. As a Site User I can log in to my account so that I can leave reviews.

21. As a Site User I can Delete my Review so that I can change my review or delete it if I want to.

22. As a Site User I can log in to my account so that I can Ask questions.

23. As a Site User I can view questions so that I can see what other people have had to say about the site.

#### Site Admin goals

24. As a Site Admin I can add, read, update and delete products so that I can manage the content.

25. As a Site Admin I can see all checkout orders so that I can see what people are buying.

26. As a Site Admin I can create, read, update and delete questions so that I can manage my content.

27. As a Site Admin I can create, read, update and delete reviews so that I can manage my content.

28. As a Site Admin I can manage the wishlist so that I can keep track of the wishlists.

29. As a Site Admin I can search for all my content so that I can find what I am interested in.

### Technical design

### Design

* A big part of my design inspiration came from the music site [Thomann](https://www.thomann.de/se/index.html). I also looked a lot on [Gear4music](https://www.gear4music.se/sv/). I also got a lot of inspiration and help from the study material *Boutique Ado* from [Code Institute](https://codeinstitute.net/se/).

#### Colors

* For the colors I wanted a grounded and basic look, letting the instruments speak for the page. Based on that i went with a white background with banners marking of some parts with stronger grey colors.

#### Fonts

* I chose the font [*Prompt*](https://fonts.google.com/specimen/Prompt?query=prompt) as it felt right for my page.

### Wireframes

* Below you can see the images of the wireframes

<details><summary>index.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/index_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/index_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/index_mobile.png">
    </details>
</details>

<details><summary>add_products.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/add_products_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/add_products_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/add_products_mobile.png">
    </details>
</details>

<details><summary>edit_products.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/edit_products_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/edit_products_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/edit_products_mobile.png">
    </details>
</details>

<details><summary>product_detail.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/product_detail_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/product_detail_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/product_detail_mobile.png">
    </details>
</details>

<details><summary>products.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/products_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/products_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/products_mobile.png">
    </details>
</details>

<details><summary>questions.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/questions_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/questions_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/questions_mobile.png">
    </details>
</details>

<details><summary>wishlist.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/wishlist_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/wishlist_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/wishlist_mobile.png">
    </details>
</details>

<details><summary>bag.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/bag_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/bag_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/bag_mobile.png">
    </details>
</details>

<details><summary>checkout.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/checkout_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/checkout_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/checkout_mobile.png">
    </details>
</details>

<details><summary>checkout_success.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/checkout_success_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/checkout_success_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/checkout_success_mobile.png">
    </details>
</details>

<details><summary>404.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/404_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/404_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/404_mobile.png">
    </details>
</details>

<details><summary>profile.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/profile_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/profile_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/profile_mobile.png">
    </details>
</details>

<details><summary>reset_password.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/reset_password_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/reset_password_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/reset_password_mobile.png">
    </details>
</details>

<details><summary>login.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/login_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/login_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/login_mobile.png">
    </details>
</details>

<details><summary>logout.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/logout_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/logout_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/logout_mobile.png">
    </details>
</details>

<details><summary>signup.html</summary>
    <details><summary>desktop</summary>
        <img src="docs/wireframes/signup_desktop.png">
    </details>
    <details><summary>tablet</summary>
        <img src="docs/wireframes/signup_tablet.png">
    </details>
    <details><summary>mobile</summary>
        <img src="docs/wireframes/signup_mobile.png">
    </details>
</details>

### Database diagram

* The database has multiple models;
    * **Wishlist** / Custom model
    * **Review** / Custom model
    * **Question** / Custom model


* 
<details><summary>Database Diagram</summary>
<img src="docs/database_diagram/database_diagram.JPG">
</details>

## Features

* **Carousel**

* The opening of the site shows a carousel with instrument images
<br>
<img src="docs/features/feature_instruments.JPG">

### User stories covered by this feature:

    1. As a Site Visitor I can see pictures of instruments when I enter the page so that I know what kind of page I am on.
<hr>

* **Categories Nav**

* A feature was implemented to show a navbar with the instrument categories
<br>
<img src="docs/features/feature_categories.JPG">

### User stories covered by this feature:

    2. As a Site Visitor I can see music instrument categories so I can find the products I am interested in.
<hr>

* **Product List**

* A feature was implemented to show a list of products to scroll thru
<br>
<img src="docs/features/feature_product_list.JPG">

### User stories covered by this feature:

    3. As a Site Visitor I can scroll thru a list of products so that I can find the product I want.
<hr>

* **Product Detail**

* A feature was implemented to show a single product 
<br>
<img src="docs/features/feature_product_detail.JPG">

### User stories covered by this feature:

    4. As a Site Visitor I can click on a product and see information about the product so I can get a better view of the product.
<hr>

* **Sort**

* A feature was implemented so users can sort products
<br>
<img src="docs/features/feature_sort.JPG">

### User stories covered by this feature:

    5. As a Site Visitor I can sort products so I can find the product I want.
<hr>

* **Search**

* A feature was implemented so users can search for products
<br>
<img src="docs/features/feature_search.JPG">

### User stories covered by this feature:

    6. As a Site Visitor I can search for products so I can find the relevant one for me.
<hr>

* **Add to bag**

* A feature was implemented so users can add products to bag
<br>
<img src="docs/features/feature_add_to_bag.JPG">

### User stories covered by this feature:

    7. As a Site Visitor I can add products to a bag so I can see everything I have added.
    9. As a Site Visitor I can add products to a bag so that I can buy them
<hr>

* **Update and Delete products in bag**

* A feature was implemented so users can update their bag
<br>
<img src="docs/features/feature_update_delete_product.JPG">

### User stories covered by this feature:

    8. As a Site Visitor I can Update and Delete products in bag so I can Remove products I dont want.
<hr>

* **Add, Buy products**

* A feature was implemented so users can add and buy products
<br>
<img src="docs/features/feature_add_to_bag.JPG">

### User stories covered by this feature:

    9. As a Site Visitor I can add products to a bag so that I can buy them
    7. As a Site Visitor I can add products to a bag so I can see everything I have added.
<hr>

* **Buy Product**

* A feature was implemented so the user can buy a product.
<br>
<img src="docs/features/feature_buy_product.JPG">

### User stories covered by this feature:

    10. As a Site Visitor I can buy a product so I can get the product I want.
<hr>

* **Email Confirmation**

* A feature was implemented so the user gets an email when completing an order.
<br>
<img src="docs/features/feature_email_confirmation.JPG">

### User stories covered by this feature:

    11. As a Site Visitor I can get an email confirmation so I can feel confident the purchase is ok.
<hr>

* **Order Confirmation**

* A feature was implemented so the user gets an order confirmation when completing an order.
<br>
<img src="docs/features/feature_order_confirmation.JPG">

### User stories covered by this feature:

    12. As a Site Visitor I can view an order confirmation so I can feel confident everything is ok.
<hr>

* **Notifications**

* A feature was implemented so the user gets notifications.
<br>
<img src="docs/features/feature_notifications.JPG">

### User stories covered by this feature:

    13. As a Site Visitor I can browse the site and get notifications messages so I can know if things are working or not.
<hr>

* **Back to top button**

* A feature was implemented so the user can get to the top of the products page when browsing the site.
<br>
<img src="docs/features/feature_back_to_top.JPG">

### User stories covered by this feature:

    14. As a Site Visitor I can click on a button so that I can get to the top of the page quickly.
<hr>

* **Read Reviews**

* A feature was implemented so the user can read reviews.
<br>
<img src="docs/features/feature_read_reviews.JPG">

### User stories covered by this feature:

    15. As a Site Visitor I can read reviews so that I can see which products customers are happy with.
<hr>

* **Account creation**

* A feature was implemented so the user can create an account.
<br>
<img src="docs/features/feature_signup_account.JPG">

### User stories covered by this feature:

    16. As a Site Visitor I can create an account so that I can have personal info saved.
<hr>

* **Personal Info**

    **Requires LOGIN**

* A feature was implemented so the user can save their info.
<br>
<img src="docs/features/feature_create_account.JPG">

### User stories covered by this feature:

    17. As a Site User I can log in to my account so that I can save my personal info.
<hr>

* **Wishlist**

    **Requires LOGIN**

* A feature was implemented so the user can add a product to a wishlist.
<br>
<img src="docs/features/feature_add_to_wishlist.JPG">

### User stories covered by this feature:

    18. As a Site User I can add a product to a wishlist so that I can keep track of products I want.
<hr>

* **Delete from wishlist**

    **Requires LOGIN**

* A feature was implemented so the user can delete a product from a wishlist.
<br>
<img src="docs/features/feature_delete_from_wishlist.JPG">

### User stories covered by this feature:

    19. As a Site User I can delete a product from a wishlist so that I can remove products I dont want.
<hr>

* **Leave Reviews**

    **Requires LOGIN**

* A feature was implemented so the user can leave reviews.
<br>
<img src="docs/features/feature_add_review.JPG">

### User stories covered by this feature:

    20. As a Site User I can log in to my account so that I can leave reviews.
<hr>

* **Delete Review**

    **Requires LOGIN**

* A feature was implemented so the user can delete their review.
<br>
<img src="docs/features/feature_delete_review.JPG">

### User stories covered by this feature:

    21. As a Site User I can Delete my Review so that I can change my review or delete it if I want to.
<hr>

* **Ask Questions**

    **Requires LOGIN**

* A feature was implemented so the user can ask questions.
<br>
<img src="docs/features/feature_add_question.JPG">

### User stories covered by this feature:

    22. As a Site User I can log in to my account so that I can Ask questions.
<hr>

* **View Questions**

    **Requires LOGIN**

* A feature was implemented so the user view questions.
<br>
<img src="docs/features/feature_view_question.JPG">

### User stories covered by this feature:

    23. As a Site User I can view questions so that I can see what other people have had to say about the site.
<hr>

* **Admin Products**

    **Requires SUPERUSER**

* A feature was implemented so the admin can easily update, add and delete products from the site.
<br>
<img src="docs/features/feature_add_product_admin.JPG">
<img src="docs/features/feature_edit_product_admin.JPG">
<img src="docs/features/feature_delete_product_admin.JPG">

### User stories covered by this feature:

    24. As a Site Admin I can add, read, update and delete products so that I can manage the content.
<hr>

* **Admin Checkout**

    **Requires SUPERUSER**

* A feature was implemented so the admin can see orders from the admin page.
<br>
<img src="docs/features/feature_checkout_admin.JPG">

### User stories covered by this feature:

    25. As a Site Admin I can see all checkout orders so that I can see what people are buying.
<hr>

* **Admin Questions**

    **Requires SUPERUSER**

* A feature was implemented so the admin can control the questions.
<br>
<img src="docs/features/feature_questions_admin.JPG">

### User stories covered by this feature:

    26. As a Site Admin I can create, read, update and delete questions so that I can manage my content.
<hr>

* **Admin Reviews**

    **Requires SUPERUSER**

* A feature was implemented so the admin can control the reviews.
<br>
<img src="docs/features/feature_review_admin.JPG">

### User stories covered by this feature:

    27. As a Site Admin I can create, read, update and delete reviews so that I can manage my content.
<hr>

* **Admin Wishlist**

    **Requires SUPERUSER**

* A feature was implemented so the admin can control the wishlists.
<br>
<img src="docs/features/feature_wishlist_admin.JPG">

### User stories covered by this feature:

    28. As a Site Admin I can manage the wishlist so that I can keep track of the wishlists.
<hr>

* **Admin Search**

    **Requires SUPERUSER**

* Features was implemented so the admin can control the site.
<br>
## See admin features

### User stories covered by this feature:

    29. As a Site Admin I can search for all my content so that I can find what I am interested in.
<hr>

### Features left to implement

* I want to implement a feature for users to update their reviews.

* I want to implement a feature so the admin can answer users questions on question page

* I want to implement a feature for top sellers

* I want to implement a feature for best sellers

* I want to implement a feature so the user can see how many products are in their wishlist on all pages

* I want to implement a feature where if the user makes a purchase with a product from the wishlist it is removed from the wishlist

* I want to implement a feature so the users can have a bigger profile with images and more personal info to give a more personal experience on review fields

* I want to implement a feature for the delete buttons to have validation before deleting

## Technologies used

### Languages

* Python

* HTML

* CSS

* Django 3.2

* Javascript

## Libraries and programs

* [Github](https://github.com/)

* [Gitpod](https://gitpod.io/projects)

* [VS code](https://code.visualstudio.com/)

* [Bootstrap 5](https://getbootstrap.com/)

* [Heroku for deployment and storing Postgresql database](https://id.heroku.com/login)

* [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/)

* [Balsamiq](https://balsamiq.com/)

* [Pep8 Online](http://pep8online.com/)

* [Ami responsivedesign](http://ami.responsivedesign.is/)

* [Lighthouse](https://developers.google.com/web/tools/lighthouse)

* [HTML Validator](https://validator.w3.org/)

* [CSS Validator](https://jigsaw.w3.org/css-validator/)

* [Google Fonts](https://fonts.google.com/)

* [Database diagrams](https://app.quickdatabasediagrams.com/)

## Testing

### Validator testing

#### HTML

<details><summary>No errors were found on index.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/index_validation.JPG">
</details>

<details><summary>No errors were found on add_products.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/add_products_validation.JPG">
</details>

<details><summary>No errors were found on edit_product.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/edit_product_validation.JPG">
</details>

<details><summary>No errors were found on product_detail.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/product_detail_validation.JPG">
</details>

<details><summary>No errors were found on products.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/products_validation.JPG">
</details>

<details><summary>No errors were found on questions.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/questions_validation.JPG">
</details>

<details><summary>No errors were found on wishlist.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/wishlist_validation.JPG">
</details>

<details><summary>No errors were found on bag.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/bag_validation.JPG">
</details>

<details><summary>No errors were found on checkout.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/checkout_validation.JPG">
</details>

<details><summary>No errors were found on checkout_success.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/checkout_success_validation.JPG">
</details>

<details><summary>No errors were found on 404.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/404_validation.JPG">
</details>

<details><summary>No errors were found on profile.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/profile_validation.JPG">
</details>

<details><summary>No errors were found on reset_password.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/reset_password_validation.JPG">
</details>

<details><summary>No errors were found on login.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/login_validation.JPG">
</details>

<details><summary>No errors were found on logout.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/logout_validation.JPG">
</details>

<details><summary>No errors were found on signup.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/signup_validation.JPG">
</details>
<hr>

#### CSS

<details><summary>No errors were found on base.css when passing through Jigsaw W3 Validator.</summary>
<img src="docs/validation/css/base.JPG">
</details>

<details><summary>No errors were found on checkout.css when passing through Jigsaw W3 Validator.</summary>
<img src="docs/validation/css/checkout.JPG">
</details>

<details><summary>No errors were found on profile.css when passing through Jigsaw W3 Validator.</summary>
<img src="docs/validation/css/profile.JPG">
</details>
<hr>


#### Python

<details><summary>BAG</summary>
    <details><summary>No errors were found on bag_tools.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/bag/bag_tools.JPG">
    </details>
    <details><summary>No errors were found on contexts.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/bag/contexts.JPG">
    </details>
    <details><summary>No errors were found on urls.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/bag/urls.JPG">
    </details>
    <details><summary>No errors were found on views.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/bag/views.JPG">
    </details>
</details>

<details><summary>CHECKOUT</summary>
    <details><summary>No errors were found on admin.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/checkout/admin.JPG">
    </details>
    <details><summary>No errors were found on apps.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/checkout/apps.JPG">
    </details>
    <details><summary>No errors were found on forms.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/checkout/forms.JPG">
    </details>
    <details><summary>No errors were found on models.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/checkout/models.JPG">
    </details>
    <details><summary>No errors were found on signals.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/checkout/signals.JPG">
    </details>
    <details><summary>No errors were found on urls.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/checkout/urls.JPG">
    </details>
    <details><summary>No errors were found on views.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/checkout/views.JPG">
    </details>
    <details><summary>No errors were found on webhook_handler.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/checkout/webhook_handler.JPG">
    </details>
    <details><summary>No errors were found on webhooks.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/checkout/webhooks.JPG">
    </details>
</details>

<details><summary>HOME</summary>
    <details><summary>No errors were found on urls.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/home/urls.JPG">
    </details>
    <details><summary>No errors were found on views.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/home/views.JPG">
    </details>
</details>

<details><summary>INSTRUMENTA</summary>
    <details><summary>No errors were found on settings.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/instrumenta/settings.JPG">
    </details>
    <details><summary>No errors were found on urls.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/instrumenta/urls.JPG">
    </details>
</details>

<details><summary>PRODUCTS</summary>
    <details><summary>No errors were found on admin.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/products/admin.JPG">
    </details>
    <details><summary>No errors were found on forms.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/products/forms.JPG">
    </details>
    <details><summary>No errors were found on models.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/products/models.JPG">
    </details>
    <details><summary>No errors were found on urls.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/products/urls.JPG">
    </details>
    <details><summary>No errors were found on views.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/products/views.JPG">
    </details>
    <details><summary>No errors were found on widgets.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/products/widgets.JPG">
    </details>
</details>

<details><summary>PROFILES</summary>
    <details><summary>No errors were found on forms.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/profiles/forms.JPG">
    </details>
    <details><summary>No errors were found on models.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/profiles/models.JPG">
    </details>
    <details><summary>No errors were found on urls.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/profiles/urls.JPG">
    </details>
    <details><summary>No errors were found on views.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/profiles/views.JPG">
    </details>
</details>

<details><summary>QUESTIONS</summary>
    <details><summary>No errors were found on admin.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/questions/admin.JPG">
    </details>
    <details><summary>No errors were found on forms.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/questions/forms.JPG">
    </details>
    <details><summary>No errors were found on models.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/questions/models.JPG">
    </details>
    <details><summary>No errors were found on urls.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/questions/urls.JPG">
    </details>
    <details><summary>No errors were found on views.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/questions/views.JPG">
    </details>
</details>

<details><summary>WISHLIST</summary>
    <details><summary>No errors were found on admin.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/wishlist/admin.JPG">
    </details>
    <details><summary>No errors were found on models.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/wishlist/models.JPG">
    </details>
    <details><summary>No errors were found on urls.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/wishlist/urls.JPG">
    </details>
    <details><summary>No errors were found on views.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/wishlist/views.JPG">
    </details>
</details>

<details><summary>No errors were found on custom_storages.py when passing through PEP8 Validator.</summary>
    <img src="docs/validation/python/custom_storages.JPG">
    </details>
<hr>

#### Javascript

<details><summary>No errors were found on bag.js when passing through jshint.</summary>
<img src="docs/validation/javascript/bag.JPG">
</details>

<details><summary>No errors were found on emailjs.js when passing through jshint.</summary>
<img src="docs/validation/javascript/emailjs.JPG">
</details>

<details><summary>No errors were found on products.js when passing through jshint.</summary>
<img src="docs/validation/javascript/products.JPG">
</details>

<details><summary>No errors were found on profile.js when passing through jshint.</summary>
<img src="docs/validation/javascript/profile.JPG">
</details>

<details><summary>No errors were found on stripe_elements.js when passing through jshint.</summary>
<img src="docs/validation/javascript/stripe_elements.JPG">
</details>
<hr>

#### Accessibility

<details><summary>No errors were found on the index.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_index_validation.JPG">
</details>

<details><summary>No errors were found on the add_product.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_add_products_validation.JPG">
</details>

<details><summary>No errors were found on the edit_product.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_edit_products_validation.JPG">
</details>

<details><summary>No errors were found on the product_detail.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_product_detail_validation.JPG">
</details>

<details><summary>No errors were found on the products.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_products_validation.JPG">
</details>

<details><summary>No errors were found on the questions.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_questions_validation.JPG">
</details>

<details><summary>No errors were found on the wishlist.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_wishlist_validation.JPG">
</details>

<details><summary>No errors were found on the bag.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_bag_validation.JPG">
</details>

<details><summary>No errors were found on the checkout.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_checkout_validation.JPG">
</details>

<details><summary>No errors were found on the checkout_success.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_checkout_success_validation.JPG">
</details>

<details><summary>No errors were found on the 404.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_404_validation.JPG">
</details>

<details><summary>No errors were found on the profile.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_profile_validation.JPG">
</details>

<details><summary>No errors were found on the reset_password.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_reset_password_validation.JPG">
</details>

<details><summary>No errors were found on the login.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_login_validation.JPG">
</details>

<details><summary>No errors were found on the logout.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_logout_validation.JPG">
</details>

<details><summary>No errors were found on the signup.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_signup_validation.JPG">
</details>
<hr>

#### Performance

<details><summary>index.html</summary>
<img src="docs/validation/lighthouse/index_light.JPG">
</details>

<details><summary>add_products.html</summary>
<img src="docs/validation/lighthouse/add_products_light.JPG">
</details>

<details><summary>edit_products.html</summary>
<img src="docs/validation/lighthouse/edit_products_light.JPG">
</details>

<details><summary>product_detail.html</summary>
<img src="docs/validation/lighthouse/product_detail_light.JPG">
</details>

<details><summary>products.html</summary>
<img src="docs/validation/lighthouse/products_light.JPG">
</details>

<details><summary>questions.html</summary>
<img src="docs/validation/lighthouse/questions_light.JPG">
</details>

<details><summary>wishlist.html</summary>
<img src="docs/validation/lighthouse/wishlist_light.JPG">
</details>

<details><summary>bag.html</summary>
<img src="docs/validation/lighthouse/bag_light.JPG">
</details>

<details><summary>checkout.html</summary>
<img src="docs/validation/lighthouse/checkout_light.JPG">
</details>

<details><summary>checkout_success.html</summary>
<img src="docs/validation/lighthouse/checkout_success_light.JPG">
</details>

<details><summary>profile.html</summary>
<img src="docs/validation/lighthouse/profile_light.JPG">
</details>

<details><summary>reset_password.html</summary>
<img src="docs/validation/lighthouse/reset_password_light.JPG">
</details>

<details><summary>login.html</summary>
<img src="docs/validation/lighthouse/login_light.JPG">
</details>

<details><summary>logout.html</summary>
<img src="docs/validation/lighthouse/logout_light.JPG">
</details>

<details><summary>signup.html</summary>
<img src="docs/validation/lighthouse/signup_light.JPG">
</details>
<hr>


## Browser Compatibility

* Chrome: The website is combatible and behaves as expected.

* Firefox: The website is combatible and behaves as expected.

* Edge: The website is combatible and behaves as expected.

## Further testing

* I have tested the website on One Plus 8T

* Friends and family has been asked to review the site.

## Testing user stories

1. As a Site Visitor I can see pictures of instruments when I enter the page so that I know what kind of page I am on.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  The carousel is on the home page |    arrive on home page    |       carousel will appear on home page     |  Works as expected  |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_1.png">
</details>
<hr>


2. As a Site Visitor I can see music instrument categories so I can find the products I am interested in.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Categories are present in navbar  | click choosen category |      navbar will appear on every page  | Works as expected |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_2.png">
</details>
<hr>


3. As a Site Visitor I can scroll thru a list of products so that I can find the product I want.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Page of products  |  Click any category | User will be taken to products page         | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_3.png">
</details>
<hr>


4. As a Site Visitor I can click on a product and see information about the product so I can get a better view of the product.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Product Details  |  Click on a product | User will be taken to product detail page       | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_4.png">
</details>
<hr>


5. As a Site Visitor I can sort products so I can find the product I want.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  sorting button  |  click on button and choose sorting | products will be sorted         | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_5.png">
</details>
<hr>


6. As a Site Visitor I can search for products so I can find the relevant one for me.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Search bar  |  search for product | User will be taken to products page with products found         | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_6.png">
</details>
<hr>


7. As a Site Visitor I can add products to a bag so I can see everything I have added.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Add to bag  |  Click on product > click on add to bag | product will be added to bag         | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_7.png">
</details>
<hr>


8. As a Site Visitor I can Update and Delete products in bag so I can Remove products I dont want.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Update and remove products  | Go to checkout > Click on update to update quantity, click on remove to remove | User will be taken to products page   | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_8.png">
</details>
<hr>


9. As a Site Visitor I can add products to a bag so that I can buy them

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Add to bag  |  Click on product > click on add to bag | product will be added to bag         | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_7.png">
</details>
<hr>


10. As a Site Visitor I can buy a product so I can get the product I want.
11. As a Site Visitor I can get an email confirmation so I can feel confident the purchase is ok.
12. As a Site Visitor I can view an order confirmation so I can feel confident everything is ok.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  checkout  |  add product to bag > click on checkout > click secure checkout > fill out delivery info > click complete order | order will be processed, user will get email conf, and come to order conf         | Works as expected   |
|  email confirmation  |  complete an order | User will get an email confirmation         | Works as expected   |
|  order confirmation  |  complete an order | User will be redirected to order confirmation         | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_10.png">
</details>
<hr>


13. As a Site Visitor I can browse the site and get notifications messages so I can know if things are working or not.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  notifications  |  add to bag, edit, remove | User will get a notification         | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_13.png">
</details>
<hr>


14. As a Site Visitor I can click on a button so that I can get to the top of the page quickly.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Back to top button  |  Click button | User will be taken to top of page         | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_14.png">
</details>
<hr>


15. As a Site Visitor I can read reviews so that I can see which products customers are happy with.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Reviews on products  |  Go to product detail > scroll down | User will find reviews or no reviews        | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_15.png">
</details>
<hr>


16. As a Site Visitor I can create an account so that I can have personal info saved.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Create account  |  Go to signup > fill out the form > verify email > confirm email | User will now have an account        | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_16.png">
</details>
<hr>


17. As a Site User I can log in to my account so that I can save my personal info.

* **Requires log in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Personal info  |  when logged in click my profile  > fill out the form > click update information | User will now have saved personal info        | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_17.png">
</details>
<hr>


18. As a Site User I can add a product to a wishlist so that I can keep track of products I want.

* **Requires log in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  add to wishlist |  go to product detail > click add to wishlist        |          product now added to wishlist  |   Works as expected |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_18.png">
</details>
<hr>

* **If not logged in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  add to wishlist |  wishlist not present in nav                  |          Visitor will not see wishlist button  |   Works as expected |
|  add to wishlist button |  wishlist button not present in product detail                  |          Visitor will not see wishlist button  |   Works as expected |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_18_not_logged_in.png">
</details>
<hr>


19. As a Site User I can delete a product from a wishlist so that I can remove products I dont want.

* **Requires log in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|   delete from wishlist      |  go to wishlist > click delete from wishlist  |   product will be removed from wishlist  | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_19.png">
</details>
<hr>

* **If not logged in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|   delete from wishlist      |  Fill out wishlist url  |  Visitor will be redirected to login page                | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_19_not_logged_in.png">
</details>
<hr>


20. As a Site User I can log in to my account so that I can leave reviews.

* **Requires log in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|   review underneath product   |   go to product_detail > scroll down > fill out form  |  the review will be posted underneath product  |  Works as expected  |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_20.png">
</details>
<hr>

* **If not logged in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|   review underneath product   |   go to product_detail > scroll down > fill out form  |  Visitor will not see form  but links to register and sign in |  Works as expected  |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_20_not_logged_in.png">
</details>
<hr>


21. As a Site User I can Delete my Review so that I can change my review or delete it if I want to.

* **Requires log in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  delete review  |   click on delete review  |   review will be removed  | Works as expected   |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_21.png">
</details>
<hr>

* **If not logged in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|   delete review   |   click on delete review  |  Visitor will not see delete review button |  Works as expected  |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_21_not_logged_in.png">
</details>
<hr>


22. As a Site User I can log in to my account so that I can Ask questions.
23. As a Site User I can view questions so that I can see what other people have had to say about the site.

* **Requires log in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  form for asking questions |    click questions button > scroll down > fill out form    |     Question will appear top of the screen    |   Works as expected |
|  page with questions |    click questions button    |     Questions will appear on the screen    |   Works as expected |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_22.png">
</details>
<hr>


* **If not logged in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|   question button in nav   |   click question button  |  Visitor will not see question button |  Works as expected  |
|   question url   |   Fill out url  |  Visitor will be redirected to signin page |  Works as expected  |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_22_not_logged_in.png">
</details>
<hr>


24. As a Site Admin I can add, read, update and delete products so that I can manage the content.

* **Requires admin**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Create product   | click my account > click product management > Fill out form > click add product   |  admin will be redirected to product detail page with new product  |   Works as expected |
|  Edit product   |  on products page > click edit on a product > edit change > click update product | admin will be redirected to product detail page with updated product    |   Works as expected |
|  Delete product   |  any product site > click delete  |      product will be deleted          |   Works as expected |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_24_create.png">
<img src="docs/test/userstory_24_edit.png">
<img src="docs/test/userstory_24_delete.png">
</details>
<hr>


* **If not admin**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  add product url   | Fill out url    |  user will be taken to login page  |   Works as expected |
|  Edit product url   |  Fill out url    |  user will be taken to login page    |   Works as expected |
|  Delete product url   |  Fill out url    |  user will be taken to login page          |   Works as expected |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_24_not_superuser.png">
</details>
<hr>


25. As a Site Admin I can see all checkout orders so that I can see what people are buying.

* **Requires admin**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Checkout admin   |  Log in to admin site > click orders  |  orders will appear  |   Works as expected |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_25.png">
</details>
<hr>


26. As a Site Admin I can create, read, update and delete questions so that I can manage my content.

* **Requires admin**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Create question   |  Log in to admin site > click question > add question > Fill out form > save  |  Question will appear at the top  |   Works as expected |
|  Read question   |  Log in to admin site > click question > choose question |      Whole question will appear           |   Works as expected |
|  Update question   |  Log in to admin site > click question > choose question > update question > save  |      Question will be updated           |   Works as expected |
|  Delete question   |  Log in to admin site > click question > choose question > delete question > delete  |      Question will be deleted          |   Works as expected |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_26_create.png">
<img src="docs/test/userstory_26_read.png">
<img src="docs/test/userstory_26_update.png">
<img src="docs/test/userstory_26_delete.png">
</details>
<hr>


27. As a Site Admin I can create, read, update and delete reviews so that I can manage my content.

* **Requires admin**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Create reviews   |  Log in to admin site > click reviews > add reviews > Fill out form > save  |  reviews will appear at the top  |   Works as expected |
|  Read reviews   |  Log in to admin site > click reviews > choose reviews |      Whole reviews will appear           |   Works as expected |
|  Update reviews   |  Log in to admin site > click reviews > choose reviews > update reviews > save  |      reviews will be updated           |   Works as expected |
|  Delete reviews   |  Log in to admin site > click reviews > choose reviews > delete reviews > delete  |      reviews will be deleted          |   Works as expected |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_27_create.png">
<img src="docs/test/userstory_27_read.png">
<img src="docs/test/userstory_27_update.png">
<img src="docs/test/userstory_27_delete.png">
</details>
<hr>


28. As a Site Admin I can manage the wishlist so that I can keep track of the wishlists.

* **Requires admin**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Create wishlist   |  Log in to admin site > click wishlist > add wishlist > choose user and products > save  |  wishlist will appear at the top  |   Works as expected |
|  Read wishlist   |  Log in to admin site > click wishlist > choose wishlist |      wishlist will appear and products will be greyed out           |   Works as expected |
|  Update wishlist   |  Log in to admin site > click wishlist > choose wishlist > update wishlist > save  |      wishlist will be updated           |   Works as expected |
|  Delete wishlist   |  Log in to admin site > click wishlist > choose wishlist > delete wishlist > delete  |      wishlist will be deleted          |   Works as expected |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_28_create.png">
<img src="docs/test/userstory_28_read.png">
<img src="docs/test/userstory_28_update.png">
<img src="docs/test/userstory_28_delete.png">
</details>
<hr>


29. As a Site Admin I can search for all my content so that I can find what I am interested in.

* **Requires admin**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Search   |  Log in to admin site > click model > search in search bar or filter  |  Relevant content will appear  |   Works as expected |
<details><summary>Screenshot</summary>
<img src="docs/test/userstory_29.png">
</details>
<hr>


## Bugs

* **Bug:** Django took base.html from allauth instead of the top base.html.

    * **Fix:** Remove blank space before file name.

* **Bug:** Footer was overlapping content.

    * **Fix:** Removed Bootstrap class fixed-footer.

* **Bug:** Site would not open.

    * **Fix:** Fixed typo in bag/urls.py from name=view to name=view_bag.

* **Bug:** Module not found, could not open server.

    * **Fix:** Fixed typo in context.py to contexts.py.

* **Bug:** Background in navbar would not cover the navbar when scrolling.

    **Fix:** Added constant white background to navbar.

* **Bug:** The grand total, bag total and delivery was not updating correctly.
    
    **Fix:** I changed the calculation in contexts.py from adding to multiplying *total += quantity * product.price*

* **Bug:** The body went underneath the header.
    
    **Fix:** I added a missing closing bracket in base.css.

* **Bug:** Site would not deploy correctly.
    
    **Fix:** I added a missing closing bracket for sql database.

* **Bug:** Content was overflowing on x axis.
    
    **Fix:** I added a parent div for banner under content with classes, **container-fluid** and **w-100**.


### Known bugs

* 

## Deployment

### Deploying to Heroku

1. Use **pip3 freeze > requirements.txt** in terminal to save libraries that needs to be installed on Heroku as well.

2. Create **Procfile** and add **web: gunicorn newsblog.wsgi**

3. Log in to Heroku.

4. Click on the **new** button in the top right corner and in the drop down menu choose **Create new app**.

5. Choose a name for the app and a region and click **Create app**.

6. Go to the **resources** tab and go to **add-ons**, search for **postgres** and add **heroku postgres**.

7. Go to the **settings** tab and go to **Config Vars**, click **Reveal Config Vars** and copy the DATABASE_URL**VALUE**. Add **DATABASE_URL** and **VALUE** to env in the code.

8. Add **SECRET_KEY** and **VALUE** to **Config Vars** and add to env in code.

9. Add **DATABASES** in settings.py to fork with heroku database

10. Write python3 manage.py migrate in terminal

11. Add url in settings.py on **ALLOWED_HOSTS**

12. Go to the **deploy** tab and pick **GitHub** as deployment method.

13. Search for a repository and connect to it.

14. Click the button **enable automatic deploys** and then the button **deploy branch**.

15. Wait for the app to build and then click the **view** button.

### Forking a repository

1. Log in to Github.
2. Find the repository.
3. In the top right corner click the fork button.
4. Now you will have a copy of the repository in your account.

### Cloning a repository
1. Log in to Github.
2. Find the repository.
3. Above the file window locate the green code button and click it.
4. To clone the repository using https copy the link.
5. Open Git bash.
6. Change the current directory to where you want the repository cloned.
7. In your terminal type now type “Git clone” followed by the repository you copied.
8. Press Enter.
9. Done.

## Credit

### Numerous videos, sites and articles was used to create this site.

* [This video was used for building rating and comments](https://www.youtube.com/watch?v=OvTs8BMLb7o).<br>
[This video was also used](https://www.youtube.com/watch?v=MZwKoi0wu2Q).<br>
[This site was used for the checkboxes](https://cdf.9vo.lt/1.11/django.forms.widgets/RadioSelect.html).<br>

* [Form rendering was a help from this site](https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html#custom-crispy-field)

## Acknowledgement

* My Mentor Mo has been invaluable, he pushed me to challenge myself and he was able to provide consistent and helpful feedback throughout my project.
