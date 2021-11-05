#  Project Testing

   * [ Functionality Test ](#functionality-test)
        
   * [ Compatibility testing ](#Compatibility-testing) 

   * [Code Validation Test](#Code-validation-test)
 
   * [User Stories Testing](#user-stories-testing)

   * [Error found during site development ](#Error-found-during-site-development)
       
   * [ Performance Testing ](#performance-testing)

## Functionality Testing

   * I used Chrome developer tools throughout the project for testing and solving problems with responsiveness and 
     style issues.

   * Main navigation Menu, all the drop-down menus, links and search bar work correctly.

   * Mobile menu links and dropdown functionality work correctly.

   * All the buttons throughout the  website link correctly and works great, back to top button works.

   * Home page Flickity carousel works good on all the devices.

   * All products are displayed correctly at different screen sizes.

   * Sort for price and name orders items work correctly.

   * Product cards link through to the product detail page for the product shown.

   * Carousel at product detail page works correctly.
   

## Compatibility Testing 

  * The website has been tested across a broad range of physical and virtual desktop, tablet and mobile devices. Additionally, the site has been checked on a browsers including Chrome, Edge.

  * Project has been tested on different Physical  devices such as Desktop PC , Ipad and on diffrent Mobiles Iphone x, Samsung Note 20 ,iphone 7 it works 
    great and its fully responsive.

    <img src="readme-doc/desktop-test.jpg">

    <img src="readme-doc/iphon-11-pro.jpg">

    <img src="readme-doc/s-note-20.jpg">
 
   [Back to Highlights ](#highlights)

  * Virtual devices have consisted of the following on Google Chrome:

    <img src="readme-doc/testing-device.png">

## Code Validation Test

 PEP8 online, JSHint, W3C Markup Validation Service and CSS Validation Service were used to validate all project pages ensuring no syntax errors are present.

 ### HTML

  * To make it easier to validate html code, since using Django throughout all pages, which results in errors in online validators.

  * There was no error on html pages but there was warning caused on some of the webpages because of  missing div , section , <h> and <p> tags.

 ### CSS Validation

 <img src="readme-doc/css-validation.png">

 ## User Stories Testing

 ### First Time Visitor Goals 
 
  #### Quickly understand what the site is about

   * When visitor enters website, the visitors is welcomed by a some stunning product images and  carousel which contains new arrival product images  another thing a really clean and white bg header with drop down menu that clealy explains the purpose of the site,A customer should be left in no doubt what the site is selling.

   
  #### Browse Products

  * On Home page under the hero image provide carousel which contains new arrival product images which moves right to left, Auto-playing will pause when mouse is hovered over, and resume when mouse is hovered off. Auto-playing will stop when the carousel is clicked or a cell is selected. One click will bring user to that particular product detail. 
    
    <img src="readme-doc/user-testing-2.png">


  * Under the home page Carousel there is two diffrent section one is men's fashion and other one is women's fashion on click which will lead user to that particular 
  product category. There is one buttton on each image which will lead user to that particular gender category.

     <img src="readme-doc/user-testing-3.png">

  * In the navbar there are links to All Products and drop-down menus for Men , Women and Bag. There is other links on the navbar for sale Products and User account.

    <img src="readme-doc/user-testing-1.png">

  * Navigation bar provides one serach bar which will help user to save time to find fast any particular product or category on just one click.
 
      <img src="readme-doc/user-testing-7.png">

  * There is a ‘Sort by’ option on all the products pages from which the customer can order by price and name from high to low or low to high.
     
      <img src="readme-doc/user-testing-6.png">

  * There is one button on Hero image of Home page for Shop Now which  will take the customer to the All products page.

   <img src="readme-doc/user-testing-1.png">

 * There is brands section each brand leads user to that particular brands products.

   <img src="readme-doc/user-testing-4.png">


  * At the bottom of the home page I have placed one  christmas count down which will make user to stay connect with website.

    <img src="readme-doc/user-testing-5.png">
 
 [Back to Highlights ](#highlights)

#### Sale Products

 * There is a link to sale products on the navbar.

 * The products on sale have a red badge in the top left of the product card labelled ‘Sale’ and product discount percent have green color, its on right top of card. This should be clearly visible to customers in the product.

   <img src="readme-doc/user-testing-8.png">


#### Related Products 

   * In the product detail page related products are shown below the product Review.

   * Related products are from the same product category and same gender.

   <img src="readme-doc/user-testing-9.png">

#### Purchase a product without register/login

  * products can be purchased without registering. 

  * Registration/login is required to save personal details and to see purchase history as well as leave a review.


#### Register 

 * The customer signs up with email address, username and password, User account link top right under the serach bar and in mobile menu at bottom of the drop-down menus.

    <img src="readme-doc/user-testing-10.png">

 * A verification email is sent with a link to confirm this is correct.

 *  The link returns the customer to the David & yenny collection site where they are required to click the Confirm button to complete the registration process.

#### Receive messages 

 * The customer receives success, informational or error messages to confirm actions throughout the site.

     <img src="readme-doc/user-testing-12.png">
 
 [Back to Highlights ](#highlights)

#### Recover Password 

 * There is a ‘Forgot Password?’ link on the login screen.

   <img src="readme-doc/user-testing-11.png">

 * The user is required to re-enter their email address and click Reset My Password.

 * A confirmation message is displayed and email sent. 

 * The user has to click the link in the email to create a new password. 

#### Account Security 

  * User accounts are protected by Django Allauth.

  * Payments are secured by Stripe and webhooks to ensure the process completes.

### Returning Visitor 

 #### Save my contact details 

 * At checkout there is a checkbox to ‘Save delivery address to my profile’ for authorised users.

#### See previous orders 

 * Order history is available in the Profile page.

#### Add a review 

 * The Add Review form is displayed in the Reviews section if the user is authenticated.

 * User has authorization to add review but can't edit or delete them just super user can delete any unsatisfactory reviews.

#### Log in and out 

  * As a returning visitor, I want to be able to easily log in, if I already registered last time visiting. Visitor can click on my account drop-down menu on right top to login.

 [Back to Highlights ](#highlights)


### Author of website 

#### Ensure website is secure and safe

  * Django @login_required decorators added to maintain authenticated access only to secure site areas.

  * Allow superuser access only to admin area.

#### CRUD for Products and Reviews

 * A superuser/Author has access to Product Management to add new products.

 * Existing products can be update or delete using the links under the products cards on the product a page or on the product detail page. 

 * Items can be added to the sale via the check box on the Edit Product page.

 * A discount percent can be set as desired.

 * Author/superuser has permissions to delete any review. This is done using the Delete button on each review.

## Error found during site development

The developer face several issues during the development of the site ,Some of the issues below I got During my site development :-

* I got syntax error! forgot to load endif tag which cause syntax error at product detail page.

  <img src="readme-doc/testing-error-1.png">

* I had very much tuff time while I was working on stripe! first I got authenticationError at checkout page, asking me all the time I did not provide API keys , actually I had provided all the keys.. PUBLIC KEY A and SECRET KEY
 In a terminal first I used a command:  
      Set STRIPE_PUBLIC_KEY= key 
      set STRIPE_SECRET_KEY=key
  even I have save them in my Configure environment variables in gitpod , still giving back error. Then I took  tutor support help to resolve this error, after talk to tutor support I got replace keys scope in environment variables I saved the keys to direct to my current repo `jas-sin82/d-y-collection-milestone-4` instead 
  to github username `jas-sin82.`

   <img src="readme-doc/testing-error-4.png">

*  I got syntax error! forgot to load endfor tag which cause syntax error at product sale page.
   

    <img src="readme-doc/testing-error-2.png">
 
*  I got syntax error! forgot to load endif tag which cause syntax error at bag.html page.
   

    <img src="readme-doc/testing-error-3.png">


 ## Performance Testing

 <img src="readme-doc/light-house-testing-1.png">

 <img src="readme-doc/light-house-testing-2.png">

 <img src="readme-doc/light-house-testing-3.png">

 <img src="readme-doc/light-house-testing-4.png">


  
