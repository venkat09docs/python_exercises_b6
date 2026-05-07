# [exp for var in collection if cond]

# SET COMPREHENSIONS

# Convert all names to capitalize first letter, ensuring consistent formatting
names = {'alice', 'BOB', 'charlie', 'DAVE'}

cap = {name.capitalize() for name in names}
print(cap)

# Dict COMPREHENSIONS

hyperparams = {'layers': 3, 'units': 256, 'dropout': 0.2}

# Create a new dictionary where all values are doubled -

# hyper*2 for hyper in hyperparams

new_hyperparams = {key: val * 2 for key, val in hyperparams.items()}
print(new_hyperparams)

# Create a set of keys (in uppercase) where values are greater than 0.2

# key.upper(): value   for key , value in hyperparams.items() if value > 0.2

new_dict = {key.upper(): val for key, val in hyperparams.items() if val > 0.2}
print(new_dict)

years = [2020, 2021, 2022]
dataset_sizes = [10000, 25000, 50000]

print(dict(zip(years, dataset_sizes)))

sales = {2022: 50000, 2023: 75000, 2024: 100000}

profit = {year: revenue * (15/100) for year, revenue in sales.items()}
print(profit)





