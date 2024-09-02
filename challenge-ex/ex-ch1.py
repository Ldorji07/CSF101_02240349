with open('fruit_transactions.txt','r') as file:  
    data = file.read() 

print(data)

with open('fruit_transactions.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        print(line.strip())

first_line