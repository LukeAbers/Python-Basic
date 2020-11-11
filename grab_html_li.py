#output.txt containing raw HTML
f = open("output.txt","r")
f = f.read()
l = 0
arrayList = []
while l > -1:
        tmp = f.find("<li",l)
        tmp2 = f.find("</li>")
        arrayList.append([tmp:tmp2])
