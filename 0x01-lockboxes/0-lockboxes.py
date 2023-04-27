#!/usr/bin/python3
"""A method to determine if all the boxes can be opened"""


def canUnlockAll(boxes):
    """A Function that will return True if all boxes are unlocked"""
    key_list = []
    still_locked = []
    boxes_unlocked = []

    for box in boxes:
        current_position = boxes.index(box)
        if current_position == 0:
            boxes_unlocked.append(current_position)

            if not box:
                continue
            # maybe I can add a else if current_position !== 0
            # && current_position in key_list:...
            else:
                keys_in_box = []
                for key in box:
                    keys_in_box.append(key)
                    key_list.append(key)
        else:
            if current_position in key_list:
                if current_position not in boxes_unlocked:
                    boxes_unlocked.append(current_position)
                keys_in_box = []
                for key in box:
                    keys_in_box.append(key)
                    key_list.append(key)
            else:
                still_locked.append(current_position)
    if not still_locked:
        return True
    else:
        for box in list(still_locked):
            if box in key_list:
                keys_in_box = []
                for key in boxes[box]:
                    keys_in_box.append(key)
                    key_list.append(key)
                if box not in boxes_unlocked:
                    boxes_unlocked.append(box)
                still_locked.remove(box)
        if not still_locked:
            return True

        return False


boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[], [1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
