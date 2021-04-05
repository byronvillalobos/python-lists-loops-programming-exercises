#Remember import random function here:
import random
#The magic is here:

def generate_random_items():
    my_list = []
    adding = random.randint(0, 1)

    for i in range(0, 10(my_list)):
        my_list.append(adding)
        i += i
    return my_list

my_stupid_list = generate_random_items()
print(my_stupid_list)
