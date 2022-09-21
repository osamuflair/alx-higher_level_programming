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
	int i;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return NULL;
	else
	{
		new_node->n = number;
		tmp = *head;

		i = 0;
		while (i < 4)
		{
			tmp = tmp->next;
			i++;
		}
		new_node->next = tmp->next;
		tmp->next = new_node;
		return (new_node);
	}
}
