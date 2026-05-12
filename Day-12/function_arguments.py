# FUNCTION ARGUMENTS

# 5 TYPES OF FUNCTION ARGUMENTS:

# 1. **Positional Arguments**

def display_weather(temp, humidity, wind_speed):
    print(f'Temparature => {temp}C, Humidity => {humidity}%, wind Speed => {wind_speed}km/h')

display_weather(20, 70, 30)

# 2. **Keyword (Named) Arguments** - Arguments that are explicitly named when passed.

display_weather(humidity=80, wind_speed=40, temp=30)

display_weather(10, wind_speed=20, humidity=60)

display_weather(wind_speed=20, temp=10, humidity=60)

display_weather(10, wind_speed=20, humidity=60)

# Mixing positional and keyword arguments (order still matters for positional)
display_weather(70, 15, wind_speed=22)

# 3. **Default Arguments**

def adjust_lightning(room, brightness=75, color_temp=4000):
    """Adjusts lighting settings for a given room."""
    print(f'Adjusting lighting in {room} to {brightness}% brightness and {color_temp}K color temp.')

adjust_lightning('Living Room')

adjust_lightning('Kitchen', brightness=50)

adjust_lightning('Kitchen', 50, 3500)

adjust_lightning('Bedroom', 80)

# 4. USING *args (ARBITRARY POSITIONAL ARGUMENTS)


def calculate_total_cost(base_cost, *items):
    """Calculates the total cost by adding additional variable costs."""
    print(items)
    total_cost = base_cost + sum(items)
    print(total_cost)

calculate_total_cost(5)
calculate_total_cost(5, 10, 15, 20, 25)

def create_hashtags(*tags):
    """Creates hashtags based on tags."""
    return ' '.join(tags)

print(create_hashtags())

# 5. USING **kwargs (ARBITRARY KEYWORD ARGUMENTS)

def display_user_info(**user_data):
    """Displays user information using keyword arguments."""
    for key, value in user_data.items():
        print(f'{key}: {value}')

# Function call with multiple named arguments
display_user_info(name='Alice', age=30, membership='Premium')

display_user_info(name='Alice', age=30)

display_user_info()



