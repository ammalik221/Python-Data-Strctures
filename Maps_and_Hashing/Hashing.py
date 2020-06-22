"""
A simle Hash table lookup implemented in Python 3.0

The advantage of hash tables is that they provide a constant time lookup.
In this example, I am assuming that all the values stored will be strings and of atleast length greater than 2.
Then the hash value is calculated using the formula - 
         hash value = ascii(string[0])*100 + ascii(string[1])
This hash value is the index at which the strings will be stored.
"""

class HashTable(object):
    def __init__(self):
        self.hash_table = [None]*100000
        
    def store_value(self, value):
        index = self.hash_value(string)
        if self_table[index] != None:
            # in case of collision, store both values the same location
            self_table[index].append(string)
        else:
            self_table[index] = [string]
            
    def lookup_value(self, string):
        """ returns the index where the string is stored """
        index = self.hash_value(string)
        if self.hash_table[index]:
            return index
        else:
            return -1
          
    def hash_value(self, string):
        """ calculates the hash value """
        return ord(string[0])*100 + ord(string[1])
      
if __name__ == "__main__":
    # test case
    table = HashTable()
    
    table.store('AMMAR')
    
    # will print the index at which this string is stored
    # output - 6577
    print(table.lookup_value('AMMAR'))




