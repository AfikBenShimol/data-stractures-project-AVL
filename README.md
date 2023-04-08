# data-stractures-project-AVL

This is the first programming project in data structures course. </br>
In this project we will implement an ADT of a List using an AVL tree. </br>

- [AVL Tree List class](#AVL-Tree-List-Class)
    - [functions & time complexity table](#AVLTreeList-functions-&-time-complexity)  
- [Authors](#authors)

## AVL Tree List Class

AVL Tree List include the implementation of the list's functionality and the methods that the user will use.
Behind the scenes the list is saved in a self balancing binary tree (AVL tree) that maintaines a size attribute in each node. Size of a node is the size of the tree whose root is the node.

### AVLTreeList functions & time complexity

| Function      | Description                                                                                                                                | Time Complexity | 
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| empty()       | Returns true if and only if the list is empty.                                                                                             | O(1)            |
| retrieve(i)   | Returns the value of the i'th element in the list if exist, if not, returns None.                                                          | O(log(n))       |
| insert(i,s)   | Inserts the value s in index i if there are at least i element in the list and Return num of rotations made while fixing the AVL.          | O(log(n))       |
| delete(i)     | Removes the i'th element from the list if exists and Return num of rotations made while fixing the AVL or -1 if the element doesn't exist. | O(log(n))       |
| first()       | Returns the value of the first element in the list and or None if it's empty.                                                              | O(1)            |
| last()        | Returns the value of the last element in the list and or None if it's empty.                                                               | O(1)            |
| listToArray() | Returns an array with of the list's elements in the index order, or empyy array if the list is empty.                                      | O(n)            |
| length()      | Returns the number of elements in the list.                                                                                                | O(1)            | 
| permutation() | Returns new list with the same elements in random order.                                                                                   | O(n)     |
| sort()        | Returns new list with the same elements in sorted order.                                                                                   | O(n*log(n))     |
| concat(lst)   | Concats lst to the end of the list and returns the absulute value of the height difference between the list and lst.                       | O(log(n))       |
| search(val)  | Returns the first index of the element with the given value in the list or -1 if it doesnt exist.                                          | O(n)            |

## Authors

- Dor Liberman ([dorlib](https://github.com/dorlib))
- Afik Ben Shimol ([AfikBenShimol](https://github.com/AfikBenShimol))

If you have any questions or feedback, I would be glad if you will contact me via mail.

<p align="left">
  <a href="afik1200@gmail.com"> 
    <img alt="Connect via Email" src="https://img.shields.io/badge/Gmail-c14438?style=flat&logo=Gmail&logoColor=white" />
  </a>
</p>

This project was created for educational purposes, for personal and open-source use.

If you like my content or find my code useful, give it a :star:

