class Node(object) :

    def __init__( self , element , n = None ) :
        self.data = element
        self.next_node = n

    def get_next( self ) :
        return self.next_node

    def set_next( self , n ) :
        self.next_node = n

    def get_data( self ) :
        return self.data

    def set_data( self , element ) :
        self.data = element

    def to_string( self ) :
        return "Wartosc: " + str(self.data)


class CircularLinkedList(object) :

    def __init__( self , r = None ) :
        self.root = r
        self.size = 0

    def get_size( self ) :
        return self.size

    def add( self , element ) :
        if self.get_size() == 0 :
            self.root = Node(element)
            self.root.set_next(self.root)
        else :
            new_node = Node(element , self.root.get_next())
            self.root.set_next(new_node)
        self.size += 1

    def remove( self , element ) :
        this_node = self.root
        prev_node = None

        while True :
            if this_node.get_data() == element :  # znalzeione
                if prev_node is not None :
                    prev_node.set_next(this_node.get_next())
                else :
                    while this_node.get_next() != self.root :
                        this_node = this_node.get_next()
                    this_node.set_next(self.root.get_next())
                    self.root = self.root.get_next()
                self.size -= 1
                return True  # usuniecie
            elif this_node.get_next() == self.root :
                return False  # nie znaleziono
            prev_node = this_node
            this_node = this_node.get_next()

    def find( self , element ) :
        this_node = self.root
        while True :
            if this_node.get_data() == element :
                return element
            elif this_node.get_next() == self.root :
                return False
            this_node = this_node.get_next()

    def print_list( self ) :
        if self.root is None :
            return
        this_node = self.root
        print(this_node.to_string())
        while this_node.get_next() != self.root :
            this_node = this_node.get_next()
            print(this_node.to_string())


list = CircularLinkedList()
list.add(4)
list.add(7)
list.add(2)
list.add(11)
list.add(54)
print("Znajdz 8" , list.find(7))
print("Znajdz 12" , list.find(12))  # nie ma takie elementu, więc błąd

print("Rozmiar = " + str(list.get_size()))
list.print_list()
list.remove(7)
print("Rozmiar = " + str(list.get_size()))
