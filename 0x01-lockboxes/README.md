# 0x01 lockboxes




# Requirements

## General

1. Allowed editors: vi, vim, emacs
2. All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
4. All your files should end with a new line
5. The first line of all your files should be exactly #!/usr/bin/python3
6. A README.md file, at the root of the folder of the project, is mandatory
7. Your code should be documented
8. Your code should use the PEP 8 style (version 1.7.x)
9. All your files must be executable









### Task
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

1. Prototype: def canUnlockAll(boxes)
2. boxes is a list of lists
3. A key with the same number as a box opens that box
4. You can assume all keys will be positive integers
5. There can be keys that do not have boxes
6. The first box boxes[0] is unlocked
7. Return True if all boxes can be opened, else return False


```

carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
```


output
```
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
```
