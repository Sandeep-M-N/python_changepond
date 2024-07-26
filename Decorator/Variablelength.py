# *args


# def sum_all(*args):

    

#     for i in args:
#         for j in i:

#             print(j)
        


# output = sum_all(1,2,3,4,5)
# print(output)

def staffdetails(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} is {value}')
def main():
    changepond ={
        'Name': 'sandeep',
        'Age' : 22,
        'MobileNum':8610036988
    }
    # sum_all(changepond)
    staffdetails(**changepond)

if __name__=="__main__":
    main()


