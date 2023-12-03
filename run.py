import pyfiglet 
import gspread #library first downloaded through terminal : pip3 install gspread google-auth
from google.oauth2.service_account import Credentials #imports just specific Credentials function from library, no need to import complete library
from pprint import pprint # --> must not be deployed. but very handy when coding and testing
from datetime import datetime 


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
pricing_worksheet = SHEET.worksheet('pricing')
extra_info_worksheet = SHEET.worksheet('extra_info')
sales_worksheet = SHEET.worksheet('sales')


def logo_festival_name():
    """
    Returns Festival Name (fest_name) introduced by organizer
    in festival_settings worksheet, to be set as the logo
    in the console welcome message
    """
    fest_name = festival_settings.col_values(1)[-1:]
    #pprint(fest_name)
    return fest_name


fes_name = logo_festival_name()
festival_name = fes_name[0]


def logo_font():
    """
    Returns Font selected by organizer in
    festival_settings worksheet, to design the logo
    in the console welcome message
    """
    font = festival_settings.col_values(2)[-1:]
    #pprint(font)
    return font


font_selection = logo_font() #returns string with last item in logo_font column from festival_settings worksheet
logo_font = font_selection[0] #removes '[]'

logo = pyfiglet.figlet_format(festival_name, logo_font) # pyfiglet method to create Festival Name as Logo, then printed in welcome message in main()


def print_inventory(dct):
    """
    Returns printed dictionary (dct) formated as 1 row for each entry,
    removes '[]' and ',' as such: {item} {amount} €, aligning amounts
    e.g.: Adult 1 Day Access  75 €
    """
    print("\nPRICING:\n")
    for item, amount in dct.items(): 
        print(f'{item:25}{amount} €')
        
    # print("\n")    



def pricing():
    """
    Returns dict of ticket_types and ticket_prices
    taken from 'pricing' worksheet
    """
    ticket_types = pricing_worksheet.col_values(2)[1:] #retrieves 1st column, from 2nd row onwards (eludes 1st row) and creates list of strings
    ticket_prices = pricing_worksheet.col_values(3)[1:] #retrieves 3rd column, from 2nd row onwards (eludes 1st row) and creates list of strings
    
    price_per_ticket = dict(zip(ticket_types, ticket_prices))

    return price_per_ticket


pricing = pricing() # dict of ticket_types & ticket_prices, returned by pricing()


def display_pricing_list():
    """
    Asks user by input if s/he wants to see the Pricing List,
    in which case calls print_inventory(pricing), passing 'pricing' dict as argument
    """
    p = input("Press Y if you want to see the Pricing List:\n").lower()
    
    if p == "y":       
        print_inventory(pricing)
    elif p != "y":
        print("Maybe see you next time...")
        main()
        

def extra_info():
    """
    Returns list of extra info in 'extra_info' worksheet per item
    """
    print("\nDETAILED INFO:\n")
    full_info = extra_info_worksheet.get_all_values()[1:] #creates list of lists, starting at row 2 (one list per row)

    for i in full_info: # prints each row formated as follows
        print(f"{i[1]} --> Includes: {i[2]}, {i[3]}, {i[4]}")
    print("\n")


NEW_ORDER = {
        'invoice_num' : ' ',
        'invoice_date' : ' ',
        'user_name' : ' ',
        'user_email' : ' ',
        'adult_one_day' : 0,
        'adult_full_event' : 0,
        'child_one_day' : 0,
        'child_full_event' : 0,
        'fest_pack' : 0,
        'backstage_day_bonus' : 0,
        'backstage_full_bonus' : 0
    }


