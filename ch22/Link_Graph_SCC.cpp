//SCC:Strongly Connected Component

#include <iostream>
using namespace std;

#define N 10
#define WHITE 0
#define GRAY 1
#define BLACK 2



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
	int color;
	Vertex *p;
	int d, f;
	Vertex(int i):head(NULL),color(WHITE),p(NULL),d(0x7fffffff),id(i){}
};

struct Graph{
	Vertex *V[N+1];//N个顶点
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

int time = 0;
bool flag = 0;
int Sort[N+1] = {N};


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
	}
}
 
Graph* Reverse(Graph *G){
	Graph *ret = new Graph;
	int i;
	for(i = 1; i <= N; i++){
		Edge *E = G->V[i]->head;
		while(E){
			Edge *e = new Edge(E->end, E->start);
			InsertEdge(ret, e);
			E = E->next;
		}
	}
	return ret;
}

void DFS_Visit(Graph *G, Vertex *u){
	if(flag)cout<<char('p'+u->id)<<' ';
	u->color = GRAY;
	time++;
	u->d = time;
	Vertex *v;
	Edge *e = u->head;
	while(e){
		v = G->V[e->end];
		if(v->color == WHITE){
			v->p = u;
			DFS_Visit(G, v);
			e->type = 1;
		}
		else if(v->color == GRAY){
			e->type = 2;
		}
		else if(v->color == BLACK){
			if(u->d < v->d)
				e->type = 3;
			else
				e->type = 4;
		}
		e = e->next;
	}
	u->color = BLACK;
	time++;
	u->f = time;
	if(flag == 0){
		Sort[Sort[0]] = u->id;
		Sort[0]--;
	}
}

void DFS(Graph *G){
	int i;
	for(i = 1; i <= N; i++)
	{
		G->V[i]->id = i;
		G->V[i]->color = WHITE;
		G->V[i]->p = NULL;
	}
	time = 0;
	for(i = 1; i <= N; i++){
		int j;
		if(flag == 0)
			j = i;
		else j = Sort[i];	//!!!!!
		if(G->V[j]->color == WHITE){
			DFS_Visit(G, G->V[j]);
			if(flag)cout<<endl;
		}
	}
}
void Strongly_Connected_Component(Graph *G){
	DFS(G);
	Graph *G2 = Reverse(G);
	flag = 1;
	DFS(G2);
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
		//无向图，要加两条边 
		//E = new Edge(end, start); 
		//InsertEdge(G, E); 
	}
	Strongly_Connected_Component(G);
	return 0;
}


