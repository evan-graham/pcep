# Coding Exercise 5: Refund Policy Helper
#
# Scenario:
#
# Let's help an online store with their new refund policy. 
# In this store, you can return an item and get a refund in 2 cases:
# 
# 1. Within 10 days from the day of purchase, given that you have not used the item, or
# 2. No matter when you bought it, when the item broke down through no fault of your own.
#
# Write a program that first asks the user three questions and then informs them whether they can get a refund. 
#
# Ask the following questions:
#
# How many days ago have you purchased the item? << add a space at the end of this prompt 
# Have you used the item at all [y/n]?  << add a space at the end of this prompt
# Has the item broken down on its own [y/n]?  << add a space at the end of this prompt
#
# Based on the answers and the refund policy explained above, print either:
#
# You can get a refund.
# or:
# You cannot get a refund.

q1 = int(input('How many days ago have you purchased the item? '))
q2 = input('Have you used the item at all [y/n]? ')
q3 = input('Has the item broken down on its own [y/n]? ')

if (q1 <= 10 and q2 == 'n') or q3 == 'y':
    print('You can get a refund.')
else:
    print('You cannot get a refund.')
