#include<stdio.h>
#include<stdlib.h>
struct node{
int data;
struct node* next;
};
struct node *head= NULL;
void InsertAtBeg(int data);
void InsertAtEnd(int data);
void DeleteAtBeg();
void DeleteAtEnd();
void Print();
int main(){

    int choice;
    while(choice!=6){
        printf("");
        scanf("%d",&choice);
        switch(choice){

        case 1:{printf("Enter value of element\n");
                int data;
                scanf("%d",&data);
                InsertAtBeg(data);
                break;
                }
        case 2:{printf("Enter value of element\n");
                int data;
                scanf("%d",&data);
                InsertAtEnd(data);
                break;
                }
        case 3:{
                Print();
                break;
                }
        case 4:{
                DeleteAtBeg();
                break;
                }
        case 5:{
                DeleteAtEnd();
                break;
                }
        case 6:{
                exit(0);
                }

        }
    }

return 0;
}
void InsertAtBeg(int data){


    struct node *temp=(struct node*)malloc(sizeof(struct node));
    if(head==NULL){
    temp->data=data;
    head=temp;
    temp->next=NULL;
    }
    else{
        temp->data = data;
        temp->next = head;
        head = temp;
    }
}

void Print(){
    if(head==NULL){
        printf("Linked list is empty\n");
    }
    else{
        struct node *temp;
    temp=head;
    while(temp){
        printf("%d ",temp->data);
        temp = temp->next;
    }
    }printf("\n");
}

void InsertAtEnd(int data){
    struct node *temp=(struct node*)malloc(sizeof(struct node));
    if(head==NULL)
    {
        //LL is empty
        temp->data = data;
        temp->next = NULL;
        head = temp;
    }
    else{
        struct node *newnode =head;
        temp->data=data;
        temp->next = NULL;
        while(newnode->next){
            newnode = newnode->next;
        }
        newnode->next = temp;
    }
}
void DeleteAtBeg(){
    if(head==NULL){
        printf("Linked list is empty\n");
    }
    else{
        printf("%d deleted from beginning successfully.\n",head->data);
        head = head->next;
    }
}
void DeleteAtEnd(){
    if(head==NULL){
        printf("Linked list is empty\n");
    }
    else{
        struct node *temp = (struct node*)malloc(sizeof(struct node*));
        struct node *prev = (struct node*)malloc(sizeof(struct node*));
        temp = head;
        while(temp->next){
            prev = temp;
            temp = temp->next;
        }
        printf("%d deleted from end successfully.\n",temp->data);
        prev->next = NULL;
    }
}
