# polymorphysm
num1 = 1
num2 = 2
print(num1 + num2)

str1 = "Python"
str2 = "Programming"
print(str1 + " " + str2)

print(1 * 2)
print('-' * 30)


# ######################################################
class Vehicle:
    run_state = 'stopped'

    def ride(self):
        print(f'We run {str(self)}')
        self.run_state = 'started'


v1 = Vehicle()

print(Vehicle.__dict__)
print(v1.__dict__)
v1.ride()
print(Vehicle.__dict__)
print(v1.__dict__)
