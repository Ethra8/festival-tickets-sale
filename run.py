import pyfiglet 
import gspread #library first downloaded through terminal : pip3 install gspread google-auth
from google.oauth2.service_account import Credentials #imports just specific Credentials function from library, no need to import complete library
from pprint import pprint # --> must not be deployed. but very handy when coding and testing
from datetime import datetime
import math

import smtplib

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

settings_worksheet = SHEET.worksheet('settings')
pricing_worksheet = SHEET.worksheet('pricing')
extra_info_worksheet = SHEET.worksheet('extra_info')
sales_worksheet = SHEET.worksheet('sales')
stock_worksheet = SHEET.worksheet('stock')


item_sales_new_order = sales_worksheet.row_values(1) #gets key values to create NEW_ORDER dict
values_sales_new_order = sales_worksheet.row_values(3) #gets mock values for each key to create NEW_ORDER dict

item_type = pricing_worksheet.col_values(1)[0]
code = pricing_worksheet.col_values(4)[0]
code_example = pricing_worksheet.col_values(4)[1]


# dict NEW_ORDER takes user inputs all along the app to create final invoice, also including total amount 
NEW_ORDER = dict(zip(item_sales_new_order, values_sales_new_order))
DATE = datetime.today().strftime('%Y-%m-%d')
TIME = datetime.today().strftime('%H:%M')
print(TIME)


logo_name = settings_worksheet.col_values(1)[1]
logo_font = settings_worksheet.col_values(2)[1]

#takes welcome message before and after logo from settings worksheet 
welcome_msg_before_logo = settings_worksheet.col_values(3)[1]
welcome_msg_after_logo = settings_worksheet.col_values(4)[1]

#Create vars for every item in pricing worksheet (item_code) and user-friendly readable item name 
item1_human = pricing_worksheet.col_values(2)[1]
item1_code = pricing_worksheet.col_values(4)[1]
item1_qty = 0

item2_human = pricing_worksheet.col_values(2)[2]
item2_code = pricing_worksheet.col_values(4)[2]
item2_qty = 0

item3_human = pricing_worksheet.col_values(2)[3]
item3_code = pricing_worksheet.col_values(4)[3]
item3_qty = 0

item4_human = pricing_worksheet.col_values(2)[4]
item4_code = pricing_worksheet.col_values(4)[4]
item4_qty = 0

item5_human = pricing_worksheet.col_values(2)[5]
item5_code = pricing_worksheet.col_values(4)[5]
item5_qty = 0

item6_human = pricing_worksheet.col_values(2)[6]
item6_code = pricing_worksheet.col_values(4)[6]
item6_qty = 0

item7_human = pricing_worksheet.col_values(2)[7]
item7_code = pricing_worksheet.col_values(4)[7]
item7_qty = 0

item8_human = pricing_worksheet.col_values(2)[8]
item8_code = pricing_worksheet.col_values(4)[8]
item8_qty = 0

item9_human = pricing_worksheet.col_values(2)[9]
item9_code = pricing_worksheet.col_values(4)[9]
item9_qty = 0

item10_human = pricing_worksheet.col_values(2)[10]
item10_code = pricing_worksheet.col_values(4)[10]
item10_qty = 0

item11_human = pricing_worksheet.col_values(2)[11]
item11_code = pricing_worksheet.col_values(4)[11]
item11_qty = 0

item12_human = pricing_worksheet.col_values(2)[12]
item12_code = pricing_worksheet.col_values(4)[12]
item12_qty = 0

item13_human = pricing_worksheet.col_values(2)[13]
item13_code = pricing_worksheet.col_values(4)[13]
item13_qty = 0


def logo():
    """
    Prints brand name (logo_name) introduced by organizer
    in settings_worksheet worksheet, to be set as the logo
    in the console welcome message
    """
    logo = pyfiglet.figlet_format(logo_name, logo_font) # pyfiglet method to create Festival Name as Logo, then printed in welcome message in main()

    print(logo)


def welcome():
    print(f"\n\n {welcome_msg_before_logo}\n")
    logo()
    print('\n{:^50}'.format(f'{welcome_msg_after_logo}'))
    go_to_pricing_list = input("\n\n Press ANY KEY to access\n").lower()

    if go_to_pricing_list:
        return True
    return False



def print_inventory(dct):
    """
    Returns printed PRICING LIST (dct) formated as 1 row for each entry,
    removes '[]' and ',' by: {item} {amount} €, also aligning amounts
    e.g.: Adult 1 Day Access  75 €
          Child Full Access   90 €
    """
    print("\n PRICING:\n")
    for item, amount in dct.items(): 
        print(f' {item:30}{amount} €')
    
    

