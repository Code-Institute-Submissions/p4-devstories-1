<h1 align="center">Devstories</h1>

[View the live project here.](https://app-devstories.herokuapp.com/)

Devstories is a blog site for devevelopers to share their knowladge and projects that they are working describing how they made them but not going into too much detail but just a brief explination of their project. Its also a place were friends of developers can visit and see what their next project is that they are working on etc.

For this project I wanted to make a blog site for developers where developers can sign up and make a blog about their own projects or anything related to tech my target audience is mainly developers or friends who are developers or looking for inspiration about new tech news or keeping in touch with developer friends and their progress.

![chrome_8m7zbaA5kC](https://user-images.githubusercontent.com/43074374/212039145-93d7763d-2349-4f4f-a7df-1c060cb806be.png)

## User Experience

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, You will be able to navigate the site with minimal effort and ease.
        2. As a First Time Visitor, You will be able to view a list of current blog posts posted.
        3. As a First Time Visitor, You will be able to sign up and and login.
        4. As a First Time Visitor, You will be able to sign for the newsletter.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, You will be to check to see if there are any new blog posts.
        1. As a Returning Visitor, You will be able to see if anyone has commented or liked your post.

    -   #### Frequent User Goals
        1. As a Frequent User, You will be to upload a new blog post.
        2. As a Frequent User, You will be to edit your pervious blog posts.
        3. As a Frequent User, You will be to delete your blog posts.
    
    - ### Admin user stories
        1. As a supersuer you will be able to see a list of users who registered on the site
        2. As a supersuer you will be able to remove any users registered on the site
        3. As a supersuer you will be able to manage content such as blogs that users post
        4. As a supersuer you will be able to see who signs up for the newletter
        5. As a supersuer you will be able to manage people comments users post

-   ## Target Audience
    - The target audience for the website was for developers who like to blog about or talk about their projects

-   ## Technical design
    - ### Agile design
    - An Agile approach to creating this app has been applied. Githubs projects was used to track user stories and implement ideas based on their level of importance for allowing use of the app with no loss of functionality or user experience.

    - By taking using AGILE methodology in this project i was able to deliver a site which had all required functionality. Due to the time limit on this project i was not able to incorporate all intial listed features, but this is where an AGILE approach is great for app design. The project displays this by having User stories in the Done section and the ones which decided to be left for future put in the future implementation.

    - ### Crud Functionality
    - Devstories handles data with full CRUD Functionality:
    - Create - Users can create, account, profile, post a blog
    - Read - Users can view the posts of other users and their own.
    - Update - Users can update their blog posts with new context
    - Delete - Users can delete their own blog posts 


-   ### Colours
     -   The three main colours used are white, and gray / black.
    
-   #### Typography
        -   The Lato, sans-serif is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Lato, sans-serif is a clean font used frequently in programming, so it is both attractive and appropriate.

-   #### Imagery
        -   Imagery is important. The images are set up form the users when they create a blog on the site they can choose to add an image to make their blog stand out more.

# Structure

*   ### Database
    - The site uses a backend database built with the Django framework and the use of ElephantSQL Postgres for the deployed site.

*   ### Web pages
    - User experience was one of the main driving factors in this project. A simple, clear and easy to navigate app was the desired outcome. 

    - Home Page: The home page conists of a navigation bar with the name of the site and site links it will also show you the hero image for the site which is a picture I got from unsplash

    - New Post page: The new post page is basically the users profile page with a blog post form which the user can fill out to post a blog to the home page and ther is also a upate email for the news letter

    - Register Page: The Register page consists of a sign up form for the user to create a user name and a password for their account
    
    - Login Page: The Login page consists of a similar form like the register page but this for after the user has created their account
  
* ### Github - User Project Kanban Board
    - During development I used the project kanban board in github for keeping track of the progress during development for the site.

* ### ERD - Entity Relation Diagram schema
    - (Database Schema Image) Before I started to code this project I created a Diagram Entity Relationship - Database Schema using dbdiagram. I created this to easier understand the database models that I was going to create for this project.

    ![brave_CmCzB2JWsj](https://user-images.githubusercontent.com/43074374/212040156-a850818f-7bef-4e64-b30d-9609f3e8c2e4.png)

* # Wireframes

    ## Home Page
    ![brave_jcHe22KHLj](https://user-images.githubusercontent.com/43074374/211255744-f8c4ebb7-e51f-433e-af3f-04058ba0f00d.png)

    ## Blog detail page

    ![brave_NQ0fJRyE7X](https://user-images.githubusercontent.com/43074374/211285283-07ffe0a2-0214-45b2-8242-af1c844b7cfa.png)

    ## Create A blog post page

    ![brave_gIDkLiR1iU](https://user-images.githubusercontent.com/43074374/212045355-6b4e60b2-9011-48d7-901a-8ff14c3dadae.png)

    ## Mobile view

    ![brave_sB6i2mnM8f](https://user-images.githubusercontent.com/43074374/212040561-a67da01b-91f3-4201-ab12-1e67bb562197.png)

### Frameworks, Tech Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
3. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
4. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
5. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
6. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
7. [Unsplash:](https://unsplash.com/)
    - Unsplash was used for some of the pictures on the blog site by typing in tech in to the search bar.
8. [pixabay:](https://pixabay.com/)
    - pixabay was used for some of the pictures for testing posting a blog on the site
9. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.
10. [Cloudinary:](https://cloudinary.com/)
    - Cloudinary was used to store the images that go on the website

## Features 

- I aimed to achive a nice easy to navigate site with minimal effort
- I aimed the site to be driven more towards developers who wish to blog and talk about their projects
- I aimed to bring in more people and people who are new to tech and want to learn more.

In this section, I will go over each of the sections on the website such as the Navigation Bar, Main Page, Blog page, Footer section, admin 

### Existing Features

- __Navigation Bar__

  - Featured on all three pages, the full responsive navigation bar includes links to the Logo, Home page, Gallery and Sign Up page and is identical in each page to allow for easy navigation. There is a a section for the hero image on the home page 
  - This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button.

  ![chrome_hbhay1ERXT](https://user-images.githubusercontent.com/43074374/212045508-9e686763-c063-4b73-8f86-c53bdfdb9955.png)

  - This is if a user is logged in 

  ![chrome_I8fiFhBl7S](https://user-images.githubusercontent.com/43074374/212045695-2c132a74-eb4a-4ac1-b3b5-fd901bf7f706.png)


- __The Main Page Content__

  - This is the main pages content where it displayes the hero image and all the blogs desplayed on the website.

![chrome_HIjXE26s0Z](https://user-images.githubusercontent.com/43074374/212045769-b95f4429-1a25-4a21-b635-dd7b9bb82c68.png)

- __Blog Page__

  - The blog page Is the New post page this is only accessible after a user has logged in as you can see in the navigation bar the login and register links change to new post and log out.

  ![chrome_vbxvXGM19l](https://user-images.githubusercontent.com/43074374/212045884-75e6d15c-a76f-4e38-8051-853284b70a82.png)


- __Detailed Blog Page__

  - The Detailed blog page is where vistors who arent signed up can read more about a blog but if a user is signed up only that user who created the blog will have the option of updating or deleting the post. Also once the user logged in they will have the option for 
 
  - The view for when a visitor wants to see the detailed version and options to edit or delete their post if logged in whe a user is not logged in this wont be displayed

  ![chrome_ltVjyy40uW](https://user-images.githubusercontent.com/43074374/212045974-ada99b14-939b-4cf0-b222-032e2177ef2d.png)


  - This is what it looks like for the user when they want to post a comment on a post once they are logged in.

  
  ![chrome_YXOIcSYhmN](https://user-images.githubusercontent.com/43074374/212046177-7fd17b7e-4e76-4248-a727-4f7fef3ca175.png)


- __Blog Features__

  - This feature is for when a user likes a blog post the counter increments by one for every like

  ![chrome_G8BmnQ8JQ8](https://user-images.githubusercontent.com/43074374/212046315-a7a1cd09-59ad-4ba5-b5a7-a03593cfd562.png)

- __The Footer__ 

  - The footer of the website just consists of the name and some text and the copyright symbol.

  ![chrome_E7b4bClEQD](https://user-images.githubusercontent.com/43074374/212046427-9635a569-0d56-42a1-a4d8-05a84b8a8668.png)

- __The Sign Up Page__

  - The Sign up page consists of the navigation and hero image and a form which will allow you to create an account on the website

  ![chrome_RpXtNPJKC8](https://user-images.githubusercontent.com/43074374/212046501-9f398472-38c8-4007-af11-7ce9c363812a.png)

- __The login Page__

  - The Sign in or login page consists of the navigation and hero image and a form you can fill out to login to your account

  ![chrome_HdUDtPKnQm](https://user-images.githubusercontent.com/43074374/212046613-f0240645-5fdb-48ae-bd0b-2d6afb2c7cd9.png)

- __The Newsletter Section__

  - The newsletter section is where users can register their email they use to get notified for any changes or posts being added to the site

  ![chrome_fTwsDRzJqx](https://user-images.githubusercontent.com/43074374/212047112-49ccf8dc-4132-4890-850c-3fef64807a55.png)

## Testing 

### Browser Testing 

- Browsers test on
    - Chrome : Tested it on chrome everything seemed to be working fine 
    - Firefox : Tested it on firefox everything seemed to be working fine 
    - Brave : Test it on Brave everything seemed to be working fine


### Validator Testing 

- HTML
  - I ran the site through the html validator

- CSS
  - I ran the site through the css validator  

### Further Testing
-   There seemd to be some issues with the mobile responsivenes
-   There was also some issues regarding the navigtion bar not being responsive needs fixing
-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## Unfixed Bugs

Some bugs have come up during development one is the comments and sending out newsletter email

### Bug One Comments
Comments seem to duplicate when you refresh after posting a comment

![chrome_tLgtdwGjeF](https://user-images.githubusercontent.com/43074374/212047409-1a557f9e-ca89-40ac-b71b-af6f12794d26.png)

### Bug Two Newsletter emails
I have implemented the custom logic for a user to add their email to the newsletter its just sending out emails for notifications is slighty broken at the url /newsletter/send seems to be loading for a while then gets suck on a 502 error while trying to use send grid I tried using mail gun before but I ran into some issues with their support because I made a mistake in the settings on another project which made them lock my account making it unsuable for this project.

## Deployment

### GitHub

The projects code was stored on github

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/owenbcoding/p4-devstories)


### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/owenbcoding/p4-devstories)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/owenbcoding/p4-devstories)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/owenbcoding/p4-devstories
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/owenbcoding/p4-devstories
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Heroku And Elephant SQL

### For hosting 
  - Start by creating your database on elephantSQL then make sure its set up correctly with the proper settings
  
    ![brave_ENEKcAzdhN](https://user-images.githubusercontent.com/43074374/211292027-be8ad86a-69bf-47aa-9a09-604ebea31edb.png)


  - Next go to heroku and make and connect your github repo to the app you made in heroku 
    
    ![brave_zIhDJlSFfG](https://user-images.githubusercontent.com/43074374/211292159-d6bbb5cc-4c6f-4c6d-8feb-24d5c1496227.png)


### Content 

- The Hero image for the home page was take from unplash by searching tech in the search bar
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used are from these two free image sites Unplash and Pixabay

## Credits 

- Credit to
 - Code institute for project and read me template 
 - Unsplash for free nice images for blog posts https://unsplash.com/s/photos/study
 - Pixabay for free images for blog posts https://pixabay.com/images/search/tech/?manual_search=1

