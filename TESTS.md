# Testing records for Milestone4 Project
## All testing conducted manually
### Click on dates below to view details
<details>
<summary>20/10/20</summary>
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