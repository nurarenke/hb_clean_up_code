SALESPERSON_INDEX = 0
INTERNET_INDEX = 1
STAR_BORDER = 80

def print_border():
    '''creates a star border between each section'''
    print "*" * STAR_BORDER

print_border()

def count_melon_types_and_prices():
    # opens the "orders-by-type" file
    file_data = open("orders-by-type.txt")

    melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}

    # iterate through each line in the "orders-by-type" file
    for line in file_data:
        orders_tokens = line.split("|") #split data on the line by "|"
        melon_type = orders_tokens[1]
        melon_count = int(orders_tokens[2])
        melon_tallies[melon_type] += melon_count

    file_data.close()

    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        # print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)
        print "We sold {} {} melons at {:.2f} each for a total of {:.2f}".format(melon_tallies[melon_type], melon_type, price, revenue)


count_melon_types_and_prices()

print_border()

f = open("orders-with-sales.txt")
sales = [0, 0]
for line in f:
    d = line.split("|")
    if d[1] == "0":
        sales[0] += float(d[3])
    else:
        sales[1] += float(d[3])
print "Salespeople generated ${:.2f} in revenue.".format(sales[1])
print "Internet sales generated ${:.2f} in revenue.".format(sales[0])
if sales[1] > sales[0]:
    print "Guess there's some value to those salespeople after all."
else:
    print "Time to fire the sales team! Online sales rule all!"

print_border()
