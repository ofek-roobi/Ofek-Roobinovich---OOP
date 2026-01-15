class invoice:
    def __init__(self,invoice_id,customer_name,date , base_amount,discount):
        self.invoice_id=invoice_id
        self.customer_name=customer_name
        self.date=date
        self.is_paid=False
        self._discount=discount
        self._base_amount=base_amount
          
    

    @property
    def base_amount(self):
       
       return self._base_amount
    
    @base_amount.setter
    def base_amount(self,value):
        if value<0:
            raise ValueError('base amount cant be negative')
        self.base_amount=value


    @property
    def discount(self,value):

        return self._discount
    
    @discount.setter
    def discount(self,value):

        if value<0 or value>=self._base_amount:
            raise ValueError(" the discount cant be negative or the discount is bigger then amount ")
    

    def calculate_total(self):
        total_amount=self._base_amount-self._discount
        return total_amount
    
    def mark_as_paid(self):
        self.is_paid=True
        print(f' invoice {self.invoice_id}  paid proptlly  ')
        
    def __str__(self):
        
        status=" paid"
        if self.is_paid==False:
            status="unpaid "
        return (f'____ inovice number : { self.invoice_id}____\ncustomer name is __ {self.customer_name} _\n the date is __{self.date} _\n the base amount is :  {self._base_amount}__\n the discount is : {self._discount} __\n the total amount is : {self.calculate_total()}_\n the status is {status}')

        