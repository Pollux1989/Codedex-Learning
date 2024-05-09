#####--------33. Drive Thru--------#####

print('##########--🖤🖤💛💛 Welcome to GYG 💛💛🖤🖤--##########')

def get_item(x):
    if x == 1:
        return '🌯 Burrito'
    elif x == 2:
        return '🥤 Coke'
    elif x == 3:
        return '🍟 Fies'
    elif x == 4:
        return '🍧 Cone '
    elif x == 5:
        return '🍗 Tenders'
    else:
        return 'Invalid Option'
    
def menu_option():
    print ('Choose the option in the Menu: ')
    print('1.🌯 Burrito')
    print('2.🥤 Coke')
    print('3.🍟 Fies')
    print('4.🍧 Cone')
    print('5.🍗 Tenders')

menu_option()

item = int(input('What would you like to order?: '))
print(get_item(item))
