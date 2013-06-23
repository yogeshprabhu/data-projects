import MapReduce
import sys

"""
Inverted index in the Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for word in words:
      mr.emit_intermediate(word, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mylist=[]
    
    for term in list_of_values:
        if term not in mylist:
            mylist.append(term)
            
    mr.emit((key, mylist))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
