#!/usr/bin/env python

meal = 45.45
tax = .08
tip = .15

tax_value = meal * tax
meal_with_tax = meal + tax
tip_value = meal_with_tax * tip

total = meal_with_tax + tip_value

print "The cost of the meal without tax and tip is %r." % meal
print "At a tax rate of %r, the total amount of the tax is %r." % (tax, tax_value)
print "You should tip %r, or %r of the cost of the meal with tax included." % (tip_value, tip)
print "With tax and tip included, the total cost of the meal is %r." % total