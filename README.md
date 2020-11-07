# **Denis Lymer Milestone Project 4**
## **Code Institute - Full Stack Frameworks With Django Module**
### **Django Full-Stack Project - 'Hit Record'**
#### "Welcome to Hit Record! The one-stop shop for all your music needs - tunes, tables, tees & more..."

I wanted to apply some of my working life experience and passions into my Milestone 4 project.
Previously I have worked in a record store, been an audio engineer, a DJ and a professional musician
amongst other things. I decided to create an online store combining some of these passions.
I wanted it to sell music in various formats (vinyl, CD, digital etc..), the means to play and listen
to the music (turntables, cd players, headphones and accessories) and merchandise items like hats and tshirts
of artists and bands. I wanted it to be bright, streamlined and easy to navigate for users. And I wanted it to
be intuitive for admins with easy to use CRUD functionality behind the scenes.

I settled on calling it 'Hit Record' as it can have two meanings, both relevant to what I was trying to achieve.
a Hit Record can be a well-selling album or single by a musical artist, and Hit Record can also refer to the 
ability of hardware to record or dub audio by pressing or clicking the Record button. I felt this title neatly
encapsulated the philosophy of the project.

## **Link to the website**

https://hit-record.herokuapp.com/

## **Link to the github repository**

https://github.com/menacethedenis/CI_Milestone_4_Denis_Lymer

