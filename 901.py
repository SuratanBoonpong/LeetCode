class StockSpanner:
    def __init__(self):
        self.stock = []
        self.indexOfStock = []
    def next(self, price: int) -> int:
        self.stock.append(price)
        while(self.indexOfStock!=[] and self.stock[self.indexOfStock[-1]] <= self.stock[-1]):
           self.indexOfStock.pop()
        output = len(self.stock)-1
        if(self.indexOfStock == []):
            output += 1
        else:
            output = output - self.indexOfStock[-1]
        self.indexOfStock.append(len(self.stock)-1)
        return output