#!/usr/bin/env python

from optparse import OptionParser

parser = OptionParser()

parser.add_option("-m", "--meal", dest="meal", help="cost of meal without tax")
parser.add_option("-x", "--tax", dest="tax", help="tax rate as decimal")
parser.add_option("-t", "--tip", dest="tip", help="percent you'd like to tip", default=".15")

(options, args) = parser.parse_args()

if not options.meal:
	parser.error("Oops! You forgot to enter the cost of the meal!")
if not options.tax:
	parser.error("Oops! You forgot to enter the tax percentage as a decimal!")

meal=float(options.meal)
tax=float(options.tax)
tip=float(options.tip)

tax_value = meal * tax
meal_with_tax = meal + tax
tip_value = meal_with_tax * tip

total = meal_with_tax + tip_value

print "The cost of the meal without tax and tip is $%.2f." % meal
print "At a tax rate of %.2f, the total amount of the tax is $%.2f." % (tax, tax_value)
print "You should tip $%.2f, or %.2f of the cost of the meal with tax included." % (tip_value, tip)
print "With tax and tip included, the total cost of the meal is $%.2f." % total