import datetime

count = 0
now = datetime.datetime.now()
msg = "Current date and time : "
str1 = msg + now.strftime("%Y-%m-%d %H:%M:%S")
print (str1)
for i in str1:
    count += 1
print("The above message contains "+str(count)+" characters.")