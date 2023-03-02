from data_structures.array import Array
from data_structures.binary_search_tree import BST
from data_structures.doubly_linked_list import DoublyLinkedList
from data_structures.graph import Graph
from data_structures.hash_table import HashTable
from data_structures.queue import Queue
from data_structures.singly_linked_list import LinkedList
from data_structures.stack import Stack


def array_ds():
    arr = Array()

    print("\nPushing...")
    arr.push(1)
    arr.push(4)
    arr.push(7)
    arr.push(10)

    print("\nArray: ", arr)

    print("\nPoping...")
    print(arr.pop())
    print(arr.pop())
    print(arr.pop())
    print(arr.pop())

    print("\n1Array: ", arr)


def hash_table_ds():
    ht = HashTable(3)

    ht.set("grapes", 100)
    ht.set("apples", 200)
    ht.set("lemons", 300)
    ht.set("oranges", 400)

    print("\nHash Table: ", ht)

    print("\nGrapes: ", ht.get("grapes"))
    print("\nApples: ", ht.get("apples"))
    print("\nLemons: ", ht.get("lemons"))
    print("\nOranges: ", ht.get("oranges"))

    print("\nKeys: ", ht.keys())


def singly_linked_list_ds():
    ll = LinkedList(14)

    ll.append(16)
    ll.append(20)

    ll.prepend(12)
    ll.prepend(10)

    ll.insert(0, 8)
    ll.insert(5, 18)
    ll.insert(9, 22)

    ll.remove(0)
    ll.remove(6)

    print("\nLinked List: ", ll)
    print("\nLinked List (Array): ", ll.listify())


def doubly_linked_list_ds():
    dll = DoublyLinkedList(5)

    dll.append(7)

    dll.prepend(3)

    dll.insert(0, 1)
    dll.insert(5, 9)

    dll.remove(4)

    print("\nDoubly Linked List: ", dll)
    print("\nDoubly Linked List (Array): ", dll.listify())


def stack_ds():
    stk = Stack()

    print(f"\nIs the stack empty? {stk.is_empty()}")

    stk.push(3)
    stk.push(2)
    stk.push(1)
    stk.push(8)
    stk.push(5)

    print("\nPushed 5 items")
    print("\nStack: ", stk)
    print("\nStack (Array): ", stk.listify())
    
    stk.pop()
    stk.pop()

    print("\nPopped 2 items")
    print("\nStack: ", stk)
    print("\nStack (Array): ", stk.listify())

    print(f"\nPeek: {stk.peek()}")
    print(f"\nIs the stack empty? {stk.is_empty()}")
    


def queue_ds():
    q = Queue()

    print(f"\nIs the queue empty? {q.is_empty()}")

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print("\nEnqueued 5 items")
    print("\nQueue: ", q)
    print("\nQueue (Array): ", q.listify())
    
    q.dequeue()
    q.dequeue()

    print("\nDequeued 2 items")
    print("\nQueue: ", q)
    print("\nQueue (Array): ", q.listify())

    print(f"\nPeek: {q.peek()}")
    print(f"\nIs the queue empty? {q.is_empty()}")

def bst_ds():
    print("BSTs aren't implemented accurately yet.")
    
    bt = BST()

    bt.insert(20)
    bt.insert(4)
    bt.insert(9)
    bt.insert(1)
    bt.insert(170)
    bt.insert(6)
    bt.insert(15)

    print("\nBinary Search Tree: ", bt)

def graph_ds():
    g = Graph()

    g.add_vertex("0")
    g.add_vertex("1")
    g.add_vertex("2")
    g.add_vertex("3")
    g.add_vertex("4")
    g.add_vertex("5")
    g.add_vertex("6")

    g.add_edge("3", "1")
    g.add_edge("3", "4")
    g.add_edge("4", "2")
    g.add_edge("4", "5")
    g.add_edge("1", "2")
    g.add_edge("1", "0")
    g.add_edge("0", "2")
    g.add_edge("6", "5")

    g.show_adjacency_list()
    