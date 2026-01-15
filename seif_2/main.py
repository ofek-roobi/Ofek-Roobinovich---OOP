from Asset import*
from Stock import*
from Bond import*
from option import *


def main():
    sym=input(" plese chose your  symol asset:   ")
    current_price=float(input(" the price of  assets:  "))
    quantity=float(input("plese chose how many asset do you want:  "))
    my_asset= Asset(sym,current_price,quantity)
    print(my_asset)

    new_price=float(input("the update price is __"))
    my_asset.update_price(new_price)
    print(my_asset)

    stock_sector = input("Enter Sector (e.g., Technology): ")
    stock_div_rate = float(input("Enter Dividend per Share: "))
    
    my_stock=stock(sym,current_price,quantity,stock_sector,stock_div_rate)
    print(my_stock)
    new_price=float(input("the new price is __"))
    my_stock.update_price(new_price)
    div_income = my_stock.calculate_dividend()
    print(f"Total Dividend Income: {div_income}")
    print()
    print(my_stock)


    bond_rate = float(input("Enter Bond rate:   "))
    bond_date = input("Enter Maturity Date (dd/mm/yyyy):   ")
    my_bond=Bond(sym , current_price, quantity, bond_rate, bond_date)
    print(my_bond)
    print()
    rate_income=my_bond.calculate_rate()
    print(f'rate income : {rate_income}')
    print(my_bond)

   
    strike = float(input("Enter Strike Price: "))
    exp_date = input("Enter Expiration Date: ")
    opt_type = input("Enter Option Type (Call/Put): ")

    My_Option = option(sym, current_price, quantity, strike, exp_date, opt_type)
    print(My_Option)
    print()
    if My_Option.is_in_the_money():
        print("Good news! The option is currently profitable.")
    else:
        print("Note: The option is currently not profitable.")



if __name__=="__main__":
    main()