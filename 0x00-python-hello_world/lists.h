#ifndef LISTS_H
#define LISTS_H

/* Struct for a node in the list */
typedef struct Node {
    int data;
    struct Node* next;
} Node;

/* Function prototypes */
Node* createNode(int data);
void insertNode(Node** head, int data);
void deleteNode(Node** head, int data);
void printList(Node* head);

#endif /* LISTS_H */
