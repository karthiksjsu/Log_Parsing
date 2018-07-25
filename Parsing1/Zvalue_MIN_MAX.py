import re
List_ZM=[]
List_ZF=[]

filename ="C:\\Users\\ROME Servicing\\Documents\\Python_project\\PlacementSearch.log"

file = open(filename, "r")
for line in file:

    matched=re.search(r'(\d\s+)(.*)(\<sci_[c|d]cFlow\>\s+)(\[UNIT=1\]\s+)(\w{9}\s+)((dis)?connect:\s+)(E|1ae|1be)(\d{1,3})\<\-\>(W|1aw|1bw)(\d{1,3}).*ZM=(\d{1,})\s+YM=(\d{1,})\,\s+ZF=(\d{1,})\s+YF=(\d{1,})',line)

  
    if (matched):
        ZM=int(matched.group(12))
        ZF=int(matched.group(14))
        print (line)
        List_ZM.append(ZM)
        List_ZF.append(ZF)
        
    else:
        #print ("Nothing matched")
        continue
       
print ("Z male Maximum   =",max(List_ZM))
print ("Z male Minimum   =",min(List_ZM))
print ("Z Female Maximum =",max(List_ZF))
print ("Z Female Minimum =",min(List_ZF))



    

