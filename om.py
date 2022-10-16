list = ['sunday', 'monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday', 'Saturday']
num = []

count = int()

for i in range(len(list)):
    user_input = float(
        input(f"enter the temperature in {list[i]}="))  # USER INPUT
    num.append(user_input)  # ADDING IN THE EMPTY (NUM) LIST
    count += user_input  # ADDING VLAUE FOR AVERAGE TEMPERATURE
print("---------------------------------------------")

for i in range(len(list)):
    # PRINTING DEEGREE TO FAHRENHEITE
    print(f"{num[i]} celsius is equal to {num[i]*1.8+32} fahrenheit")

temp = int()
for i in range(len(list)):  # BUBBLE SORT
    for j in range(len(list)):
        if (num[i] < num[j]):
            temp = num[i]
            num[i] = num[j]
            num[j] = temp

print("---------------------------------------------")
# PRINTING THE HIGHEST LOWEST AND AVG
print(f"higest={num[6]} lowest={num[0]} avg={count/7}")
