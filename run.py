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

settings_worksheet = SHEET.worksheet('settings')
pricing_worksheet = SHEET.worksheet('pricing')
extra_info_worksheet = SHEET.worksheet('extra_info')
sales_worksheet = SHEET.worksheet('sales')


item_sales_new_order = sales_worksheet.row_values(1) #gets key values to create NEW_ORDER dict
values_sales_new_order = sales_worksheet.row_values(2) #gets mock values for each key to create NEW_ORDER dict

ticket_type = pricing_worksheet.col_values(1)[0]
code = pricing_worksheet.col_values(4)[0]
code_example = pricing_worksheet.col_values(4)[1]


# dict NEW_ORDER takes user inputs all along the app to create final invoice, also including total amount 
NEW_ORDER = dict(zip(item_sales_new_order, values_sales_new_order))
DATE = datetime.today().strftime('%Y-%m-%d')
TIME = datetime.today().strftime('%H:%M')
print(TIME)

festival_name = settings_worksheet.col_values(1)[1]
logo_font = settings_worksheet.col_values(2)[1]

welcome_msg_before_logo = settings_worksheet.col_values(3)[1]
welcome_msg_after_logo = settings_worksheet.col_values(4)[1]



def logo():
    """
    Prints brand name (logo_name) introduced by organizer
    in settings_worksheet worksheet, to be set as the logo
    in the console welcome message
    """
    logo = pyfiglet.figlet_format(festival_name, logo_font) # pyfiglet method to create Festival Name as Logo, then printed in welcome message in main()

    print(logo)



def print_inventory(dct):
    """
    Returns printed PRICING LIST (dct) formated as 1 row for each entry,
    removes '[]' and ',' by: {item} {amount} €, also aligning amounts
    e.g.: Adult 1 Day Access  75 €
          Child Full Access   90 €
    """
    print("\nPRICING:\n")
    for item, amount in dct.items(): 
        print(f'{item:25}{amount} €')
    
    extra_info()
    

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


def exit_app():
    """
    Brings user to final question before exit point and goodbye message, giving last chance to continue before order is lost.
    If user decides to continue, Pricing list is printed, and sale continues.
    """
    exit_confirmation = input("\n Are you sure you want to exit program? In case you have a pending order, it will get lost.\n\nType E (EXIT) to close program, or any other key to continue with your order:\n").lower()
    
    if exit_confirmation == "e":
        print(f"\n Maybe see you some other time, have a lovely day!\n\n{logo()}\n\n(c) {festival_name} 2023\n\n\n")
    if exit_confirmation != "e":
        print_inventory(pricing)



def extra_info():
    """
    Returns printed list of extra info per item taken from 'extra_info' worksheet,
    formated to be human-friendly.
    """
    extra_info_message = settings_worksheet.col_values(5)[1]
    print(f"\n{extra_info_message}\n")
    
    full_info = extra_info_worksheet.get_all_values()[1:] #creates list of lists, starting at row 2 (one list per row)
    for i in full_info: # prints each row formated as follows
        print(f"{i[1]} --> Includes: {i[2]}, {i[3]}, {i[4]}")
    print("\n")
    order()



