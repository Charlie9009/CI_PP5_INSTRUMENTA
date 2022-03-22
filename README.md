# Instrumenta

<img src="">

<hr>

## Welcome to my Site [Instrumenta]()!

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

* The goal of this project is for the site owner to practice Django and to create a News Blog for other users.

## User experience

### Target audience

* This site is targeted towards people who would like to share news.

### User stories

#### Site Visitor

1. As a Site Visitor I can read news so I can keep up to speed with the world.

2. As a Site Visitor I can create an account so that I can interact with the content, add my own content and search for content.

3. As a Site Visitor I can view questions so that I can see what other people have had to say about the site.

#### Site User

4. As a Site User I can create, read, update and delete posts so that I can manage my content.

5. As A Site User I can search for posts so I can find the relevant one for me.

6. As a Site User I can click on a post and see comments and the post so I can get a better view of the posts.

7. As a Site User I can read comments so that I can get a nuanced view of the news.

8. As a Site User I can comment on a post so that I can ask question and be a part of the conversation.


#### Site owner goals

9. As a Site Admin I can create, read, update and delete posts so that I can manage my content.

10. As a Site Admin I can mark posts with warnings so that I can keep track of users abusing the page.

11. As a Site Admin I can search for posts, comments and questions so that I can find what I am interested in.

12. As a Site Admin I can answer questions so that users feel included in the site.

### Technical design

### Design

* 

#### Colors

