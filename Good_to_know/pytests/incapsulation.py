class Phone:
    number = "111-11-11"
    def print_number(self):
        print( "Phone number is: ", self.number )

    def get_number(self):
        return self.number

my_phone = Phone()
my_phone.print_number()
print(my_phone.get_number())