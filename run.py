import pyfiglet 
  
logo = pyfiglet.figlet_format("ROCK FEST", font = "bubble" ) 
price_adult_one_day = 75 #value taken from spreadsheet
price_adult_per_day = f"{price_adult_one_day} €"
price_child_one_day = 45 #value taken from spreadsheet
price_child_per_day = f"{price_child_one_day} €"

print("\n\n   WELCOME TO \n\n" + logo + "\n\n       BUY YOUR TICKETS NOW!\n\n")
print(f"PRICING: \n\n - Adult per day: {price_adult_per_day} \n - Children under 12 years old: {price_child_per_day} \n ")

