#include "lists.h"
/**
 * check_cycle: A function that checks if a list has a cycle
 * list: A linked list
 * return: 1 if cycle is present or 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *hd, *tl; /* hd is head, tl is tail */
	if (!list || !list->next)
		return (0);
	hd = list;
	tl = list;
	while (tl != NULL && hd != NULL && hd->next != NULL)
	{
		tl = tl->next;
		hd = hd->next->next;
		if (tl == hd)
		{
			return (1);
		}
	}
	return (0);
}
