
class calculator:
    result = 0

    '''addition'''
    def add(self, val):
        self.result = self.result + val
        return self.result

    '''subtraction'''
    def subtract(self,val):
        self.result = self.result - val
        return self.result

    def getResult(self):
        return self.result
