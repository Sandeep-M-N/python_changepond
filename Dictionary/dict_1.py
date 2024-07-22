# watch_details = {
#     'titan':8000,
#     'fastrack':9000,
#     'omega':9000,
#     'titan':12000
# }
# print(watch_details)  #titan (considers the latest key)
# print(type(watch_details))
# print(watch_details['titan'])
# watch_details['omega']=4000
# watch_details['sonata']=6000
# print(watch_details)

# create a dictionary food of itwms
# food_menu = {
#     'dosa':30,
#     'poori':20,
#     'pongal':15
# }
# print(food_menu)
# food_menu['pongal']=25
# food_menu['idly']=12
# print(food_menu)

# nested dictionary
users = {
    'sandeep_rao':{
        'firstname':'sandeep',
        'lastname':'rao',
        'location':'chennai'
    },
    'basil_ahamad':{
        'firstname':'basil',
        'lastname':'ahamad',
        'location':'chennai'
    },
   'siva_lingam': {
        'firstname':'siva',
        'lastname':'lingam',
        'location':'chennai'
    }
}
print(users['sandeep_rao']['firstname'])
print(users['sandeep_rao']['location'])
