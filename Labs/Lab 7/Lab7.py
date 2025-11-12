# in this lab we will work with complex data structures and reursion
# write three functions that recursivley acces data to make final result

"""
Explanation of Recursion:
- This is a programming concept that solves a probblem by calling itself
- there is a base case that is a stopping condition
- the recursive step is where the functon calls itself with a midified input that moves closer to the base case??
- each step we get closer and closer to the base case

"""


def reformat(data):
    # take in data in the second format and return dta in the first format

    data_in = [
        {"type": "Drink", "name": "Tea", "price": 2.5},
        {"type": "Drink", "name": "Chocolate Milk", "price": 3.0},
        {"type": "Food", "name": "Hotdog", "price": 0.5},
        {"type": "Food", "name": "Burger", "price": 4.0},
    ] # i am not really sure where I am going to use this yet

    # we need to make a new menu
    menu = {} # blank dictionary that we wil luse recurison in to fill

    for item in data:
        # for item in data loops through all - needs to be a recursion loop
        item = item["type"]
        name = item["name"]
        price = item["price"]

        if item not in menu:
            # we are starting off with blank menu dictionary so we will be workng backwards aka recursion
            menu[item] = {}
            # basically we are creting a new dictionary inside of our menu dictionary???

        # now for that item we need to add the name of each item and the price
        menu[type][name] = price


    return menu



 data_in = [
        {"type": "Drink", "name": "Tea", "price": 2.5},
        {"type": "Drink", "name": "Chocolate Milk", "price": 3.0},
        {"type": "Food", "name": "Hotdog", "price": 0.5},
        {"type": "Food", "name": "Burger", "price": 4.0},
    ]
reformatted_data = reformat(data_in)
print(reformatted_data)


def nth(data, n):
    # data is n a weird format
    # everything is a nested touple with two elements
    #the first element is always the value that is part of the data
    # the second is either a tuple with more data or the value none

    for i in range(n):
        # Before we jump to the next node, check if we've fallen off the end when we get to none
        if current_node is None:
            return None

        # Go to the next node in the chain
        current_node = current_node[1]

    if current_node is not None:
        return current_node[0]
    else:

        return None



print(f"nth_simple(data, 0) -> {nth_simple(data, 0)}")  # Output: 5
print(f"nth_simple(data, 2) -> {nth_simple(data, 2)}")  # Output: "hello"
print(f"nth_simple(data, 4) -> {nth_simple(data, 4)}")  # Output: 2
print(f"nth_simple(data, 5) -> {nth_simple(data, 5)}")  # Output: None
print(f"nth_simple(data, 100) -> {nth_simple(data, 100)}")  # Output: None


def where(data):

    count = 0

    #  Data is a dictionary
    if isinstance(data, dict):
        for key, value in data.items():
            # Recursively search in both ke and values
            count += where(key)
            count += where(value)

    #Data is a list
    elif isinstance(data, list):
        for item in data:
            # waldo can be a value in a list.
            # Recursively search in each item.
            count += where(item)

    # Data is a string
    elif isinstance(data, str):
        if data == "Waldo":
            count += 1


    return count


data_waldo = {
    "Waldo": [
        "Wilma",
        "Willy",
        "Walter",
        "Wendy",
        {
            "Will": "William",
            "Wren": ["Waldo", "Warren"]
        },
    ],
    "Wanda": {
        "Whitney": "Waldo",
        "Woody": ["Willard", "Webster", "Waldo"]
    },
    "Wilber": {},
    "Waldo": "Wednesday",
    "Wade": "Wilson",
    "Wallace": ["Wilfred", "Waldo"]
}

print("\nProblem 3 Output:")
print(f"where(data_waldo) -> {where(data_waldo)}")  # Expected: 6 [cite: 90]
print(f"where('Waldo') -> {where('Waldo')}")  # Expected: 1 [cite: 91]
print(f"where('Willow') -> {where('Willow')}")  # Expected: 0 [cite: 92]
print(f"where(['Willard', 'Webster', 'Waldo']) -> {where(['Willard', 'Webster', 'Waldo'])}")  # Expected: 1 [cite: 93]