import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y','Z']
nums=['0','1','2','3','4','5','6','7','8','9']
spl_chars=['@','!','#','%','*','(',')','{','}']
password_list=[]
num_letters=int(input("enter num of letters"))
num_splchars=int(input("enter num of spl chars"))
num_nums=int(input("enter num of letters"))
for i in range(num_letters+1):
    password_list.append(random.choice(letters))
for i in range(num_splchars+1):
    password_list.append(random.choice(spl_chars))
for i in range(num_nums+1):
    password_list.append(random.choice(nums))
print(password_list)
random.shuffle(password_list)
print(password_list)
password=''
for i in password_list:
    password+=i
print(f"password is:{password}")
    