def order_inputs():
    """
    User inputs items (ORDER_ITEM), and number of tickets to be included in order (NEW_ORDER).
    Gives ValueError if user introduces a number>30 or other than an integer.
    User can also return to welcome message, or exit app at any stage to cancel order.
    Returns NEW_ORDER
    """
    ORDER_ITEM = input(f"\n Type {code} (e.g.:{code_example}) of {ticket_type} you want to include to your order,\n Type P to view (PRICING LIST), or E to (EXIT):\n").lower()
    try:
        if ORDER_ITEM == "e":
            exit_app()
            return False
        if ORDER_ITEM == "p":
            print_inventory(pricing)
            return False
        if ORDER_ITEM == "a1": # ADULT 1 DAY ACCESS
            try:
                adult_one_day = int(input("\nHow many 'Adult 1 Day Access' do you want to order? - Type a number from 1 - 30\n"))
                
                if adult_one_day < 0 or adult_one_day > 30:
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f"You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['adult_one_day'] = adult_one_day

            print(f"\nSuccessfully added to your cart: {adult_one_day} ticket(s) of 'Adult 1 Day Access'")
            print(NEW_ORDER)
            
            continue_ordering = input("\nType any key to order more tickets, P to view PRICING LIST, or F to FINISH ORDER:\n").lower()

            if continue_ordering == "f":
                print("Your order is being processed...")
                process_order(NEW_ORDER)
                return False
            if continue_ordering == "p":
                print_inventory(pricing)
                return False
            if continue_ordering != "p" or continue_ordering != "f":
                list_keyword_item()
                # return True

        if ORDER_ITEM == "af": # ADULT FULL ACCESS
            try:
                adult_full_event = int(input("\nHow many 'Adult Full Event Access' do you want to order? - Type a number from 1 - 30\n"))
                
                if adult_full_event < 0 or adult_full_event > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f"You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['adult_full_event'] = adult_full_event
            print(f"\nSuccessfully added to your cart: {adult_full_event} ticket(s) of 'Adult Full Event Access'")
            print(NEW_ORDER)

            continue_ordering = input("\nType any key to order more tickets, P to view PRICING LIST, or F to FINISH ORDER:\n").lower()

            if continue_ordering == "f":
                print("Your order is being processed...")
                process_order(NEW_ORDER)
                return False
            if continue_ordering == "p":
                print_inventory(pricing)
                return False
            if continue_ordering != "p" or continue_ordering != "f":
                list_keyword_item()
                # return True

        if ORDER_ITEM == "c1": # CHILD 1 DAY ACCESS
            try:
                child_one_day = int(input("\nHow many 'Child 1 Day Access' do you want to order? - Type a number from 1 - 30\n"))
                
                if child_one_day < 0 or child_one_day > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f"You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['child_one_day'] = child_one_day
            print(f"\nSuccessfully added to your cart: {child_one_day} ticket(s) of 'Child 1 Day Access'")
            
            print(NEW_ORDER)
            continue_ordering = input("\nType any key to order more tickets, P to view PRICING LIST, or F to FINISH ORDER:\n").lower()

            if continue_ordering == "f":
                print("Your order is being processed...")
                process_order(NEW_ORDER)
                return False
            if continue_ordering == "p":
                print_inventory(pricing)
                return False
            if continue_ordering != "p" or continue_ordering != "f":
                list_keyword_item()
                # return True

        if ORDER_ITEM == "cf": # CHILD FULL ACCESS
            try:
                child_full_event = int(input("\nHow many 'Child Full Event Access' do you want to order? - Type a number from 1 - 30\n"))
                
                if child_full_event < 0 or child_full_event > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f"You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['child_full_event'] = child_full_event
            print(f"\nSuccessfully added to your cart: {child_full_event} ticket(s) of 'Child Full Event Access'")

            print(NEW_ORDER)
            continue_ordering = input("\nType any key to order more tickets, P to view PRICING LIST, or F to FINISH ORDER:\n").lower()

            if continue_ordering == "f":
                print("Your order is being processed...")
                process_order(NEW_ORDER)
                return False
            if continue_ordering == "p":
                print_inventory(pricing)
                return False
            if continue_ordering != "p" or continue_ordering != "f":
                list_keyword_item()
                # return True

        if ORDER_ITEM == "fp": # FULL PACK
            try:
                fest_pack = int(input("\nHow many 'Fest Pack' do you want to order? - Type a number from 1 - 30\n"))
                
                if fest_pack < 0 or fest_pack > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f"You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['fest_pack'] = fest_pack
            print(f"\nSuccessfully added to your cart: {fest_pack} ticket(s) of 'Fest Pack'")
            print(NEW_ORDER)
            continue_ordering = input("\nType any key to order more tickets, P to view PRICING LIST, or F to FINISH ORDER:\n").lower()

            if continue_ordering == "f":
                print("Your order is being processed...")
                process_order(NEW_ORDER)
                return False
            if continue_ordering == "p":
                print_inventory(pricing)
                return False
            if continue_ordering != "p" or continue_ordering != "f":
                list_keyword_item()
                # return True

        if ORDER_ITEM == "b1": # BACKSTAGE 1 DAY ACCESS
            try:
                backstage_day_bonus = int(input("\nHow many 'Backstage 1 Day Bonus' do you want to order? - Type a number from 1 - 30\n"))
                
                if backstage_day_bonus < 0 or backstage_day_bonus > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f"You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['backstage_day_bonus'] = backstage_day_bonus
            print(f"\n Successfully added to your cart: {backstage_day_bonus} ticket(s) of 'Fest Pack'")
            print(NEW_ORDER)
            continue_ordering = input("\n Type any key to order more items, P to view (PRICING LIST), or F to (FINALIZE ORDER):\n").lower()

            if continue_ordering == "f":
                print(" Your order is being processed...")
                process_order(NEW_ORDER)
                return False
            if continue_ordering == "p":
                print_inventory(pricing)
                return False
            if continue_ordering != "p" or continue_ordering != "f":
                list_keyword_item()
                # return True

        if ORDER_ITEM == "bf": # BACKSTAGE FULL ACCESS
            try:
                backstage_full_bonus = int(input("\n How many 'Backstage Full Bonus' do you want to order? - Type a number from 1 - 30\n"))
                
                if backstage_full_bonus < 0 or backstage_full_bonus > 30 :
                    raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                    f"You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print(f" Invalid data: {e}, please try again.")
                order_inputs()
            
            NEW_ORDER['backstage_full_bonus'] = backstage_full_bonus
            print(f"\n Successfully added to your cart: {backstage_full_bonus} ticket(s) of 'Fest Pack'")
            print(NEW_ORDER)
            continue_ordering = input("\n Type any key to order more tickets, P to view PRICING LIST, or F to FINISH ORDER:\n").lower()

            if continue_ordering == "f":
                print(" Your order is being processed...")
                process_order(NEW_ORDER)
                return False
            if continue_ordering == "p":
                print_inventory(pricing)
                return False
            if continue_ordering != "p" or continue_ordering != "f":
                list_keyword_item()
                # return True
        
        if ORDER_ITEM != "a1" or ORDER_ITEM !="af" or ORDER_ITEM !="c1" or ORDER_ITEM !="cf" or ORDER_ITEM !="fp" or ORDER_ITEM !="b1" or ORDER_ITEM !="bf" or ORDER_ITEM != "p" or ORDER_ITEM != "f" or continue_ordering != "f" or continue_ordering != "p":
            raise ValueError( #ValueError is renamed as e in except, and goes in the {e} in final message
                f" You must type a correct KEYWORD"
            )

        if ORDER_ITEM == "e":
            exit_app()
        
        if ORDER_ITEM == "p":
            print_inventory(pricing)
    
    except ValueError as e:
        print(f"\n Invalid data: {e}, please try again.")
        order_inputs()
            
    # return NEW_ORDER


