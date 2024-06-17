# Data Structures and Algorithms Project

## Introduction
This project aims to explore and implement various search and sorting algorithms, which are fundamental in the study of data structures and algorithms (DSA). These algorithms are widely used to solve complex problems efficiently.

## Search Algorithms

### Linear Search
Linear Search is the simplest algorithm for searching an element in a list. It sequentially checks each element of the list until the desired element is found or the end of the list is reached.

**Time Complexity:** O(n), where n is the number of elements in the list.

### Binary Search
Binary Search is a more efficient algorithm than linear search but requires the list to be sorted. It repeatedly divides the list in half and compares the middle element with the target value, reducing the search space by half each step.

**Time Complexity:** O(log n), where n is the number of elements in the list.

## Sorting Algorithms

### Bubble Sort
Bubble Sort is a simple sorting algorithm that compares adjacent elements and swaps them if they are in the wrong order. This process is repeated until the list is sorted.

**Time Complexity:** O(n²), where n is the number of elements in the list.

### Selection Sort
Selection Sort selects the smallest element from the list and places it in the first position, then the second smallest, and so on. This process is repeated until the entire list is sorted.

**Time Complexity:** O(n²), where n is the number of elements in the list.

### Insertion Sort
Insertion Sort builds the sorted list one item at a time, inserting each new element into its correct position.

**Time Complexity:** O(n²), where n is the number of elements in the list.

### Merge Sort
Merge Sort is a sorting algorithm based on the divide and conquer technique. It divides the list into smaller sublists, sorts them, and then merges them to obtain the final sorted list.

**Time Complexity:** O(n log n), where n is the number of elements in the list.

### Quick Sort
Quick Sort is also based on the divide and conquer technique. It selects a pivot and partitions the list into two sublists: one with elements less than the pivot and the other with elements greater. The sublists are then sorted recursively.

**Time Complexity:** O(n log n) on average, where n is the number of elements in the list.
