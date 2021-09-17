    
class Node:
   def __init__(self, key, data):
      self.key = key  
      self.data = data
      self.left = None
      self.right = None

class Bintree:
    def __init__(self):
        self.root = None

    def store(self, key, newvalue):
        self.root = rekstore(self.root, key, newvalue)


    def search(self, key):
        # returnerar value om key finns i trädet, KeyError annars
        if key in self:                         #this calls upon __contains__
            return reksearch(self.root, key)
        else:
            raise  KeyError ("key doesnt exist")
  
    def __contains__(self, key):
        # True om key finns i trädet, False annars
        if reksearch(self.root, key):       #if the reksearch function returns a value then that means when you write "if key in test" will return true
            return True
        else:                               #if you get None
            return False

  
    def write(self):
        # Skriver ut trädet i inorder
        rekwrite(self.root)
        print("\n")
    

def rekstore(nodeptr, key, newvalue):
    if nodeptr == None:             #If arrived at an empty node then insert a new node
        newNode = Node( key, newvalue )
        return newNode
        
    elif nodeptr.key == key:        #If arrived at a node with same key, update the data
        nodeptr.data = newvalue
        return nodeptr
        
    elif nodeptr.key < key:         #If the node has a key that is less, go to the right
        nodeptr.right = rekstore( nodeptr.right, key, newvalue)
        return nodeptr
        
    elif nodeptr.key > key:         #if the node has a key that is larger, go to the left
        nodeptr.left = rekstore( nodeptr.left, key, newvalue)
        return nodeptr


def reksearch(nodeptr, key):

    if nodeptr == None:             #in the case that you dont find what your looking for
        return None

    elif nodeptr.key == key:      #once arived at the correct node, return the value
        value = nodeptr.data
        return value            #returning the data associated with the key
    
    elif nodeptr.key < key: #if key is larger, search to the right 
        value = reksearch( nodeptr.right, key ) #the returned value will be placed into the variable named value here ( maybe i should have named the variable something else)
        return value                            #Return my variable named value
    
    elif nodeptr.key > key: #if key is smaller, search to the left
        value = reksearch( nodeptr.left, key)
        return value

def rekwrite(p):    #copied from lecture notes
    if p != None:
        rekwrite(p.left)
        print("The node contains the key:", p.key,)
        print("With the following value:",p.data,"\n")
        rekwrite(p.right)




################    Testing
# test = Bintree()
# test.store(25,1)
# test.store(15,2)
# test.store(10,3)
# test.store(4,4)
# test.store(12,5)
# test.store(22,6)
# test.store(18,7)
# test.store(24,8)
# test.store(50,9)
# test.store(35,10)
# test.store(31,11)
# test.store(44,12)
# test.store(70,13)
# test.store(66,14)
# test.store(90,15)


# print("tree consists of the following:\n")
# test.write()