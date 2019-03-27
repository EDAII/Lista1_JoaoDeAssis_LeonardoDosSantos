#include <iostream>
#include <stdlib.h>
#include <string>

using namespace std;

struct Node{
	string data;
	int nSearch;
	struct Node* prev;
	struct Node* next;
};

class List{
	public:
	
	struct Node* head = NULL;
	struct Node* last = NULL;
	bool search(string data) { //TODO organizar a lista a cada busca
		int pos = 0;
	   
	   if(head==NULL) {
		  return false;
	   } 
	   struct Node* current = head;
	   while(current!=NULL) {
		  if(current->data == data) { //caso encontre o dado, aumentar o numero de vezes que foi feita a busca
			 current->nSearch +=1;
			 return true;
		  }

		 else if(current->next != NULL)
			 current = current->next;
		  else
			 break;
	   }
		return false;
	}

	void push(string newdata) { //adiciona para o começo da lista
		struct Node* newnode = (struct Node*) malloc(sizeof(struct Node)); 
		newnode->data  = newdata; 
		newnode->prev = NULL; 
	  	newnode->next = head;     
		if(head !=  NULL) head->prev = newnode;     
		head = newnode; 
	}
	void print(){ //lista todos os componentes
		struct Node* aux;
		aux = head;
		while(aux!=NULL){
			cout<<aux->data<<" "<<aux->nSearch<<endl;
			aux = aux->next;
		}
	}
	
};


void swap(Node* a, Node* b) 
{ 
    Node* temp = a; 
    a = b; 
    b = temp; 
} 

















