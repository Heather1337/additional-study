import customers
from random import choice


def run_raffle():
    """Randomly pick customer and print customer info"""

    customers_list = customers.get_customers_from_file('customers.txt')
    chosen_customer = choice(customers_list)

    print("Tell {name} at {email} that they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        ))

run_raffle()   
# Hint: remember to import any functions you need from
# other files or libraries
