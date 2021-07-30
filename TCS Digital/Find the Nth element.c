#include <stdio.h>
#include<malloc.h>
struct node{
int data;
  struct node *next;
};
struct node *head=NULL;
int printList( int pos)
{
  struct node*temp;
  temp=head;
  int count=1;
  while(temp->next!=NULL)
  {
    if(count==pos)
    {
      printf("%d",temp->data);
      return 0;
    }
    else{count+=1;
    temp = temp->next;}
  }
  printf("No node found");
}
void print(){
    struct node *temp=head;
    while(temp)
    {
        printf("%d-->",temp->data);
        temp = temp->next;
    }
}

void addLast( int val)
{
    struct node *temp=(struct node*)malloc(sizeof(struct node*));
  if(head==NULL){
  		//LL is empty
    	temp->data = val;
    	temp->next=NULL;
    	head=temp;
  				}
  else{
  		struct node *Node = (struct node*)malloc(sizeof(struct node*));
    	Node=head;
    while(Node->next){
    			Node=Node->next;
    			}
    		temp->data=val;
    		temp->next = NULL;
  			Node->next = temp;
  }
}
int main()
{
 int size;
  scanf("%d",&size);
  while(size--){
    int val;
    scanf("%d",&val);
    addLast(val);
  }
 // print(head);
  //printf("\n\n");
  int pos;
  scanf("%d",&pos);
  printList( pos);
}