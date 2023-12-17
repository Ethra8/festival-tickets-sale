# FESTIVAL TICKETS SALE
## OVERVIEW

This app aims at being a useful sales point for selling access tickets for a festival, or any other event.  
It could also sell any other items, such as the following examples:
- Excursion packs
- Online courses
- Online private lesson packs

The app is linked to a Spreadsheet, which can be customized to change the following values, which will be reflected on the app, **making the app fully reusable**:
- Items' names
- Items' codes
- Items' pricing
- Items' details
- Title of items' details' list printed to user
- Company/App name (logo name)
- Logo fonts
- Initial stock
- Invoice numering

  ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/274c8f09-cb16-4c18-a7c7-791f87cc17c3)


## LIVE APP  
Access App [HERE](https://festival-tickets-sale-1bab2955093f.herokuapp.com/)

## REPOSITORY
Check out the repository [HERE](https://github.com/Ethra8/festival-tickets-sale)

## AUTHOR
Edna Torres Munill

# TABLE OF CONTENTS

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
    + [Prerequisites](#prerequisites)
      * [Create Project in Google Cloud Platform](#create-project-in-google-cloud-platform)
      * [Enable APIs](#enable-apis)
      * [Connect to APIs Through Python](#connect-to-apis-though-python)
      * [Google Sheets Template](#google-sheets-template)
    + [Deploy to Gitpod](#deploy-to-gitpod)
      * [Include Google Cloud Credentials in Project](#include-google-cloud-credentials-in-project)
      * [Install or Update Requirements txt File](#install-or-update-requirements-txt-file)
    + [Deploy in Heroku](#deploy-in-heroku)
- [Credits](#credits)
    + [Acknowledgements](#acknowledgements)

# HOW TO USE
## CUSTOMER SIDE
From a user (customer) side, the app has been designed to be user-friendly and informs at all times of the actions that are being undertaken, or options that are available.



https://github.com/Ethra8/festival-tickets-sale/assets/80659091/28265965-3251-4a44-ad10-ba01065a8b85


1. After the logo and the welcome messages appear, click ENTER to access the Pricing List
2. The Pricing List shows each item next to its price per unit
3. You are then given the following options:
   1. Type any key or pres ENTER to create a new order : A new list is shown including each item's CODE (refer to next step 4)
   2. Type D (or d) to see items' details : The items' details are listed, each item with its details indented in a sub-list
   3. Type E (EXIT): You are then asked to confirm that you want to exit the app, and if confirmed, the logo shows with a copyright notice.
4. You see the items list, each next to their unique item CODE
5. You are asked to introduce the CODE related to the item you want to order (e.g.: A1)
6. You are then asked ***'How many 'Adult Day 1 Access' do you want to include to your order?*** (referring to the item related to the code given as an example)
7. You input the number of the selected item to be included in your order (e.g.: 2)
8. You get a notification stating ***"Added to your order: 2 'Adult Day 1 Access'"***
9. You are then given the following options:
    1. Type any key or press ENTER to continue order : Points 4 - 9 are repeated all over to add new item quantity to your order
    2. Type P to return to Pricing List : Shows pricing list and follows flow since above-mentioned step 2
    3. Type F to FINALIZE order
10. Once you FINALIZE order, you are prompted to include your email, so that the invoice can be sent for due payment
11. You are then asked to include a user name to include in your invoice
12. The order is shown with the following information:
    1. Invoice number
    2. Invoice date
    3. User name
    4. User email
    5. Items ordered, showing each item's ordered units, and total price per items ordered
    6. Order's total amount
13. You are asked review order, and you are given the following options:
    1. Type any key or press enter to CONFIRM order : Go to next step 14
    2. Type U to change email or user name : YOu are asked to type your email, then to type your user name (repeat from step 11 onwards)
    3. Type C to CONTINUE ORDERING : Shows Item list with correspondent CODES (repeat from step 4 onwards)
    4. Type E to EXIT the app : Cancels the order, and you are then asked to confirm that you want to exit the app, and uppon confirmation, the logo shows with a copyright notice.
14. You are informed that the order has been confirmed, that an email has been sent, warns you that the order will be cancelled in case you fail to proceed to payment on due date.
15. Confirms that email has been sent:
    
    ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/5ef501dd-567b-4530-b66f-74efc1fc6319)


## SELLER SIDE
From the seller's side, this app is fully customizable to fit the seller's needs. Please refer to the [README worksheet](https://docs.google.com/spreadsheets/d/1ImaSd4bEFAWuswu8Sxa2yYcjWl9oec_cPdpYVZ_sVik/edit?pli=1#gid=404608901) included in the SpreadSheet for more details:  
  
![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/73a21298-0e0a-450c-898b-34baebee9956)

1. The following can be customized **directly on the SpreadSheet**, easily finding the customizable values as they are placed in **cells with a green background**:
  **1. App name** (logo name)
  **2. Logo font**
  **3. Welcome message** (before, and after logo)
  **4. Items to sell**
  **5. Price of items to sell**
  **6. Item codes**
  **7. Item details**
  **8. Title of items details list printed to user**
  **9. Inicial stock**
  **10. Final 'copyright' message includes customizable logo name**

2. Every order generates an invoice, which is included in the last empty row of the invoices worksheet:  

  ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/123d8f8f-fb86-4e09-b741-82ac3d53fe4c)  

3. The items sold are then included in the [total_items_sold Worksheet](https://docs.google.com/spreadsheets/d/1ImaSd4bEFAWuswu8Sxa2yYcjWl9oec_cPdpYVZ_sVik/edit?pli=1#gid=1046768896):  
  
  ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/97307086-91c0-435f-9809-cf79c9f5fb96)  
  
4. The remaining stock is updated through python code, and the initial stock can be manually updated to fit the seller tru stock per item:  
  
![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/47ce04d1-42b3-4f26-96ed-efbdade8644b)

5. The revenue per item is also automatically calculated after each order through python code, as well as the grand total revenue, and updated to the [total_sales Worksheet](https://docs.google.com/spreadsheets/d/1ImaSd4bEFAWuswu8Sxa2yYcjWl9oec_cPdpYVZ_sVik/edit?pli=1#gid=817408163):  

  ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/0682ec5b-9c09-416a-80b1-5503e28459fb)

**WATCH THIS VIDEO WHERE I HAVE CHANGED ALL CUSOTMIZABLE VALUES DIRECTLY ON THE SPREADSHEET TO CREATE A NEW CUSTOMIZED APP !!**  
- Changed values in ***settings worksheet***:

   ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/e0991726-8067-42ac-9f0d-e3d44e3843b5)  
  
- Changed values in ***pricing worksheet***:
  
  ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/083e03c2-292d-4cae-9945-02bbb13119a2)

- Changes values in ***item_details worksheet***:

  ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/4e0515e8-7a4b-49a7-b243-ef2ec131be9d)  

- **WATCH THE MAGIC**:  

https://github.com/Ethra8/festival-tickets-sale/assets/80659091/84abcd50-6a8e-4a44-9100-f26c08bdc172

- ALthough there were previous invoices generated with the original **ROCK FEST** settings, the items on the invoice have updated to match the items included on the Pricing Worksheet, so all is ready!:

  ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/13498246-3391-4a2b-b059-fc2e735d587f)


# FEATURES
## IMPLEMENTED FEATURES
This app contains the following features and functionalities:
1. **REUSABLE CODE** : The most distinctive feature is that values are not hard-coded, and are all retrieved from the SpreadSheet, meaning that whoever wants to reuse the code, can easily customize the app to fit needs. These are the ***customizable app values***:
   **1. App name** (logo name)
   **2. Logo font**
   **3. Welcome message** (before, and after logo)
   **4. Items to sell**
   **5. Price of items to sell**
   **6. Item codes**
   **7. Item details**
   **8. Title of items details list printed to user**
   **9. Inicial stock**
   **10. Final 'copyright' message includes customizable logo name**


https://github.com/Ethra8/festival-tickets-sale/assets/80659091/0a7f0d96-9cc1-4496-b8d8-e7025d174317


3. All data input by the user is ***trimmed***, so any white space is dismissed
4. When user is prompted to type a key, the input is ***case unsensitive***, so whether the user includes upper case or lower case letters, it will not affect the flow.
5. User can ***exit app anytime***
6. User is given ***several options***, as for instance, to view item details' list or not
7. User can ***return to pricing list at any time*** during the order
8. User is ***informed at all times*** of each *step*, and its *output*
9. Takes ***user's inputs*** (item to order, quantity, options after each step, email, user name, etc.)
10. ***Email validation*** (gives error if user doesn't include valid format example@email.vv)
11. ***Name validation*** (gives error if input is left blank)
12. ***Repeats ordering process*** as many times as the user demands, and updates order accordingly
13. ***Sends email to user with all the order data***
14. ***Includes new invoice generated from order in 'invoice worksheet'***
15. ***Updates remaining stock in 'stock worksheet'***
16. ***Updates items sold in 'total_items_sold worksheet'***
17. ***Calculates total sales income per item*** after each order, and ***updates values in 'total_sales worksheet'***
18. ***Calculates grand total of sales, and updates value in 'total_sales worksheet'***


## FUTURE FEATURES
The following features are to be implemented in a near future:
1. Create PDF using python, to be included in the email sent to the user, instead of writing the details of the order in the email body.
2. Automatically cancel order if user does not proceed to payment on due date.
   
# FLOW CHART

![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/bb2a78b5-39d3-4087-9fb2-e563c2574ac4)  


# DATA MODEL

## NEW_ORDER DICTIONARY
1. After viewing Pricing List, when user selects option to Start, the invoice is generated by the generate_order() function. Updates NEW_ORDER dictionary with new invoice_no value, and current date:
```$python
# get key values to create NEW_ORDER dict
item_sales_new_order = invoices_worksheet.row_values(1)
# get mock values for each key to create NEW_ORDER dict
values_sales_new_order = invoices_worksheet.row_values(3)
# dict NEW_ORDER takes user inputs all along the app
# to create final invoice with total amount
NEW_ORDER = dict(zip(item_sales_new_order, values_sales_new_order))

def generate_order():
    """
    New order is generated.
    New sequencial invoice_no is generated from previous invoice no.
    in invoices_worksheet, and current date
    are included in NEW_ORDER dictionary
    """
    print_slow("Loading ...\n")
    # takes last invoice_no from invoices_worksheet;
    # default e.g.: INV-10000
    invoice = invoices_worksheet.col_values(1)[-1]
    # takes initial letter of last invoice_no
    # before the '-' e.g: INV
    invoice_letters = invoice.split("-")[0]
    # takes numbers of last invoice_no after 
    # the '-' and returns string e.g.: '10000'
    invoice_no = invoice.split("-")[1]
    # turns num string to integer,
    # and adds 1 to invoice_no; e.g.: 10001
    invoice_no = int(invoice_no) + 1
    # creates new invoice_no with same format 
    # (letters-nums) e.g. INV-10001
    invoice_no = f"{invoice_letters}-{invoice_no}"

    NEW_ORDER['invoice_no'] = invoice_no
    NEW_ORDER['order_date'] = DATE
    list_keyword_item()
    return NEW_ORDER
```

![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/b4c05a69-f9c8-4836-aefa-775002ee1c34)  


# LIBRARIES USED
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

# TESTING
This app has been carefully tested, as detailed below.  

## VALIDATION TESTING
[CI Python Linter by Code Institute](https://pep8ci.herokuapp.com/) has been used to validate the code, and no errors were found:  
  
![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/0b8b5c31-3e85-4219-b0d2-9f82e60eb9a7)


## MANUAL TESTING

# DEFECTS

## DEFECTS TRACKING
I have created ***issues*** in GitHub in order to track the most relevant issues encountered, all successfully fixed:  

![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/5f429574-4f06-43a2-b628-7d87dbf5cfe9)


## DEFECTS OF NOTE
**All the defects tracked as GitHub issues have been successfully fixed**, and none remain.


## OUTSTANDING DEFECTS
No outstanding defects have been found

# DEPLOYMENT
## PREREQUISITES

## GOOGLE SHEETS TEMPLATE
This project has a Google Sheet linked to it: [festival_tickets_sales](https://docs.google.com/spreadsheets/d/1ImaSd4bEFAWuswu8Sxa2yYcjWl9oec_cPdpYVZ_sVik/edit?pli=1#gid=1072696018).  
As the project has been built in order to be as reusable as possible, you can make a copy of it:  

![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/3c4b5231-1261-4d64-910b-67f99660d37b)

After cloning the repository, updating the credentials (creds.json file), the env.py file with your own sensible data, and making sure the app is linked to your own Google account, you can update your copy made of the SpreadSheet to fit your needs.  
**IMPORTANT**: Rename your copy exactly the same as it is inicually named - **festival-tickets-sale**  
The SpreadSheet also contains a **README** Worksheet to remind you of the main instructions to avoid system breakdown, also reviewed in more detail below.  

  ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/2f66a82d-bc07-4a88-8a32-5140b96cfdd2)  

Find below the data included in each Worksheet, and which one can be to fit your needs:  
**IMPORTANT**: You may ***ONLY*** change values that are in cells with a ***green background***, but ***DO NOT change values in CELLS with a red background***, to avoid system crash.

### 1. SETTINGS WORKSHEET
This Worksheet, as its name suggests includes general settings to be customized as follows:  
1. Logo/ company name
2. Logo/ title font
3. Welcome message before logo
4. Welcome message after logo
5. Title of the item details (if you have some items that have extra detail info, suck as packs or bonus, here you can update the title the user will see when the user chooses to access the item details)  

![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/b089fd71-425c-4e57-a343-28c321e51da9)


### 2. PRICING WORKSHEET
This Worksheet, as its name suggests, includes a list of the items to be sold, and their related values, as follows:  
1. **ITEM TYPE**: You can change the type of items you are selling. E.g.: If you are selling lesson packs, you should change *TICKETS* by *PACKS*.
2. **ITEM NAMES**: Update the names of the items you are selling. E.g.: *10 lessons pack* instead of *Adult Day 1 Access*, and so on with each item.
3. **PRICE**: Change the prices of each item. ***IMPORTANT***: Use a dot '**.**' for decimal values, NOT COMMAS, as the app system does not recognize commas for decimals.
4. **CODE**: Each item has to have a unique code that will be displayed next to the item in a list. The user will have to type the code of the item to be included in the order. It is recommended to include 2 value codes to make it easy for the user to type the desired item's code.  

![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/5fa01a97-c7bf-42db-ac9b-f218e1d7981a)


### 3. ITEM DETAILS WORKSHEET
This Worksheet is meant to include the items' details to be shown to the user when the user requests to see items' details after the pricing list os displayed: 
  
![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/767ffd5c-59d4-4b6b-aa22-04ad85783cc8)  


**IMPORTANT**: You ***MUST*** include at least one item with at least one 'extra_info' to avoid system crash.  
You can customize the following:  
  
![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/67659655-a976-4fbf-b67e-d7ce94aa8e5f)

1. **item_type**: For your own record, as this will not be displayed to the client (app user)
2. **item_display_name**: This will be displayed to the client, and shouldbe the same af the ***item name*** introduced in the pricing worksheet.
3. **extra_info**: You can include until 4 different features for each item, each if which will be displayed to the client that requests to see details as the example below:
    
  ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/a24dd189-6656-4f3f-af19-65c671e114b1)


### 4. INVOICES WORKSHEET
This Worksheet, as its name suggests, shows all the invoices (orders), and should NOT be updated, unless when you make a coy of the SpreadSheet, or if a customer cancels an order. **The item names** are automatically retrieved from the Pricing Worksheet, and **Total Amount** is also automatically calculated also with the prices included in the Pricing Worksheet. 
The only data to be updated before your first invoice is generated id the original dafault invoice value ***INV-100000*** placed in a ***cell with a green background***. All other values placed in ***cells with red background should not be changed*** to avoid system breakdown.  
**IMPORTANT**: Your default invoice should contain the following format : ***letter(s)-nums*** (at least 1 letter BEFORE a mandatory **-** , and then as many **0** as your invoice numbering system requires.  

In the following screenshot, you can see two test invoices created:

  ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/ad7983ae-4c48-4798-bce0-791f48c89d3a)


### 5. TOTAL ITEMS SOLD WORKSHEET
As its name suggests, this Worksheet shows how many items have been sold (by item type). The amount is automatically calculated by the code, by summing each item type from all orders, and the item names are also automatically retrieved from the pricing worksheet, so **NO NEED TO MANUALLY UPDATE ANYTHING**. Find an example below:  
  
  ![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/f6999d62-6948-40f7-86c5-8be3c1b0c381)  
  
  
### 6. STOCK WORKSHEET
As its name suggests, this Worksheet shows the remaining stock per item type. The item names are automatically retrieved from the Pricing Worksheet, and the total remaining stock per item is automatically calculated every time the code is run. **The only values to be updated are to INITIAL STOCK per item**, values in ***cells with a green background***, from which the sold items will be sustracted.  
**IMPORTANT**: The row of 'REMAINING STOCK' should also manually be set only the 1st time, to  match the initial stock values, and then it will be automatically updated after each sale.  
  
![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/c596855a-9c07-4730-b40b-bbe56dfdc4b0)  


### 7. TOTAL SALES WORKSHEET
As its name suggests, this Worksheet shows the total sales per item, as well as the total income generated by selling each and every item. The item names are retrieved from the Princing Worksheet, and the total amounts automatically calculated, so it shouldn't be updated manually. See an example below:  
  
![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/a2e6f7ad-f1bb-4bd6-84d3-e37f142b3d83)  


## GMAIL ACCOUNT WITH API KEY
- Create a [gmail account](https://accounts.google.com/signup) 
- **WITHOUT 2-STEP AUTENTICATION** : Once you are signed in you need to make sure it has less secure app access turned on use [this link](https://myaccount.google.com/lesssecureapps?pli=1)
- **WITH 2-STEP AUTENTICATION** : These accounts require an ***application-specific password*** for less secure apps access. To get your specific app password, follow these steps:
  1. Go to your Google Account.
  2. Select Security.
  3. Under "Signing in to Google," select 2-Step Verification.
  4. At the bottom of the page, select App passwords.
  5. Enter a name that helps you remember where you’ll use the app password.
  6. Select Generate.
  7. To enter the app password, follow the instructions on your screen.
  8. The app password is the 16-character code that generates on your device.
  9. Select Done.
  10. **IMPORTANT NOTE**: The app password that you've generated is a sensitive data, so you must store it in an **env.py**. Follow the steps stated [here]():

## CREATE PROJECT IN GOOGLE CLOUD PLATFORM
- Go to [Google Cloud platform](https://console.cloud.google.com/). To create new project, click on 'New Project':
  
![image](https://github.com/Ethra8/music-festival/assets/80659091/9d5010e7-7697-49a4-96df-16a862efe005)

## ENABLE APIs
Enable the following APIs for this project:
- **Google Drive API**
- **Google Sheets API**

**1. ENABLE GOOGLE DRIVE API**:  
   1. On the project page, to enable APIs and services: Click on 'more products' dropdown, and select 'APIs and Services', then 'Library', and type 'Google Drive API' on the search bar, and enable it.
  
![image](https://github.com/Ethra8/music-festival/assets/80659091/ff6e9511-3646-4446-ab42-3b926e1e9d67)

![image](https://github.com/Ethra8/music-festival/assets/80659091/1a841a3a-6075-42c3-8aad-5801c7c6766c)

![image](https://github.com/Ethra8/music-festival/assets/80659091/f9f49842-e82a-4056-847a-04141078a282)

   2. ***Create 'Credentials'***: After clicking on 'Enable' in the previous step, you are taken to the API Overview page, where we click on 'Create Credentials':
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/6a8cd2a2-6547-4152-912c-2cdaff25d77b)

   3. On the credentials form, select 'Application Data' for the question 'What data will you be accessing?', then click 'Next':  
  
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/2182605f-aab0-4daa-bd07-f0e402d1925e)
   
   5. Then, on the next stage of the form, include a 'Service account name'. An account email will be automatically generated following your input. Then, click 'Create and Continue':  
  
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/338b3a2f-6615-4c99-8d05-32859f2db285)


   7. In the 'Role' Dropdown box choose Basic > Editor then press Continue:  

      ![image](https://github.com/Ethra8/music-festival/assets/80659091/a669bd00-2f0c-4ef4-9906-da0e663f8e0b)
  
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/557794cf-288d-4fb4-875f-122ef097a209)

   9. Other settings are optional, so click on 'Done':  

      ![image](https://github.com/Ethra8/music-festival/assets/80659091/f92a2415-7ae6-4a02-8a0e-c8af2c806471)

   11. On the 'Credentials' page, the account generated will appear at the bottom of the page. Click on it to open account page:  
    
        ![image](https://github.com/Ethra8/music-festival/assets/80659091/c9fae63b-2af5-4c2a-8bbf-d21035cfadbc)

   13. Once in the account page, click on 'Keys':
     
        ![image](https://github.com/Ethra8/music-festival/assets/80659091/5bfe5109-afa2-446a-a8e6-7f19e7cf7916)

   14. Click on the 'Add Key' dropdown and select 'Create New Key'.  
     
   15. Select JSON option. Once you click on 'Create', a file will automatically download to your 'downsloaded' folder on your device. This file will normally be downloaded to your 'downsloads' file, and will typically be named as your project name, being a .json type document:  

        ![image](https://github.com/Ethra8/music-festival/assets/80659091/692d119c-ccde-474d-b14a-6307f3ee2310)

**2. ENABLE GOOGLE SHEETS API** :
  - Go to ***'APIs and Services'*** > ***'Library'*** and type 'Google Sheets API' on the search bar. Click on it, and 'Enable'. ***No need to give credentials again, as the credentials given to Google Drive include Google Sheets***:  
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/99bba5cc-8c84-4a53-a904-3bfc4a4b68ef)

## CONNECT TO APIs THROUGH PYTHON
  - Include the SCOPE constant variable to the run.py file (no need to change it when reusing the code, just leave it as it is):
```$python
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
```
  - The following constant variables allows the code to access our SpreadSheet:
```$python
# CREDS constant variable, takes creds from file creds.json
# Allows code to access SpreadSheet
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('festival_tickets_sale')
```

## DEPLOY LOCALLY IN YOUR IDE

### INCLUDE GOOGLE CLOUD CREDENTIALS IN PROJECT
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
4. Go to the copied yu have previously made of the **Google SpreadSheet: festival_tickets_sale** and click on 'Share' to share SpreadSheet with client_email from creds.json file, so the project can access and edit the SpreadSheet. Make sure 'editor' is selected and untick 'notify people'.
5. **IMPORTANT: Avoid the creds.json file to be uploaded to GitHub**, as it contains sensible information. To do that, open ***.gitignore*** file in project, and include our creds.json file. ***Don't forget to CTR+S***:
   ![image](https://github.com/Ethra8/music-festival/assets/80659091/41d61007-2cb4-4d60-9fb6-7e8e4b26cb95)
6. **BEFORE COMMITING TO GITHUB*** : On the terminal, type 'git add .', then 'git status' and make sure the creds.json file is not in the list. Once you are reasured that it is not in the list to be commited, commit.  

### INSTALL OR UPDATE REQUIREMENTS txt FILE
Before deploying the app, the requirements.txt file included in the project must be installed with the dependencies. On the terminal, type:  
```$python
pip3 install -r requirements.txt
```
In case you install further modules or libraries, then the requirements.txt file must be updated by typing in the terminal the following command:
```$python
pip3 freeze > requirements.txt
```
## DEPLOY LOCALLY IN YOUR IDE
### SECRETS
 **IMPORTANT: Avoid secrets from being uploaded to GitHub**, open ***.gitignore*** file in project, and insure to include  creds.json and env.py ***Don't forget to CTR+S***:

![image](https://github.com/Ethra8/music-festival/assets/80659091/41d61007-2cb4-4d60-9fb6-7e8e4b26cb95)  

#### creds.json
This file holds the secrets to have access to the google drive and sheet you created in prerequisites.
1. Copy the file that you downloaded from Google Cloud Platform, and rename it as 'creds.json' and load it to your main directory in your IDE.
2. **BEFORE COMMITTING TO GITHUB** : On the terminal, type 'git add .', then 'git status' and make sure the creds.json file is not in the list. Once you are reassured that it is not in the list to be committed, commit.

#### env.py
This file holds the access to the email you created in prerequisites so the program can send confirmation emails to users.
1. Create an **env.py** file
2. Include the follwoing code:
```$python
import os
from pathlib import Path
```
3. Use the following method to store your sensitive data into system variables:
```$python
os.environ.setdefault('EMAIL_APP_PASS', 'your_own_app_password')
os.environ.setdefault('APP_EMAIL', 'your_own_google_account_email')
```
4. Include the env.py file in your .gitignore file to avoid pushing it to GitHub revealing your secret data.
5. Import Operational System to your **run.py** file so it can access the system variables secretely stored in your env.py file:
```$python
import os
```
6. To access the system variables in your run.py file, use the following method, and store them in other variables:
```$python
sender = os.environ.get("APP_EMAIL")
gmail_app_password = os.environ.get("EMAIL_APP_PASS")
```
7. **BEFORE COMMITTING TO GITHUB** : On the terminal, type 'git add .', then 'git status' and make sure the env.py file is not in the list. Once you are reassured that it is not in the list to be committed, commit.

### INSTALL REQUIREMENTS.TXT
Before deploying the app, the requirements.txt file needs to be executed to get the dependencies installed. On the terminal, type:  
```$python
pip3 install -r requirements.txt
```
### RUN THE SERVER
to run locally, type on the terminal:  
```$python -m run.py
```

## DEPLOY IN HEROKU    
### Set up new Heroku app
- Create a [Heroku account](https://signup.heroku.com/login)
- Create a new project

### ENVIRONMENT VARIABLES
Go to 'Settings' to store the environmental variables, and click on 'Config Vars':  

![image](https://github.com/Ethra8/festival-tickets-sale/assets/80659091/c820d0fa-62c9-4674-83a8-3c40e897dacf)  

Add the following variables:  

- APP_MAIL : Your app email
- EMAIL_APP_PASS : Your app password
- CREDS : creds.json (all data, including the {})
- PORT : 8000

### DEPLOYMNET METHOD
- Click the deploy tab
- Scroll down and select Github
- Use the github link and type in the name of your repository
- Click from deploy from branch and select main
- Once your application is running, switch to Automatic so that any changes are automatically reflecte in Heroku deployed app

## DEPLOY IN HEROKU    

# CREDITS
The app was coded using [Code Institute's P3 Template](https://github.com/Code-Institute-Org/p3-template), which includes all necessary features and files for it to run smoothly on Heroku, by creating a terminal, as this project does not have any front-end code.  
  
## ACKNOWLEDGEMENTS
- [Center-aligning text on console in Python](https://stackoverflow.com/questions/8907236/center-aligning-text-on-console-in-python) on Stackoverflow.com
- [Email validation through Regex](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) at [Geeksforgeeks](www.geeksforgeeks.org)
- [How To Send Email In Python via smtplib](https://www.youtube.com/watch?v=cjd9kEIxKHM&list=PL6flErFppaj0SbhDPvzC6hXFzRiP-it6i&index=8) Youtube video by [Mukesh otwani](https://www.youtube.com/@Mukeshotwani)
- [Printing slowly (Simulate typing)](https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing) on Stackoverflow.com
- [Fancy fonts for titles/logo using pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) at [Geeksforgeeks](www.geeksforgeeks.org)
- My mentor [Malia Havlicek](https://github.com/maliahavlicek) for all her meaningful insights.

