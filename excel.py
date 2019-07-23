# insert
import csv
#with open("stu.csv","w",newline="") as f:


    #data_handler=csv.writer(f,delimiter=",")
    #data_handler.writerow(["name","Age","Rollnbr"])
    #data_handler.writerow(["hira","20","555"])
    #data_handler.writerow(["urooj","22","626"])
   
    #for read
#with open("stu.csv") as f:
 #   data_handler=csv.reader(f)
  #  for data in data_handler:
       # print (data)

       # if data[0]=="urooj"
#take input from user
with open("stu.csv","w",newline="") as f:
    data_handler=csv.writer(f,delimiter=",")
    name=input("enter name")
    Age=input("enter age")
    Rollnbr=input("input rollnbr")
