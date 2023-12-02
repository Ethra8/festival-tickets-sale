![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

### CREATE GOOGLE PLATFORM PROJECT
1. Go to [Google Cloud platform](https://console.cloud.google.com/)
2. Create 'new project'  
![image](https://github.com/Ethra8/music-festival/assets/80659091/94b2cd1a-3f96-4497-84d4-bed666b95d86)
![image](https://github.com/Ethra8/music-festival/assets/80659091/f5cea9c7-4338-4536-b5d9-a477d50395a9)

3. We need to enable the following APIs for this project:
   + Google Drive API
   + Google Sheets API

4. On the project page, to enable APIs and services: Click on 'more products' dropdown, and select 'APIs and Services', then 'Library', and type 'Google Drive API' on the search bar, and enable it.   
![image](https://github.com/Ethra8/music-festival/assets/80659091/ff6e9511-3646-4446-ab42-3b926e1e9d67)

![image](https://github.com/Ethra8/music-festival/assets/80659091/1a841a3a-6075-42c3-8aad-5801c7c6766c)

![image](https://github.com/Ethra8/music-festival/assets/80659091/f9f49842-e82a-4056-847a-04141078a282)


5. Go to 'Credentials' and 'Create Credentials':  
![image](https://github.com/Ethra8/music-festival/assets/80659091/999e5073-cfce-42b2-933b-bbebbf7400b0)



### TECHNOLOGIES USED


### PYTHON MODULES INSTALLED
- pyfiglet : To style logo in welcome message. Documentation taken from [geeksforgeeks](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/)
