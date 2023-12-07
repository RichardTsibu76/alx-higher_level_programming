#include "lists.h"
/**
 * is_palindrome - checks for palindrom
 * @head: Points to the first node
 * Return: returns
 */


int is_palindrome(listint_t **head)
{
	listint_t *first, *last, *current = *head;
	int elements = 1, idx, half;

	for (; *head != NULL && current->next != NULL; elements++)
		current = current->next;
	if (*head == NULL || elements == 1)
		return (1);
	first = *head;
	last = current;
	half = (elements / 2) - 1;

	while (((first->n) == (last->n)) && half > 0)
	{
		first = first->next;
		last = *head;
		elements--;
		half--;

		for (idx = 1; idx < elements; idx++)
			last = last->next;
	}

	if ((half == 0) && ((first->n) == (last->n)))
		return (1);
	return (0);
}
