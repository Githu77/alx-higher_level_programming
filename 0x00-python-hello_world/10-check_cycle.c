#include "lists.h"

/**
* check_cycle - checks for cycle
* @list: head of pointer
* Return: 0 or 1
*
*
*
*
*
*/

int check_cycle(listint_t *list)
{
	listint_t *w;
	listint_t *w1;

	w = list;
	w1 = list;
	while (list && w && w->n)
	{
		list = list->n;
		w = w->next->n;

		if (list == w)
		{
			list = w1;
			w1 = w;
			while (1)
			{
				w = w1;
				while (w->n != list && w->n != w1)
				{
					w = w1->n;
				}
				if (w->n == list)
					break;

				list = list->n;
			}
			return (1);
		}
	}

	return (0);
}
