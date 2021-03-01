#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int data;
    struct node* next;
} Node;

void append(Node* head, int data) {
    Node* item = (Node*)malloc(sizeof(Node));
    item->data = data;
    item->next = NULL;
    
    Node* temp;
    temp = head;
    while(temp->next != NULL) {
        temp=temp->next;
    }
    temp->next = item;
}

int count(Node* head) {
  if (head==NULL) {
    return 0;
  }
  else {
    return (1+count(head->next));
  }
}

int getLastNode (Node* head, int k) {
    // 현재 위치를 계산하기 위한 변수
    int idx = 0;
    // 연결리스트의 길이 계산 함수
    int c = count(head)-1;
    // 답을 담아놓는 변수
    int answer = 0;

    printf("----------------------");

    Node* temp;
    temp = head;

    // 연결리스트의 끝이 될때까지 반복
    while(temp->next != NULL) {
        if(c - idx == k) {
            answer = temp->next->data;
        }
        idx++;
        temp=temp->next;
    }

    return answer;
}


void printList(Node* head) {
    while(head->next != NULL) {
        printf("%d ", head->next->data);
        head = head->next;
    }
    printf("\n");
}

int main() {
    Node* head = (Node*)malloc(sizeof(Node));
    append(head, 9);
    append(head, 8);
    append(head, 4);
    append(head, 14);
    append(head, 5);
    append(head, 10);
    append(head, 11);

    printList(head);

    printf("\n%dth last node is %d\n", 2, getLastNode(head, 2));
}