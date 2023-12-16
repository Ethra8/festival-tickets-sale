# FESTIVAL TICKETS SALE
## OVERVIEW

This app aims at being a useful sales point for selling access tickets for a festival, or any other event.  
It could also sell any other items, such as the following examples:
- Excusion packs
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

  
Access App [HERE](https://festival-tickets-sale-1bab2955093f.herokuapp.com/) 


### CREATE PROJECT IN GOOGLE CLOUD PLATFORM
- Go to [Google Cloud platform](https://console.cloud.google.com/). To create new project, click on 'New Project':
  
![image](https://github.com/Ethra8/music-festival/assets/80659091/9d5010e7-7697-49a4-96df-16a862efe005)

- Enable the following APIs for this project:
   + Google Drive API
   + Google Sheets API

- **ENABLE GOOGLE DRIVE API**:  
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

- **ENABLE GOOGLE SHEETS API** :
   1. Go to 'APIs and Services' > 'Library' and type 'Google Sheets API' on the search bar. Click on it, and 'Enable'. ***No need to give credentials again, as the credentials given to Google Drive include Google Sheets***:  
      ![image](https://github.com/Ethra8/music-festival/assets/80659091/99bba5cc-8c84-4a53-a904-3bfc4a4b68ef)

### INCLUDE GOOGLE CLOUD CREDENTIALS IN PROJECT
1. Copy .json credential file previously downloaded from Google Cloud Platform to our project folder, and rename it as 'creds.json' for simplicity sake.
2. Open creds.json file, and copy **client_email** generated (without including the brackets)
3. Go to our **Google SpreadSheet** and click on 'Share' to share SpreadSheet with client_email from creds.jason file, so our project can access and edit the SpreadSheet. Make sure 'editor' is selected and untick 'notify people'.
4. **IMPORTANT: Avoid the creds.json file to be uploaded to GitHub**, as it contains sensible information. To do that, open ***.gitignore*** file in project, and include our creds.json file. ***Don't forget to CTR+S***:
   ![image](https://github.com/Ethra8/music-festival/assets/80659091/41d61007-2cb4-4d60-9fb6-7e8e4b26cb95)
5. On the terminal, type 'git add .', then 'git status' and make sure the creds.json file is not in the list, before committing to GitHub.

    

### TECHNOLOGIES USED


### PYTHON MODULES INSTALLED
- pyfiglet : To style logo in welcome message. Documentation taken from [geeksforgeeks](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/)
- google-auth : To give access to GoogleSheets API. Will use our creds.json file to set authentication for the project. Full documentation [here](https://google-auth.readthedocs.io/en/master/).
- gspread : To access and update data in SpreadSheet. Full documentation [here](https://docs.gspread.org/en/latest/)
   + To install google-auth & gspread, type in terminal:  
     pip3 install gspread google-auth  
   + To upgrade pip in future for newer versions, type in terminal:  
     python.exe -m pip install --upgrade pip
- 


## ACKNOWLEDGEMENTS
- [Center-aligning text on console in Python](https://stackoverflow.com/questions/8907236/center-aligning-text-on-console-in-python) on Stackoverflow.com
- [Email validation through Regex](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) at [Geeksforgeeks](www.geeksforgeeks.org)
- [How To Send Email In Python via smtplib](https://www.youtube.com/watch?v=cjd9kEIxKHM&list=PL6flErFppaj0SbhDPvzC6hXFzRiP-it6i&index=8) Youtube video by [Mukesh otwani](https://www.youtube.com/@Mukeshotwani)
- [Printing slowly (Simulate typing)](https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing) on Stackoverflow.com
- [Fancy fonts for titles/logo using pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) at [Geeksforgeeks](www.geeksforgeeks.org)
- 

