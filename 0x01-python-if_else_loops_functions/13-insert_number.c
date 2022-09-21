#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - a function that that inserts a number into a sorted singly linked list
 * @head: the head node
 * @number: the new data to be added
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *tmp;
	listint_t *tmp2;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return NULL;
	else
	{
		new_node->n = number;
		tmp = *head;
		if (head == NULL)
			*head = new_node;
		else
		{
			while (1)
			{
				tmp2 = tmp;
				tmp = tmp->next;
				if (tmp->n > new_node->n)
					break;
			}
			new_node->next = tmp;
			tmp2->next = new_node;
		}
	return (new_node);
	}
}