def confirm_order():
    print("\n Your order has successfully been processed!\n\n You will shortly receive an email with your pdf invoice to be paid in the following 2 business days.\n\n WARNING: Your order will be cancelled if your fail to proceed to payment after 24 hours.\n\n\n Thank you!")


def process_order(order):
    """
    Generates value list (order_values) from NEW_ORDER dict, calculates final amount
    by multiplying each item cost taken from pricing worksheet, per number of items in order_values,
    appends final amount to NEW_ORDER, exports full data list to sales worksheet, and print invoice to user.
    """

    invoice = order.get('invoice_num')   
    print(f"\n Your order {invoice} is being generated...")

    user_email = input("\n Please, include your email so we can send your pending invoice as pdf, including the payment link\n").strip() # strip() method erases extra spaces before/after input data
    NEW_ORDER['user_email'] = user_email #includes user_email input value to user_email key in dict NEW_ORDER

    user_name = input("\n Please, type in a user name to be able to address you\n").strip().title() # title() method capitalizes every word in input string
    NEW_ORDER['user_name'] = user_name

    #creates list of items out of NEW_ORDER dict
    order_items = sales_worksheet.row_values(1)
    # print(order_items)

    order_values = [] #creates list from values out of NEW_ORDER dict

    #takes only values from dict NEW_ORDER, and appends to new list order_values
    for x in order.values():
        order_values.append(x)
    print(order_values)
    
    print(f"\ Hold on {user_name}, the total amount is being calculated...")

    item_prices = pricing_worksheet.col_values(3)[1:] #list of strings of each item price from pricing worksheet
    # print(item_prices)
    
    item_prices_int_list = [] #new list of floats made from list of strings item_prices

    # converts item_prices to list of floats item_prices_float_list
    for i in item_prices:
        item_prices_int_list.append(int(i))

    number_of_items_in_order_int = [] #new list of floats made from list of strings number_of_items_in_order
    
    number_of_items_in_order = order_values[4:] # takes number of items selected in the order
    
    # loop iterates through number_of_items_in_order and converts values in strings to floats, include each float to  new list number_of_items_in_order_float
    for i in number_of_items_in_order:
        number_of_items_in_order_int.append(int(i))

    # print(number_of_items_in_order_int)

    #multiplies number of items in the order with price of item
    res_list = [item_prices_int_list[i] * number_of_items_in_order_int[i] for i in range(len(item_prices_int_list))]
    # print(res_list) #gives result of multiplying item prices by number of items in order

    # sums all sums of items ordered, calculates final amount to be paid
    final_amount= sum(res_list)
    # print(str(final_amount))
    # final_amount = int(final_amount)

    order_values.pop()
    order_values.append(str(final_amount))
    # print(order_values)

    final_order = dict(zip(order_items,order_values))

    print(f" Dear {user_name},\n\nPlease review your present order before it is processed and sent to your email for due payment:\n\n")
    
    for item, value in final_order.items(): 
        print(f' {item:10} : {value}')
    
    sales_worksheet.append_row(order_values)


    
