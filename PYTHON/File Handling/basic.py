#reading a file
#or 
# f=open("D:\\CODING\\Pyspiders\\Python-Fullstack\\PYTHON\\File Handling\\sample.","r") 
# print(f)

# f=open("D:/CODING/Pyspiders/Python-Fullstack/PYTHON/File Handling/sample.txt","r")
# content=f.read()
# print(content)
##return the content

# f=open("D:/CODING/Pyspiders/Python-Fullstack/PYTHON/File Handling/sample.txt","r")
# content_=f.readlines()
# print(content_)
##returns list

# f=open("D:/CODING/Pyspiders/Python-Fullstack/PYTHON/File Handling/sample.txt","r") 
# content=f.readline()
# print(content)
## returns single line

# for line in f:
#     print(line.strip())#"\n" between lines are gone here.

##################standard way of opening a file##############
f=open("D:/CODING/Pyspiders/Python-Fullstack/PYTHON/File Handling/sample.txt","r")
d={}
for line_no,lines in enumerate(f,start=1):
    clear_lines=lines.strip()
    d[line_no]=lines

print(d)


