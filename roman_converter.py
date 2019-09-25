import math

class Converter():
    def __init__(self, number):
        if isinstance(number, int):
            self.number = number
        else:
            print('Insert a valid Integer Number!')
        self.str_roman = ''
        self.roman_dict = {
                0 : "N",
                1 : "I",
                5 : "V",
                10 : "X",
                50 : "L",
                100 : "C",
                500 : "D",
                1000 : "M"}
    
    def break_int_number(self):
        self.productByTen = self.number / 10
        self.decimalPart = math.modf(self.productByTen)
        self.dividedNumber = self.productByTen - self.decimalPart[0]
        self.goldenNumber = int(self.decimalPart[0] * 10.00001)
        return self.dividedNumber, self.goldenNumber

    def update_number(self):
        self.number = int(self.dividedNumber)

    def apply_roman_rule(self):
        self.n = self.break_int_number()[1]

        if self.n == 5:
            return [self.n]

        if self.n == 4:
            return [1, 5]

        if self.n < 4: 
            self.list = [1 for item in range(self.n)]
            return self.list
        
        if self.n > 5 and self.n < 9:
            self.list = [1 for item in range(5, self.n, 1)]
            self.list.insert(0, 5)
            return self.list[::-1] #invert list

        if self.n == 9:
            return [1 , 10]    

    def get_romandict_idx(self, turn): 
        self.turn = turn
        self.romanList = []
        self.num = self.apply_roman_rule()
        self.num = [self.turn * i for i in self.num]
        for self.value in self.num:
            self.romanList.append(self.roman_dict[self.value])
        self.update_number()
        return self.romanList
            
    def generate_values(self):
        self.turn = 1        
        self.final_list = []
        while self.number > 0:
            self.final_list += self.get_romandict_idx(self.turn)
            self.turn *= 10
        self.final_list = self.final_list[::-1] #invert list

    def list_to_string(self, l):
        self.l = l
        for i in self.l:
            self.str_roman += ''.join(i)
        return self.str_roman

    def convert(self, output_mode='string'):
        self.output_mode = output_mode
        self.generate_values()
        
        if self.output_mode == 'string':
            return(self.list_to_string(self.final_list))        
        if self.output_mode == 'list':
            return(self.final_list)



