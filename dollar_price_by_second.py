from price_of_a_currency_getter import price_of_a_currency_getter as price
from time import sleep
from keyboard import is_pressed



while not is_pressed('f'):
    print(price('dollar'))
    sleep(3)
