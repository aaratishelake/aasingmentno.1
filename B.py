n = int(input("enter the no. of element in list : "));#taking number of list element
mylist = [];
for _ in range(n):
    temp=input( ).split(" ");
    command= temp[0].strip();
    if(command=="insert"):
        mylist.insert(int(temp[1]),int(temp[2]));
    elif(command=="print"):
        print(mylist);
    elif(command=="remove"):
        mylist.remove(int(temp[1]));
    elif(command=="append"):
        mylist.append(int(temp[1]));
    elif(command=="sort"):
        mylist.sort();
    elif(command=="pop"):
        mylist.pop();
    elif(command=="reverse"):
        mylist.reverse();

