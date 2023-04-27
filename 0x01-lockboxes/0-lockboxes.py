#!/usr/bin/python3
"""A method to determine if all the boxes can be opened"""


def get_keys(main_list, indices):
    """
    Flattens a list of lists by extracting the elements of the
    sublists specified by the given indices.
    Gets the keys of the specified boxes.

    Args:
        main_list (list): A list of lists to be flattened. -> boxes
        indices (list): A list of indices to be used to access the
        sublists in the first argument.

    Returns:
        list: A flattened list containing the elements of the sublists
        specified by the given indices.
    """
    keys = []
    for i in indices:
        keys += main_list[i]
    return keys


def canUnlockAll(boxes):
    """
    Determines whether all the boxes in a list can be unlocked.

    Args:
        boxes (list): A list of lists, where each sublist represents the
        list of keys required to open a box.

    Returns:
        bool: True if all the boxes can be unlocked, False otherwise.
    """
    index = 0
    saved_keys = list(set(boxes[0]) | {0})
    new_keys_added = True

    while new_keys_added:
        new_keys_added = False
        for j in get_keys(boxes, saved_keys[index:]):
            if j not in saved_keys:
                saved_keys.append(j)
                index += 1
                new_keys_added = True
    return len(saved_keys) == len(boxes)