def order_inputs():
    ORDER_ITEM = input("\nType the KEY next to the ticket you want to include in your order:\n").lower()
    try:
        if ORDER_ITEM == "a1": # ADULT 1 DAY ACCESS
            try:
                adult_one_day = int(input("\nHow many 'Adult 1 Day Access' do you want to order? - Type a number from 1 - 30\n"))
                
                if adult_one_day < 0 or adult_one_day > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f"You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.")
                return False
            
            NEW_ORDER['adult_one_day'] = adult_one_day

            print(f"\nSuccessfully added to your cart: {adult_one_day} ticket(s) of 'Adult 1 Day Access'")
            print(NEW_ORDER)
            continue_ordering = input("\nDo you want to order more tickets? - Type Y (YES), or F (FINISH ORDER):\n").lower()
            if continue_ordering == "y":
                order_inputs()
            if continue_ordering == "f":
                print("Your order is being processed...")
                process_order(NEW_ORDER)

        if ORDER_ITEM == "af": # ADULT FULL ACCESS
            try:
                adult_full_event = int(input("\nHow many 'Adult Full Event Access' do you want to order? - Type a number from 1 - 30\n"))
                
                if adult_full_event < 0 or adult_full_event > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f"You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.")
                return False
            
            NEW_ORDER['adult_full_event'] = adult_full_event
            print(f"\nSuccessfully added to your cart: {adult_full_event} ticket(s) of 'Adult Full Event Access'")
            print(NEW_ORDER)
            continue_ordering = input("\nDo you want to order more tickets? - Type Y (YES), or F (FINISH ORDER):\n").lower()
            if continue_ordering == "y":
                order_inputs()
            if continue_ordering == "f":
                print("Your order is being processed...")
                process_order(NEW_ORDER)

        if ORDER_ITEM == "c1": # CHILD 1 DAY ACCESS
            try:
                child_one_day = int(input("\nHow many 'Child 1 Day Access' do you want to order? - Type a number from 1 - 30\n"))
                
                if child_one_day < 0 or child_one_day > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f"You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.")
                return False
            
            NEW_ORDER['child_one_day'] = child_one_day
            print(f"\nSuccessfully added to your cart: {child_one_day} ticket(s) of 'Child 1 Day Access'")
            
            print(NEW_ORDER)
            continue_ordering = input("\nDo you want to order more tickets? - Type Y (YES), or F (FINISH ORDER):\n").lower()
            if continue_ordering == "y":
                order_inputs()
            if continue_ordering == "f":
                print("Your order is being processed...")
                process_order(NEW_ORDER)

        if ORDER_ITEM == "cf": # CHILD FULL ACCESS
            try:
                child_full_event = int(input("\nHow many 'Child Full Event Access' do you want to order? - Type a number from 1 - 30\n"))
                
                if child_full_event < 0 or child_full_event > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f"You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.")
                return False
            
            NEW_ORDER['child_full_event'] = child_full_event
            print(f"\nSuccessfully added to your cart: {child_full_event} ticket(s) of 'Child Full Event Access'")

            print(NEW_ORDER)
            continue_ordering = input("\nDo you want to order more tickets? - Type Y (YES), or F (FINISH ORDER):\n").lower()
            if continue_ordering == "y":
                order_inputs()
            if continue_ordering == "f":
                print("Your order is being processed...")
                process_order(NEW_ORDER)

        if ORDER_ITEM == "fp": # FULL PACK
            try:
                fest_pack = int(input("\nHow many 'Fest Pack' do you want to order? - Type a number from 1 - 30\n"))
                
                if fest_pack < 0 or fest_pack > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f"You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.")
                return False
            
            NEW_ORDER['fest_pack'] = fest_pack
            print(f"\nSuccessfully added to your cart: {fest_pack} ticket(s) of 'Fest Pack'")
            print(NEW_ORDER)
            continue_ordering = input("\nDo you want to order more tickets? - Type Y (YES), or F (FINISH ORDER):\n").lower()
            if continue_ordering == "y":
                order_inputs()
            if continue_ordering == "f":
                print("Your order is being processed...")
                process_order(NEW_ORDER)

        if ORDER_ITEM == "b1": # BACKSTAGE 1 DAY ACCESS
            try:
                backstage_day_bonus = int(input("\nHow many 'Backstage 1 Day Bonus' do you want to order? - Type a number from 1 - 30\n"))
                
                if backstage_day_bonus < 0 or backstage_day_bonus > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f"You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.")
                return False
            
            NEW_ORDER['backstage_day_bonus'] = backstage_day_bonus
            print(f"\nSuccessfully added to your cart: {backstage_day_bonus} ticket(s) of 'Fest Pack'")
            print(NEW_ORDER)
            continue_ordering = input("\nDo you want to order more tickets? - Type Y (YES), or F (FINISH ORDER):\n").lower()
            if continue_ordering == "y":
                order_inputs()
            if continue_ordering == "f":
                print("Your order is being processed...")
                process_order(NEW_ORDER)

        if ORDER_ITEM == "bf": # BACKSTAGE FULL ACCESS
            try:
                backstage_full_bonus = int(input("\nHow many 'Backstage Full Bonus' do you want to order? - Type a number from 1 - 30\n"))
                
                if backstage_full_bonus < 0 or backstage_full_bonus > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f"You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.")
                return False
            
            NEW_ORDER['backstage_full_bonus'] = backstage_full_bonus
            print(f"\nSuccessfully added to your cart: {backstage_full_bonus} ticket(s) of 'Fest Pack'")
            print(NEW_ORDER)
            continue_ordering = input("\nDo you want to order more tickets? - Type Y (YES), or F (FINISH ORDER):\n").lower()
            if continue_ordering == "y":
                order_inputs()
            if continue_ordering == "f":
                print("Your order is being processed...")
                process_order(NEW_ORDER)
       
        # if ORDER_ITEM == "e":
        #     main()
        # if ORDER_ITEM == "p":
        #     process_order()
            return True
        if ORDER_ITEM != "a1" or ORDER_ITEM !="af" or ORDER_ITEM !="c1" or ORDER_ITEM !="cf" or ORDER_ITEM !="fp" or ORDER_ITEM !="b1" or ORDER_ITEM !="bf" or continue_ordering != "y" or continue_ordering != "f":
            raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                f"You must type a correct KEY"
            )


    except ValueError as e:
        print(f"\nInvalid data: {e}, please try again.")
        order_inputs()
            
    return NEW_ORDER



