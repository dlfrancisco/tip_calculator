#!/usr/bin/env python

meal = 45.45
tax = .08
tip = .15

tax_value = meal * tax
meal_with_tax = meal + tax
tip_value = meal_with_tax * tip

total = meal_with_tax + tip_value

print "The cost of the meal without tax and tip is $%.2f." % meal
print "At a tax rate of %.2f, the total amount of the tax is $%.2f." % (tax, tax_value)
print "You should tip $%.2f, or %.2f of the cost of the meal with tax included." % (tip_value, tip)
print "With tax and tip included, the total cost of the meal is $%.2f." % total