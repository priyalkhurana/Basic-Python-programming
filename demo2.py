def check_baggage(weight):
    if(0<=weight<=40):
        return 'true' 
    else:
        return 'false'
def check_immigration(year):
     if(2030<=year<=2050):
        return 'true' 
     else:
        return 'false'
def check_security(noc_status):
    if (noc_status.upper() == 'valid'): 
        return 'true'
    else:
        return 'false'

def traveller():
    trav_id=int(input("enter the traveller id =>"))
    trav_name=input("enter the traveller name =>") 
    bw=float(input("enter the baggage weight =>"))  
    ey=int(input("enter the expiry year =>")) 
    ns=input("enter the noc status =>")
    if(check_baggage(bw) == 'true'): 
        if(check_immigration(ey) == 'true'):
            if(check_security(ns) == 'true'):
                print(trav_id,end=',') 
                print(trav_name)
                print("allow travel to fly.")
            else:
                print(trav_id,end=',') 
                print(trav_name)
                print("details of traveller for rechecking") 
        else:
            print(trav_id,end=',')
            print(trav_name)
            print("details of traveller for rechecking")
    else:
        print(trav_id,end=',')
        print(trav_name)
        print("details of traveller for rechecking")
traveller() 