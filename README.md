# FESTIVAL TICKETS SALE
## OVERVIEW

This app aims at being a useful sales point for selling access tickets for a festival, or any other event.  
It could also sell any other items, such as the following examples:
- Excursion packs
- Online courses
- Online private lesson packs

The app is linked to a Spreadsheet, which can be customized to change the following:
- Product names
- Product codes
- Products pricing
- Company/App name (logo name)
- Logo fonts
- Initial stock
- Invoice numering

  
![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/c6cbf253-7d22-4774-adf4-3f891bf72a56)  

## LIVE APP  
Access App [HERE](https://festival-tickets-sale-1bab2955093f.herokuapp.com/)

## REPOSITORY
Check out the repository [HERE](https://github.com/Ethra8/festival-tickets-sale)

## AUTHOR
Edna Torres Munill

## TABLE OF CONTENTS

- [Overview](#overview)
- [Live App](#live-app)
- [Repository](#repository)
- [Author](#author)
- [How to Use](#how-to-use)
- [Features](#features)
    + [Implemented Features](#implemented-features)
    + [Future Features](#future-features)
- [Flow Chart](#flow-chart)
- [Data Model](#data-model)
- [Libraries Used](#libraries-used)
- [Testing](#testing)
    + [Validation Testing](#validation-testing)
    + [Manual Testing](#manual-testing)
- [Defects](#defects)
    + [Defects Tracking](#defects-tracking)
    + [Defects of Note](#defects-of-note)
    + [Outstanding Defects](#outstanding-defects)
- [Deployment](#deployment)
    + [Requirements](#requirements)
      * [Create Project in Google Cloud Platform](#create-project-in-google-cloud-platform)
        - [Enable APIs](#enable-apis)
      * [Google Sheets Template](#google-sheets-template)
    + [Deploy to Gitpod](#deploy-to-gitpod)
      * [Include Google Cloud Credentials in Project](#include-google-cloud-credentials-in-project)
      * [Update Requirements.txt](#update-requirements.txt)
    + [Deploy in Heroku](#deploy-in-heroku)
- [Credits](#credits)
    + [Acknowledgements](#acknowledgements)

## HOW TO USE


## FEATURES

### IMPLEMENTED FEATURES

### FUTURE FEATURES

## FLOW CHART

## DATA MODEL

## LIBRARIES USED
- **pyfiglet** : To style logo in welcome message. Documentation taken from [geeksforgeeks](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/)
- **google-auth** : To give access to GoogleSheets API. Will use our creds.json file to set authentication for the project. Full documentation [here](https://google-auth.readthedocs.io/en/master/).
- **gspread** : To access and update data in SpreadSheet. Full documentation [here](https://docs.gspread.org/en/latest/)
   + To install google-auth & gspread, type in terminal:  
```$python
pip3 install gspread google-auth
```  
   + To upgrade pip in future for newer versions, type in terminal:  
```$python
python.exe -m pip install --upgrade pip
```
- **datetime** : To get current date and time, for invoicing purposes. Full documentation [here](https://docs.python.org/3/library/datetime.html)
- **sys** : This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. Allows sensitible data stored in system variables stored in ***env.py*** to be accessed in our main run.py file. Full documentation [here](https://docs.python.org/3/library/sys.html)
- **os** : This module provides a portable way of using operating system dependent functionality. Full documenttion [here](https://docs.python.org/3/library/os.html).
- **time** : This module provides various time-related functions. Full documentation [here](https://docs.python.org/3/library/time.html)
- **smtplib** : This module defines an SMTP client session object that can be used to ***send mail*** to any internet machine with an SMTP or ESMTP listener daemon. Full documentation [here](https://docs.python.org/3/library/smtplib.html)
- **ssl** : This module provides access to Transport Layer Security (often known as “Secure Sockets Layer”) encryption and peer authentication facilities for network sockets, both client-side and server-side. This module uses the OpenSSL library. It is available on all modern Unix systems, Windows, macOS, and probably additional platforms, as long as OpenSSL is installed on that platform. Full documentation [here](https://docs.python.org/3/library/ssl.html)
- **re** : Regex module, to validate email input by user. Full documentation [here](https://docs.python.org/3/library/re.html)
- **email.message** : Import ***EmailMessage*** class from the ***email*** package, to send emails. Full documentation [here](https://docs.python.org/3/library/email.examples.html)

## TESTING

### VALIDATION TESTING

### MANUAL TESTING

## DEFECTS

### DEFECTS TRACKING

### DEFECTS OF NOTE

### OUTSTANDING DEFECTS

## DEPLOYMENT

### CREATE PROJECT IN GOOGLE CLOUD PLATFORM
- Go to [Google Cloud platform](https://console.cloud.google.com/). To create new project, click on 'New Project':
  
![image](https://github.com/Ethra8/music-festival/assets/80659091/9d5010e7-7697-49a4-96df-16a862efe005)

#### ENABLE APIs
Enable the following APIs for this project:
- **Google Drive API**
- **Google Sheets API**

1. **ENABLE GOOGLE DRIVE API**:  
   1. On the project page, to enable APIs and services: Click on 'more products' dropdown, and select 'APIs and Services', then 'Library', and type 'Google Drive API' on the search bar, and enable it.
  
![image](https://github.com/Ethra8/music-festival/assets/80659091/ff6e9511-3646-4446-ab42-3b926e1e9d67)

![image](https://github.com/Ethra8/music-festival/assets/80659091/1a841a3a-6075-42c3-8aad-5801c7c6766c)

![image](https://github.com/Ethra8/music-festival/assets/80659091/f9f49842-e82a-4056-847a-04141078a282)

   2. ***Create 'Credentials'***: After clicking on 'Enable' in the previous step, you are taken to the API Overview page, where we click on 'Create Credentials':
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/6a8cd2a2-6547-4152-912c-2cdaff25d77b)

   3. On the credentials form, select 'Application Data' for the question 'What data will you be accessing?', then click 'Next':  
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/2182605f-aab0-4daa-bd07-f0e402d1925e)
   
   4. Then, on the next stage of the form, include a 'Service account name'. An account email will be automatically generated following your input. Then, click 'Create and Continue':  
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/338b3a2f-6615-4c99-8d05-32859f2db285)


   5. In the 'Role' Dropdown box choose Basic > Editor then press Continue:
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/a669bd00-2f0c-4ef4-9906-da0e663f8e0b)
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/557794cf-288d-4fb4-875f-122ef097a209)

   6. Other settings are optional, so click on 'Done':
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/f92a2415-7ae6-4a02-8a0e-c8af2c806471)

   7. On the 'Credentials' page, the account generated will appear at the bottom of the page. Click on it to open account page:
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/c9fae63b-2af5-4c2a-8bbf-d21035cfadbc)

   8. Once in the account page, click on 'Keys':
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/5bfe5109-afa2-446a-a8e6-7f19e7cf7916)

   9. Click on the 'Add Key' dropdown and select 'Create New Key'.
   10. Select JSON option. Once you click on 'Create', a file will automatically download to your 'downsloaded' folder on your device:  
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/692d119c-ccde-474d-b14a-6307f3ee2310)

2. **ENABLE GOOGLE SHEETS API** :
  - Go to ***'APIs and Services'*** > ***'Library'*** and type 'Google Sheets API' on the search bar. Click on it, and 'Enable'. ***No need to give credentials again, as the credentials given to Google Drive include Google Sheets***:  
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/99bba5cc-8c84-4a53-a904-3bfc4a4b68ef)


#### GOOGLE SHEETS TEMPLATE
This project has a Google Sheet linked to it: [festival_tickets_sales](https://docs.google.com/spreadsheets/d/1ImaSd4bEFAWuswu8Sxa2yYcjWl9oec_cPdpYVZ_sVik/edit?pli=1#gid=1072696018).  
As the project has been built in order to be as reusable as possible, you can make a copy of it:  

![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/3c4b5231-1261-4d64-910b-67f99660d37b)

After cloning the repository, updating the credentials (creds.json file), and making sure the app is linked to your own Google account, you can update your copy made of the SpreadSheet to fit your needs.  
**IMPORTANT**: Rename your copy exactly the same as it is inicually named - **festival-tickets-sale**  
The SpreadSheet also contains a **README** Worksheet to remind you of the main instructions to avoid system breakdown, also reviewed in more detail below.  

  ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/2f66a82d-bc07-4a88-8a32-5140b96cfdd2)  

Find below the data included in each Worksheet, and which one can be to fit your needs:  
**IMPORTANT**: You may ***ONLY*** change values that are in cells with a ***green background***, but ***DO NOT change values in CELLS with a red background***, to avoid system crash.

##### SETTINGS WORKSHEET
This Worksheet, as its name suggests includes general settings to be customized as follows:  
1. Logo/ company name
2. Logo/ title font
3. Welcome message before logo
4. Welcome message after logo
5. Title of the item details (if you have some items that have extra detail info, suck as packs or bonus, here you can update the title the user will see when the user chooses to access the item details)  

![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/b089fd71-425c-4e57-a343-28c321e51da9)


##### PRICING WORKSHEET
This Worksheet, as its name suggests, includes a list of the items to be sold, and their related values, as follows:  
1. **ITEM TYPE**: You can change the type of items you are selling. E.g.: If you are selling lesson packs, you should change *TICKETS* by *PACKS*.
2. **ITEM NAMES**: Update the names of the items you are selling. E.g.: *10 lessons pack* instead of *Adult Day 1 Access*, and so on with each item.
3. **PRICE**: Change the prices of each item. ***IMPORTANT***: Use a dot '**.**' for decimal values, NOT COMMAS, as the app system does not recognize commas for decimals.
4. **CODE**: Each item has to have a unique code that will be displayed next to the item in a list. The user will have to type the code of the item to be included in the order. It is recommended to include 2 value codes to make it easy for the user to type the desired item's code.  

![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/5fa01a97-c7bf-42db-ac9b-f218e1d7981a)


##### ITEM DETAILS
This Worksheet is meant to include the items' details to be shown to the user when the user requests to see items' details after the pricing list os displayed: 
  
![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/767ffd5c-59d4-4b6b-aa22-04ad85783cc8)  


**IMPORTANT**: You ***MUST*** include at least one item with at least one 'extra_info' to avoid system crash.  
You can customize the following:  
  
![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/67659655-a976-4fbf-b67e-d7ce94aa8e5f)

1. **item_type**: For your own record, as this will not be displayed to the client (app user)
2. **item_display_name**: This will be displayed to the client, and shouldbe the same af the ***item name*** introduced in the pricing worksheet.
3. **extra_info**: You can include until 4 different features for each item, each if which will be displayed to the client that requests to see details as the example below:
    
  ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/a24dd189-6656-4f3f-af19-65c671e114b1)


##### INVOICES
This Worksheet, as its name suggests, shows all the invoices (orders), and should NOT be updated, unless when you make a coy of the SpreadSheet, or if a customer cancels an order. **The item names** are automatically retrieved from the Pricing Worksheet, and **Total Amount** is also automatically calculated also with the prices included in the Pricing Worksheet. 
The only data to be updated before your first invoice is generated id the original dafault invoice value ***INV-100000*** placed in a ***cell with a green background***. All other values placed in ***cells with red background should not be changed*** to avoid system breakdown.  
**IMPORTANT**: Your default invoice should contain the following format : ***letter(s)-nums*** (at least 1 letter BEFORE a mandatory **-** , and then as many **0** as your invoice numbering system requires.  

In the following screenshot, you can see two test invoices created:

  ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/ad7983ae-4c48-4798-bce0-791f48c89d3a)


##### TOTAL ITEMS SOLD
As its name suggests, this Worksheet shows how many items have been sold (by item type). The amount is automatically calculated by the code, by summing each item type from all orders, and the item names are also automatically retrieved from the pricing worksheet, so **NO NEED TO MANUALLY UPDATE ANYTHING**. Find an example below:  
  
  ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/f6999d62-6948-40f7-86c5-8be3c1b0c381)  
  
  
##### STOCK
As its name suggests, this Worksheet shows the remaining stock per item type. The item names are automatically retrieved from the Pricing Worksheet, and the total remaining stock per item is automatically calculated every time the code is run. **The only values to be updated are to INITIAL STOCK per item**, values in ***cells with a green background***, from which the sold items will be sustracted.  
**IMPORTANT**: The row of 'REMAINING STOCK' should also manually be set only the 1st time, to  match the initial stock values, and then it will be automatically updated after each sale.  
  
![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/c596855a-9c07-4730-b40b-bbe56dfdc4b0)  


##### TOTAL SALES
As its name suggests, this Worksheet shows the total sales per item, as well as the total income generated by selling each and every item. The item names are retrieved from the Princing Worksheet, and the total amounts automatically calculated, so it shouldn't be updated manually. See an example below:  
  
![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/a2e6f7ad-f1bb-4bd6-84d3-e37f142b3d83)

### DEPLOY TO GITPOD
#### INCLUDE GOOGLE CLOUD CREDENTIALS IN PROJECT
1. Copy .json credential file previously downloaded from Google Cloud Platform to our project folder, and rename it as 'creds.json' for simplicity sake.
  - Your creds.json file including your credentials should look like that:  
```$python
{
    "type": "service_account",
    "project_id": "<YOUR_VALUE>",
    "private_key_id": "<YOUR_VALUE>",
    "private_key": "<YOUR_VALUE>",
    "client_email": "<YOUR_VALUE>",
    "client_id": "<YOUR_VALUE>",
    "auth_uri": "https://accoutns.google.com/0/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cer_url": "https://www.googleapis.com/oauth2/v1/certs",
    "clien_x509_cert_url": "<YOUR_VALUE>"
}
```
3. Open creds.json file, and copy **client_email** generated (without including the brackets)
4. Go to our **Google SpreadSheet** and click on 'Share' to share SpreadSheet with client_email from creds.json file, so the project can access and edit the SpreadSheet. Make sure 'editor' is selected and untick 'notify people'.
5. **IMPORTANT: Avoid the creds.json file to be uploaded to GitHub**, as it contains sensible information. To do that, open ***.gitignore*** file in project, and include our creds.json file. ***Don't forget to CTR+S***:
   ![image](https://github.com/Ethra8/music-festival/assets/80659091/41d61007-2cb4-4d60-9fb6-7e8e4b26cb95)
6. **BEFORE COMMITING TO GITHUB*** : On the terminal, type 'git add .', then 'git status' and make sure the creds.json file is not in the list. Once you are reasured that it is not in the list to be commited, commit.  

#### UPDATE REQUIREMENTS.TXT
Before deploying the app, the requirements.txt file included in the project must be updated with the dependencies. On the terminal, type:  
```$python
pip3 install -r requirements.txt
```

### DEPLOY IN HEROKU    

## CREDITS
The app was coded using [Code Institute's P3 Template](https://github.com/Code-Institute-Org/p3-template), which includes all necessary features and files for it to run smoothly on Heroku, by creating a terminal, as this project does not have any front-end code.  
  
### ACKNOWLEDGEMENTS
- [Center-aligning text on console in Python](https://stackoverflow.com/questions/8907236/center-aligning-text-on-console-in-python) on Stackoverflow.com
- [Email validation through Regex](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) at [Geeksforgeeks](www.geeksforgeeks.org)
- [How To Send Email In Python via smtplib](https://www.youtube.com/watch?v=cjd9kEIxKHM&list=PL6flErFppaj0SbhDPvzC6hXFzRiP-it6i&index=8) Youtube video by [Mukesh otwani](https://www.youtube.com/@Mukeshotwani)
- [Printing slowly (Simulate typing)](https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing) on Stackoverflow.com
- [Fancy fonts for titles/logo using pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) at [Geeksforgeeks](www.geeksforgeeks.org)
- My mentor [Malia Havlicek](https://github.com/maliahavlicek) for all her meaningful insights.

