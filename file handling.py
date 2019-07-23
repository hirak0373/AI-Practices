# create and use file -->w
with open("name.txt","w") as f:
    f.write("hira\n")
    f.write("urooj")
with open("name.txt","a") as f:
    f.write("ali")
with open("name.txt","r") as f:
    text_of_file=f.read()
