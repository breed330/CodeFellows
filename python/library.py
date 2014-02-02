# The library should be aware of a number of shelves. Each shelf should know 
# what books it contains. Make the book object have "enshelf" and "unshelf" 
# methods that control what shelf the book is sitting on. The library should 
# have a method to report all books it contains. 

# Note: this should be just a single file with three classes 
#       (plus commands at the bottom showing it works) is all that is needed. 
#
#
#
#Requirements:
#1. Library knows number of shelves
#1a. Library can report all books it contains
#2. Shelf knows what books it contains
#3. Book controls what shelf it is sitting upon
#
#
#
# Requirement #3 can lead to a bad design if it means the book references a shelf. 
#   The book should not know about the shelf; that is the job of the shelf.
#   Reading the requirements carefully, the book *controls* what shelf it is on. 
#   Will accomplish that with the categorization of books in a library. 
#   However, not sure what 'unshelf' should accomplish. 


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    enums['length'] = len(enums.values()); #3; #hard coding this since I have no idea how to get the length of this
    return type('Enum', (), enums)
    
Category = enum('Fiction','ComputerScience','History')
    
def getNextCategory(currentCategory, shouldLoop):
    '''
    Given current Category get next
    Allow to be looped, so if at end start at beginning
    Could not get enum version working with an iterator, so hard coding it 
    '''
    #     if currentCategory < Category.length -1:
    #         # get next
    #         currentCategory += 1;
    #     elif shouldLoop:
    #         # at end
    #         currentCategory = Category[0];
    if currentCategory == Category.Fiction:
        return Category.ComputerScience;
    elif currentCategory == Category.ComputerScience:
        return Category.History;
    elif shouldLoop:
        return Category.Fiction; 
    else:
        return currentCategory; ## what do when at end? Need hasNext()
    
class Library(object):
    
    def __init__(self): 
        #create all shelves
        self.shelves=[];
        i=0;
        itrCategory = Category.Fiction;
        while i < Category.length:
            s = Shelf(itrCategory);
            self.shelves.append(s); 
            i+=1;
            itrCategory = getNextCategory(itrCategory,True);
            
        
    def shelveBooks(self, books):  
        #go through each book and cycle through shelves to shelf the book
        
        for book in books:
            print("Shelf book:"+str(book));
            i = 0; #start at first shelf
            done = False;
            while not done:
                #see if room on already created shelves            
                s = self.shelves[i];
                done  = self.shelfBook(s,book);
                i += 1;
                if not done and i == len(self.shelves):
                    print("Error: Cannot shelf book: "+str(book));
                    done = True; #no more shelves
                    



    def shelfBook(self, shelf, book):
        '''
        Try to add book to shelf (see if same category)
        Return if book was shelved.
        '''
        matches = False;
        if shelf and book.enshelf(shelf):
            shelf.addBook(book);
            matches = True;        
        return matches;
    
    def printBooks(self):
        return self.prettyprint();
        
          
    def __str__(self): 
        return self.prettyprint();

    def __repr__(self):
        return self.prettyprint();
    
    def prettyprint(self):
        if not self.shelves: 
            return 'Library [empty]';
        else:
            return '--------------\n' + str(self.shelves)+ '\n-------------.';        
#end class

        
class Shelf(object):

    def __init__(self,category):
        self.books=[];
        self.category = category;

        
    def addBook(self, book):
        '''
        Add book to shelf
        '''
        if (book.enshelf(self)):
            self.books.append(book);
        
    def removeBook(self, book):
        self.books.discard(book);

    def __str__(self): 
        return self.prettyprint();

    def __repr__(self):
        return self.prettyprint();
    
    def prettyprint(self):
        return 'cat' + "-"+str(self.category)+": "+ str(self.books)+"\n";        
#end class

class Book(object):
    
    
    def __init__(self, name,category): 
        self.name = name;
        self.category = category;
    
    
    def enshelf(self,shelf):
        '''
        This controls what shelf the book is sitting upon
        Return true if the book can sit upon this shelf
        Return false if the book cannot sit upon this shelf
        '''
        if shelf and shelf.category == self.category:
            return True; 
        return False;
        
    def unshelf(self,shelf):
        pass #TODO not sure what this will do - would need to explore requirements more
    
    
    def __str__(self): 
        return self.prettyprint();

    def __repr__(self):
        return self.prettyprint();
    
    def prettyprint(self):
        return  self.name+ '.cat-'+str(self.category); 
#end class


#Arguments for library
num = 10; # number of books


print("Begin. Creating "+ str(num)+ " books.");
#create books
i = 0;

itrCategory = Category.Fiction;
books = [];
while i < num:
    i+=1;
    #create book
    name = "Title " + str(i);
    book = Book(name,itrCategory);
    books.append(book);
    itrCategory= getNextCategory(itrCategory, True);
 
#test unknown category

books.append(Book("Bad Book",5));#add book in a category that does not exist in this library
print("Creating library with shelves.");
#create library with shelves
mylibrary = Library();

print("Shelving books")
#this time do not go randomly
mylibrary.shelveBooks(books);

print("Printing books")
#print books in library
print(mylibrary.printBooks());
 
print("End");
