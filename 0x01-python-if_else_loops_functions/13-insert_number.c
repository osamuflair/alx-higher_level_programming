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
	listint_t *temp;
	listint_t *prev_node;

	new_node = malloc(sizeof(listint_t));
	new_node->n = number;

	if (new_node == NULL)
		return NULL;
	else
	{
		if (*head == NULL)
		{
			*head = new_node;
			new_node->next = NULL;
		}
		else
		{
			if ((*head)->next == NULL)
			{
				if ((*head)->n > new_node->n || new_node->n < 0)
				{
					new_node->next = (*head)->next;
					*head = new_node;
				}
				else
				{
					(*head)->next = new_node;
					new_node->next = NULL;
				}
			}
			else
			{
				temp = *head;
				
				while (1)
				{
					if (new_node->n < 0)
					{
						new_node->next = (*head)->next;
						*head = new_node;
						free(temp);
						break;
					}
					if (temp->n > new_node->n)
					{
						new_node->next = temp;
						prev_node->next = new_node;
						break;
					}
					if (temp->next == NULL)
					{
						temp->next = new_node;
						new_node->next = NULL;
						break;
					}
					prev_node = temp;
					temp = temp->next;
				}
			}
		}
	}
	return (new_node);
}