def process_order(order):

    invoice = order.get('invoice_num')   
    print(f"Your order {invoice} is being generated...")
    
    return True


def order():
    order = input("Press Y if you want to order some tickets, or C to cancel:\n").lower()
    items = pricing_worksheet.col_values(2)[0:]
    item_keys = pricing_worksheet.col_values(4)[0:]
    
    
    if order == "y":
        print("\nProceeding ...\n")

        invoice = sales_worksheet.col_values(1)[-1] #takes last invoice_num from sales_worksheet e.g.: INV-1000
        invoice_letters = invoice.split("-")[0] #takes innitial letter of last invoice_num before the '-' e.g: INV
        invoice_num = invoice.split("-")[1] #takes numbers of last invoice_num after the '-' and returns string e.g.: '1000'
        invoice_num = int(invoice_num) + 1 #turns num string int integer, and adds 1 to invoice_num e.g.: 1001
        invoice_num = f"{invoice_letters}-{invoice_num}" #creates new invoice_num with same format (letters-nums) e.g. INV-1001
        #print(invoice_num)
        NEW_ORDER['invoice_num'] = invoice_num

        date = datetime.today().strftime('%Y-%m-%d')
        NEW_ORDER['invoice_date'] = date

        dict_item_keys = dict(zip(item_keys, items)) #creates dict merging each i from both lists
        
        for key, item in dict_item_keys.items(): #formats output of dict of KEY and ITEMS
            print(f'{key:4} : {item}')
            print('-' * 30) #adds ------- after each KEY : ITEM of the dict
        
        
    elif order != "y":
        main()
    
    order_inputs()
    return NEW_ORDER
    
    

def main():
    """
    Run all program functions
    """
    print("\n\n WELCOME TO\n")
    print(logo)
    print('\n{:^50}'.format('BUY YOUR TICKETS!\n'))
    display_pricing_list()   
    extra_info()
    order()
    # process_order()

main()