def pricing_list():
    """
    Returns dict of item_names and ticket_prices
    taken from 'pricing' worksheet
    """
    item_names = pricing_worksheet.col_values(2)[1:] #retrieves 1st column, from 2nd row onwards (eludes 1st row) and creates list of strings
    ticket_prices = pricing_worksheet.col_values(3)[1:] #retrieves 3rd column, from 2nd row onwards (eludes 1st row) and creates list of strings
    
    price_per_ticket = dict(zip(item_names, ticket_prices))

    return price_per_ticket


pricing = pricing_list() # dict of item_names & ticket_prices, returned by pricing_list()


def exit_app():
    """
    Brings user to final question before exit point and goodbye message, giving last chance to continue before order is lost.
    If user decides to continue, Pricing list is printed, and sale continues.
    """
    exit_confirmation = input("\n Are you sure you want to exit program? In case you have a pending order, it will get lost.\n\nType E (EXIT) to close program, or any other key to continue with your order:\n").lower()
    
    if exit_confirmation == "e":
        print(f"\n Maybe see you some other time, have a lovely day!\n\n{logo()}\n\n(c) {logo_name} 2023\n\n\n")
    if exit_confirmation != "e":
        print_inventory(pricing)



def extra_info():
    """
    Returns printed list of extra info per item taken from 'extra_info' worksheet,
    formated to be human-friendly.
    """
    extra_info_message = settings_worksheet.col_values(5)[1]
    print(f"\n {extra_info_message}:\n")
    
    full_info = extra_info_worksheet.get_all_values()[1:] #creates list of lists, starting at row 2 (one list per row)
    for i in full_info: # prints each row formated as follows
        print(f" {i[1]} --> Includes: {i[2]}, {i[3]}, {i[4]}")
    print("\n")
    


def continue_ordering():
    """
    Prompt user to continue order, to finalize or to exit app
    """
    continue_ordering = input("\n Type any key to continue ordering, P to view PRICING LIST, or F to FINALIZE ORDER:\n").lower()

    if continue_ordering == "f":
        print(" Your order is being processed...")
        process_order(NEW_ORDER)
        return False
    if continue_ordering == "p":
        print_inventory(pricing)
        return False
    if continue_ordering != "p" or continue_ordering != "f":
        list_keyword_item()
        return True



