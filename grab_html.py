#e.g. python grab_html.py "output.txt" "<li class=\"result-row\"" "</li>" "output.html"
import sys

#save file location
saveFileToken = sys.argv[4]

#txt file containing raw HTML
fileToken = sys.argv[1]

#open raw HTML
f = open(fileToken,"r")
fText = f.read()
f.close()

#get html tokens
startToken = sys.argv[2]
endToken = sys.argv[3]

#initialize variables
l = 0
arrayList = []

#search loop
while l > -1:
        #get slice coords
        tmp = fText.find(startToken,l)
        tmp2 = fText.find(endToken,tmp)
        
        #append slice
        arrayList.append(fText[tmp:tmp2 + len(endToken)])
        
        #reset marker
        l = fText.find(startToken,tmp2)
       
#create HTML file of results
htmlFinal = "<html>\n"
for i in arrayList:
        htmlFinal += i + "\n"
htmlFinal += "</html>"

#save HTML file
f = open(saveFileToken,"w")
f.write(htmlFinal)
f.close()
