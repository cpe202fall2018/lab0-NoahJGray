def weight_on_planets():

    lb = int(input("What do you weigh on earth? "))
    print("\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(lb * .38, lb * 2.34))
   
if __name__ == '__main__':
   weight_on_planets()
