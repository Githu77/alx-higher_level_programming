#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
* struct listint_s - singly linked list
* @x: integer
* @n: points to the next node
* Description: singly linked structure
* 
*/
typedef struct listint_s
{
    int x;
    struct listint_s *n;
} listint_t;


int check_cycle(listint_t *list);

#endif
