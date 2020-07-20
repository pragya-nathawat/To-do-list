lstqz = []
task = input("Enter task:")
lstqz.append(task)

while task != "":
    task= input("Enter task:")
    lstqz.append(task)
    
print("\n-----------")    
print("To Do List:")
print("\n-----------")
x = 0
while x < len(lstqz)-1:
    print(str(x+1) + ". " + lstqz[x])
    x += 1