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
	while (list && w && w->next)
	{
		list = list->next;
		w = w->next->next;

		if (list == w)
		{
			list = w1;
			w1 = w;
			while (1)
			{
				w = w1;
				while (w->next != list && w->next != w1)
				{
					w = w1->next;
				}
				if (w->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
