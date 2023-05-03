"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Raghad Alrebh
Date:   Nov 23, 2022
"""

import currency

# Ask the the user for a first currency code
src = input('3-letter code for original currency: ')
# Ask the the user for a second currency code
dst = input('3-letter code for the new currency: ')
# Ask the the user for an amount (of the first currency)
first = input('Amount of the original currency: ')
# assign user input to amt variable as float
amt = float(first)
# Prints the conversion to the second currency

conversion = currency.exchange(src, dst, amt)
rounded = round(conversion, 3)
print('You can exchange '+str(amt)+' '+str(src)+ ' for '+str(rounded)+' '+\
str(dst)+'.')