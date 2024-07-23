# Area of circle = PI*Radius*Radius
 

def Area(Radius,PI=3.14):
    print(Radius)
    print(PI)
    Result = PI*Radius*Radius
    return Result


def main():
    #positional Arguement
    output_1 = Area(10,12)
    print(output_1)
    # first arguement is positional & second arguement is default
    output_2= Area(10)
    print(output_2)

    # keyword arguement
    output_3 = Area(PI=3,Radius=12)
    print(output_3)

    # keyword arguement & second is default
    output_4 =Area(Radius=12)
    print(output_4)

if __name__=="__main__":
    main()