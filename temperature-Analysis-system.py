import numpy as np
temperature = np.array([
    32,34,35,36,33,31,30,
    37,38,36,35,34,33,32,
    31,30,29,28,34,36,37,
    39,40,38,36,35,34,33,
    32,31])

print("Temperature Data:\n",temperature)

# 1. Average Temperature
avg_temp = np.mean(temperature)
print("\n Average Temperature:",round(avg_temp,2))

# 2. Hottest and Coldest Day
max_temp = np.max(temperature)
min_temp = np.min(temperature)

# 3. Days above 35 degrees Celsius
# to find out this we will use boolean indexing /conditional filtering 
#hot_days = temperature[temperature>35] this will create  a boolean array[True,False.....] numpy selects only those values where condition is True so it filters all temperatures greater than 35

hot_days = temperature[temperature>35]
print("\nDays above 35 degrees Celsius:",hot_days)
print("Count:",len(hot_days))

# 4. Days below 20 degree Celsius
cold_days = temperature[temperature>20]
print("\nDays below 20 degrees Celsius:",cold_days)
print("Count:",len(cold_days))

standard_deviation = np.std(temperature)
print("\n Standard Deviation:",round(standard_deviation,2))

