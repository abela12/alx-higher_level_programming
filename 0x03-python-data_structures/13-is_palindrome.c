#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * is_palindrome - check if linked list is a palindrome
 * @head: pointer to pointer to head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int size = sizeof(int);
	int i = 1;
	int left = 0;
	int right = i - 1;
	int *arr = malloc(100000 * sizeof(int));

	arr[0] = (*head)->n;

	if (*head == NULL)
		return (1);

	temp = temp->next;

	while (temp != NULL)
	{
		size += sizeof(int);
		arr = realloc(arr, size);
		arr[i] = temp->n;
		i++;
		temp = temp->next;
	}
	for (; left < right; left++, right--)
	{
		if (arr[left] != arr[right])
			return (0);
	}
	return (1);
}