## **Table of Contents**
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Wire Frames**](#wire-frames)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**General**](#general)
    - [**Main page**](#main-page)
    - [**Add a beer page**](#add-a-beer-page)
    - [**Edit a beer page**](#edit-a-beer-page)
    - [**Delete an Entry**](#delete-an-entry)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Database**](#database)

4. [**Testing**](#testing)

5. [**Known Bugs**](#known-bugs)

6. [**Technologies Used**](#technologies-used)

7. [**Deployment**](#deployment)
    - [**Heroku Deployment**](#heroku-deployment)
    - [**Local Deployment**](#local-deployment)

8. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Acknowledgements**](#acknowledgements)

# **UX**

I did a lot of research before beginning to code this project. I viewed and explored many online stores 
that specialized in the products I wanted to sell on my own site. I kept note of my favourite aspects and 
elements of these sites before deciding on what direction to take my own UX and writing my User Stories.

### **User Stories**

I wrote the following user/admin stories to guide the project development:
* 1. As a user I want to be able to purchase my favourite music in various formats.
* 2. As a user I want to see new releases I may not be aware of.
* 3. As a user I want to be able to edit or delete previous entries.
* 4. As a user I want to be able to record an entry with the minimal amount of info if I am in a rush.

### **Wire frames**

I again used the Balsamiq desktop app to create my wireframes to use as reference points for the app.
I focused on mobile first design, then tablet and finally desktop layout.

<details>
<summary>Mobile - Main Page</summary>
<br>

![Mobile - Beer Tracker - Home page](https://user-images.githubusercontent.com/48594804/94488878-5a564180-01db-11eb-94fd-9d5b5e4a7aa4.png)

</details>
<details>
<summary>Mobile - Add Page</summary>
<br>

![Mobile - Beer Tracker - Add page](https://user-images.githubusercontent.com/48594804/94488874-59bdab00-01db-11eb-8bd0-642a90172eb9.png)

</details>
<details>
<summary>Mobile - Edit Page</summary>
<br>

![Mobile - Beer Tracker - Edit page](https://user-images.githubusercontent.com/48594804/94488877-59bdab00-01db-11eb-83d9-68ee1af1a8d8.png)

</details>

<br>

<details>
<summary>Tablet - Main Page</summary>
<br>

![Tablet - Beer Tracker - Home page](https://user-images.githubusercontent.com/48594804/94488884-5aeed800-01db-11eb-9702-32348686edab.png)

</details>
<details>
<summary>Tablet - Add Page</summary>
<br>

![Tablet - Beer Tracker - Add page](https://user-images.githubusercontent.com/48594804/94488881-5a564180-01db-11eb-9e30-c33564557671.png)

</details>
<details>
<summary>Tablet - Edit Page</summary>
<br>

![Tablet - Beer Tracker - Edit page](https://user-images.githubusercontent.com/48594804/94488882-5aeed800-01db-11eb-9d0b-4404d43f793e.png)

</details>

<br>

<details>
<summary>Desktop - Main Page</summary>
<br>

![Desktop - Beer Tracker - Home page](https://user-images.githubusercontent.com/48594804/94488873-59251480-01db-11eb-9d46-b1b30212b809.png)

</details>
<details>
<summary>Desktop - Add Page</summary>
<br>

![Desktop - Beer Tracker - Add page](https://user-images.githubusercontent.com/48594804/94488870-588c7e00-01db-11eb-89a4-f27da0d0c7c4.png)

</details>
<details>
<summary>Desktop - Edit Page</summary>
<br>

![Desktop - Beer Tracker - Edit page](https://user-images.githubusercontent.com/48594804/94488871-59251480-01db-11eb-8a8d-3ea517a4ab15.png)

</details>

# **Features**

## **Existing Features**

### **General**

* Feature 1: Navbar <details><p>The Logo and links to the 'add beer' and 'home pages' are visible on larger and tablet size screens. 
The links have a hover-over effect applied. They collapse into a hamburger button and switch from right to left of the screen on mobile devices. The nav pops in from the left of the screen when the hamburger is clicked.</p>
![navbar](https://user-images.githubusercontent.com/48594804/94607282-9ea51880-0293-11eb-9be0-18c8d0530999.png)
![navbar2](https://user-images.githubusercontent.com/48594804/94608379-4111cb80-0295-11eb-993e-4e7e2914f36e.PNG)
![navbar3](https://user-images.githubusercontent.com/48594804/94608380-41aa6200-0295-11eb-8f64-f8aea2f91ee6.PNG)
</details>

* Feature 2: Footer <details><p>The footer has an image of glasses containing beer which repeats to fill the screen on larger and tablet sizes. It disappears on mobile screens via CSS media queries. The image is copyright free and sourced from google images.</p>
![footer1](https://user-images.githubusercontent.com/48594804/94608885-f9d80a80-0295-11eb-9c23-c183084dc0a2.PNG)
</details> 

* Feature 3: Colour scheme / Design <details><p>To kickstart the overall design and layout of the site I used Materialize. It has very nice, professional looking layouts and colours. I picked the colours from the palette viewable on their website and chose beer themed hues like browns, yellows and oranges. i also made use of the Materialize buttons, effects and depth/shading effects</p>
![colourscheme](https://user-images.githubusercontent.com/48594804/94609319-81257e00-0296-11eb-8e4a-9192cb8599a0.PNG)
</details> 

### **Main page**

* Feature 4: Welcome card <details><p>This is a Materialize card with some depth and shading effects applied. It has a short welcome message and instructions on how to use the app.</p>
![welcome](https://user-images.githubusercontent.com/48594804/94609993-80411c00-0297-11eb-8334-b49e64ca9364.PNG)
</details> 

* Feature 5: 'Add a beer' button <details><p>This is a Materialize button with a pulse effect, tooltip and icon applied. As this button represents the core and main function of the app, I wanted it to be prominently positioned, to really stand out and to have its function easily identifiable by a user, fulfilling User Story 1.</p>
![addbutton](https://user-images.githubusercontent.com/48594804/94610761-afa45880-0298-11eb-86a5-a9c4fcacaf20.gif)

</details> 

* Feature 6: List of entries <details><p>This is a Materialize list to display each entry as they are added by a user. The list items display the 'Beer' and 'Brewed by' data fields prominently. There is a collapsible body triggered by the arrow button to reveal the rest of the data fields per entry.
These are 'Drank at' - to record the users location. 'On Date', 'Comments', 'Rating' and to acknowledge the times we are currently living in, I thought it would be a cool feature to add a 'Social Distancing Observed?' field signifying if the location the user was drinking in was practising social distancing. I opted for a switch on the 'add' and 'edit' pages which proved quite tricky to code in terms of writing and reading to the database and getting it displayed properly on the app after writing and/or editing but I think it was worth the effort.
There are also 'Edit' and 'Delete' buttons to the left of every entry fulfilling User Story 3. These along with the arrow button have Materialize logos and tooltips denoting their functionality, fulfilling User Story 2.</p>
![list](https://user-images.githubusercontent.com/48594804/94612336-e11e2380-029a-11eb-907e-a49cd4139b12.PNG)

</details>

### **Add a Beer page**

* Feature 7: Home/Back button <details><p>This is a Materialize button that will return a user to the main page, I positioned it prominently in case they navigated here by mistake.</p>
![addbuttonback](https://user-images.githubusercontent.com/48594804/94620760-087aed80-02a7-11eb-93c8-3743f2a1b678.PNG)

</details>

* Feature 8: Add a beer entry form <details><p>This is a Materialize form with seven fields for data entry. The first field is for the 'Beer Name'. It is a text field with a max character length of 100. I made it mandatory so as to make it impossible for a user to save a completely blank entry. I left the other fields as optional as I figured that in some situations, a user may only want to record minimal data and go back and fill in more later. This fulfills User Story 4.</p>
<br><p>'Brewery Name' and 'Drank at' are also text fields of max length 100. 'On Date' triggers the Materialize Datepicker which keeps all date entries uniform. 'Comments' is a text area with max length of 300 characters. Rating is a number field with a minimun value of zero and maximum value of 10. There are also increment and decrement arrows on the right of the field.</p>
<br><p>Lastly is the switch for 'Social Distancing Observed'. As I mentioned earlier this was difficut to get right but I am happy with it and I believe it gives the app some current relevancy. At the bottom of the form is the submit button (titled 'Beer Me!') which when clicked, writes the data to the MongoDB Atlas database I set up. It also returns the user to the main page where their entry will be available to view.</p>
![addform](https://user-images.githubusercontent.com/48594804/94621087-9a82f600-02a7-11eb-8503-569a87c3191e.PNG)

</details>

### **Edit a beer page**
* Feature 9: Edit a beer entry form <details><p>This page is identical to the Add a beer page in terms of layout and structure. It is accessed by clicking the 'Edit' button beside an entry on the mainpage. Then it pulls the relevant data from the MongoDB Atlas database and displays them in the correct fields. All fields are fully editable and changes are commited to the database by clicking the 'Confirm Edit' button. This also returns the use to the mainpage so they can view their edited entry.</p>
![edit](https://user-images.githubusercontent.com/48594804/94622716-960c0c80-02aa-11eb-9435-5da24563af50.PNG)

</details>

### **Delete an entry**
* Feature 10: Delete an Entry <details><p>The delete function is available beside every entry on the main page. Once clicked it removes all data related to the entry from the MongoDB Atlas database and removes the entry from view on the app.</p>
![delete](https://user-images.githubusercontent.com/48594804/94623138-70333780-02ab-11eb-92da-6d467a173417.png)

</details>

## **Features Left to Implement**

* I would like to add a search page/functionality so a user can browse their entries if their lists get very long.

* It might be useful to add beer style categories for larger lists, so they can be sorted more easily.

* Adding API functionality that connects the user to larger beer databases so they can compare their reviews would be a great feature. At the moment I cannot find a reliable one that does not charge a fee for usage.

# **Database**
I wired my app up to a MongoDB Atlas database. I created 2 collections but ended up using only 1 - Ratings.

<details><summary>Database Screenshot</summary>

![database](https://user-images.githubusercontent.com/48594804/94627405-572f8400-02b5-11eb-92d5-af7e10dc0df9.PNG)
</details>

# **Testing**
I conducted extensive manual testing as I was coding this project. I documented the testing in an A4 notepad and have transcribed it here by date for reference.

<details>
<summary>10/9/20</summary>
After setting up my Gitpod workspace, I created app.py and base.html files and pushed to GitHub to ensure changes were committing successfully. No issues.
</details>
<details>
<summary>17/9/20</summary>
I setup a basic Flask app, requirements.txt and Procfile. I was able to successfully run the app with Python via the Terminal.
I then created a Heroku app on the Heroku website and linked it to my GitHub repository. I was able to successfuly view my app in the browser.
</details>
<details>
<summary>18/9/20</summary>
An error in my code prevented my Flask app from running. After careful examination this turned out to be a syntax error in my app.py file which was easily fixed.
</details>
<details>
<summary>22/9/20</summary>
The app is taking shape now and my basic pages are setup. It took some time to get them to connect and write to the MongoDB Atlas database. Again I had some syntax errors that I could fix no problem. Tested successfully writing and editing an entry to the database. No issues.
</details>
<details>
<summary>23/9/20</summary>
Setup all pagelinks and interconnectivity. Thoroughly tested in the browser to ensure all navigation worked as expected. Delete functionality was not clearing all entries from MongoDB Atlas database. There was a problem with my routing that I had to consult the Code Institute tutor support team on. I recoded this successfully and it is now working fine.
<br> Created an env.py file to hide my MongoDB password. Setup GitIgnore file to ensure it does not get pushed to my repository. Also created the key on Heroku in the Config Vars section. Tested once complete and app works as expected on localhost but not on Heroku. Fixed by relinking my Github repository on the Heroku website. env.py file is not being pushed to Git repository.
</details>
<details>
<summary>24/9/20</summary>
<br> Made large amounts of code and style changes today. Ran into some issues with my app/database relationship but was able to resolve without need for tutor support. I regularly checked localhost to ensure expected behaviour and made good use of Chrome Developer Tools to help solve positioning problems. At end of day checked Heroku app and all working as expected.
</details>
<details>
<summary>25/9/20</summary>
<br> Much the same as yesterday, large amount of code and CSS changes today. Any issues were resolved without much problem. Checked all code in validators to ensure I wasn't missing anything. Some stray tags detected which I removed and my Jinga code is showing as an error in the HTML validator but as far as I know this is normal.
</details>
<details>
<summary>26/9/20</summary>
<br> Happy with core code so today thoroughly checked all functionality several times and all links and buttons several times. No issues.
</details>
<details>
<summary>28/9/20</summary>
Bug detected when viewing the app on mobile device running Chrome for Android. The Navbar logo is popping out of the navbar into the body element. Was several hours trying to resolve myself and with Code Institute Tutors. This unfortuantely is unresolved. See 'Known Bugs' section below for further details.
</details>
<details>
<summary>29/9/20</summary>
One final pass of code through validators and thorough testing of all app functionality before submission. No issues apart from known display issue caught yesterday.
</details>

## **Known Bugs**
When testing the app on my own mobile device I encountered a display issue with the logo in the navbar. It is partially popping out into the body element. I tried to resolve this using CSS media queries. If the app is viewed and resized in Chrome Developer Tools it can be observed that the media queries work and the issue is fixed. However despite saving and commitiing the changes to GitHub and Heroku, the issue is still observable on the mobile device.
<br> I was several hours online with the Code Institute tutors trying to resolve this. Four different tutors looked at the issue with me but a resolution was not found. The most likely cause is a bug with Materialize itself when interacting with Chrome. I was told by the tutors to log it as a bug in my documentation and explain it for the assessor.

<details><summary>Bug Screenshot</summary>

![bugscreenshot](https://user-images.githubusercontent.com/48594804/94626660-73cabc80-02b3-11eb-914d-2489dc597e77.PNG)
</details>


# **Technologies Used**

## **Materialize** - https://materializecss.com/
Materialize was used as the Framework for the app and I incorporated many of its features, as detailed above. I really enjoyed getting to know it and it was a nice change from Bootstrap which I used for my 2 previous Milestone Projects.

## **HTML5** - https://www.w3.org/TR/html52/
HTML5 was used for the general structuring and positioning on the app.

## **CSS3** - https://www.w3.org/Style/CSS/Overview.en.html
CSS3 was used to style the website.

## **Python3** - https://www.python.org/
Python was used to run the application.

## **Javascript** - https://www.javascript.com/
Javascript is used in conjunction with the Materialize framework to operate the forms and data entry functionality.

## **JQuery** - https://jquery.com/
JQuery was used to deploy javascript functionality with Materialize.

## **Flask** - https://flask.palletsprojects.com/en/1.1.x/
Flask was used to dynamically generate pages, links and other content within the app.

## **MongoDB Atlas** - https://www.mongodb.com/
MongoDB was used as the database to read, write, edit and delete data from the app interface.

## **Pymongo** - https://pypi.org/project/pymongo/
Pymongo was used to handle the interaction between Python and MongoDB.

## **Jinja** - https://jinja.palletsprojects.com/en/2.11.x/
Jinja was used as a templating language for Python. I really enjoyed learning this and found it incredibly useful.

## **Balsamiq** - https://balsamiq.com/wireframes/
Balsamiq was used to create my wireframes at the start of this project.

## **Heroku** - https://www.heroku.com/
Heroku was used to host the final deployed version of the app.

## **Git, GitPod & GitHub** - https://github.com/
Gitpod was used as the development environment. Git and Github were used for version control. My repository was linked to my Heroku app for synchronised commit pushes.

## **HTML validator** - https://validator.w3.org/ 
This was used to ensure the code on my HTML pages were error free.

## **CSS validator** - https://jigsaw.w3.org/css-validator/
This was used to ensure my CSS stylesheet was error free.

## **CSS Autoprefixer** - https://autoprefixer.github.io/
This was used to check for webkit styles when attempting to rectify a known bug.

# **Deployment**
 This project was fully developed in [GitPod](https://www.gitpod.io/). To start off I used the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) available on [GitHub](https://github.com/). 
 As I was building the project I regularly committed my code to my [GitHub Repository](https://github.com/menacethedenis/CI_Milestone_3_Denis_Lymer) by pushing it from my local Git repository via command prompts from the GitPod terminal.
 <br>

 The app is deployed on [Heroku](https://beer-tracker-ci-ms3.herokuapp.com/). This was connected directly to my [GitHub Repository](https://github.com/menacethedenis/CI_Milestone_3_Denis_Lymer) to allow synchronised pushes of any commits I made.

## **Heroku Deployment**
Deployment to [Heroku](https://beer-tracker-ci-ms3.herokuapp.com/) from the [GitHub Repository](https://github.com/menacethedenis/CI_Milestone_3_Denis_Lymer) was completed using the following steps:
1. In the browser, navigate to the [Heroku dashboard](https://dashboard.heroku.com/) and login with username and password.
2. Click the **New** button on the top right of the dashboard and select **Create New App** from the dropdown menu.
3. Enter a name for the app, this must be unique, the autoprompt will guide you. Then select the most relevant region for you and click the **Create App** button.
4. The app will now be created and will open on the **Deploy** tab. Under the  **Deployment Method** select **GitHub**.
5. Login using GitHub username and password and select the relevant Repository in the search box. Once found, click **Connect** and under **Manual Deploy** select the relevant branch and click **Deploy Branch**. The app will now deploy based on the latest commit pushed to the Repository.
6. Click the **Settings** tab, scroll down to the **Config Vars** section and click the **Reveal Config Vars** button.
7. Click the Add button and create key:value pairs for IP, PORT and any URIs or Secret Keys required by your project.
8. Scroll back to the top of the page, click the **More** button and select **Restart all dynos**.
9. Finally, scroll down to the **Domains** section and click the link to your app to open the deployed app in the browser. 

## **Local Deployment**
The Technologies used in this project are listed above. To deploy locally you will need the following minimum requirements:
*Local or browser based development environment.
*Git - local and online GitHub repository.
*Python and Flask installed in your development environment.
*MongoDB Atlas - account, cluster and collection.

1. Navigate to this projects [GitHub Repository](https://github.com/menacethedenis/CI_Milestone_3_Denis_Lymer), click the green **Clone or download** button and copy the clone URL.
2. In the terminal of your development environment, navigate to or create the folder you would like to clone the repository files into.
3. Use the **git clone** command combined with the clone URL and press enter to clone the files to your selected folder.
```
git clone https://github.com/menacethedenis/CI_Milestone_3_Denis_Lymer
```
4. In the terminal install the required modules using the pip3 install command.
```
pip3 install -r requirements.txt
```
5. Once the terminal has confirmed all installs have been successful run the app on an Open Port with the following command.
```
python3 app.py
```

# **Credits**
## **Content**

This app is based heavily on the lessons from the Code Institute Data Centric Development Module. I also referenced several threads on Stack Overflow when I was trying to resolve some issues but I did not use anyone elses code. 

<br>The Code Institute tutors were also very helpful in assisting some bug resolution, particularly the known display bug detailed above.

<br>Before starting this project I had a look at some other students projects that had been posted on the Code Institute Slack channels, to get a feel for what others were doing and to hopefully ensure my idea hadn't already been taken. This was purely research, I did not use any other student's code.

<br>The image used in the footer was sourced via google images and is open-source.

## **Acknowledgements**
I would like to thank the tutors at the Code Institute and my mentor Spencer Barriball for their outstanding support, patience, advice and encouragement.
<br>

Thanks also to the Code Institute student care team for keeping me on track, checking in and always being so understanding, empathetic and helpful.