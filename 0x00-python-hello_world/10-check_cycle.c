#include "lists.h"

/**
 * check_cycle - Checks if as singly linked list has a cycle in it
 * @list: This is points to the head
 * Return: 0 no cyle , 1 when there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *step1, *step2;

	if (list == NULL)
		return (0);
	step1 = list;
	step2 = list;

	while (step1 != NULL && step2 != NULL && step2->next != NULL)
	{
		step1 = step1->next;
		step2 = step2->next->next;
		if (step1 == step2)
			return (1);
	}
	return (0);
}
