from Asset import*
class option(Asset):
    def __init__(self, symbol, current_price, quantity,Strike_Price , Type , Expiration_Date ):
        super().__init__(symbol, current_price, quantity)
        self.Strike_Price = Strike_Price
        self.Type = Type
        self.Expiration_Date = Expiration_Date
    def is_in_the_money(self):
        if self.Type == "Call":
            return self.current_price > self.Strike_Price
        else: 
            return self.current_price < self.Strike_Price

    def str(self):
        return f"{super().str()}\nType : Option\nStrike Price : {self.Strike_Price}\n Option Type : {self.Type}\nExpiration Date : {self.Expiration_Date}\n{self.is_in_the_money()}"    