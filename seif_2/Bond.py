from Asset import*
class Bond(Asset):

    def __init__(self, symbol, current_price, quantity,rate,date):
        super().__init__(symbol, current_price, quantity)
        self.rate=rate
        self.date=date

    def calculate_rate(self):
         asset_value=self.calculate_Asset_value()
         rate_value= asset_value*self.rate
         return rate_value
    
    def __str__(self):
        return f"{super().__str__()}\n type: BOND\n rate :{self.rate} \n rate_value : {self.calculate_rate()}\n date: {self.date}"
    
