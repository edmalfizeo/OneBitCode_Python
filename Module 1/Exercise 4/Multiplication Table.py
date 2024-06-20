initial_number = int(input("Enter initial number: "))
final_number = int(input("Enter final number: "))
choosen_number = int(input("Enter the number for multiplying : "))
multiplication_table = [f"{choosen_number} * {x} = {choosen_number * x}" for x in range(initial_number, final_number+1)]
for result in multiplication_table:
    print(result)