* For the colors I wanted a more sophisticated clean look, after some googling I found [visme](https://visme.co/blog/website-color-schemes/) and number 7 on the list caught my attention. I took that as a starting point and experimented a bit.

#### Fonts

* I chose the font [*Roboto*](https://fonts.google.com/specimen/Roboto) as it felt neutral and did not stick out.

### Wireframes

* Below you can see the images of the wireframes

<details><summary>index.html</summary>
<img src="docs/wireframes/index_wireframe.png">
<img src="docs/wireframes/index_tablet_wireframe.png">
<img src="docs/wireframes/index_mobile_wireframe.png">
</details>

<details><summary>login.html</summary>
<img src="docs/wireframes/login_wireframe.png">
<img src="docs/wireframes/login_tablet_wireframe.png">
<img src="docs/wireframes/login_mobile_wireframe.png">
</details>

<details><summary>signout.html</summary>
<img src="docs/wireframes/signout_wireframe.png">
<img src="docs/wireframes/signout_tablet_wireframe.png">
<img src="docs/wireframes/signout_mobile_wireframe.png">
</details>

<details><summary>register.html</summary>
<img src="docs/wireframes/register_wireframe.png">
<img src="docs/wireframes/register_tablet_wireframe.png">
<img src="docs/wireframes/register_mobile_wireframe.png">
</details>

<details><summary>post_create.html</summary>
<img src="docs/wireframes/post_create_wireframe.png">
<img src="docs/wireframes/post_create_tablet_wireframe.png">
<img src="docs/wireframes/post_create_mobile_wireframe.png">
</details>

<details><summary>post_delete_confirm.html</summary>
<img src="docs/wireframes/post_delete_confirm_wireframe.png">
<img src="docs/wireframes/post_delete_confirm_tablet_wireframe.png">
<img src="docs/wireframes/post_delete_confirm_mobile_wireframe.png">
</details>

<details><summary>post_detail.html</summary>
<img src="docs/wireframes/post_detail_wireframe.png">
<img src="docs/wireframes/post_detail_tablet_wireframe.png">
<img src="docs/wireframes/post_detail_mobile_wireframe.png">
</details>

<details><summary>post_update.html</summary>
<img src="docs/wireframes/post_update_wireframe.png">
<img src="docs/wireframes/post_update_tablet_wireframe.png">
<img src="docs/wireframes/post_update_mobile_wireframe.png">
</details>

<details><summary>question.html</summary>
<img src="docs/wireframes/question_wireframe.png">
<img src="docs/wireframes/question_tablet_wireframe.png">
<img src="docs/wireframes/question_mobile_wireframe.png">
</details>

<details><summary>search_results.html</summary>
<img src="docs/wireframes/search_results_wireframe.png">
<img src="docs/wireframes/search_results_tablet_wireframe.png">
<img src="docs/wireframes/search_results_mobile_wireframe.png">
</details>

### Database diagram

* The database has three models;
    * Post
    * Comment
    * Question
* Post and Comment have a many to one relationship and also uses the imported *User* class model for username and passwords.

* Question does not have any relationship with the other models.
<details><summary>Database Diagram</summary>
<img src="docs/database_diagram/database_diagram.JPG">
</details>

## Features

* **News List**

* The opening of the site shows a list of posts
<br>
<img src="docs/features/feature_view_news.JPG">

### User stories covered by this feature:

    1. 
<hr>

* **Account creation**

* A feature was implemented for a user to create an account
<br>
<img src="docs/features/feature_register.png">

### User stories covered by this feature:

    2. 
<hr>

* **Questions**

* A feature was implemented where the admin answers users questions
<br>
<img src="docs/features/feature_question.png">

### User stories covered by this feature:

    3. 
<hr>

* **Crud**

**Requires log in**

* A feature was implemented so users can create, read, update and delete their posts
<br>
<img src="docs/features/feature_crud.png">

### User stories covered by this feature:

    4.
<hr>

* **Search**

**Requires log in**

* A feature was implemented so users can search for content
<br>
<img src="docs/features/feature_search.png">

### User stories covered by this feature:

    5. 
<hr>

* **Open Post**

**Requires log in**

* A feature was implemented so users can click on a post to read it
<br>
<img src="docs/features/feature_read_post.png">

### User stories covered by this feature:

    6. 
<hr>

* **Read Comments**

**Requires log in**

* A feature was implemented so users see comments made underneath the post
<br>
<img src="docs/features/feature_read_comment.png">

### User stories covered by this feature:

    6. 
<hr>

* **Make Comments**

**Requires log in**

* A feature was implemented so users can make comments on posts
<br>
<img src="docs/features/feature_make_comment.png">

### User stories covered by this feature:

    6. 
<hr>

* **Admin Crud**

**Requires superuser**

* A feature was implemented so the admin can manage the content on the page
<br>
<img src="docs/features/feature_admin_crud.png">

### User stories covered by this feature:

    9. 
<hr>

* **Admin Warning**

**Requires superuser**

* A feature was implemented so the admin can mark posts with warnings to keep track of abusing users
<br>
<img src="docs/features/feature_admin_warning.png">

### User stories covered by this feature:

    10.
<hr>

* **Admin Search**

**Requires superuser**

* A feature was implemented so the admin can search for posts
<br>
<img src="docs/features/feature_admin_search.png">

### User stories covered by this feature:

    11. 
<hr>

* **Admin Questions**

**Requires superuser**

* A feature was implemented so the admin can answer and post questions
<br>
<img src="docs/features/feature_admin_question.JPG">

### User stories covered by this feature:

    5. 
    11. 
<hr>

### Features left to implement

* 

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

<details><summary>No errors were found on login.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/login_validation.JPG">
</details>

<details><summary>No errors were found on logout.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/logout_validation.JPG">
</details>

<details><summary>No errors were found on post_create.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/post_create_validation.JPG">
</details>

<details><summary>No errors were found on post_delete_confirm.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/post_delete_confirm_validation.JPG">
</details>

<details><summary>No errors were found on post_detail.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/post_detail_validation.JPG">
</details>

<details><summary>No errors were found on post_update.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/post_update_validation.JPG">
</details>

<details><summary>No errors were found on question.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/question_validation.JPG">
</details>

<details><summary>No errors were found on register.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/register_validation.JPG">
</details>

<details><summary>No errors were found on search_results.html when passing through WC3 Validator.</summary>
<img src="docs/validation/html/search_results_validation.JPG">
</details>
<hr>

#### CSS

<details><summary>No errors were found on the CSS file when passing through Jigsaw W3 Validator.</summary>
<img src="docs/validation/css/css_validation.JPG">
</details>
<hr>


#### Python

<details><summary>No errors were found on admin.py when passing through PEP8 Validator.</summary>
<img src="docs/validation/python/admin_validation.JPG">
</details>

<details><summary>No errors were found on blog_urls.py when passing through PEP8 Validator.</summary>
<img src="docs/validation/python/blog_urls_validation.JPG">
</details>

<details><summary>No errors were found on forms.py when passing through PEP8 Validator.</summary>
<img src="docs/validation/python/forms_validation.JPG">
</details>

<details><summary>No errors were found on models.py when passing through PEP8 Validator.</summary>
<img src="docs/validation/python/models_validation.JPG">
</details>

<details><summary>No errors were found on newsblog_urls.py when passing through PEP8 Validator.</summary>
<img src="docs/validation/python/newsblog_urls_validation.JPG">
</details>

<details><summary>No errors were found on views.py when passing through PEP8 Validator.</summary>
<img src="docs/validation/python/views_validation.JPG">
</details>
<hr>

#### Javascript

<details><summary>No errors were found on news.js when passing through jshint.</summary>
<img src="docs/validation/javascript/news_validation.JPG">
</details>
<hr>

#### Accessibility

<details><summary>No errors were found on the base/index.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_base_index_validation.JPG">
</details>

<details><summary>No errors were found on the login.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_login_validation.JPG">
</details>

<details><summary>No errors were found on the logout.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_logout_validation.JPG">
</details>

<details><summary>No errors were found on the signup.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_register_validation.JPG">
</details>

<details><summary>No errors were found on the question.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_question_validation.JPG">
</details>

<details><summary>No errors were found on the delete_confirm.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_delete_confirm_validation.JPG">
</details>

<details><summary>No errors were found on the post_create.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_post_create_validation.JPG">
</details>

<details><summary>No errors were found on the post_detail.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_post_detail_validation.JPG">
</details>

<details><summary>No errors were found on the post_update.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_post_update_validation.JPG">
</details>

<details><summary>No errors were found on the search_results.html when passing through Wave Web Accessibility Validator.</summary>
<img src="docs/validation/accessibility/wave_search_results_validation.JPG">
</details>
<hr>

#### Performance

<details><summary>index.html</summary>
<img src="docs/validation/lighthouse/index_light.JPG">
</details>

<details><summary>login.html</summary>
<img src="">
</details>

<details><summary>logout.html</summary>
<img src="">
</details>

<details><summary>post_create.html</summary>
<img src="">
</details>

<details><summary>post_delete_confirm.html</summary>
<img src="">
</details>

<details><summary>post_detail.html</summary>
<img src="">
</details>

<details><summary>post_update.html</summary>
<img src="">
</details>

<details><summary>question.html</summary>
<img src="">
</details>

<details><summary>register.html</summary>
<img src="">
</details>

<details><summary>search_results.html</summary>
<img src="">
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

1. As a Site Visitor I can read news so I can keep up to speed with the world.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  The newspost are on the home page |    arrive on home page    |       posts will appear on home page     |  Works as expected  |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


2. As a Site Visitor I can create an account so that I can interact with the content, add my own content and search for content.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Form to fill out account info  | Click register button and fill out form |      When form is submited, user will be logged in  | Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


3. As a Site Visitor I can view questions so that I can see what other people have had to say about the site.

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Page to display questions  |  Click the question button | User will be taken to the question page         | Works as expected   |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


4. As a Site User I can create, read, update and delete posts so that I can manage my content.
**Requires log in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Create posts|  Click on *new post* button            |          User will be taken to a form to fill out  |   Works as expected |
|  Read posts|  Posts are present on home page, click *read more* button to read the hole post | User will be taken to post  |   Works as expected |
|  Update posts|  Click on *read more* of own created post, click *edit* and then *update* | User will updated post  |   Works as expected |
|  Delete posts|  Click on *read more* of own created post, click *delete* and then *yes, delete* | User will be taken to home page  |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>

* **If not logged in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Create posts|  Click on *new post* button                  |          Visitor will not see *new post* button  |   Works as expected |
|  Read posts|  Click *read more* button to read the hole post | Visitor will be taken to register page  |   Works as expected |
|  Update posts|  Click on *read more*                       |      Visitor will be taken to register page  |   Works as expected |
|  Update posts|  Write url for updating post                   |     Visitor will be taken to log in page  |   Works as expected |
|  Delete posts|  Click on *read more*                           | Visitor will be taken to log in page  |   Works as expected |
|  Delete posts|  Write url for deleting post                     | Visitor will be taken to log in page  |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


5. As A Site User I can search for posts so I can find the relevant one for me.
**Requires log in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|   Searching for posts      |  Fill out search bar and click *search* button  |   A user will be taken to search page with results underneath  | Works as expected   |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>

* **If not logged in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|   Searching for posts      |  Fill out search bar and click *search* button  |  Visitor will not see search bar                | Works as expected   |
|   Searching for posts      |  Write url for searching                   |  Visitor will be taken to log in page             | Works as expected   |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


6. As a Site User I can click on a post and see comments and the post so I can get a better view of the posts.
**Requires log in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|   Comments underneath posts   |   Click on *read more* button  |  A user will be taken to the post and underneath comments will appear  |  Works as expected  |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>

* **If not logged in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|   Comments underneath posts   |   Click on *read more* button  |  Visitor will be taken to register page                |  Works as expected  |
|   Comments underneath posts   |   Write url for post  | Visitor will be taken to log in page                           |  Works as expected  |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


7. As a Site User I can read comments so that I can get a nuanced view of the news.
**Requires log in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Comments underneath posts  |    Click on *read more* button  |   A user will be taken to the post and underneath comments will appear  | Works as expected   |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


8. As a Site User I can comment on a post so that I can ask question and be a part of the conversation.
**Requires log in**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Form underneath comments |    Fill out form, *submit*    |       After submit user will be taken to top of the page with the newest comment at the top  |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


9. As a Site Admin I can create, read, update and delete posts, comments and questions so that I can manage my content.
**Requires superuser**

* **Post**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Create post   |  Log in to admin site > click *post* > *add post* > Fill out form > *save*  |  Post will appear at the top of the home site  |   Works as expected |
|  Read post   |  Log in to admin site > click *post* > choose post |      Whole post will appear           |   Works as expected |
|  Update post   |  Log in to admin site > click *post* > choose post > update post > *save*  |      Post will be updated           |   Works as expected |
|  Delete post   |  Log in to admin site > click *post* > choose post > delete post > *delete*  |      Post will be deleted          |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>

* **Comment**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Create comment   |  Log in to admin site > click *comment* > *add comment* > Fill out form > *save*  |  Comment will appear at the top of the home site  |   Works as expected |
|  Read comment   |  Log in to admin site > click *comment* > choose comment |      Whole comment will appear           |   Works as expected |
|  Update comment   |  Log in to admin site > click *comment* > choose comment > update comment > *save*  |      Comment will be updated           |   Works as expected |
|  Delete comment   |  Log in to admin site > click *comment* > choose comment > delete comment > *delete*  |      Comment will be deleted          |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>

* **Question**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Create question   |  Log in to admin site > click *question* > *add question* > Fill out form > *save*  |  Question will appear at the top of the home site  |   Works as expected |
|  Read question   |  Log in to admin site > click *question* > choose question |      Whole question will appear           |   Works as expected |
|  Update question   |  Log in to admin site > click *question* > choose question > update question > *save*  |      Question will be updated           |   Works as expected |
|  Delete question   |  Log in to admin site > click *question* > choose question > delete question > *delete*  |      Question will be deleted          |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>

* **If not superuser**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Create post   |              Log in to admin site      |  If user isn't authorized logging in wont be possible  |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>

10. As a Site Admin I can mark posts with warnings so that I can keep track of users abusing the page.
**Requires superuser**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
| Marking posts with warnings  |   Log in to admin site > click *post* > choose post > in drop down menu choose warning |  Post will be marked with warning  | Works as expected   |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>


11. As a Site Admin I can search for posts, comments and questions so that I can find what I am interested in.
**Requires superuser**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Search post   |  Log in to admin site > click *post* > search in search bar  |  Relevant post(s) will appear  |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Search comment   |  Log in to admin site > click *comment* > search in search bar  |  Relevant comment(s) will appear  |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Search question   |  Log in to admin site > click *question* > search in search bar  |  Relevant question(s) will appear  |   Works as expected |
<details><summary>Screenshot</summary>
<img src="">
</details>
<hr>

12. As a Site Admin I can answer questions so that users feel included in the site.
**Requires superuser**

|             Feature           |        Action        |                 Expected result                    |   Actual result     |
|            :----------:       |    :------------:    |               :-----------------:                  | :---------------:   |
|  Add questions  |   Log in to admin site > click *question* > click *add question* > fill out form > if answered it will appear on front end > *save* |   |  Works as expected |
<details><summary>Screenshot</summary>
<img src="">
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

* 

## Acknowledgement

* My Mentor Mo has been invaluable, he pushed me to challenge myself and he was able to provide consistent and helpful feedback throughout my project.
