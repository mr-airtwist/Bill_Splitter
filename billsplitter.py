# write your code here
import random


friends = {}
print("Enter the number of friends joining (including you): ")
num = int(input())
print()
if num <= 0:
    print('No one is joining for the party')
else:
    print("Enter the name of every friend (including you), each on a new line: ")
    for i in range(1, num + 1):
        friends[input()] = 0
    print()
    print('Enter the total bill value: ')
    total = int(input())
    for friend in friends:
        friends[friend] = round(total / len(friends), 2)
    print()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    lucky = input()
    if lucky == 'Yes':
        print()
        lucky_friend = random.choice(list(friends))
        print(f'{lucky_friend} is the lucky one!')
        friends[lucky_friend] = 0
        for friend in friends:
            if friend != lucky_friend:
                friends[friend] = round(total / (len(friends) - 1), 2)
    else:
        print()
        print('No one is going to be lucky')
    print()
    print(friends)
