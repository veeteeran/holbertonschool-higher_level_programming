#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

size_t len_listint(const listint_t *h);
/**
 * is_palindrome - checks if list is a palimdrome
 * @head: pointer to pointer to head of list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, start, size, end;
	int *array;

	if (*head == NULL || head == NULL)
		return (1);

	size = len_listint(*head);
	array = malloc(sizeof(int) * size);
	if (array == NULL)
		return (0);

	current = *head;
	i = 0;
	while (current != NULL)
	{
		array[i] = current->n;
		current = current->next;
		i++;
	}
	end = size - 1;
	for (start = 0; start < size / 2; start++, end--)
	{
		if (array[start] != array[end])
			return (0);
	}
	free(array);
	return (1);
}

/**
 * len_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t len_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}

	return (n);
}
