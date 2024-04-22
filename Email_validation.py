email=input("Enter Your Email :") #g@g.in ,gagan@gamil.com closing condition
k=0
j=0
d=1
# first condition check email length is 6 or more then 6
if len(email)>=6:
   # second  condition check email first letter is alphabet or not
   if email[0].isalpha():
      # third condition check "@" in string and count "@" in email
        if ("@" in email) and (email.count("@")==1):
           # 4th codition check "." in email then we can use Negitive indexing means(-1,-2,-3,-4)all website using "." in emails 3rd and 4th position but double time "." not using in email/gmail
            if (email[-4]==".")^(email[-3]=="."):
             # 5th we can check in our email  using space 
                if(" " in email) and (email.count(" ")==1): 
                #  6th we can check in our email  using digits   
                   for i in email:
                      if i==i.isdigit():
                          i=="1"
                          k=1
                      elif i.isalpha():
                       if i==i.upper():  # w-- W==w, W==W
                           j=1 
                           continue
                       if k==1 or j==1:
                          print("wrong Email 5")
                else:
                    print(" Right Email....")
            else:
               print("wrong Email 4")
        else:
          print("wrong Email 3 ")
          
   else:
       print("wrong Email 2 ")
else:
    print("wrong Email 1 ")