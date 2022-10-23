# before: 1-2-3-4-5-6-7
def traverse(head: ListNode) -> None:
    # if list is empty, then return
    if not head: return
    
    slow, fast, dummy = head, head, ListNode(0, head)
    # puts slow in the middle
    while fast and fast.next:
        slow = slow.next;
        fast = fast.next.next;
    #        d h     s     f
    # after: 0-1-2-3-4-5-6-7


# Original LL: 1-2-3-4-5-6-7
#     Round 1: 1-2-3-4-5-6-7  
#        Slow: s
#        Fast: f
#     Round 2: 1-2-3-4-5-6-7  
#        Slow:   s 
#        Fast:     f
#     Round 3: 1-2-3-4-5-6-7  
#        Slow:     s
#        Fast:         f
#     Round 4: 1-2-3-4-5-6-7  
#        Slow:       s
#        Fast:             f
