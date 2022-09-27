<h1 align=center>Real Estate Project</h1>


<br>
<img src="/Amiresponsive.png">

<br>


#
[Here is a link to the final project](https://real-estate-project-yc.herokuapp.com/)
#

## User Experience

### User Stories

1. As a user, I would like to be able to:


2. As a logged in user, I would like to be able to:


#
### 1. Strategy

  + **Project Goal**


### 2. Scope

 * A simple, straightforward, intuitive UX experience
 * An explicit content
 * An easy navigation for the user through all of the features
 * A site that is visually appealing on most devices



### 3. Structure

* A clear and straightforward layout is in place to ensure users can navigate intuitively and have a leisurely experience
* Navbar is fixed on top to facilitate users to navigate through pages easily
* A Small dropdown menu navigation is the same on all pages at small screen sizes to ensure easy navigation


### 4. Skeleton

* Wireframes were created with Balsamiq. <br>
* The project was developed from initial wireframes, and some modifications were made during the development process in response to user feedback


<details>
<summary>Click to see wireframes:</summary>
<br>

[HomePage]() <br>
[Page]() <br>
[Page]() <br>
[Page]() <br>
[HomePage mobile]() <br>
[mobile]() <br>
[mobile]() <br>
[mobile]() <br>


</details>

### 5. Surface

* Colours

- The colour scheme was chosen based on the background image I wanted to use sitewide:
I used [Coolors](https://coolors.co/) to generate a colour palette based on the image.
<details>
<summary>Click to see Colours:</summary>
<br>

![Main colours]()<br>

</details>


**Font Selection**
 
Two fonts were chosen with [Google Fonts](https://fonts.google.com/) to be used across the entire site.

The chosen fonts were ... , ... as back up fonts for lists, forms, buttons and paragraphs.
#
## Existing Features

### **Navbar**

+ Fixed Navbar to allow the user easy access to all pages

1. 

<img width="700" src="">

2. 

<img width="700" src="">

3. 

<img width="700" src="">

4. 

<img width="700" src="">

### **Home page**

<img width="700" src="">


### **About page** 

<img width="700" src="">


### **Featured Listings page**

<img width="700"  src="">

#
## Future Features

I would like to...

#
## Languages Used


## Frameworks, Libraries & Programs Used

+ Balsamiq: Balsamiq was used to create the wireframes during the design process
+ Favicon Generator: Used to create favicon used on the website
+ Git: Gitpod IDE was used for version control by utilizing the Gitpod terminal to commit and Push to GitHub
+ GitHub: GitHub respository is used to store the project's code after being pushed from Gitpod
+ Google Fonts: Google fonts are used to add fonts for aesthetic and UX purposes
+ Django: Framework used to add structure to the platform
+ Bootstrap4: Framework used to add structure and responsiveness
+ AmIResponsive: Used to generate mockup image

## Testing and Code Validation


## Deployment


<details>
<summary>Heroku Deployment Steps: </summary>

 1. Ensure all dependencies are listed within the requirements.txt file

 Within the terminal in Gitpod type `pip3 --local freeze > requirements.txt`, and a list with all requirements will be created to be read by Heroku.

 2. Setting up Heroku
  * NB Due to security issues connecting github directly to heroku (at the time this project was deployed),
    first you must log into your heroku account via the terminal in gitpod (more info on this further down).
      
    2.1 Next, navigate to the [Heroku](https://www.heroku.com/) website

    2.2 Login to Heroku
    
    <img width="300" src="static/assets/img/readme_img/heroku/herokulogin.png">

    2.3 Click on `New` (top right) and Create a new app
    
    <img width="300" src="static/assets/img/readme_img/heroku/herokunewapp.png">
    
    2.4 Choose a project name and set your location
    
    <img width="400" src="static/assets/img/readme_img/heroku/herokucreateapp.png">

    2.5. Navigate to the `Resources` tab

    <img width="700" src="static/assets/img/readme_img/heroku/herokuresourcestab.png">

    2.6. In the `Add ons` section, search for Heroku Postgres and select it on the list
      - A pop up will appear, select, 'Hobby Dev' and click `Submit order form`
    
    <img width="700" src="static/assets/img/readme_img/heroku/herokupostgres.png">
    
    2.7.1. Next, You would usually navigate to the `deploy` tab;
      - Click on connect to Github
      - Search for the repository named Metal-Re-Injection
      - And connect heroku to Github.<br>
    2.7.2. But, as mentioned above this is not possible for the time being.
      - So instead, In order to connect gitpod to heroku type:
          - `$ heroku login -i`
          - Then enter your heroku credentials,
          - Now you are logged into heroku in Gitpod
          - Once all code is commited and pushed to Github, simply push code from Gitpod to heroku using the command:<br>
        <img width="500" src="static/assets/img/readme_img/heroku/pushheroku.png"><br>
          - Heroku will start the build process, this can be viewed under the `Activity` tab<br>
        <img width="400" src="static/assets/img/readme_img/heroku/herokubuild.png"><br>
          - Once the build process has completed, navigate to `Open App`
          - The app should now be ready to view
    
    2.8. Navigate to the settings tab
    
    2.9.  Click on Config Vars, and add Cloudinary, Database URL (from Heroku-Postgres) and Secret key
    <img width="700" src="static/assets/img/readme_img/heroku/configvarsheroku.png">

</details>

<details>
<summary>Forking the GitHub Repository </summary>

* By forking the GitHub Repository, you will be able to make a copy of the original repository on your own GitHub account, allowing you to view and/or make changes without affecting the original repository by using the following steps:

    - Log in to your own GitHub and locate the GitHub Repository you wish to fork
    - At the top of the Repository (not top of page), just above the "Settings" button on the menu, locate the "Fork" button.
    - You should now have a copy of the original repository in your GitHub account

* Making a Local Clone

    - Log in to your own GitHub and locate the GitHub Repository
    - Under the repository name, click "Clone or download"
    - To clone the repository using HTTPS, under "Clone with HTTPS", copy the link
    - Open Git Bash
    - Change the current working directory to the location where you want the cloned directory to be made
    - Type git clone, and then paste the URL you copied in Step 3

 $ git clone https://github.com/Yari-Carelli/Real-Estate-Project

Press Enter. Your local clone will be created

</details>


## Acknowledgements

- Code institute for the amazing Tutors on the course
- My brilliant Mentor Rohit Sharma for his patience, excellent advice on my code, pushing me back on track
    when I started to lose faith, taking time out of his own day and duties to answer all of my questions with absolute perfection, and just generally being a Python God!
- My family for their support, patience and testing
- Everybody on Slack for tips, advice, quick fixes and support
