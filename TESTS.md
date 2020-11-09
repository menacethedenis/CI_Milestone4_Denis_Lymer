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
Adjusted several typos. Tried another test of delete function from admin side and got a 404 error in the browser. This is documented further in the Known Bugs
section.
</details>
<details>
<summary>31/10/20</summary>
Setup Heroku database, app and Amazon Webs Services bucket. Test pushes to all were successful. Set sensitive information to environmental variables in Gitpod
and Config Variables in Heroku. No issues when tested. Noticed several display issues on site when checking responsiveness on Google Dev Tools.
Fixed and adjusted with HTML and CSS stylings. Did some regression testing on Stripe functionality, checked Webhooks, all returned successfully.
Setup automated email via Django and linked to my own gmail account. Hid sensitive info with environmental variables. Tested functionality with
TempMail and was successfully able to create a new user and verify their email address with temporary mail account.
</details>

<details>
<summary>2/11/20</summary>
Major Flake8 error tidy up today. Some syntax, indentation, whitespace, expected lines and line too long errors were all fixed.
Did a quick regression test of the site to check I had inadvertently changed anything and discovered that the AllAuth password validation
functionality was throwing an error. I couldn't spot any errors in the settings.py file so I checked Stack Overflow. Discovered that I shouldn't use '\' to
bump to next line when tidyng some code, I needed to use '+'.
So I changed this:
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation. /
                UserAttributeSimilarityValidator',
    },
To this:
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'UserAttributeSimilarityValidator',
    },

and everyting worked as expected.
</details>
<details>
<summary>3/11/20</summary>
Created new custom models for Turntables & Headphones. COmpleted entire process for adding/deleting products to and from store and all worked fine.
</details>
<details>
<summary>4/11/20</summary>
Noticed search function was not returning Turntable or Headphone models eben though they were displaying when navigated to via the relevant categories.
Could not figure this out so checked with Code Institute tutors. They advised this would be far too complex an issue to resolve for this project and
I should go back to just using the Products model for store items. Had updated a lot of HTM and CSS stylings in the meantime so instead of rolling back
the project to an earlier commit. I deleted the 2 models entirely from the project and moved on.
</details>
<details>
<summary>5/11/20</summary>
Full site functionality regression test to ensure nothing had changed after changing the models yesterday. No issues. Major styling updates sitewide via CSS and
HTML. All displaying well in various browser sizes when checked on Google Devtools.
</details>
<details>
<summary>6/11/20</summary>
Removed placeholder images and imported correct ones. Added more products and categories via JSON fixtures. All displaying fine.
Another full test of site functionality. No issues.
</details>
<details>
<summary>7/11/20</summary>
Lighthouse highlighted a button display error I had not previously noticed. Fixed it with CSS and HTML.
</details>
<details>
<summary>8/11/20</summary>
Full site functionality test revealed some display issues on Allauth templates. These were easily remedied via CSS and HTML.
Fixed some display issues on smaller screens. Grammar and spelling check on README and TESTS markdown files.
Ran all HTML and CSS files through validators.
Final full site test via User/Admin stories - documented in follwoing section.
</details>

### Click on User/Admin Stories below to view details of manual functionality testing after project completion
#### **User**
<details>
<summary>As a user I want to be able to purchase my favourite music in various formats.</summary>

</details>
<details>
<summary>As a user I want to see new releases I may not be aware of.</summary>

</details>
<details>
<summary>As a user I want to be able to edit or delete items or quantities in a shopping bag.</summary>

</details>
<details>
<summary>As a user I want to be able to save my user profile for ease of purchase in the future.</summary>

</details>
<details>
<summary>As a user I want a secure checkout experience.</summary>

</details>
<details>
<summary>As a user I want an easy to navigate site.</summary>

</details>
<details>
<summary>As a user I want a good experience on different device sizes.</summary>

</details>
<details>
<summary>As a user I want to see more info/details about a product if I want them.</summary>

</details>
<details>
<summary>As a user I want to be able to see my previous order history.</summary>

</details>
<details>
<summary>As a user I want to be able to edit or update my user settings and address information.</summary>

</details>
<details>
<summary>As a user I want to be able to browse and/or purchase without having to register or save my personal details.</summary>

</details>
<details>
<summary>As a user I want to easily view a running subtotal of my purchases.</summary>

</details>
<details>
<summary>As a user I want to know if I qualify for free delivery or how much I need to spend to do so.</summary>

</details>
<details>
<summary>As a user I want to be able to login/logout of my account easily.</summary>

</details>

#### **Admin**
<details>
<summary>As an admin I want to be able to login from anywhere on the site.</summary>

</details>
<details>
<summary>As an admin I want to be able to edit or delete items from the site.</summary>

</details>
<details>
<summary>As an admin I want to be able to add new items to the site easily.</summary>

</details>
<details>
<summary>As an admin I want to change the categories of products like New Arrivals or Clearance.</summary>

</details>
<details>
<summary>As an admin I want to be able to view the registered site users.</summary>

</details>
<details>
<summary>As an admin I want to be able to add, edit or delete other users.</summary>

</details>

## **Known Bugs**
Observed on Chrome browser running on Windows 10.
Sometimes when logged into the site as an admin, using the delete button under a product to remove it from the site
throws the following error:

"Page not found (404)
Request Method:	GET
Request URL:	http://localhost:8000/
Raised by:	home.views.index
No Product matches the given query."

Any attempt to refresh the page or navigate to a different page also produces the error. It is impossible to reload the site
in the standard browser but it runs without issue in incognitio mode. This happened several times throughout development of the project
and was extremely frustrating. Trying the empty cache and hard reset function in Developer tools did not remedy it, the only way
I could get the site to run again in the standard browser was to completely clear the cache and all cookies from the previous week in
advanced chrome settings, stop my Gitpod workspace and log out of it and every other site I was logged into,
close all browser windows and open a fresh session.