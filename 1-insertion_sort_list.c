#include "sort.h"


/**
 * insertion_sort_list - implements the insertion sort algorithm
 *
 * @list: doubly linked list to be sorted
 */
void insertion_sort_list(listint_t **list)
{
	int i, j;
	listint_t *tmp, *k;

	printf("Hello\n");
	i = 0;
	tmp = (listint_t *)malloc(sizeof(*list));
	k = (listint_t *)malloc(sizeof(*list));
	if (!tmp)
		return;
	tmp = *list;
	k = tmp;
	while(k)
	{
		k = k->next;
		i++;
	}
	printf("%d", i);
	tmp = tmp->next;
	k = tmp;
	while (k)
	{
		tmp = k;
		if ((tmp->n) > (tmp->prev->n))
		{
			printf("Hi\n");
		}
		else
		{
			for (j = 0; j < i; j++)
			{
				/*printf("Ho\n");*/
				tmp->prev->next = tmp->next;
				tmp->next->prev = tmp->prev;
				tmp->next = tmp->prev;
				tmp->prev->prev->next = tmp;
				tmp->prev = tmp->prev->prev;
				print_list(*list);
			}
		}
		k = k->next;
	}
}
