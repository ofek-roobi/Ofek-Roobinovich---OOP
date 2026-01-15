from invoice import*

def main():
        invoice_id = input("Enter Invoice ID: ")
        name = input("Enter Customer Name: ")
        date = input("Enter Date (dd/mm/yyyy): ")
        amount = float(input("Enter Base Amount: "))
        disc = float(input("Enter Discount: "))

        MY_INVOICE=invoice(invoice_id, name,date,amount ,disc)
        print(f'\n{MY_INVOICE}\n')
        my_finilprice= MY_INVOICE.calculate_total()
        print(f' the finel price {my_finilprice}\n')
        MY_INVOICE.mark_as_paid()
        print(f'\n{MY_INVOICE}\n')



if __name__ =="__main__":
    main()


