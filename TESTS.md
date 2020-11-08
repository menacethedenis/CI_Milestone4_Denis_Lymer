# Testing records for Milestone4 Project
## All testing was conducted manually and is documented below
<hr>

## Testing overview
My testing for this project is divided into two parts. First as I was coding/building the project,
I tested each new feature or function as I was going by using the tools available to me via Gitpod.
The current build of the website was almost always open on the localhost open port 8000, initiated 
by the entering the following command in the project terminal:
```
python3 manage.py runserver
```

Django in general has excellent error debugging functionality. If an error occurs a very detailed description
of why it happened and where the error is coming from will appear in etiher the terminal or the browser.
This makes life so much easier when trying to fix issues.

I also kept a close eye on the Gitpod 'Problems' tab, which was excellent for flagging basic syntax and indentation 
errors across all the languages I was using. It doesnt like Jinja very much but otherwise is very helpful. I much prefer 
to tidy these small, not neccessarily code-breaking, errors up as I am coding, rather than leave it all to take care of in one big lump.

Another very powerful tool which helped me greatly was Flake8. This was vital for ensuring the quality of code in 
my project adhered to industry standards. I could view all current errors by entering the following command in
the terminal:
```
python3 -m flake8
```
This produced a list of errors in the terminal and by holding the Ctrl keyboard button and clicking on one, Gitpod
would navigate me directly to the exact line of the error. A very useful feature.
<br>

Secondly, once the project was finished, I manually tested the site functionality and robustness by using 
my User/Admin Stories as guidelines. My previous testing experience served me well here as I did my best to break the site!
<hr>

### Click on dates below to view details of daily testing during project coding
<details>
<summary>20/10/20</summary>
After generating a new Git repository from the Code Institute template, I setup my Gitpod workspace.
I created a manage.py file, installed Django and pushed to GitHub to ensure commits were happening 
successfully. No issues.
</details>
<details>
<summary>21/10/20</summary>
Much of today was spent setting up Allauth to deal with site user management and registration functionality.
Some minor syntax issues were throwing errors as I was testing user registration in the browser but these were
easily adjusted. I setup my base.hmtl file, Home app and some templates, relationally linked with Jinja and was able to 
successfully view them in the browser.
</details>
<details>
<summary>22/10/20</summary>
Updated headers and Jinja templating. Headers were displaying poorly in browser so adjusted via HTML styles and CSS.
</details>
<details>
<summary>23/10/20</summary>
Bulk upload of products and categories from fixtures file was continuously failing. Eventually realised I had accidentally transferred
the same data from the JSON formatter for my products to both files. Updated the Categories file with the correct code and upload was successful.
Added nav bars to my mainpage and mobile headers. Tested views and dropdown functionality in the browser. Some slight display issues remedied via
CSS and HTML styles. Also fixed some linter issues flagged in Gitpod. Flake8 does not seem to like Jinja and is flagging problems in my HTML
templates as I have no doctype specified on Line 1. I checked this with Code Institute tutor support and they told me to ignore it.
</details>
<details>
<summary>24/10/20</summary>
Today I built my Products and Product Details pages. Took quite some time to get these linking correctly. Had to refer to Code Institute tutorials
several times. All is working as expected now and basic details and images are displaying in the browser.
</details>
<details>
<summary>26/10/20</summary>
Added Search form to header and tested in browser. No issues finding correct products or returning no matches. Added sort bar to products page. This did
not work in the browser. Checked code and noticed syntax errors. Once remedied sort function works. Also created bag app today. Could not get it to calculate
delivery costs and had to refer to Code Institute tutorials for assistance here. Eventually bag app works and displays fine in browser with correct calculations
for delivery threshold.
</details>
<details>
<summary>27/10/20</summary>
More work on bag app today. Needed further assistance from Code Institute tutorials when coding the context processor. It works fine in browser.
All basic functionality works such as add/remove and update qunatities etc.. Also added toast notifications. These were not displaying at all initially.
Checked my code and noticed they were not at the correct folder level in my directory. After adjusting this they work.
</details>
<details>
<summary>28/10/20</summary>
Tidied up Toasts with CSS, they look good in the browser now. Basic Checkout app views, templates and Models setup along with Stripe functionality and signals. The forms
are visible in the browser but need styling.
</details>
<details>
<summary>29/10/20</summary>
Setup Webhook handlers with assistance from Code Institute tutorials. Had to fix multiple syntax errors before I could get a successful response.
</details>
<details>
<summary>30/10/20</summary>
Created superuser for site to access admin backend. Tidied up some grammatical display errors. A lot of back and forth between the code and the browser
trying to get the delete function to work but eventually got the code correct. Linter showing errors on the models.py file in the Profiles app.
Adjusted several typos. Tried another test of delete function from admin side and got a 404 error in the browser:
"Page not found (404)
Request Method:	GET
Request URL:	http://localhost:8000/
Raised by:	home.views.index
No Product matches the given query."
<br>
This broke the site. I could not navigate to any other pages even after refreshing. 
</details>

### Click on User/Admin Stories below to view details of manual functionality testing after project completion

## **Known Bugs**
When testing the app on my own mobile device I encountered a display issue with the logo in the navbar. It is partially popping out into the body element. I tried to resolve this using CSS media queries. If the app is viewed and resized in Chrome Developer Tools it can be observed that the media queries work and the issue is fixed. However despite saving and commitiing the changes to GitHub and Heroku, the issue is still observable on the mobile device.
<br> I was several hours online with the Code Institute tutors trying to resolve this. Four different tutors looked at the issue with me but a resolution was not found. The most likely cause is a bug with Materialize itself when interacting with Chrome. I was told by the tutors to log it as a bug in my documentation and explain it for the assessor.

<details><summary>Bug Screenshot</summary>

![bugscreenshot](https://user-images.githubusercontent.com/48594804/94626660-73cabc80-02b3-11eb-914d-2489dc597e77.PNG)
</details>