#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
int is_palindrome(listint_t **head)
{
	int a;

	if ((*head) == 0 || (*head)->next == 0)
		a = 1;
	else
	{
		listint_t **end;
		listint_t *temp;
		listint_t *prev_node;

		temp = prev_node = *head;
		while (temp->next != 0)
		{
			prev_node = temp;
			temp = temp->next;
		}
		if ((*head)->n != temp->n)
			a = 0;
		else
		{
			prev_node->next = 0;
			(*head) = (*head)->next;
			end = &(*head);
			is_palindrome(end);

		}
	}
	free(*head);
	return a;
}
