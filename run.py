import pyfiglet
import gspread  # noqa library first downloaded through terminal : pip3 install gspread google-auth
from google.oauth2.service_account import Credentials  # noqa imports just specific Credentials function from library,no need to import complete library
from pprint import pprint  # noqa  --> must not be deployed. but very handy when coding and testing
from datetime import datetime
import sys,time,random
import math
import smtplib
import ssl
import os
if os.path.exists('env.py'):
    import env
import re  # regex email validator
from email.message import EmailMessage


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]





def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


print_slow("Loading ...")


# CREDS constant variable, takes creds from file creds.json
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('festival_tickets_sale')

settings_worksheet = SHEET.worksheet('settings')
pricing_worksheet = SHEET.worksheet('pricing')
extra_info_worksheet = SHEET.worksheet('extra_info')
invoices_worksheet = SHEET.worksheet('invoices')
stock_worksheet = SHEET.worksheet('stock')
total_items_sold_worksheet = SHEET.worksheet('total_items_sold')
total_sales_worksheet = SHEET.worksheet('total_sales')

item_sales_new_order = invoices_worksheet.row_values(1)  # noqa gets key values to create NEW_ORDER dict
values_sales_new_order = invoices_worksheet.row_values(3)  # noqa gets mock values for each key to create NEW_ORDER dict

item_type = pricing_worksheet.col_values(1)[0]
code = pricing_worksheet.col_values(4)[0]
code_example = pricing_worksheet.col_values(4)[1]

# noqa dict NEW_ORDER takes user inputs all along the app to create final invoice, also including total amount
NEW_ORDER = dict(zip(item_sales_new_order, values_sales_new_order))
DATE = datetime.today().strftime('%Y-%m-%d')
TIME = datetime.today().strftime('%H:%M')

logo_name = settings_worksheet.col_values(1)[1]
logo_font = settings_worksheet.col_values(2)[1]

# takes welcome message before and after logo from settings worksheet
welcome_msg_before_logo = settings_worksheet.col_values(3)[1]
welcome_msg_after_logo = settings_worksheet.col_values(4)[1]

# noqa Create vars for every item in pricing worksheet (item_code) and user-friendly readable item name
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

# Make a regular expression
# for validating an Email with regex
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def logo():
    """
    Prints brand name (logo_name) introduced by organizer
    in settings_worksheet worksheet, to be set as the logo
    in the console welcome message
    """
    logo = pyfiglet.figlet_format(logo_name, logo_font)  # noqa pyfiglet method to create Festival Name as Logo, then printed in welcome message in main()

    print(logo)


def welcome():
    print_slow('\n\n{:^50}'.format(f'{welcome_msg_before_logo}'))
    print("\n")
    logo()
    # print_slow('{:^50}'.format(f'{welcome_msg_after_logo}'))
    go_to_pricing_list = input(" Press ANY KEY to access\n").lower()

    if go_to_pricing_list:
        return True
    return False


def print_inventory(dct):
    """
    Returns printed PRICING LIST (dct) formated as 1 row for each entry,
    removes '[]' and ',' as: {item} {amount} €, also aligning amounts
    e.g.: Adult 1 Day Access  75 €
    """
    print_slow(" PRICING LIST:\n\n")
    for item, amount in dct.items():
        print(f' {item:30}{amount} €')

    view_details_option()


def pricing_list():
    """
    Returns dict of item_names and ticket_prices
    taken from 'pricing' worksheet
    """
    item_names = pricing_worksheet.col_values(2)[1:]  # noqa retrieves 1st column, from 2nd row onwards (eludes 1st row) and creates list of strings
    ticket_prices = pricing_worksheet.col_values(3)[1:]  # noqa retrieves 3rd column, from 2nd row onwards (eludes 1st row) and creates list of strings

    price_per_ticket = dict(zip(item_names, ticket_prices))

    return price_per_ticket


pricing = pricing_list()  # noqa dict of item_names & ticket_prices, returned by pricing_list()


