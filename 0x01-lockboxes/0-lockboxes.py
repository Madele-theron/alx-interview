#!/usr/bin/python3
"""A method to determine if all the boxes can be opened"""


def canUnlockAll(boxes):
    """A Function that will return True if all boxes are unlocked"""
    keyList = []
    stillLocked = []
    boxesUnlocked = []

    for box in boxes:
        currentPosition = boxes.index(box)
        if currentPosition == 0:
            boxesUnlocked.append(currentPosition)

            if not box:
                print("box is empty, no keys found")
            # maybe I can add a else if currentPosition !== 0
            # && currentPosition in keyList:...
            else:
                keysInBox = []
                for key in box:
                    print("key:", key)
                    keysInBox.append(key)
                    keyList.append(key)
                print(f"boxes[{currentPosition}] -> {keysInBox}")
        else:
            if currentPosition in keyList:
                if currentPosition not in boxesUnlocked:
                    boxesUnlocked.append(currentPosition)
                keysInBox = []
                for key in box:
                    print("key:", key)
                    keysInBox.append(key)
                    keyList.append(key)
                print(f"boxes[{currentPosition}] -> {keysInBox}")
            else:
                print(f"box[{currentPosition}] is locked, we don't have a key")
                stillLocked.append(currentPosition)
    if not stillLocked:
        print("we've unlocked all the boxes")
        return "YAY"
    else:
        print(f"boxes that are still locked: {stillLocked}")
        print(f"saved keys: {keyList}")
        for box in list(stillLocked):
            print("current box:", box)
            if box in keyList:
                keysInBox = []
                for key in boxes[box]:
                    keysInBox.append(key)
                    keyList.append(key)
                print(f"boxes[{box}] -> {keysInBox}")
                print(f"saved keys: {keyList}")
                if box not in boxesUnlocked:
                    boxesUnlocked.append(box)
                stillLocked.remove(box)
                print(f"boxes still locked {stillLocked}, removed box {box}")
                print(f"boxes unlocked: {sorted(boxesUnlocked)}")
                print(f"boxes that are still locked: {stillLocked}")
            print("current box:", box)
        print("current box:", box)
        print("still locked:", stillLocked)
        if not stillLocked:
            return True
        print("THESE BOXES ARE STILL LOCKED", stillLocked)
        return False


boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[], [1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
