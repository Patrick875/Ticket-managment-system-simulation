from datetime import datetime
from data import maximum,getTime
someData=0
# print(data)
adminData=0
adminPassword='12345'
currentTime=datetime.now().hour+2

def loginForm():
    print('Welcome to Ticket queuing system.\nIt is '+ str(currentTime) +' '+ str(datetime.now().minute )+'\nSelect your role to use the system')
    print('Select an option: ')
    role= input('1.Admin\n2.Passenger \n')

    if(role=='Passenger' or role =='2'):
        print('At this moment the estimate  waiting time on the line is:' + str(getTime(currentTime)) )
        if( getTime(currentTime)>= maximum):
            print('You may come in some minutes. Now the line is busy')
        else:
            print('Join the queue you will be served in no time!!!')

    elif(role=='Admin' or role=='1'):
       password=input('please enter your password :')
       while(password != adminPassword):
           print('wrong password, try again')
       else:
           print('Welcome at Admin it is: ' )
           print('At this moment the passengers in line are '+ str( adminData))
           if(getTime(currentTime) >= maximum):
               print('send in another teller') 
           else:
                print('The line is working fine')

loginForm()
