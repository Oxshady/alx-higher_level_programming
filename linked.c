#include <stdio.h>
#include <stdlib.h>
// typedef struct Node
// {
// 	int x;
// 	struct Node* next;

// }Node;

// int main()
// {
// 	Node root;
// 	root.x = 3;
// 	root.next = malloc(sizeof(Node *));
// 	root.next->x = 5;
// 	root.next->next = NULL;
// 	Node *curr = &root;
// 	while (curr)
// 	{
// 	printf("node one %i\n",curr->x);
// 	curr = curr->next;
// 	}

// 	// printf("node one %i\n",root.x);
// 	// printf("node two %i\n",root.next->x);
// 	free(root.next);
// return (0);
// }
////////////// double liked list
typedef struct node
{
	int x;
	struct node *next;
	struct node *prev;
} Node;
int main(void)
{
	Node *tail = malloc(sizeof(Node));
	Node *head = malloc(sizeof(Node));
	if (tail == NULL || head == NULL)
		exit(1);
	tail->x = 1;
	tail->prev = NULL;
	tail->next = malloc(sizeof(Node));
	if (tail->next == NULL)
		return (2);
	tail->next->x = 3;
	tail->next->prev = tail;
	tail->next->next = malloc(sizeof(Node));
	if (tail->next->next == NULL)
		return (3);
	tail->next->next->x = 7;
	tail->next->next->prev = tail->next;
	tail->next->next->next = NULL;
	head = tail->next->next;

	// Node* curr = tail;
	// while (curr)
	// {
	// 	printf("%d\n", curr->x);
	// 	curr = curr->next;
	// }
	Node* curr = head;
	while (curr)
	{
		printf("%d\n", curr->x);
		curr = curr->prev;
	}
	
	return (0);
}
// 
