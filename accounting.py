SALESPERSON_INDEX = 0
INTERNET_INDEX = 1
STAR_BORDER = 80

def print_border():
    '''creates a star border between each section'''
    print "*" * STAR_BORDER

def count_melon_types():
    # opens the "orders-by-type" file
    file_data = open("orders-by-type.txt")

    melon_tallies = {"Musk":0, 
     "Hybrid":0, 
    "Watermelon":0, 
    "Winter": 0}

    # iterate through each line in the "orders-by-type" file
    for line in file_data:
        # split data on the line by "|"
        orders_tokens = line.split("|") 
        # tokenize the individual melons and their count found in each line
        melon_type = orders_tokens[1]
        melon_count = int(orders_tokens[2])
        #this adds the melon type with the melon count to create a tally of how many melons sold
        melon_tallies[melon_type] += melon_count

    file_data.close()
    return melon_tallies


def total_melon_revenue(melon_tallies):
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0
    # iterates through each melon type in melon tallies
    for melon_type in melon_tallies:
        # find the right price for each melon type
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        # print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)
        print "We sold {} {} melons at {:.2f} each for a total of {:.2f}".format(melon_tallies[melon_type], melon_type, price, revenue)


def total_sales_diff():

    sales_data_file = open("orders-with-sales.txt")
    online_sales = 0
    salespeople_sales = 0

    # interates through each line in the sales data file
    for line in sales_data_file:
        sales_tokens = line.split("|")
        # create totals for online sales and salespeople sales
        # online sales's id is all 0, everyone else has different ids
        if sales_tokens[1] == "0":
            online_sales += float(sales_tokens[3])
        else:
            salespeople_sales += float(sales_tokens[3])

    print "Salespeople generated ${:.2f} in revenue.".format(salespeople_sales)
    print "Internet sales generated ${:.2f} in revenue.".format(online_sales)
    if online_sales > salespeople_sales:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"

    sales_data_file.close()







print_border()

melon_tallies = count_melon_types()

total_melon_revenue(melon_tallies)

print_border()

total_sales_diff()

print_border()
