import pyfiglet 
import gspread #library first downloaded through terminal : pip3 install gspread google-auth
from google.oauth2.service_account import Credentials #imports just specific Credentials function from library, no need to import complete library
from pprint import pprint # --> must not be deployed. but very handy when coding and testing


#SCOPE in a constant, in Python, constant variables are written in CAPITALS
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

#CREDS is another constant variable, takes creds from file
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('festival_tickets_sale')

festival_settings = SHEET.worksheet('festival_settings')

price_worksheet = SHEET.worksheet('sales')
prices = price_worksheet.get_all_values() #gets all values in worksheet --> creates list of strings for each row
#print(prices)

def logo_festival_name():  
    fest_name = festival_settings.col_values(1)[-1:]
    #pprint(fest_name)
    return fest_name


fes_name = logo_festival_name()
festival_name = fes_name[0]

def logo_font():
    font = festival_settings.col_values(2)[-1:]
    return font

font = "bubble"
logo = pyfiglet.figlet_format(festival_name, font) 
# price_adult_one_day = 75 #value taken from spreadsheet
# price_adult_per_day = f"{price_adult_one_day} €"
# price_child_one_day = 45 #value taken from spreadsheet
# price_child_per_day = f"{price_child_one_day} €"

print("\n\n   WELCOME TO \n\n" + logo + "\n\n       BUY YOUR TICKETS NOW!\n\n")
#print(f"PRICING: \n\n - Adult per day: {price_adult_per_day} \n - Children under 12 years old: {price_child_per_day} \n ")

