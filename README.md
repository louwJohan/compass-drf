
 <h1 align="center">Compass API</h1>

[View the live project here](https://compass-drf.herokuapp.com/)

Compass API is written to be used as a backend for a real estate type app. It uses the Django Rest Framework. The API has various app that can be used. It has a follow model that can be used for users following other user, a listing model where all the property listings can be saved, a messages model for sending messages to other users, a saved model for users to save their favorite listings and a profile model to update profile pictures or write something about the user. 


## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Planning](#planning)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience (UX)

### User stories :

* US01: Register/Login
  - As a **Site User**I can **create a profile** so that **I can access the features of the site**
* US02: Post a listing
  - As a **Site User** I can **log in** so that **I can list a property for sale**
* US03: Follow a User
  - As a **Site User** I can **follow a other user** so that **I can see all his listings and stay up to date if he lists new properties**
* US04: Messages
  - As a **Site User** I can **send a message** so that **I can request more info on the property or request a viewing**
* US05: Save a Listing
  - As a **Site User** I can **save a listing** so that **I can keep all the listings I like**
* US06: Update Profile
  - As a **Site User** I can **update my profile** so that **I can change my photo or write something about myself**
* US07: Update Listing
  - As a **Site User** I can **update my listing** so that **change the price or the description or photo**
* US08: Delete a listing
  - As a **Site User** I can **delete my listings** so that **I can remove a listing if a property is sold**
* US09: Listing security
  - As a **Site User** I can **change only my own listings** so that **no one else can change my listings**
* US10: Delete saved Listing
  - As a **Site User** I can **delete a saved listing** so that **I can remove it from my list of saved items**
* US11: Unfollow a user
  - As a **Site user** I can **unfollow a user** so that **I can no loger follow a user**
* US12: Delete a message
  - As a **Site user** I can **delete a message** so that **the user I sent the message to can no longer see it**


## Features

### Existing Features

-   __F01 Landing page__
    The landing page is very basic and welcome the user to the page.

    ![landing page](images/LANDING.jpg)
   

-   __F02 Follow page__
    
    The follow view show the following
    - ID 
    - Owner of the profile
    - Created at (when it was created)
    - Followed (the id of the user being followed)
    - Follwed name (the username of the user being followed)

    The following page can be accessed through https://compass-drf.herokuapp.com/following/.
    A message detail can be accessed by adding the id to the end expel. https://compass-drf.herokuapp.com/following/3.
    The owner of the profile will be able to delete the followed user.
    The information is paginated and only 12 posts is displayed per page

    ![Follow](images/follow.jpg)

-   __F03 Listing page__
    
    The Listings page has a list of all the property listings. I has many features.
    - ID 
    - Owner (Listing owner)
    - create at (When created)
    - updated at (when updated)
    - Title (short description)
    - is_owner (checks if current user is owner)
    - description (description of item)
    - type_of_property (what type of property expel. detached house, apartment etc.)
    - bedrooms (number of bedrooms)
    - area (area of property)
    - price (price of property)
    - commerce_type (is the property for rent or for sale)
    - saved_id (id of user that saved property)
    - images (images of property nr 1 to 8)
    - saved_count (the amount of users that has saved the property)
    - messages count (the amount of messages sent to owner)
    - profile_image (the profile image of the owner)
    - profile_id (profile id of owner)
    The information is paginated and only 12 posts is displayed per page
    https://compass-drf.herokuapp.com/listings/ displays a list
    https://compass-drf.herokuapp.com/listings/2 displays a the listing with the id 2. 
    The owner is the only user that can update or delete the listing

    ![Listing](images/listings.jpg)

-   __F04 Messages page__
    
    The messages has the following information
    - ID
    - owner (owner of the message)
    - listing (id of listing message is querying)
    - created_at (when message was created)
    - title (short title or heading)
    - content (content of message)
    - name (name of sender)
    - surname (surname of sender)
    - phone_number (number of sender)
    - email (email of sender)
    - listing_owner (id of listing owner)
    The information is paginated and only 12 posts is displayed per page
    https://compass-drf.herokuapp.com/messages/ displays list of messages
    https://compass-drf.herokuapp.com/messages/1 displays message with id 1.
    The owner is the only user that can update or delete the message.

    ![Messages page](images/messages.jpg)
    

-   __F05 Profile page__
    
    The users must be signed in to access the recipes page and the booking page.

    ![Login](static/images/login.jpg)
    ![Sign-up](static/images/sign-up.jpg)

-   __F06 Booking page User__
    
    The booking page displays a input to choose a day for a visit to the restaurant. When you choose a day the page renders the rest of the form. The form must be completed name, surname, telephone number amount of people and the times available. If a time is fully booked it will not appear in the available times. When a booking is confirmed the page redirects to the booking details.
    
    The booking page has a link to view your bookings in a list. If you click on one of the bookings it opens a page with the details of the booking and allows you to delete the booking
    
    ![Booking page top](static/images/booking_top.jpg)
    ![Booking page bottom](static/images/booking_bottom.jpg)
    ![Booking form](static/images/booking_form.jpg)
    ![Booking list page](static/images/your_bookings.jpg)
    ![Booking detail page](static/images/booking_details.jpg)

-   __F07 Recipe page User__
    
    The recipe link in the navigation directs the logged in user to a list that displays the recipes created by the chef. The user can choose a recipe and click on the link that will redirect them to a page that displays the details of the recipe 

    ![Recipe list](static/images/recipe_list.jpg)
    ![Recipe Detail](static/images/recipe_detail.jpg)
    

-   __F08 Booking page Staff__
    
    Staff members accessing the booking page has more options to choose from. There is a closed list that redirects them to a closed day list, there is also a link to create a new closed day. The link create new closed day will display a form to be completed and when posted will redirect to the item created. They can access a closed day by selecting one from the list and it will redirect them to a detail page where they can edit or delete the item. 

    The booking list link redirects them to a page with an input. They can select a day and it will display the booking for that day. If there are no bookings a message will display saying there are no bookings for that day.

    ![Booking day list](static/images/bookings_for_day.jpg)
    ![Booking day select](static/images/booking_for_day_choose.jpg)
    ![Closed list](static/images/closed_days_list.jpg)
    ![Closed Details](static/images/closed_details.jpg)
    ![Create closed day](static/images/create_closed.jpg)

-   __F09 Menu list(Staff member)__
    
    the Menu list page can only be accessed by a staff member. It displays a list of all the items on the menu. When a item is selected it displays the items details and the staff member can edit the item or delete it.
    The menu list page has a link to create a new menu item and will display a from to be completed.

    ![Menu list](static/images/menu_list.jpg)
    ![Menu details](static/images/menu_list_details.jpg)
    ![Menu Create Item](static/images/create_menu_item.jpg)

-   __F10 Recipe List(Staff members)__
    
    The Recipe list navigation link is only displayed to staff members. The link displays a recipe list page and has a link to create new recipes. The create new recipe page displays a from to be completed to create a new recipe. 

    When a recipe is selected from the list the details of the recipe is displayed with links to edit or delete the recipe.

    ![Recipe List](static/images/recipe_list_staff.jpg)
    ![Recipe Detail](static/images/recipe_detail_staff.jpg)
    ![Recipe create](static/images/create_new_recipe.jpg)


### Features which could be implemented in the future

-   __Social login__
    
    Add login by using social accounts

-   __Recipe likes__
    
    Implement function for users to like recipes 

## Design

-   ### Wireframes
Balsamiq was used to create the wire frames for the project and was used as a guide for the project
![Home](static/images/home_wireframe.jpg)
![Menu](static/images/menu_wireframe.jpg)
![Booking](static/images/booking_day_wf.jpg)
![Recipes](static/images/recipe_wf.jpg)
![Recipe Detail](static/images/recipe_detailwf.jpg)


**Database Design**

- PostgreSQL was used for the database

**Recipe Post**
- Stores all the data for the recipes

| **Key**        |  **Type**     | **Purpose**|
|-------------- |-------------- |-------------|
| _id           |  ObjectId     | ObjectId of this document
| title   |   String      | stores the title of the recipe
| author     |   User Id     | stores the id of the User object
| content     |   String      | stores the content of the recipe
| featured_image        |   Image      | stores a image of the recipe
| created_on      |   date      | stores the date the recipe was created 

**TimeSlot**
- Stores all the bookings made by customers

| **Key**        |  **Type**     | **Purpose**|
|-------------- |-------------- |-------------|
| _id           |  ObjectId     | ObjectId of this document
| date   |   string      | stores the date of the booking
| time     |   string     | stores the time of the booking
| first_name     |   String      | stores the customers first name
| last_name        |   String     | stores the customers Last name
| phone      |   number     | stores the customers number
| number_of_people     |   number      | stores the number of people attending
| user      |   User Id      | stores the Users Id

**Closed**
- Stores all the dates the restaurant is closed

| **Key**        |  **Type**     | **Purpose**|
|-------------- |-------------- |-------------|
| _id           |  ObjectId     | ObjectId of this document
| day  |   date     | stores the date 
| reason    |   string     | stores the reason the store is closed
| user      |   User Id      | stores the Users Id that created the event

**FoodMenu**
- Stores all the menu items

| **Key**        |  **Type**     | **Purpose**|
|-------------- |-------------- |-------------|
| _id           |  ObjectId     | ObjectId of this document
| title  |   string      | stores the title of the dish
| description     |   string     | stores a short description of the dish
| course     |   number      | stores a number indicating to a course
| price        |   number    | stores the price of the dish


## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

-   [Google Fonts:](https://fonts.google.com/) used for the Raleway font
-   [Font Awesome:](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.
-   [Git:](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/) is used as the respository for the project code after being pushed from Git. In addition, for this project GitHub was used for the agile development aspect through the use of User Stories (GitHub Issues) and tracking them on a Kanban board.
-   [Balsamiq:](https://balsamiq.com/) was used to create the wireframes during the design process.
-   [Django](https://www.djangoproject.com/) was used as the framework to support rapid and secure development of the application
-   [Bootstrap](https://getbootstrap.com/) was used to build responsive web pages
-   [Gunicorn](https://gunicorn.org/) was used as the Web Server to run Django on Heroku
-   [dj_database_url](https://pypi.org/project/dj-database-url/) library used to allow database urls to connect to the postgres db
-   [psycopg2](https://pypi.org/project/psycopg2/) database adapter used to support the connection to the postgres db
-   [Cloudinary](https://cloudinary.com/) used to store the images used by the application
-   [Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) used for account registration and authentication
-   [coverage](https://coverage.readthedocs.io/en/coverage-5.5/) used to check how much of the python code has been covered by 
automated tests

## Testing

### Validator Testing 

- [HTML Validator](https://validator.w3.org/)

    - As this project uses Django templates the html has been validated by manually clicking through the application pages, copying the source of the rendered pages and then validating this version of the html using the W3C Validator (link shown above).

    - Results: All pages passed without errors except the Recipe detail page. An error was indicated for use of % in width attribute in image tag, expected a number.
  

- [CSS Validator](https://jigsaw.w3.org/css-validator/)

  - Results: No errors were found in style.css


- [Python Validator](http://pep8online.com/)

  <details>
    <summary>Booking admin.py</summary>

  [Booking admin.py](pep8/booking_admin.txt)
  </details>
  
  <details>
    <summary>Booking models.py</summary>
    
  [Booking models.py](pep8/booking_models.txt)
  </details>

  <details>
    <summary>Booking test_views.py</summary>
    
  [Booking test_views.py](pep8/booking_test_views.txt)
  </details>

  <details>
    <summary>Booking views.py</summary>
    
  [Booking views.py](pep8/booking_views.txt)
  </details>
  
  <details>
    <summary>Easy Recipes admin.py</summary>
    
  [Easy Recipes admin.py](pep8/easy_recipe_admin.txt)
  </details>
  
  <details>
    <summary>Easy Recipes models.py</summary>
    
  [Easy Recipes models.py](pep8/easy_recipe_models.txt)
  </details>

  <details>
    <summary>Easy Recipes test_views.py</summary>
    
  [Easy Recipes test_views.py](pep8/easy_recipe_test_views.txt)
  </details>

  <details>
    <summary>Easy Recipes views.py</summary>
    
  [Easy Recipes views.py](pep8/easy_recipe_views.txt)
  </details>

  <details>
    <summary>Home views.py</summary>
    
  [Home views.py](pep8/home_views.txt)
  </details>

  <details>
    <summary>Menu admin.py</summary>
    
  [Menu admin.py](pep8/menu_admin.txt)
  </details>

  <details>
    <summary>Menu models.py</summary>
    
  [Menu models.py](pep8/menu_models.txt)
  </details>
  
  <details>
    <summary>Menu test_views.py</summary>
    
  [Menu test_views.py](pep8/menu_test_views.txt)
  </details>

  <details>
    <summary>Menu views.py</summary>
    
  [Menu views.py](pep8/menu_views.txt)
  </details>

### Automated Testing

   - [Django testing tools](https://docs.djangoproject.com/en/3.2/topics/testing/tools/) were used to test the application python code.  
   - DB tests were run in the development environment against a local SQLite3 database. 
   - Tests were written for the following files :

      - Booking tests for [views.py](booking/views.py):  test file: [test_views.py](booking/test_views.py)
      - Easy Recipe tests for [views.py](easy_recipe/views.py): test file: [test_views.py](easy_recipe/test_views.py)
      - Menu tests for [views.py](menu/views.py):  test file: [test_views.py](menu/test_views.py)
      - Home tests for [views.py](home/views.py): test file: [test_views.py](home/test_views.py)

  - Django test results and coverage :   
    ![Python Test Results](static/images/coverage1.jpg)
    ![Python Test Results Continued](static/images/coverage2.jpg)


### Browser Compatibility

- Chrome DevTools was used to test the responsiveness of the application on different screen sizes.
 
    
### Manual Testing Test Cases and Results

- The application was tested for both site users and staff users. Recipes was added, updated and deleted. Menu add items, edit and delete items was tested. Booking was tested for two users booking at the same time for the same time slot. The reset password was tested with the email confirmation. Adding, deleting and editing closed days was tested. Customer booking and deleting was tested. All links and navigation links were tested.

### Known bugs

- Currently no known bugs.

## Deployment

### How to Clone the Repository 

- Go to the https://github.com/louwJohan/project4-ci repository on GitHub 
- Click the "Code" button to the right of the screen, click HTTPs and copy the link there
- Open a GitBash terminal and navigate to the directory where you want to locate the clone
- On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process
- To install the packages required by the application use the command : pip install -r requirements.txt
- When developing and running the application locally set DEBUG=True in the settings.py file
- Changes made to the local clone can be pushed back to the repository using the following commands :

  - git add *filenames*  (or "." to add all changed files)
  - git commit -m *"text message describing changes"*
  - git push

- N.B. Any changes pushed to the master branch will take effect on the live project once the application is re-deployed from Heroku

### Create Application and Postgres DB on Heroku
- Log in to Heroku at https://heroku.com - create an account if needed.
- From the Heroku dashboard, click the Create new app button.  For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.
- On the Create New App page, enter a unique name for the application and select region.  Then click Create app.
- On the Application Configuration page for the new app, click on the Resources tab.
- In the Add-ons search bar enter "Postgres" and select "Heroku Postgres" from the list - click the "Submit Order Form" button on the pop-up dialog.
- Next, click on Settings on the Application Configuration page and click on the "Reveal Config Vars" button - check the DATABASE_URL has been automatically set up. 
- Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1.
- Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols.
- The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :

  - DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

  - SECRET_KEY = os.environ.get('SECRET_KEY')

- In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command : python3 manage.py migrate 
- Make sure the project requirements.txt file is up to date with all necessary supporting files by entering the command : pip3 freeze --local > requirements.txt
- Commit and push any local changes to GitHub.
- In order to be able to run the application on localhost, add SECRECT_KEY and DATABASE_URL and their values to env.py

### Configure Cloudinary to host images used by the application
- Log in to Cloudinary - create an account if needed.  To create the account provide your name, email and set up a password.  For "primary interest" you can choose "Programmable Media for image and video API".  Click "Create Account" and you will be sent an email to verify your account and bring you to the dashboard.
- From the dashboard, copy the "API Environment variable" value by clicking on the "Copy to clipboard" link.
- Log in to Heroku and go to the Application Configuration page for the application.  Click on Settings and click on the "Reveal Config Vars" button.
- Add a new Config Var called CLOUDINARY_URL and assign it the value copied from the Cloudinary dashboard, but remove the "CLOUDINARY_URL=" at the beginning of the string. 
- In order to be able to run the application on localhost, also add the CLOUDINARY_URL environment variable and value to env.py

### Connect the Heroku app to the GitHub repository
- Go to the Application Configuration page for the application on Heroku and click on the Deploy tab.
- Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository (the one used for this project is (https://github.com/louwJohan/project4-ci) and click on Connect to link up the Heroku app to the GitHub repository code.
- Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Manual Deploy was selected.
- The application can be run from the Application Configuration page by clicking on the Open App button.
- The live link for this project is (https://the-smoking-goat.herokuapp.com/)

### Final Deployment steps
Once code changes have been completed and tested on localhost, the application can be prepared for Heroku deployment as follows :
- Set DEBUG flag to False in settings.py
- Ensure requirements.txt is up to date using the command : pip3 freeze --local > requirements.txt
- Push files to GitHub
- In the Heroku Config Vars for the application delete this environment variable :  DISABLE_COLLECTSTATIC
- On the Heroku dashboard go to the Deploy tab for the application and click on deploy branch


## Credits 

### Code 
- Much of the coding and testing relies heavily on information in the "Hello Django" and "I Think Therefore I Blog" walkthroughs in the Code Institue Full Stack Frameworks module. 
- 


### Media 
- The Raleway font used was imported from [Google Fonts](https://fonts.google.com/)
- Fontawesome was used for icons [Font Awesome](https://fontawesome.com/)
- The applicaiton favicon was created from the "exchange" icon image on [Font Awesome](https://fontawesome.com/) 
- Pexels.com was used for all the images[Pexels](https://www.pexels.com/)
  
