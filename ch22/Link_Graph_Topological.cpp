#include <iostream>
#include <queue>
using namespace std;

#define N 10

//边结点结构
struct Edge{
	int start;
	int end;
	Edge *next;
	int type;
	Edge(int s, int e):start(s),end(e),next(NULL){}
};

struct Vertex{
	int id;
	Edge *head;
	int degree;
	Vertex(int i):head(NULL),degree(0),id(i){}
};

struct Graph{
	Vertex *V[N+1];
	Graph(){
		int i;
		for(i = 1; i <= N; i++)
			V[i] = new Vertex(i);
	}
	~Graph(){
		int i;
		for(i = 1; i <= N; i++)
			delete V[i];
	}
};

queue<int> Q;
int time = 0;

//插入边
void InsertEdge(Graph *G, Edge *E){
	if(G->V[E->start]->head == NULL)
		G->V[E->start]->head =E;
	else{
		Edge *e1 = G->V[E->start]->head, *e2 = e1;
		while(e1 && e1->end < E->end){
			e2 = e1;
			e1 = e1->next;
		}
		if(e1 && e1->end == E->end)
			return;
		if(e1 == e2){
			E->next = e1;
			G->V[E->start]->head =E;
		}
		else{
			e2->next = E;
			E->next = e1;
		}
		G->V[E->end]->degree++;
	}
}
//拓扑排序
void Topological(Graph *G){
	while(!Q.empty())
		Q.pop();
	int i;
	for(i = 1; i <= N; i++){
		if(G->V[i]->degree == 0)
			Q.push(i);
	}
	while(!Q.empty()){
		int t = Q.front();
		Q.pop();
		cout<<char(t+'l')<<' ';
		Edge *e = G->V[t]->head;
		while(e){
			G->V[e->end]->degree--;
			if(G->V[e->end]->degree == 0)
				Q.push(e->end);
			e = e->next;
		}
	}
	cout<<endl;
}

int main(){
	Graph *G = new Graph;
	Edge *E;
	int i;
	char start, end;
	for(i = 1; i <= 14; i++){
		cin>>start>>end;
		E = new Edge(start-'p', end-'p');
		InsertEdge(G, E);
//		E = new Edge(end, start);
//		InsertEdge(G, E);
	}
	Topological(G);
	return 0;
}
