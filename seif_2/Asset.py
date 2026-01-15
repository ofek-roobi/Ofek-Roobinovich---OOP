class Asset():
    

    def __init__(self,symbol , current_price,quantity):
        self.symbol=symbol
        self._current_price=current_price
        self._quantity=quantity

    @property
    def current_price(self):
        return self._current_price
    
    
    @current_price.setter

    def current_price(self,value):
        if value<0:
            raise ValueError (" the value price cant be bellow -0")
        self._current_price= value
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter

    def quantity(self,value):
        if value<0:
            raise ValueError (" the value of quantity cant be bellow -0")
        self._quantity = value


    def calculate_Asset_value(self):
        value=self._current_price * self._quantity
        return value

    def update_price(self ,value ):
        self._current_price=value

        print( f'----update----\n the current price is {self._current_price} ')


    def __str__(self):
        return (f'---ASSETS--\n symbol:{self.symbol} \n assrts_value :{self.calculate_Asset_value()}')
    



    