def exit_app():
    """
    Brings user to final question before exit point and goodbye message,
    giving last chance to continue before order is lost.
    If user decides to continue, Pricing list is printed, and sale continues.
    """
    print_slow("\n Are you sure you want to exit program?\n")
    print_slow(" In case you have a pending order, it will get lost.\n")
    print_slow(" Type E (EXIT) to close program,\n")
    print_slow(" or any other key to continue with your order:\n")
    exit_confirmation = input("\n").lower().strip()

    if exit_confirmation == "e":
        print_slow("\n Maybe see you some other time, have a lovely day!\n")
        logo()
        print(f"\n\n(c) {logo_name} 2023\n\n\n")
    if exit_confirmation != "e":
        print_inventory(pricing)


def extra_info():
    """
    Returns printed list of items extra info taken from 'extra_info' worksheet,
    formated to be human-friendly.
    """
    extra_info_message = settings_worksheet.col_values(5)[1]
    print(f"\n {extra_info_message}:")

    full_info = extra_info_worksheet.get_all_values()[1:]  # noqa creates list of lists, starting at row 2 (one list per row)
    for i in full_info:  # prints each row formated as follows
        print(f"\n {i[1]}:\n\t{i[2]}\n\t{i[3]}\n\t{i[4]}")
    
    print_slow("\n Press ANY KEY to (ORDER),\n")
    order = input(" or E (EXIT):\n").lower().strip()

    if order == "e":
        exit_app()
        return False
    if order == "r":
        main()
        return False
    if order != "e" or order != "r":
        generate_order()


def continue_ordering():
    """
    Prompt user to continue order, to finalize or to exit app
    """
    print_slow("\n Type ANY KEY to (CONTINUE ORDERING)\n")
    print_slow(" P to return to (PRICING LIST)\n")
    continue_ordering = input(" F to (FINALIZE ORDER):\n").lower().strip()

    if continue_ordering == "f":
        print(" Finalizing order ...")
        check()
        return False
    if continue_ordering == "p":
        print_inventory(pricing)
        return False
    if continue_ordering != "p" or continue_ordering != "f":
        list_keyword_item()
        return True


