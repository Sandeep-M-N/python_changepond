
def make_car(CarName,CarModel,**specs):
    print(f'carname : {CarName}')
    print(f'carmodel: {CarModel}')
    for key,value in specs.items():
        print(f'{key} : {value}')

def main():
    make_car('toyota','innova',color='blue',rate=2000000)
    

if __name__=="__main__":
    main()