def list_keyword_item():

    print(f"\n Each {ticket_type} has a {code} associated in the system:\n")
    items = pricing_worksheet.col_values(2)[0:]
    item_keys = pricing_worksheet.col_values(4)[0:]

    dict_item_keys = dict(zip(item_keys, items)) #creates dict merging each i from both lists
    
    for key, item in dict_item_keys.items(): #formats output of dict of KEY and ITEMS
        print(f' {key:8} : {item}')
        print('-' * 30) #adds ------- after each KEY : ITEM of the dict
            
    order_inputs()


def order():
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

        invoice = sales_worksheet.col_values(1)[-1] #takes last invoice_num from sales_worksheet e.g.: INV-10000
        invoice_letters = invoice.split("-")[0] #takes innitial letter of last invoice_num before the '-' e.g: INV
        invoice_num = invoice.split("-")[1] #takes numbers of last invoice_num after the '-' and returns string e.g.: '1000'
        invoice_num = int(invoice_num) + 1 #turns num string int integer, and adds 1 to invoice_num e.g.: 1001
        invoice_num = f"{invoice_letters}-{invoice_num}" #creates new invoice_num with same format (letters-nums) e.g. INV-1001
        #print(invoice_num)
        NEW_ORDER['invoice_num'] = invoice_num
        NEW_ORDER['invoice_date'] = DATE

        list_keyword_item()
        return NEW_ORDER
    
    
def main():
    """
    Run all program functions
    """
    print(f"\n\n {welcome_msg_before_logo}\n")
    logo()
    print('\n{:^50}'.format(f'{welcome_msg_after_logo}'))
    print_inventory(pricing)
  
    

main()