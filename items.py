indian=['rice','samoasa','nann']
chainse=['noodles','frogs','snakes']
italinan=['pizza','pasta','cheese']


dish=input("enter your dish:  ")

if dish in indian:
    print("it is an indian")
elif dish in chainse:
    print("it is a chainses") 
elif dish in italinan:
    print("it is a italian")
else:
    print("not defined")           