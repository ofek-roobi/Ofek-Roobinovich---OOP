from Asset import*
class stock(Asset):
    def __init__(self, symbol, current_price, quantity,sector,dividend):
        super().__init__(symbol, current_price, quantity)
        self.sector=sector
        self.dividend=dividend
    
    def calculate_dividend(self):
        dividend=self._quantity*self.dividend
        return dividend
    
    def __str__(self):
        return f"{super().__str__()}\n type: STOCK \n sector :{self.sector}\n dividend :{self.dividend}"
    
