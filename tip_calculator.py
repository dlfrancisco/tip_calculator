#!/usr/bin/env python

import sys

meal = sys.argv[1]
tax = sys.argv[2]
tip = sys.argv[3]

meal_float = float(meal)
tax_float = float(tax)
tip_float = float(tip)

tax_value = meal_float * tax_float
meal_with_tax = meal_float + tax_float
tip_value = meal_with_tax * tip_float

total = meal_with_tax + tip_value

print "The cost of the meal without tax and tip is $%.2f." % meal_float
print "At a tax rate of %.2f, the total amount of the tax is $%.2f." % (tax_float, tax_value)
print "You should tip $%.2f, or %.2f of the cost of the meal with tax included." % (tip_value, tip_float)
print "With tax and tip included, the total cost of the meal is $%.2f." % total