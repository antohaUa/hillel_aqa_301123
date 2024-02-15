# __del__

class VehicleDel:
    def __del__(self):
        print(f"Instance deleted {self=}")

    def other(self):
        print("Somethig other")




vd1 = VehicleDel()
vd1.other()
vd2 = VehicleDel()
print('instance created')

vd1 = None
print('After variable reassign')

