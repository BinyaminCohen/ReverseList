class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    prev = None
    current = head

    while current:
        next_node = current.next  # Temporarily save the next node: 2 3
        current.next = prev  # Reverse the current node's pointer: none 1
        prev = current  # Move prev and current one step forward :1 2
        current = next_node # 2 3
    return prev  # Prev will be the new head of the reversed list


# Example Usage:
# Creating a linked list 1->2->3->None
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

# Reversing the linked list
reversed_head = reverse_list(node1)


# Now the list is 3->2->1->None

# Function to print list contents
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Print the reversed list
print_list(reversed_head)
