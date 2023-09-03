#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """
    x = len(boxes)
    boxes_seen = set([0])
    boxes_unseen = set(boxes[0]).difference(set([0]))
    while len(boxes_unseen) > 0:
        y = boxes_unseen.pop()
        if not y or y >= x or y < 0:
            continue
        if y not in boxes_seen:
            boxes_unseen = boxes_unseen.union(boxes[y])
            boxes_seen.add(y)
    return x == len(boxes_seen)
