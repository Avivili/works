# -*- coding=utf-8 -*-
import pyinputplus as pp  #third party lib，need pip install
def order_menu():
    price=0
    re_bread=pp.inputMenu(['wheat','white ','sourdough'],prompt='input your bread type:\n',numbered=True)
    if re_bread=='wheat'or re_bread=='white':
        price+=3
    else:
        price+=5
    print('price is ￥%s'%price)
    re_protein=pp.inputMenu(['chicken','tuekey','ham','tofu'],prompt='input your protein type:\n',numbered=True)
    if re_protein=='ham'or re_protein=='tofu':
        price+=2
    elif re_protein=='turkey':
        price+=3
    else:
        price+=4
    print('price is ￥%s'%price)
    cheeseWant=pp.inputYesNo(prompt='want some cheese?')
    if cheeseWant=='yes':
        re_cheese=pp.inputMenu(['cheddar','Swiss','mozzarella'],prompt='input your cheese type:\n',numbered=True)
        if re_cheese == 'cheddar' :
            price += 2
        elif re_cheese == 'Swiss':
            price += 3
        else :
            price += 4
    print('price is ￥%s'%price)
    sauceWant=pp.inputYesNo(prompt='want some mayo,mustard,lettuce,tomato?\n')
    bergnum=pp.inputInt(prompt='how many hamberg do you want?\n',min=1)
    total_price=price*bergnum

    print('the total price is ￥%s'%total_price)


if __name__=='__main__':
    order_menu()




