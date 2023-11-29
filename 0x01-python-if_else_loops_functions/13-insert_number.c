#include "lists.h"
#include  <stddef.h>

/**
 * insert_node - This block of code insert a node
 * @head: a pointer to the first node
 * @number: number for the insertion
 * Return: this will ret a new list on success
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new_node;

	new_node = malloc(sizeof(listint_t)); /*dynamically allocating memory for new node*/
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if ((current == NULL) || ((current->n) > (new_node->n)))
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}
	while (current->next != NULL)
	{
		if ((current->next->n) > (new_node->n))
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		else
			current = current->next;
	}
	current->next = new_node;
	return (new_node);
}
