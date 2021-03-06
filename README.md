# Introduction to Azure applications
## Article CMS (FlaskWebProject)

This project is a Python web application built using Flask. The user can log in and out and create/edit articles. An article consists of a title, author, and body of text stored in an Azure SQL Server along with an image that is stored in Azure Blob Storage. You will also implement OAuth2 with Sign in with Microsoft using the `msal` library, along with app logging.

## Demo: 
![](demo.gif)

## Table of Contents:

1. [Azure Portal](#azure-portal)
    * [Resource Group](#resource-group)
    * [Azure SQL Database](#azure-sql-database)
    * [Storage Account](#storage-account)
    * [Blob Container](#blob-container)
    * [OAuth2 with MSAL](#oauth2-with-msal)
    * [Azure Active Directory](#register-app-in-azure-active-directory)
    * [Monitoring and Logging in Azure](#monitoring-and-logging-in-azure)
    * [Deploy App with App Service](#deploy-app-with-app-service)
    * [Store Log Streams](#store-log-streams)
2. [Screenshots](#screenshots)
3. [Getting started](#getting-started)
4. [Dependencies](#dependencies)
5. [Troubleshooting](#troubleshooting)
6. [Udacity Requirements](#udacity-requirements)

## Azure Portal: 

### ```Resource Group:```

1. On Azure Portal, find ```Resource Groups``` > ```Create a resource group```
2. Fill in information: 
```
Subscription: Azure for Students
Resource group: azure-resourcegroup
Region: (US) West US 2
```
3. Hit ```Create```

### ```Azure SQL Database:```
1. On Azure Portal, find ```SQL Database``` > ```Create```
2. Fill in information: 
```
Subscription: Azure for Students
Resource Group: azure-resourcegroup
Database name: azure-db
Server > Create new > 
    Fill in information for creating new server: 
        Server name: azure-dbserver
        Server admin login: ploratran
        Password: *********
        Location: (US) West US 2
Want to use SQL elastic pool? NO
Compute + Storage > Configure database > Basic (for less demanding workloads) > Apply
```
3. On  ```Next: Networking``` page, select: 
```
Connectivity method: Public endpoint
Firewall rules: 
    Allow Azure services and resources to access this server: YES
    Add current client IP address: YES
```
4. Hit ```Create```
5. On Azure portal > SQL databases > click on the newly created azure-db > Query editor (preview)
6. Login SQL server using server admin login and password created in step 2, you should see database table as below: 

<img src="screenshots/sql.png" width="600" height="350"> 


### ```Storage Account:```

1. On Azure Portal, find ```Storage Account``` > ```Create```
2. Fill in information:
```
Subscription: Azure for Students
Resource group: azure-resourcegroup
Storage account name: blob123
Performance: Standard
Account kind: StorageV2 (general purpose v2)
Replication: leave as default setting
```
3. Click ```Next: Networking```: 
```
Connectivity method: Public endpoint (all networks)
Network routing: leave as default
```

4. Click ```Next: Data protection``` > ```Next: Advanced```
```
Blob storage: 
    Allow Blob public access: Enabled
    Blob access tier (default): Cool
```

5. Click ```Review + create``` > ```Create```


### ```Blob Container:```

1. On ```Storage account```, look on the left hand side for ```Blob Service``` > ```Containers```
2. Click ```+ Container``` to create a Blob Container.
3. Fill in information: 
```
Name: images
Public access level: Container (anonymous read access for containers and blobs)
```
4. Hit ```Create```. 
5. In ```Storage Account```, look on the left panel. Under ```Settings``` > ```Properties```, you should see the storage endpoint URL as below: 

<img src="screenshots/blob-endpoint.png" width="600" height="350"> 

### ```OAuth2 with MSAL:```

1. On Azure portal, navigate to ```Azure Active Directory``` > ```App registrations```
2. On the left panel, look for ```Authentication``` > ```Add a platform```
2. Choose ```Web``` for ```Configure platforms```, then fill in inforamtion:
```
Redirect URIs: https://localhost:5555/getAToken
Logout URL: https://localhost:5555/login
```

<img src="screenshots/redirecturl.png" width="600" height="350"> 


### Register app in ```Azure Active Directory:``` 

Azure Active Directory is Microsoft’s solution for single sign-on (SSO) and multi-factor authentication (MFA). Using this in combination with the Microsoft Authentication Library (MSAL) to use "Sign in with Microsoft" buttons in an app, although it can be used more broadly for identity management purposes within an organization. The "tenant" in Azure AD is usually equivalent to an organization.

1. On Azure portal, navigate to ```Azure Active Directory```, then hit ```Create```
2. Create a new tenant (if not exists) as below: 

<img src="screenshots/tenant.png" width="600" height="350"> 

3. On the left panel, click on ```App registrations```, and fill in data as picture below: 
```
Name: bertelsmann-azure
Supported account types: Accounts in any organizational directory (Any Azure AD directory - Multitenant) and personal ....
Redirect URI: /getAToken
```

4. Hit ```Create``` to register new application

5. On the left panel, click ```Certificates & secrets``` > ```New client secret```. Save this new Client Secret on ```config.py```

6. After successfully registered the app, look on the left panel for ```Authentication```. Make sure Redirect URIs and Front-channel logout URL have the correct URIs as below: 

<img src="screenshots/redirecturl.png" width="600" height="350"> 

### ```Monitoring and Logging in Azure:```

Flask doesn't output regular print statements as you'd see in other Python apps. However, the logger contained within a Flask app does output to sys.stderr. Flask apps actually have this logger by default, and it uses the logging library from the Python standard library. 

1. In ```__init__.py``` the logging level to warning, it can be done as follows :
```
app.logger.setLevel(logging.WARNING)
```

2. Update the stream handler for the logger to only pay attention to warnings and above:
```
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)
app.logger.addHandler(streamHandler)
```

### Deploy App with ```App Service:```

1. On Azure portal, navigate to ```Web App```, then hit ```Create```

2. On the ```Create Web App``` page, fill in information as below, then click ```Create```:

```
Subscription: leave as default
Resource group: azure-resourcegroup

Name: ploratran
Publish: Code
Runtime stack: Python 3.7 or higher
Operating System: Linux
Region: West US 2

Linux Plan (West US 2): leave as default
Sku and size: Free F1 (1GB memory) 
```
3. Go back to ```Resource Group``` and visit the deployed website. If you see the site as picture below, the web app was deployed correctly: 

<img src="screenshots/azure-webapp.png" width="600" height="350">

4. Go back to ```App Service```, look at ```Deployment``` section on the left panel. Click on ```Deployment Center```

5. Click on ```Settings```, and fill in information as picture below: 

<img src="screenshots/deployment-center.png" width="600" height="350">

6. After deploying the app, navigate to the url to make sure the code was successfully deployed onto Web App

### Store ```Log Streams:```

1. Create a new ```Storage Account``` to store log streams in Azure portal. Go back to [Storage Account](#storage-account) section and fill with the following information: 

```
Subscription: Azure for Students
Resource group: azure-resourcegroup
Storage account name: loggin123
Performance: Standard
Account kind: StorageV2 (general purpose v2)
Replication: leave as default setting
```

At this point, there should be 2 Storage accounts, 1 for storing images and 1 for storing log streams.

2. Go back to ```App Service```. Look on the left panel for ```Log streams```. Log Streams page will display all logs.

3. Now, look on the left panel for ```Diagnosti settings (preview)``` > ```Add diagnostic setting```

4. Select the following information as below:
```
Diagnostic setting name: login-signin-sigup
log: AppServiceConsoleLogs
Destination details: Archive to a storage account
Location: West US 2
Subscription: leave as default
Storage account: logging123
```


## Screenshots:

1. A screenshot from running the FlaskWebProject on Azure:

<img src="screenshots/post.png" width="600" height="350"> 

2. A screenshot from the Azure Portal showing all of the contents of the Resource Group. The resource group must (at least) contain the following:
- Storage Account
- SQL Server
- SQL Database
- Resources related to deploying the app

<img src="screenshots/resources.png" width="600" height="350"> 

3. A screenshot showing the created tables and one query of data from the initial scripts.

<img src="screenshots/sql1.png" width="600" height="350"> 

4. A screenshot showing an example of blob endpoints for where images are sent for storage.

<img src="screenshots/blob-endpoint.png" width="600" height="350"> 

5. A screenshot of the redirect URIs related to Microsoft authentication.

<img src="screenshots/redirecturl.png" width="600" height="350"> 

6. A screenshot showing one potential form of logging with an "Invalid login attempt" and "admin logged in successfully", taken from the app's Log stream.

<img src="screenshots/log-stream.png" width="600" height="350"> 

## Getting Started:

1. Install the app locally by running:
```
$ pip install -r requirements.txt
$ python3 application.py
```

2. Open browser and navigate to ```https://localhost:5555```

3. Sign in using ```Microsoft OAuth2 with MSAL```, the application home page should look like below: 

<img src="screenshots/sign-in.png" width="600" height="350"> 

<img src="screenshots/home.png" width="600" height="350"> 

<img src="screenshots/post.png" width="600" height="350"> 

4. Sign out: 

<img src="screenshots/sign-out.png" width="600" height="350"> 

## Dependencies

1. A free Azure account
2. A GitHub account
3. Python 3.7 or later
4. Visual Studio 2019 Community Edition (Free)
5. The latest Azure CLI (helpful; not required - all actions can be done in the portal)

All Python dependencies are stored in the requirements.txt file. To install them, using Visual Studio 2019 Community Edition:
1. In the Solution Explorer, expand "Python Environments"
2. Right click on "Python 3.7 (64-bit) (global default)" and select "Install from requirements.txt"

## Troubleshooting

- Mac users may need to install `unixodbc` as well as related drivers as shown below:
    ```bash
    brew install unixodbc
    ```
- Check [here](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver15) to add SQL Server drivers for Mac.

## Udacity Requirements: 

### Log In Credentials for FlaskWebProject

- Username: admin
- Password: pass

Or, once the MS Login button is implemented, it will automatically log into the `admin` account.

### Project Instructions (For Student)

You are expected to do the following to complete this project:
1. [x] Create a Resource Group in Azure.
2. [x] Create an SQL Database in Azure that contains a user table, an article table, and data in each table (populated with the scripts provided in the SQL Scripts folder).
    - [x] Provide a screenshot of the populated tables as detailed further below.
3. [x] Create a Storage Container in Azure for `images` to be stored in a container.
    - [x] Provide a screenshot of the storage endpoint URL as detailed further below.
4. [x] Add functionality to the Sign In With Microsoft button. 
    - This will require completing TODOs in `views.py` with the `msal` library, along with appropriate registration in Azure Active Directory.
5. [x] Choose to use either a VM or App Service to deploy the FlaskWebProject to Azure. Complete the analysis template in `WRITEUP.md` (or include in the README) to compare the two options, as well as detail your reasoning behind choosing one or the other. Once you have made your choice, go through with deployment.
6. [x] Add logging for whether users successfully or unsuccessfully logged in.
    - [x] This will require completing TODOs in `__init__.py`, as well as adding logging where desired in `views.py`.
7. [x] To prove that the application in on Azure and working, go to the URL of your deployed app, log in using the credentials in this README, click the Create button, and create an article with the following data:
	- Title: "Hello World!"
	- Author: "Jane Doe"
	- Body: "My name is Jane Doe and this is my first article!"
	- Upload an image of your choice. Must be either a .png or .jpg.
   [x] After saving, click back on the article you created and provide a screenshot proving that it was created successfully. Please also make sure the URL is present in the screenshot.
8. [x] Log into the Azure Portal, go to your Resource Group, and provide a screenshot including all of the resources that were created to complete this project. (see sample screenshot in "example_images" folder)
9. [x] Take a screenshot of the Redirect URIs entered for your registered app, related to the MS Login button.
10. [x] Take a screenshot of your logs (can be from the Log stream in Azure) showing logging from an attempt to sign in with an invalid login, as well as a valid login.

### example_images Folder

This folder contains sample screenshots that students are required to submit in order to prove they completed various tasks throughout the project.

1. article-cms-solution.png is a screenshot from running the FlaskWebProject on Azure and prove that the student was able to create a new entry. The Title, Author, and Body fields must be populated to prove that the data is being retrieved from the Azure SQL Database while the image on the right proves that an image was uploaded and pulled from Azure Blob Storage.
2. azure-portal-resource-group.png is a screenshot from the Azure Portal showing all of the contents of the Resource Group the student needs to create. The resource group must (at least) contain the following:
	- Storage Account
	- SQL Server
	- SQL Database
	- Resources related to deploying the app
3. sql-storage-solution.png is a screenshot showing the created tables and one query of data from the initial scripts.
4. blob-solution.png is a screenshot showing an example of blob endpoints for where images are sent for storage.
5. uri-redirects-solution.png is a screenshot of the redirect URIs related to Microsoft authentication.
6. log-solution.png is a screenshot showing one potential form of logging with an "Invalid login attempt" and "admin logged in successfully", taken from the app's Log stream. You can customize your log messages as you see fit for these situations.

