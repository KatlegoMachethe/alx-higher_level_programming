#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list is a cycle
 * Return: 1 if list is a cycle, otherwise zer0
 */

int check_cycle(listint_t *list)
{
	listint_t *speed = list;
	listint_t *speed_low = list;

	if (!list)
		return (0);
	while (1)
	{
		if (speed->next != NULL && speed->next->next != NULL)
		{
			speed = speed->next->next;
			speed_low = speed_low->next;
			if (speed == speed_low)
				return (1);
		}
		else
			return (0);
	}
}
