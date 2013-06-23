import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: word 
    # value: list of occurrence counts
    orderlist=[]
    linelist=[]
    for mylist in list_of_values:
        if mylist[0] == "order":
            orderlist.append(mylist)
        else:
            linelist.append(mylist)
            
    for item in orderlist:
        for line in linelist:
            mr.emit(item + line)
        
            

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
