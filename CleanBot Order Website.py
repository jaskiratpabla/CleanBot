from random import randint
#Importing Random Integer Function from the Random Library in Python.

print('Welcome to the CleanBot Order Website')
print('This website will navigate you through the process of ordering your affordable CleanBot.')
#Introduction to the Website.

print('\nEach CleanBot costs $119.99 CAD. \nIf you purchase 5 CleanBots, you can get a discounted price of $549.99 CAD. \n')
#Informing users about CleanBot Pricing.

bots = int(input('How many CleanBots would you like to order today: '))
#Asking the user how many CleanBots they want to order.
if bots<5:
  price = bots*119.99
#If the user is ordering less than 5 CleanBots, simply multiply the unit rate by the number of CleanBots.
elif bots>4:
  price = int(bots/5)*549.99 + (bots-int(bots/5)*5)*119.99
#Otherwise, if the user is ordering more than 5 CleanBots, calcuate how many sets of 5 Cleanbots are in the order and multiply the number sets by the discount rate for 5 Cleanbots. Then, calculate the number of leftover CleanBots and multiply them by the single rate price.

print('\nIf you would like to order',bots,'CleanBots, your total price will be: $'+'%.2f'%(price)+'. Please note that the discount stated above is applied for every 5 CleanBots in your purchase. For example, if you order 13 CleanBots, your order will consist of 2 sets of five CleanBots, and 3 single CleanBots. So, discounts are automatically applied to every set of 5 CleanBots within your purchase.')

option = input('\nWould you like to continue with this purchase (Answer with Yes or No): ')
#Displaying the cost of the user's order and informing them that the set of 5 CleanBot discount has been applied for every set of 5 CleanBots they have purchased.

if option == 'Yes':
  days = str(randint(3,9))
  print ('Your order of',bots,'CleanBots has been sucessfully placed. Expect your CleanBots to arrive in approximately',days,'days. Thank you for shopping with us!')
#Informing the user that their order has been placed successfully and to expect their delivery in a random amount of days. The reason the number of days is random because this is not an actual website, rather it is just a prototype of code that would actually work for an order website. Inforamtion regarding payment and real shipping dates have been omitted due to the fact that shipping time cannot actually be calculated and payment information cannot be processed through GitHub.
else:
  print('\nYour CleanBots order has been sucessfully declined. We are sorry that you do not want to order any CleanBots. Enjoy the rest of your day!')
#Informing the user that their order has been declined successfully.