def order_inputs():
    """
    User inputs items (ORDER_ITEM), and number of tickets to be included in order (NEW_ORDER).
    Gives ValueError if user introduces a number>30 or other than an integer.
    User can also return to welcome message, or exit app at any stage to cancel order.
    Returns NEW_ORDER
    """
    ORDER_ITEM = input(f"\n Type {code} (e.g.:{code_example}) of {item_type} you want to include to your order,\n Type P to view (PRICING LIST), or E to (EXIT):\n").lower()  
   
    try:
        if ORDER_ITEM == "e":
            exit_app()
            return False
        if ORDER_ITEM == "p":
            print_inventory(pricing)
            return False
        
        if ORDER_ITEM == item1_code or ORDER_ITEM == item1_code.lower(): # 1st item in pricing worksheet
            try:
                item1_qty = int(input(f"\nHow many '{item1_human}' do you want to order? - Type a number from 1 - 30\n"))
                
                if item1_qty < 1 or item1_qty > 30:
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f" Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER[f'item1'] = item1_qty

            print(f"\n Successfully added to your cart: {item1_qty} '{item1_human}'")
            continue_ordering()
            return False

        if ORDER_ITEM == item2_code or ORDER_ITEM == item2_code.lower(): # 2nd item in pricing worksheet
            try:
                item2_qty = int(input(f"\nHow many '{item2_human}' do you want to order? - Type a number from 1 - 30\n"))
                
                if item2_qty < 1 or item2_qty > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f" Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['item2'] = item2_qty
            print(f"\n Successfully added to your cart: {item2_qty} '{item2_human}'")
            continue_ordering()
            return False

        if ORDER_ITEM == item3_code or ORDER_ITEM == item3_code.lower(): # 3rd item in pricing worksheet
            try:
                item3_qty = int(input(f"\n How many '{item3_human}' do you want to order? - Type a number from 1 - 30\n"))
                
                if item3_qty < 1 or item3_qty > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f" Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['item3'] = item3_qty
            print(f"\n Successfully added to your cart: {item3_qty} '{item3_human}'")
            continue_ordering()
            return False

        if ORDER_ITEM == item4_code or ORDER_ITEM == item4_code.lower(): # 4th item in pricing worksheet
            try:
                item4_qty = int(input(f"\n How many '{item4_human}' do you want to order? - Type a number from 1 - 30\n"))
                
                if item4_qty < 1 or item4_qty > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f" Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['item4'] = item4_qty
            print(f"\n Successfully added to your cart: {item4_qty} '{item4_human}'")
            continue_ordering()
            return False

        if ORDER_ITEM == item5_code or ORDER_ITEM == item5_code.lower(): # 5th item in pricing worksheet
            try:
                item5_qty = int(input(f"\n How many '{item5_human}' do you want to order? - Type a number from 1 - 30\n"))
                
                if item5_qty < 1 or item5_qty > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f" Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['item5'] = item5_qty
            print(f"\n Successfully added to your cart: {item5_qty} '{item5_human}'")
            continue_ordering()
            return False

        if ORDER_ITEM == item6_code or ORDER_ITEM == item6_code.lower(): # 6th item in pricing worksheet
            try:
                item6_qty = int(input(f"\n How many '{item6_human}' do you want to order? - Type a number from 1 - 30\n"))
                
                if item6_qty < 1 or item6_qty > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f" Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['item6'] = item6_qty
            print(f"\n Successfully added to your cart: {item6_qty} '{item6_human}'")
            continue_ordering()
            return False

        if ORDER_ITEM == item7_code or ORDER_ITEM == item7_code.lower(): # 7th item in pricing worksheet
            try:
                item7_qty = int(input(f"\n How many '{item7_human}' do you want to order? - Type a number from 1 - 30\n"))
                
                if item7_qty < 1 or item7_qty > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f" Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['item7'] = item7_qty
            print(f"\n Successfully added to your cart: {item7_qty} '{item7_human}'")
            continue_ordering()
            return False

        if ORDER_ITEM == item8_code or ORDER_ITEM == item8_code.lower(): # 8th item in pricing worksheet
            try:
                item8_qty = int(input(f"\n How many '{item8_human}' do you want to order? - Type a number from 1 - 30\n"))
                
                if item8_qty < 1 or item8_qty > 30:
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f" Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['item8'] = item8_qty

            print(f"\n Successfully added to your cart: {item8_qty} '{item8_human}'")
            continue_ordering()
            return False

        if ORDER_ITEM == item9_code or ORDER_ITEM == item9_code.lower(): # 9th item in pricing worksheet
            try:
                item9_qty = int(input(f"\n How many '{item9_human}' do you want to order? - Type a number from 1 - 30\n"))
                
                if item9_qty < 1 or item9_qty > 30:
                    raise ValueError( # ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f" Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['item9'] = item9_qty

            print(f"\n Successfully added to your cart: {item9_qty} '{item9_human}'")
            continue_ordering()
            return False

        if ORDER_ITEM == item10_code or ORDER_ITEM == item10_code.lower(): # 10th item in pricing worksheet
            try:
                item10_qty = int(input(f"\n How many '{item10_human}' do you want to order? - Type a number from 1 - 30\n"))
                
                if item10_qty < 1 or item10_qty > 30:
                    raise ValueError( # ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f" Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['item10'] = item10_qty

            print(f"\n Successfully added to your cart: {item10_qty} '{item10_human}'")
            continue_ordering()
            return False

        if ORDER_ITEM == item11_code or ORDER_ITEM == item11_code.lower(): # 1st item in pricing worksheet
            try:
                item11_qty = int(input(f"\nHow many '{item11_human}' do you want to order? - Type a number from 1 - 30\n"))
                
                if item11_qty < 1 or item11_qty > 30:
                    raise ValueError( # ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f" Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['item11'] = item11_qty

            print(f"\n Successfully added to your cart: {item11_qty} '{item11_human}'")
            continue_ordering()
            return False

        if ORDER_ITEM == item12_code or ORDER_ITEM == item12_code.lower(): # 1st item in pricing worksheet
            try:
                item12_qty = int(input(f"\nHow many '{item12_human}' do you want to order? - Type a number from 1 - 30\n"))
                
                if item12_qty < 1 or item12_qty > 30:
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f" Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['item12'] = item12_qty

            print(f"\n Successfully added to your cart: {item12_qty} '{item12_human}'")
            continue_ordering()
            return False

        if ORDER_ITEM == item13_code or ORDER_ITEM == item13_code.lower(): # 1st item in pricing worksheet
            try:
                item13_qty = int(input(f"\nHow many '{item13_human}' do you want to order? - Type a number from 1 - 30\n"))
                
                if item13_qty < 1 or item13_qty > 30:
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f" Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['item13'] = item13_qty

            print(f"\n Successfully added to your cart: {item13_qty} '{item13_human}'")
            continue_ordering()
            return False

        
        if ORDER_ITEM != item1_code or ORDER_ITEM !=item2_code or ORDER_ITEM !=item3_code or ORDER_ITEM !=item4_code or ORDER_ITEM !=item5_code or ORDER_ITEM !=item6_code or ORDER_ITEM !=item7_code or ORDER_ITEM !=item8_code or ORDER_ITEM !=item9_code or ORDER_ITEM !=item10_code or ORDER_ITEM !=item11_code or ORDER_ITEM !=item12_code or ORDER_ITEM !=item13_code:
            raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                f" You must type a correct {code} (e.g.:{code_example})."
            )

        if ORDER_ITEM == "e":
            exit_app()
            return False
        
        if ORDER_ITEM == "p":
            print_inventory(pricing)
            return False
    
    except ValueError as e:
        print(f"\n Invalid data: {e}, please try again.")
        order_inputs()
            
    return True



def send_email_to_user():
    """
    Connects to smtp to send email to user
    """
    sender = "sell.tickets.app@gmail.com"
    user_name = NEW_ORDER.get('user_name')
    user_email = NEW_ORDER.get('user_email')
    
    message = f"""From: From Edna <{sender}>
    To: {user_name}, <{user_email}>
    Subject: SMTP test email
    
    This is a test email message!
    """

    sender = "sell.tickets.app@gmail.com"
    gmail_app_password = "hjamkshirdxecddq"
    receiver = user_email
    
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender, gmail_app_password)
        server.ehlo()
        server.sendmail(sender, receiver, message)
        server.close()
        print("\n Email sent.\n")
        logo()
        print(f'\n(c) {logo_name} 2023\n\n\n')
        
    except Exception as exception:
        print("Error: %s!\n\n % Exception")
    
    calculate_stock(NEW_ORDER, 'stock')



def process_order(order):
    """
    Generates value list (order_values) from NEW_ORDER dict,
    calculates the order's final amount
    by multiplying each item cost taken from pricing worksheet, per number of items in order_values.
    It appends final amount to NEW_ORDER and prints invoice to user.
    Then user is given the option to confirm order, return to ordering, or exit app.
    If user confirms order, invoice full data is exported to sales worksheet.
    """

    invoice = order.get('invoice_no')   
    print(f"\n Your order {invoice} is being generated...")

    order_item_names = sales_worksheet.row_values(2) # takes list of items out of sales worksheet, in a user-friendly version

    user_email = input("\n Please, include your email so we can send your pending invoice as a pdf file, together with the payment link\n").strip() # strip() method erases extra spaces before/after input data
    NEW_ORDER['user_email'] = user_email # includes user_email input value to user_email key in dict NEW_ORDER
    
    user_name = input("\n Please, type in a user name to create your invoice\n").strip().title() # title() method capitalizes every word in input string
    NEW_ORDER['user_name'] = user_name

    print(f"\n Hold on {user_name}, the total amount is being calculated...\n")

    order_values = [] # creates list from values out of NEW_ORDER dict
    
    for x in order.values(): # takes only values from dict NEW_ORDER, and appends to new list order_values
        order_values.append(x)

    item_prices = pricing_worksheet.col_values(3)[1:] #list of strings of each item price from pricing worksheet
    
    item_prices_float_list = [] #new list of floats made from list of strings item_prices

    for i in item_prices:   # converts item_prices to list of floats item_prices_float_list
        item_prices_float_list.append(float(i))

    number_of_items_in_order_float = [] #new list of floats made from list of strings number_of_items_in_order
    
    number_of_items_in_order = order_values[4:] # takes number of items selected in the order, eluding user and invoice data until col4
    
    for i in number_of_items_in_order:   # loop iterates through number_of_items_in_order and converts values in strings to floats, include each float to  new list number_of_items_in_order_float
        number_of_items_in_order_float.append(float(i))

    res_list = [item_prices_float_list[i] * number_of_items_in_order_float[i] for i in range(len(item_prices_float_list))] # multiplies number of items in the order with price of item

    total_amount= sum(res_list) # sums all subtotals of items ordered, calculates total_amount to be paid
    
    total_amount = round(total_amount, 2) # rounds total_amount to floor, and only 2 decimals

    order_values.pop() # takes out default 0 value for total_amount in NEW_ORDER dict, where values have been retrieved previously
    
    order_values.append(str(total_amount)) # appends to the order values the total_amount

    final_order = dict(zip(order_item_names,order_values))  # creates new dict for final_order, with item as keys, and num. of items as values. Includes final amount key:value

    print(f" Dear {user_name},\n\n Please review your present order before it is processed and sent to your email for due payment:\n\n")
    
    for item, value in final_order.items():  # only prints items which value is not 0
        if value != '0': 
            print(f' {item:10} : {value}')
    
    user_order_confirmation = input("\n Press any key to CONFIRM ORDER, C to (CONTINUE ORDERING), or E to (EXIT) ").lower()

    if user_order_confirmation == "c":
        list_keyword_item()

    if user_order_confirmation == "e":
        exit_app()

    if user_order_confirmation != "c" or user_order_confirmation != "e":
        sales_worksheet.append_row(order_values)
        print(f"\n Your order has successfully been processed!\n\n You will automatically receive an email with your pdf invoice to be paid in the following 2 business days.\n\n WARNING: Your order will be cancelled if your fail to proceed to payment after 24 hours.\n\n Thank you!")
        send_email_to_user()
        return True
    

    
def list_keyword_item():
    """
    Print list of items and codes, and runs order_inputs()
    """

    print(f"\n Each {item_type} has a {code} associated in the system:\n")
    items = pricing_worksheet.col_values(2)[0:]
    item_keys = pricing_worksheet.col_values(4)[0:]

    dict_item_keys = dict(zip(item_keys, items)) #creates dict merging each i from both lists
    
    for key, item in dict_item_keys.items(): #formats output of dict of KEY and ITEMS
        print(f' {key:8} : {item}')
        print('-' * 30) #adds ------- after each KEY : ITEM of the dict

    order_inputs()
       
    

def generate_order():
    """
    Prompts user to start ordering, to return to welcome message, or to exit.
    """
    order = input(" Press any key to order, type R (RETURN), or type E (EXIT):\n").lower()

    if order == "e":
        exit_app()
        return False
    if order == "r":
        main()
        return False
   
    if order != "e" or order != "r":
        print("\n Proceeding ...")

        invoice = sales_worksheet.col_values(1)[-1] #takes last invoice_no from sales_worksheet e.g.: INV-10000
        invoice_letters = invoice.split("-")[0] #takes innitial letter of last invoice_no before the '-' e.g: INV
        invoice_no = invoice.split("-")[1] #takes numbers of last invoice_no after the '-' and returns string e.g.: '1000'
        invoice_no = int(invoice_no) + 1 #turns num string int integer, and adds 1 to invoice_no e.g.: 1001
        invoice_no = f"{invoice_letters}-{invoice_no}" #creates new invoice_no with same format (letters-nums) e.g. INV-1001
        #print(invoice_no)
        NEW_ORDER['invoice_no'] = invoice_no
        NEW_ORDER['order_date'] = DATE

        return NEW_ORDER


def calculate_stock(data, worksheet):
    """
    Update stock worksheet, add new row with result of sustracting the items in invoice to each item remaining stock.
    """
    order_values = [] # creates list from values out of NEW_ORDER dict
    
    for x in data.values(): # takes only values from dict NEW_ORDER, and appends to new list order_values
        order_values.append(x)
    
    stock_to_sustract = order_values[4:] # keep only qty of items in invoice - erases user data and invoice details
    
    stock_to_sustract_int = [] #creates new list of integers

    for z in stock_to_sustract: #creates new list of integers: stock_to_sustract_int from number of each item in order
        stock_to_sustract_int.append(int(z))

    stock_to_sustract_int.pop() # erases last item in list = total amount

    existing_stock = stock_worksheet.get_values()[-1] #gets values in last row of stock worksheet
    
    existing_stock_int = [] #creates new list of integers
    
    for y in existing_stock: #creates new list of integers: existing_stock_int from number of each item in stock
        existing_stock_int.append(int(y))
    
    new_stock = [existing_stock_int[i] - stock_to_sustract_int[i] for i in range(len(existing_stock_int))] # sustracts number of each item type in order from number of each item type in stock
    
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(new_stock) #includes each item's remaining stock to 1st empty row in stock worksheet


    
def main():
    """
    Run all program functions
    """
    welcome()
    print_inventory(pricing)
    extra_info()
    generate_order()
    list_keyword_item()


main()



