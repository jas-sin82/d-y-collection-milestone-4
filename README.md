# David & Yenny Collection ( Online Fashion Boutique)

[View Live Project Here](https://d-y-collection-milestone-4.herokuapp.com/)


## Full Stack Framework Milestone 4 project.

### Overview

This project presents a Online Fashion Boutique call David & Yenny Collection. Boutique provides both fashionable & stylish range of clothes and bags both for men's and women's. I have designed this project/ecommerce store , fully focus on Database creation, security and UI / UX. Website has a few diffrent webpages each page has different contents and product description but as user prospective each webpage will easily and smoothly will navigate user to their destination.

# Highlights


 * [User Experience (UX)](#User-experience-UX)

   * [User Desire](#user-desire)

   * [User Stories](#user-stories)


 * [Design](#design)

   * [Colors](#colors)

   * [Typography](#typography)

   * [Imagery](#imagery)

   * [Icons](#icons)

   * [Wireframes of website](#wireframes-of-website)

   * [ Responsive Screenshots ](#responsive-screenshots)

 * [Database Model](#database-model) 

 * [Features](#features)

 * [Technology used in a Project](#technology-used-in-a-Project)

 * [Testing](#testing)

 * [Deployment](#Deployment)
 
 * [Credits](#credits)

 
 #  User Experience (UX)

 ## User Desire

  
  * User will be easy intractive with the Webiste beacuse all the webpages/navlinks will easily and smoothly will navigate 
    user to their destination.

  * User is looking for online webstore with product offers and wide range of stylish and modern clothes.

  * User is looking for online webstore where user is able to make a login and profile so they can save their purchase details for future need.

  * User is looking for online webstore where they can read and leave product review.

  *  User is looking for online webstore after order has processed, they will have purchase conformation by email.
  

[Back to Highlights ](#highlights)

 ## User Stories  

 * As a first Time Visitor!

    * I want to easily understand the main purpose of the site so I can decide to stay longer.

    * I want to all the webpages/navlinks will easily and smoothly navigate user to their destination.

    * I want  to search for sale products  or just any particular product without spending much time.

    * I want to buy a product without  registration or login.

    *  Getting a full order conformation by email.

    *  I want to Read product review so I will know about product quality. 

    *  I want to make login and save my profile for future purchase.

    *  I want to able to  recover my password if I forgotten it.

    *  I want to ensure my personal information/bank card detail is safe and secure.

 * As a returning visitor:

    * Able to easily register and update my profile information.

    *  Able to leave product review easily.

    *  Able to see my purchase history, what I have purchased.

    *  Able to save my contact details.

    * Able to get free order delivery to save money.


 *   As an Author of the site:

     * Be able to add new Products CRUD (author can Update, add, delete products stock according to its popularity or unpopularity )!

     * As a Author I want to fully Ensure website is safe and secure, so I can secure my company and reputation.
 
     * Be able to change sale discount percent according to occasion or festivals offers.

     * Be able to Delete inappropriate product reviews, which could affect business.

# Strategy 

 * As a author I have Choose a white bg and light colors for web design that will help to convert visitors to regular user.
   The home page contain some of the beautiful products images and carousel which will attract visitors to find out more about 
   website.

 * As a Author I have Choose this unique name , logo and design which will help my business to attract new users.

 *  As a Author I have placed one christmas sale section which will hold my user to stay tuned until christmas sale..

[Back to Highlights ](#highlights)


# Design

  ### Colors 

  * Themecolor of the webpage is white. White color has used as background color through out the whole website.I have placed three buttons on the home page color of orange And black background with white text.The main purpose behind to use just white background, black text and the images with light background used throughout the project is to make user intraction above.

  * Main nav which is clean and clear white color with black text and beautiful logo of company, I have used box shadow to make nav bar more user intrative.

  * Mobile navigation menu (side bar) with a clear white background with black text and  with red color left border on each nav links when its drop down which will  be imaging  experience for customer/user.

  * Fade color #abbaab and box shadow used in footer which is perfectly good combination with rest of the website and more user intrative.

  ### Typography 

   * There will be two fonts used throughout the website. Roboto , Playfair Display SC and Serif specific so that will be used for the fall back font,
      Playfair Display SC font used in  webpage headings and 80% content to make more user intractive.

  ### Imagery

   * Choices of the images is an important component of this website both product images and the other images used throughout the website. I choosed clean images that will intract Visitors. Hero image at the home page to catch the visitors intrerest and strategically add Flickity carousel which contains some stunning new arrival products images and bottom of the page christmas day timer which count down the christmas sale, which will help to attract visitors to look more in side webpage.

   * Brand logo D & Y is represents a family brand name David & Yenny which is it self great attraction for user to know more about brand and products.

  ### Icons 

   * All icons used has taken from Font Awesome [Font Awesome.](https://fontawesome.com/). I have used search button icon,bag icon, user account icon, 
     direction icon used in keep shopping buttons, edit ,delete ,add produts and product review, dropdown menu and for external links social media
     icon in the footer.

  ### Wireframes of website

  I used a balsamiq to create a wireframe. Here is link [balsamiq](https://www.balsamiq.com/)

  [Home Page](https://share.balsamiq.com/c/p7vuW6A6X9ZKB1G5sMRbMH.png) 

  [Product Page](https://share.balsamiq.com/c/WHwCLtJd5qhjaGesYQbg6.png) 

  [Product Detail](https://share.balsamiq.com/c/hMXGnAmdFAnFegsaQs9VLB.png) 

  [Bag Page](https://share.balsamiq.com/c/tSDn1chacg569Ut1fLti8M.png)


  ### Responsive Screenshots

  <img src="responsive/ipad.png">

  <img src="responsive/nest-hub-max.png">
 
  <div><img src="responsive/iphone-5.png"></div>
 
  <div><img src="responsive/iphone-6.png"></div>

  <div><img src="responsive/nest-hub.png"></div>

  [Back to Highlights ](#highlights)


# Database Model

 During development the website will use SQLite3 which is the default database used by Django. Once deployed the website will use a PostgreSQL database which can be added/hosted by Heroku.


 The database schema was captured using [DB Diagram](https://dbdiagram.io/home)

 <img src="responsive/database-schema.png">
  

## Profile App

### User Profile Model

|Name             |Database Key            |Field Type         | Validation Requirements                     |
|-----------------|------------------------|-------------------|---------------------------------------------|
|User             |user                    |OneToOneField(User)|on_delete=models.CASCADE                     |
|Phone Number     |default_phone_number    |CharField          |max_length=20, null=True, blank=True         |
|Street Address 1 |default_street_address1 |CharField          |max_length=80, null=True, blank=True         |
|Street Address 2 |default_street_address2 |CharField          |max_length=80, null=True, blank=True         |
|Town or City     |default_town_or_city    |CharField          |max_length=40, null=True, blank=True         |
|County           |default_county          |CharField          |max_length=80, null=True, blank=True         |
|Postcode         |default_postcode        |CharField          |max_length=20, null=True, blank=True         |
|Country          |default_country         |CountryField       |blank_label='Country', null=True, blank=True |


## Products App


### Category Model
| Name             | Database Key            | Field Type              | Validation Requirements                               |
|------------------|-------------------------|-------------------------|-------------------------------------------------------|
| Name             | name                    | CharField               | max_length=254                                        |
| Friendly Name    | friendly_name           | CharField               | max_length=254, null=True, blank=True                 |


### Brand Model
| Name             | Database Key            | Field Type              | Validation Requirements                               |
|------------------|-------------------------|-------------------------|-------------------------------------------------------|
| Name             | name                    | CharField               | max_length=254                                        |
| Friendly Name    | friendly_name           | CharField               | max_length=254, null=True, blank=True                 |


### Product Model
| Name             | Database Key            | Field Type              | Validation Requirements                               |
|------------------|-------------------------|-------------------------|-------------------------------------------------------|
| Sku              | sku                     | CharField               | max_length=254, default="", blank=True                |
| Category         | category                | ForeignKey              | null=True, blank=True, on_delete=models.SET_NULL      |
| Brand            | brand                   | ForeignKey              | null=True, blank=True, on_delete=models.SET_NULL      |
| Name             | name                    | CharField               | max_length=254L                                       |    
| Description      | description             | TextField               | None                                                  |        
| Price            | price                   | DecimalField            | max_digits=6, decimal_places=2                        |    
| On Sale          | on_sale                 | BooleanField            | default=False, blank=True                             |
| Discount Percent | discount_percent        | DecimalField            | max_digits=2, decimal_places=0, blank=True, null=True |
| Image A          | image_a                 | ImageField              | null=True, blank=True                                 |
| Image B          | image_b                 | ImageField              | null=True, blank=True                                 |
| Image c          | image_c                 | ImageField              | null=True, blank=True                                 |
| Image d          | image_d                 | ImageField              | null=True, blank=True                                 |   
| Average Rating   | average_rating          | DecimalField            | max_digits=4, decimal_places=2, null=True, blank=True |   
| Gender           | gender                  | CharField               | max_length=1, choices=GENDER                          |
| Size             | size                    | BooleanField            | default=False, null=True, blank=True                  |   
| Date Added       | date_added              | DateTimeField           | default=timezone.now                                  |

### Review Model
| Name            | Database Key   | Field Type           | Validation                                                                |
| --------------- | -------------- | ---------------------| --------------------------------------------------------------------------|
| User            | User           | ForeignKey(User)     | on_delete=models.CASCADE, null=False, blank=False, related_name='review'  |
| Product         | product        | ForeignKey(Product)  | on_delete=models.CASCADE, null=False, blank=False, related_name='product' |
| Title           | title          | CharField            | max_length=254                                                            |
| Review Text     | review_text    | TextField            | None                                                                      |
| Review Rating   | review_rating  | IntegerField         | choices=RATING, default=5                                                 |
| Date Added      | date_added     | DateTimeField        | auto_now_add=True                                                         |


## Checkout App

### Order Model
| Name                     | Database Key    | Field Type                 | Validation                                                   |
| ------------------------ | --------------- | ---------------------------| -------------------------------------------------------------|
| Order Number             | order_number    | CharField                  | max_length=32, null=False, editable=False                    |
| User Profile             | user_profile    | ForeignKey(UserProfile)    | on_delete=models.SET_NULL, null=True, related_name='orders'  |
| Full Name                | full_name       | CharField                  | max_length=50, null=False, blank=False                       |
| Email Address            | email           | EmailField                 | max_length=254, null=False, blank=False                      |
| Phone Number             | phone_number    | CharField                  | max_length=20, null=False, blank=False                       |
| Country                  | country         | CountryField               | blank_label='Country *', null=False, blank=False             |
| Postcode                 | postcode        | CharField                  | max_length=20, null=True, blank=True                         |
| Town or City             | town_or_city    | CharField                  | max_length=40, null=False, blank=False                       |
| Street Address 1         | street_address1 | CharField                  | max_length=80, null=False, blank=False                       |
| Street Address 2         | street_address2 | CharField                  | max_length=80, null=True, blank=True                         |
| County                   | county          | CharField                  | max_length=80, null=True, blank=True                         |
| Date                     | date            | DateTimeField              | auto_now_add=True                                            |
| Delivery Cost            | delivery_cost   | DecimalField               | max_digits=6, decimal_places=2, null=False, default=0        |
| Order Total              | order_total     | DecimalField               | max_digits=10, decimal_places=2, null=False, default=0       |
| Grand Total              | grand_total     | DecimalField               | max_digits=10, decimal_places=2, null=False, default=0       |
| Original Bag             | original_bag    | TextField                  | null=False, blank=False, default=''                          |
| Stripe Payment Intent ID | stripe_pid      | CharField                  | max_length=254, null=False, blank=False, default=''          |


### Order Line Item Model
| Name            | Database Key   | Field Type          | Validation                                                                   |
| --------------- | -------------- | --------------------| -----------------------------------------------------------------------------|
| Order           | order          | ForeignKey(Order)   | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'  |
| Product         | product        | ForeignKey(Product) | null=False, blank=False, on_delete=models.CASCADE                            |
| Quantity        | quantity       | IntegerField        | null=False, blank=False, default=0                                           |
| Line Item Total | lineitem_total | DecimalField        | max_digits=6, decimal_places=2, null=False, blank=False, editable=False      |

[Back to Highlights ](#highlights)

# Features

## Existing Features

  Every page of the website features a consistently responsive and intuitive layout and navigational system:
 
 ### General features

  *  All the webpages are fully responsive on all devices.

  *  Footer will seen on  most of all the important pages it contains Company name and social links as well.

  *  All the  cards images and text are fully responsive.

  *  Search functionality which will help to find products by name and category.

 ### Header
   
  * The header will be in a fixed position at the top of the screen and will not scroll with the page contents. This allows visitors easy access to navigate the site via the menu.

  * The header will include a company name under the name all the nav-links some of them are dropdown menu and on right side on top one search bar which will help user to find products faast on just one click, under the search bar I have placed user account menu and cart.

  * The navigation links in the My Account dropdown will change when the user is registered and logged in.

  * On mobile menu all the links has shifted in side bar push menu, header just contain company name,on left side mobile menu button and right side cart.

 ### Home page 

  * Home page contains some beautiful images will attract user.

  * On Home page under the hero image I have placed Flickity carousel which contains new arrival products with nice Auto-play.
    Auto-playing will pause when mouse is hovered over, and resume when mouse is hovered off. Auto-playing will stop when the carousel is clicked or a cell is selected.

  * Under the  carousel there is two product image one is belongs to men's products and other one to women's products.. both images navigate user to particular product but the buttons lead user to men's all product and women's  all products.  

  * At the bottom of page Strategically placed christmas sale timer which will attract more users.

 ### Product Page

  * The Product page will display a list of all the products available on the site or the products from a particular category. This could be men's, women's, bag and sale  products.

  * The page will clearly display the product image, product name, product category and price of the product.

  * Clicking on the product image will open up a new page containing more details on the selected product.

  * If the user is super user/ author! there is some addition links on each item allow the  super user to edit/delete the product.


 ### Product Detail

  * This will display all data associated with a particular product. There will be button to allow the user to add the product to their shopping basket.

  * If the user is super user/author! there is some addition links on each item allow the  super user to edit/delete the product.

  * There is product review section where loged in user can add their product review.

  * At the bottom of the page there is product related section where user is able to see some extra products which will be related to users choosen product.

 ### Shopping Bag Page

  * The shopping bag will display all items that that have been added by the user.
  
  * For each item it will show the unit price, quantity and subtotal.

  * The user can change the quantity against each item and also remove it from their back if they no longer wish to purchase the product.

  * At the bottom of the page the basket total, delivery cost and order total will be displayed.

  * A Keep Shopping & Checkout button will also be displayed at the bottom of the page.

  [Back to Highlights ](#highlights)

 ### Checkout Page

  * The Checkout page will contain a brief summary of the order and a form for the delivery details.

  * If the user is logged in then the form will be automatically fill with any address information the user has saved in their profile.

  * The payment information system will be implemented by Stripe and it will allow the user to enter a card number, expiry date and CVC number.

  * Buttons at the bottom of the page will allow the user to complete the order or adjust the order.

 ### Profile Page

  * Once a user is registered they will have access to their profile page. 
  
  * This allows the user to enter default delivery information and  view previous orders.

## Features left  which I want to implement in future:-

  * To add the wish list functionality, so user can add products in their wish list, and Items from the wish list can delete or add to the users shopping cart. 

  * User can Log in account with social media instead typing manually user name and password.

  * Email Newsletter Subscription by using Django and AJAX.

  * Contact form.

# Technology used in a Project 

 ## Frameworks, Libraries & Programs

  ### Languages

  * This website uses HTML, CSS, JavaScript & Python programming languages.

  ### Libraries & Frameworks

   * [Font Awesome](https://fontawesome.com/): provided all icons (social media icons etc.) used throughout the site.
   * [Google Fonts](https://fonts.google.com/): provided the Roboto , Playfair Display SC and Seriffont that is used throughout this website.
   * [Bootstrap](https://getbootstrap.com/): a frontend framework for implementing responsive websites.
   * [jQuery](https://jquery.com/): JavaScript library.
   * [Django](https://www.djangoproject.com/): A Python based framework for developing secure and maintainable websites - the core of this project.
   * [Amazon Web Services (AWS)](https://aws.amazon.com/): was used to host all static and media files using the [S3](https://aws.amazon.com/s3/) and [IAM](https://aws.amazon.com/iam/) services.
   * [Stripe](https://stripe.com/gb): an API framework for processing secure payments.

  ### Database

   * [Postgres](https://www.postgresql.org/) - Relational database, hosted and deployed via Heroku.

   ### Tools

  * [Balsamiq](https://balsamiq.com/): was used to made the initial wireframe models of the website.
  * [DB Diagram](https://dbdiagram.io/home) : was used to made the database structure and relationships.
  * [GitPod](https://gitpod.io/): was use as the development environment.
  * [GitHub](https://github.com/): was used to manage the configuration and control of the project.
  * [Heroku](https://heroku.com): was used to deploy the project
  * [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/): Chrome tools used during the project development to debug problems and to test the website.
  * [Favicon](https://favicon.io/): was used to generate the favicon for the website.
  * [Flickity](https://flickity.metafizzy.co/): was used to made the Home page new arrival products slider.

    [Back to Highlights ](#highlights)

  
# Testing


# Deployment

## Version control

The project was deployed on GitHub Pages. I used Gitpod as a work space where I commited all changes to git version control system. 
I used push command in Gitpod to save changes into GitHub.


### To run localy

   * Log in to GitHub and click on repository to download ([Milestone Project 4](https://github.com/jas-sin82/d-y-collection-milestone-4.git)).
   
   * Select `Code` and click Download the ZIP file.
   
   * After download you can extract the file and use in your local environment.
   
   * Second option is you can [Clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/ cloning-a-repository)
     or [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repository ([Milestone Project 4](https://github.com/jas-sin82/d-y-collection-milestone-4.git) into your github account.
 
### Deploying to Heroku from Gitpod

  1. Open [Heroku](https://heroku.com) in the browser and login or create a new account if required.

  2. On the Heroku Dashboard click New->Create New App.

  3. Give the app a new name and choose a region closest to you. Click the Create App button.

  4. On the resource tab provision a new Postgres database selecting the free Hobby Dev plan.

  5. To use Postgres in the application two packages are required - these are dj-database-url and psycopg2. To install these in Gitpod type the following commands:
    
     * `pip3 install dj_database_url`
     * `pip3 install psycopg2-binary`

  6.  Freeze the requirements in Gitpod by typing `pip3 freeze > requirements.txt`. Heroku will use the requirements.txt file to install these packages during  deployment.

  7.  Open the settings.py file and import the dj_database_url package by adding `import dj_database_url` at the top of the file.

  8. In the database section comment out the default configuration and replace with the code below. The DATABASE_URL can be found under the settings tab in Heroku in the Config Vars section.

     
   ```
    DATABASES = {
        'default': dj_database_url.parse('DATABASE_URL')
    }
   
   ```

   9. As a new database has been connected the migrations will need to run again to setup the database. Type in the following commands in Gitpod to run the migrations.
    
      * `python3 manage.py makemigrations`
      * `python3 manage.py migrate`

  [Back to Highlights ](#highlights)

  10. The database can be populated using the fixtures and JSON files. Run the following commands to load the data into the Postgres database:
    
      * `python3 manage.py loaddata Categories `
      * `python3 manage.py loaddata  Brands `
      * `python3 manage.py loaddata products`

  11. Create a superuser account for Django Administrator Panel using command    

        `python3 manage.py createsuperuser`.

  12. For the app to run the Gunicorn webserver package is required. To install this package run command 
  
        `pip3 install gunicorn`.

  13. Freeze the requirements by running command 
  
        `pip3 freeze > requirements.txt`.

  14. In the root directory of the project create a Procfile by running command `touch Procfile`.

  15. Open the Procfile copy  web: `gunicorn david_yenny_collection.wsgi:application`.      

  16. Login to Heroku using the `heroku login -i` command.

  17. Enter the following command to set DISABLE_COLLECTSTATIC:

        `heroku config:set DISABLE_COLLECTSTATIC=1 --app app-name`

  18. In the settings.py file add the Heroku app the list of allowed hosts. Also add in localhost to ensure the app still works in Gitpod.
      
      `ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']`

  19. Commit & push to GitHub.

  20. Initialise the Heroku repository using command: 
    
       `heroku git:remote -a app-name`.

  21. In Heroku on the Deploy tab select GitHub as Deployment method.

  22. Search for respository and click Connect.

  23. Click Enable Automatic Deploys.

  24. Create a new Django secret key using the [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) website.

  25. In Heroku under the Settings tab create a new Config Var with a key name of SECRET_KEY with the value set to the key generated in the previous step.

  26. To ensure the Heroku app picks up this key add the following to the settings.py file:

      `SECRET_KEY = os.environ.get('SECRET_KEY', '')`

  27. Commit the changes to Github. Heroku should pickup the changes from Github and deploy the site to app-name.herokuapp.com.
   
  [Back to Highlights ](#highlights)

  ### AWS S3 Configuration

  The AWS S3 service will be used to host all static files and images.

  1. Open [AWS](https://aws.amazon.com) in the browser and login creating a new account if required.

  2. Open the AWS Management Console and search for the S3 service.

  3. Click 'Create New Bucket' to create a new bucket.

  4. Select the region closet to you.

  5. Make sure Bucket will be publically access and then Click 'Create bucket'.

  6. Select your bucket from the bucket list. In the properties tab turn on static website hosting and set the following default values then click save.
    
      * Index document: `index.html`
      * Error document: `error.html`

7. In the Permissions tab paste in the following CORS configuration then click save.

```
    [
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
    ]
```

8. In the Permissions tab go to the Bucket policy section and click the Edit button. Click the Policy Generator button to create a new security policy.

* Policy Type: S3 Bucket Policy
    * Principal: *
    * Actions: GetObject
    * ARN: Copy the ARN from the Bucket Policy tab and paste here.
    * Click Add Statement then Generate Policy.
    * Copy the new policy and paste into the Bucket Policy editor.
    * To allow access to all resources add a "/*" onto the end of the Resource key value.
    * Save the new policy.

9. In the Permissions tab go to the Access Control section and click the Edit button. On the "Everyone (public access)" line check the List checkbox and click Save changes.

10. Go back to the services and select IAM (Identity and Access Management) to add a new user. IAM will be used to create new group, create an access policy giving the group access to the S3 bucket and to assign a user to the group so they can use the policy to access the files in the S3 bucket.

11. Under User Groups click the Create Group button. Enter a group name then scroll to the bottom and click Create group.

12. Under Policies click the Create Policy button.

    * Go to the JSON tab and select Import managed policy.
    * Search for the `AmazonS3FullAccess` policy and Import this.
    * From the S3 Bucket Policy page copy the ARN and paste this twice into 
    the Resource key.
    ```
        "Resource": [
            "arn:aws:s3:::s3-bucket-name",
            "arn:aws:s3:::s3--bucket-name/*"
        ]
    ```
[Back to Highlights ](#highlights)

13. Click the Review Policy button giving the policy a name and description. Click the Create Policy button to save all changes.

14. Under User Groups select the group that was created above. On the Permissions tab select Attach Policies from the Add permissions dropdown menu. Search for the policy that was created above, select it and click the Add permissions button.

15. Under Users click the Add Users button and give the user a name. Check the Access Key - Programmatic access option and click next. On the next page add the user to the new group that was created above. Click through to the end then click Create User.

16. Download the CSV file this contains the user access key and secret access key which will be used by the Django app for authentication.

17. To connect Django to the new S3 Bucket two new packages are required: boto3 and django-storages.

    * `pip3 install boto3`
    * `pip3 install django-storages`

18. Freeze the requirements:
 
    `pip3 freeze > requirements.txt`.

19. In the settings.py file add 'storages' to the INSTALLED_APPS list.

20. Add the following configuration to the settings.py file. As the S3 Bucket is only required when using Heroku an if statement is used to check if the variable USE_AWS exists. 
```
    if 'USE_AWS' in os.environ:
        # Bucket Config
        AWS_STORAGE_BUCKET_NAME = 'bucket-name'
        AWS_S3_REGION_NAME = 'eu-west-2'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
```

 21. In Heroku at the following Config Vars to the app. The AWS keys can be found in the csv file that was downloaded when creating the S3 user. The DISABLE_COLLECTSTATIC can also be removed as Heroku will get the static files from AWS for any future deploys.
    * `AWS_ACCESS_KEY_ID : From the csv file`
    * `AWS_SECRET_ACCESS_KEY : From the csv file`
    * `USE_AWS : True`
    * Remove variable `DISABLE_COLLECTSTATIC`

22. In the settings.py file add the following inside the USE_AWS if statement to tell Django where the static files will be sourced from in production.
    
    * `AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'`

23. The next step is to configure Django to use S3 to store our static files whenever someone runs `collectstatic` and to also store any uploaded images in the S3 bucket.

24. In the root folder create a file by running: 

      `touch custom_storages.py`.

25. Copy the following configuration into the file and save:

```
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage
    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION
    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
``` 

26. In the settings.py file add the following inside the USE_AWS if statement to configure Django to use our custom storage class for static file storage and to override the static and media URLs in production.

```
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
[Back to Highlights ](#highlights)

27. In the settings.py add the following lines to the top of the USE_AWS if statement. These will configure the browser to cache static files for a long time as they don't change often.

```
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

```

28. At this point all the changes can be committed to Github triggering Heroku to deploy the app. Confirm all the static files have been uploaded to the S3 bucket.

29. To add the media files to the S3 bucket go to AWS S3, select the bucket and click on Create folder. Create a folder called media.

30. Inside the media folder click Upload to upload all the media files to the S3 bucket. Grant public-read access.
     

# Credits

* Code Institute tutor support.

* Students on Slack for a helping hand when I've got stuck.

* My mentor gbenga_mentor for helpfull feedback througout the project.

## Hints & Ideas

  * https://www.python.org/

  * https://stackoverflow.com/

  * W3Schools https://www.w3schools.com

  * Code Artisan Lab https://www.youtube.com/hashtag/codeartisanlab

  * Image used as product was sourced from [Zalando](https://www.zalando.se/man-home/). 

  * Bootstrap 5.1 was used throughout the site so that it is responsive to different devices and viewport sizes.[Bootstrap5.1](https://getbootstrap.com/docs/5.1/getting-started/introduction/)

  * Django documentation [Django](https://docs.djangoproject.com/en/3.2/)

  ## To finish this project I have used [Code Institute gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template) 