def order_inputs():
    """
    User inputs ORDER_ITEM, and number of items to be included in NEW_ORDER.
    Gives ValueError if user introduces a number>30 or other than an integer.
    User can also return to welcome message,
    or exit app at any stage to cancel order.
    Returns NEW_ORDER
    """
    print_slow(f"\n\n Type {code} (e.g.:{code_example}) of the {item_type}\n")
    print_slow(f" you want to order,\n")
    print_slow(" P to return to (PRICING LIST), or\n")
    ORDER_ITEM = input(f" E to (EXIT):\n").lower().strip()

    try:
        if ORDER_ITEM == "e":
            exit_app()
            return False
        if ORDER_ITEM == "p":
            print_inventory(pricing)
            return False

        if ORDER_ITEM == item1_code.lower():  # noqa 1st item in pricing worksheet
            try:
                print(f" How many '{item1_human}' do you want to order?\n")
                item1_qty = int(input(f" Type a number from 1 - 30:\n"))

                if item1_qty < 1 or item1_qty > 30:
                    raise ValueError(  # noqa ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print_slow(f" Invalid data: {e},\n")
                print_slow(" please try again.")
                order_inputs()

            NEW_ORDER[f'item1'] = item1_qty

            print_slow(f"\n Added to your order: {item1_qty} '{item1_human}'\n")
            continue_ordering()
            return False

        if ORDER_ITEM == item2_code.lower():  # noqa 2nd item in pricing worksheet
            try:
                print_slow(f" How many '{item2_human}' do you want to order?\n")
                item2_qty = int(input(f" Type a number from 1 - 30:\n"))

                if item2_qty < 1 or item2_qty > 30:
                    raise ValueError(  # noqa ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print_slow(f" Invalid data: {e},\n")
                print_slow(" please try again.")
                order_inputs()

            NEW_ORDER['item2'] = item2_qty
            print_slow(f"\n Added to your order: {item2_qty} '{item2_human}'\n")
            continue_ordering()
            return False

        if ORDER_ITEM == item3_code.lower():  # noqa 3rd item in pricing worksheet
            try:
                print_slow(f" How many '{item3_human}' do you want to order?\n")
                item3_qty = int(input(f" Type a number from 1 - 30:\n"))

                if item3_qty < 1 or item3_qty > 30:
                    raise ValueError(  # noqa ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
                else:
                    NEW_ORDER['item3'] = item3_qty
                    print_slow(f"\n Added to your order: {item3_qty} '{item3_human}'\n")
                    continue_ordering()
                    return True
                
            except ValueError as e:
                print_slow(f" Invalid data: {e},\n")
                print_slow(" please try again.")
                NEW_ORDER['item3']
                order_inputs()

        if ORDER_ITEM == item4_code.lower():  # noqa 4th item in pricing worksheet
            try:
                print_slow(f" How many '{item4_human}' do you want to order?\n")
                item4_qty = int(input(f" Type a number from 1 - 30:\n"))

                if item4_qty < 1 or item4_qty > 30:
                    raise ValueError(  # noqa ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print_slow(f" Invalid data: {e},\n")
                print_slow(" please try again.")
                order_inputs()

            NEW_ORDER['item4'] = item4_qty
            print_slow(f"\n Added to your order: {item4_qty} '{item4_human}'\n")
            continue_ordering()
            return False

        if ORDER_ITEM == item5_code.lower():  # noqa 5th item in pricing worksheet
            try:
                print_slow(f" How many '{item5_human}' do you want to order?\n")
                item5_qty = int(input(f" Type a number from 1 - 30:\n"))

                if item5_qty < 1 or item5_qty > 30:
                    raise ValueError(  # noqa ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print_slow(f" Invalid data: {e},\n")
                print_slow(" please try again.")
                order_inputs()

            NEW_ORDER['item5'] = item5_qty
            print_slow(f"\n Added to your order: {item5_qty} '{item5_human}'\n")
            continue_ordering()
            return False

        if ORDER_ITEM == item6_code.lower():  # noqa 6th item in pricing worksheet
            try:
                print_slow(f" How many '{item6_human}' do you want to order?\n")
                item6_qty = int(input(f" Type a number from 1 - 30:\n"))

                if item6_qty < 1 or item6_qty > 30:
                    raise ValueError(  # noqa ValueError is renamed as e in except, and goes in the {e} in final message
                    f" You must type a number from 1 to 30"
                    )
            except ValueError as e:
                print_slow(f" Invalid data: {e},\n")
                print_slow(" please try again.")
                order_inputs()

            NEW_ORDER['item6'] = item6_qty
            print_slow(f"\n Added to your order: {item6_qty} '{item6_human}'\n")
            continue_ordering()
            return False

        if ORDER_ITEM != item1_code or ORDER_ITEM != item2_code or ORDER_ITEM != item3_code or ORDER_ITEM != item4_code or ORDER_ITEM != item5_code or ORDER_ITEM != item6_code:
            raise ValueError(  # noqa ValueError is renamed as e in except, and goes in the {e} in final message
                f" You must type a correct {code} (e.g.:{code_example})."
            )

        if ORDER_ITEM == "e":
            exit_app()
            return False

        if ORDER_ITEM == "p":
            print_inventory(pricing)
            return False

    except ValueError as e:
        print_slow(f"\n Invalid data: {e}, please try again.")
        order_inputs()

    return True


def send_email_to_user():
    """
    Connects to smtp to send email to user
    """
    user_name = NEW_ORDER.get('user_name')
    user_email = NEW_ORDER.get('user_email')
    order_number = NEW_ORDER.get('invoice_no')

    sender = os.environ.get("APP_EMAIL")
    gmail_app_password = os.environ.get("EMAIL_APP_PASS")
    # context = ssl.create_default_context()

    # port = 465  # SSL encrypted port
    try:
        msg = EmailMessage()
        msg['Subject'] = f"Invoice from {logo_name}"
        msg['From'] = f'{logo_name}'
        msg['To'] = user_email
        msg.set_content(f"Hi {user_name},\nPlease find attached the invoice of your order {order_number}.")

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender, gmail_app_password)
        server.send_message(msg)
        server.quit()
        print_slow("Email sent!")

    except Exception as exception:
        print("Error: %s!\n\n % Exception")

    calculate_stock(NEW_ORDER, 'stock')


def check():
    """
    Regex email validation. If email pass validation,
    """
    print_slow("\n Please, include your email to receive\n")
    user_email = input(" your pending invoice and payment details:\n").strip()  # noqa strip() method erases extra spaces before/after input data

    if(re.fullmatch(regex, user_email)):
        print_slow("Valid Email")
        NEW_ORDER['user_email'] = user_email  # noqa includes user_email input value to user_email key in dict NEW_ORDER
        process_order(NEW_ORDER)
        
    else:
        print_slow("Invalid Email")
        check()


def process_order(order):
    """
    Generates list of values (order_values) from
    NEW_ORDER dict,
    calculates the order's final amount
    by multiplying each item cost taken from pricing worksheet
    per number of items in order_values.
    It appends final amount to NEW_ORDER and prints invoice to user.
    User is given the option to confirm order, return to ordering, or exit app.
    If user confirms order, invoice full data is exported to sales worksheet.
    """
    user_name = input("\n\n Please, type in a user name to create your invoice\n").strip().title()  # noqa title() method capitalizes every word in input string
    NEW_ORDER['user_name'] = user_name
    
    invoice = order.get('invoice_no')
    print_slow(f"\n Your order {invoice} is being generated...\n")
    print_slow(f"\n Hold on {user_name},\n")
    print_slow(" the total amount is being calculated...\n")

    order_item_names = invoices_worksheet.row_values(2)  # noqa takes list of items out of sales worksheet, in a user-friendly version

    order_values = []  # noqa creates list from values out of NEW_ORDER dict

    for x in order.values():  # noqa takes only values from dict NEW_ORDER, and appends to new list order_values
        order_values.append(x)

    item_prices = pricing_worksheet.col_values(3)[1:]  # noqa list of strings of each item price from pricing worksheet

    item_prices_float_list = []  # noqa new list of floats made from list of strings item_prices

    for i in item_prices:   # noqa converts item_prices to list of floats item_prices_float_list
        item_prices_float_list.append(float(i))

    number_of_items_in_order_float = []  # noqa new list of floats made from list of strings number_of_items_in_order

    number_of_items_in_order = order_values[4:]  # noqa takes number of items selected in the order, eluding user and invoice data until col4

    for i in number_of_items_in_order:  # noqa loop iterates through number_of_items_in_order and converts values in strings to floats, include each float to  new list number_of_items_in_order_float
        number_of_items_in_order_float.append(float(i))

    res_list = [item_prices_float_list[i] * number_of_items_in_order_float[i] for i in range(len(item_prices_float_list))]  # noqa multiplies number of items in the order with price of item

    total_amount = sum(res_list)  # noqa sums all subtotals of items ordered, calculates total_amount to be paid

    total_amount = round(total_amount, 2)  # noqa rounds total_amount to floor, and only 2 decimals

    order_values.pop()  # noqa takes out default 0 value for total_amount in NEW_ORDER dict, where values have been retrieved previously

    order_values.append(str(total_amount))  # noqa appends to the order values the total_amount

    final_order = dict(zip(order_item_names, order_values))  # noqa creates new dict for final_order, with item as keys, and num. of items as values. Includes final amount key:value

    print_slow("\n Please review your order before")
    print_slow("\n it is processed and sent to your email for due payment:\n\n")

    for item, value in final_order.items():  # noqa only prints items which value is not 0
        if value != '0':
            print(f' {item:10} : {value}')

    print_slow("\n Press ANY KEY to (CONFIRM ORDER),\n")
    print_slow(" U to (CHANGE) email or name\n")
    print_slow(" C to (CONTINUE ORDERING),\n")
    user_order_confirmation = input(" or E to (EXIT)\n").lower().strip()

    if user_order_confirmation == "c":
        list_keyword_item()
        return False
    if user_order_confirmation == "e":
        exit_app()
        return False
    if user_order_confirmation == "u":
        check()
        return False
    else:
        invoices_worksheet.append_row(order_values)
        print_slow(f" Order confirmed!\n")
        print_slow("\n You will automatically receive an email with your invoice")
        print_slow("\n to be paid in the following 2 business days.")
        print_slow("\n\n WARNING: Your order will be cancelled if you fail to")
        print_slow("\n proceed to payment on due date.\n\n Thank you!\n")
        send_email_to_user()
        return True


def list_keyword_item():
    """
    Print list of items and codes, and runs order_inputs()
    """
    print_slow(f"\n Each {item_type} has a {code} associated in the system:\n\n")
    items = pricing_worksheet.col_values(2)[0:]
    item_keys = pricing_worksheet.col_values(4)[0:]

    dict_item_keys = dict(zip(item_keys, items))  # noqa creates dict merging each i from both lists

    for key, item in dict_item_keys.items():  # noqa formats output of dict of KEY and ITEMS
        print(f' {key:5} : {item}')
        print('-' * 33)  # adds ---- after each KEY : ITEM of the dict

    order_inputs()


def view_details_option():
    print_slow("\n Press ANY KEY to (ORDER),\n")
    print_slow(" D to see (DETAILS),\n")
    detailed_info = input(" E to (EXIT)\n").lower().strip()

    if detailed_info == "d":
        extra_info()
        return True
    if detailed_info == "e":
        exit_app()
        return True
    else:
        generate_order()
        # return True    


def generate_order():
    """
    Prompts user to start ordering,
    to return to welcome message, or to exit.
    If user starts order, new sequencial
    invoice_no and current date are
    included in NEW_ORDER
    """
    print_slow("Loading ...\n")

    invoice = invoices_worksheet.col_values(1)[-1]  # noqa takes last invoice_no from invoices_worksheet; default e.g.: INV-10000
    invoice_letters = invoice.split("-")[0]  # noqa takes initial letter of last invoice_no before the '-' e.g: INV
    invoice_no = invoice.split("-")[1]  # noqa takes numbers of last invoice_no after the '-' and returns string e.g.: '10000'
    invoice_no = int(invoice_no) + 1  # noqa turns num string int integer, and adds 1 to invoice_no; e.g.: 1001
    invoice_no = f"{invoice_letters}-{invoice_no}"  # noqa creates new invoice_no with same format (letters-nums) e.g. INV-10001

    NEW_ORDER['invoice_no'] = invoice_no
    NEW_ORDER['order_date'] = DATE
    list_keyword_item()
    return NEW_ORDER


def calculate_subtotals_sales():
    
    items_sold = total_items_sold_worksheet.get_values()
    # print(items_sold)
    # items_soldId = '1046768896'

    items_sold_by_itemnum = items_sold[0]
    items_sold_by_nums = items_sold.pop()

    items_sold_dict = dict(zip(items_sold_by_itemnum, items_sold_by_nums))
    pprint(items_sold_dict)

    items1_sold_list = invoices_worksheet.col_values(5)[2:]  # noqa creates list of str with all items1 sold in each order
    items1_sold_int = []  # noqa new list with items1_sold converted to int for further sum
    
    for i in items1_sold_list:
        items1_sold_int.append(int(i))

    items1_sold = sum(items1_sold_int)
    print(items1_sold)

    items_sold_dict['item1'] = items1_sold

    items2_sold_list = invoices_worksheet.col_values(6)[2:]  # noqa creates list of str with all items1 sold in each order
    items2_sold_int = []  # noqa new list with items1_sold converted to int for further sum
    for i in items2_sold_list:
        items2_sold_int.append(int(i))

    items2_sold = sum(items2_sold_int)
    print(items2_sold)

    items_sold_dict['item2'] = items2_sold

    items3_sold_list = invoices_worksheet.col_values(7)[2:]  # noqa creates list of str with all items1 sold in each order
    items3_sold_int = []  # noqa new list with items1_sold converted to int for further sum
    for i in items3_sold_list:
        items3_sold_int.append(int(i))

    items3_sold = sum(items3_sold_int)
    print(items3_sold)

    items_sold_dict['item3'] = items3_sold

    items4_sold_list = invoices_worksheet.col_values(8)[2:]  # noqa creates list of str with all items1 sold in each order
    items4_sold_int = []  # noqa new list with items1_sold converted to int for further sum
    for i in items4_sold_list:
        items4_sold_int.append(int(i))

    items4_sold = sum(items4_sold_int)
    print(items4_sold)

    items_sold_dict['item4'] = items4_sold

    items5_sold_list = invoices_worksheet.col_values(9)[2:]  # noqa creates list of str with all items1 sold in each order
    items5_sold_int = []  # noqa new list with items1_sold converted to int for further sum
    for i in items5_sold_list:
        items5_sold_int.append(int(i))

    items5_sold = sum(items5_sold_int)
    print(items5_sold)

    items_sold_dict['item5'] = items5_sold

    items6_sold_list = invoices_worksheet.col_values(10)[2:]  # noqa creates list of str with all items1 sold in each order
    items6_sold_int = []  # noqa new list with items1_sold converted to int for further sum
    for i in items6_sold_list:
        items6_sold_int.append(int(i))

    items6_sold = sum(items6_sold_int)
    print(items6_sold)

    items_sold_dict['item6'] = items6_sold

    items_sold_values = []  # noqa creates list from values out of items_sold_dict dict.

    for x in items_sold_dict.values():  # noqa takes only values from dict NEW_ORDER, and appends to new list order_values
        items_sold_values.append(x)
    list_of_lists = [[el] for el in items_sold_values]
    pprint(list(list_of_lists))
    
    total_items_sold_worksheet.append_row(items_sold_values)
    range_name = '2:3'  # A1 notation refers to all cells in row(s) x:x
    total_items_sold_worksheet.update(range_name=range_name, values=list_of_lists,)
    # total_items_sold_worksheet.update('A2:B4', [[42], [43]])
    # total_items_sold_worksheet.update('B3:G3', items_sold_values)
    # total_items1_sold_column = total_items_sold_worksheet.col_values(2)
    # pprint(total_items1_sold_column)
    # # total_items1_sold = total_items_sold_worksheet.col_values(2)[-1]
    # total_items1_sold_column.pop()
    # pprint(total_items1_sold_column)
    # total_items1_sold_column_updated = total_items1_sold_column + items1_sold
    # pprint(total_items1_sold_column_updated)


def calculate_stock(data, worksheet):
    """
    Update stock worksheet last empty row with result of sustracting the items
    in invoice to each item remaining in stock.
    """
    order_values = []  # creates list from values out of NEW_ORDER dict

    for x in data.values():  # noqa takes only values from dict NEW_ORDER, and appends to new list order_values
        order_values.append(x)

    stock_to_sustract = order_values[4:]  # noqa keep only qty of items in invoice - erases user data and invoice details

    stock_to_sustract_int = []  # noqa creates new list of integers

    for z in stock_to_sustract:  # noqa creates new list of integers: stock_to_sustract_int from number of each item in order
        stock_to_sustract_int.append(int(z))

    stock_to_sustract_int.pop()  # erases last item in list = total amount

    existing_stock = stock_worksheet.get_values()[-1]  # noqa gets values in last row of stock worksheet

    existing_stock_int = []  # creates new list of integers

    for y in existing_stock:  # noqa creates new list of integers: existing_stock_int from number of each item in stock
        existing_stock_int.append(int(y))

    new_stock = [existing_stock_int[i] - stock_to_sustract_int[i] for i in range(len(existing_stock_int))]  # noqa  sustracts number of each item type in order from number of each item type in stock

    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(new_stock)  # noqa includes each item's remaining stock to 1st empty row in stock worksheet
    calculate_subtotals_sales()


def main():
    """
    Run program functions
    """
    welcome()
    print_inventory(pricing)
    

main()
