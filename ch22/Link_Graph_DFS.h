#include <iostream>
#include <queue>
using namespace std;

#define N 100

#define WHITE 0
#define GRAY 1
#define BLACK 2

#define NONE 0
#define TREE 1
#define BACK 2
#define FORWARD 3
#define CROSS 4

struct Edge{
	int start;
	int end;
	int value;
	int type;	//TREE, BACK, FORWARD, CROSS
	Edge *next;
	Edge(int s, int e, int v)
		:start(s),end(e),value(v),type(NONE),next(NULL){}
};

struct Vertex{
	int d, f;
	int color;
	int p;
	Edge *head;
	Vertex():color(WHITE),p(0),head(NULL){};
};

class Link_Graph{
public:
	int time;
	int n;
	Vertex *V;
	Link_Graph(int num):n(num){
		V = new Vertex[n+1];
	}
	~Link_Graph(){
		delete []V;
	}
	void AddSingleEdge(int start, int end, int value = 1)
	{
		Edge *NewEdge = new Edge(start, end, value);
		if(V[start].head == NULL || V[start].head->end > end){
			NewEdge->next = V[start].head;
			V[start].head = NewEdge;
		}
		else{
			Edge *e = V[start].head, *pre = e;
			while(e != NULL && e->end < end){
				pre = e;
				e = e->next;
			}
			if(e && e->end == end){
				delete NewEdge;
				return;
			}
			NewEdge->next = e;
			pre->next = NewEdge;
		}
	}
	void AddDoubleEdge(int a, int b, int value = 1){
		AddSingleEdge(a, b, value);
		AddSingleEdge(b, a, value);
	}
	void DeleteSingleEdge(int start, int end){
		Edge *e = V[start].head, *pre = e;
		while(e && e->end < end){
			pre = e;
			e = e->next;
		}
		if(e == NULL || e->end > end) return;
		if(e == V[start].head)
			V[start].head = e->next;
		else
			pre->next = e->next;
		delete e;
	}
	void DeleteDoubleEdge(int a, int b)
	{
		DeleteSingleEdge(a, b);
		DeleteSingleEdge(b, a);
	}
	void DFS();
	void DFS_Visit(int u);
	void Print_Vertex_Time();
	void Print_Edge_Type();
};

void Link_Graph::DFS(){
	int u;
	for(u = 1; u <= n; u++){
		V[u].color = WHITE;
		V[u].p = NULL;
	}
	time = 0;
	for(u = 1; u <= n; u++)
		if(V[u].color == WHITE)
			DFS_Visit(u);
}

void Link_Graph::DFS_Visit(int u){
	int v;
	Edge *e;
	V[u].color = GRAY;
	time++;
	V[u].d = time;
	e = V[u].head;
	while(e){
		v = e->end;
		if(V[v].color == WHITE){
			V[v].p = u;
			DFS_Visit(v);
			e->type = TREE;
		}
		else if(V[v].color == GRAY){
			e->type = BACK;
		}
		else if(V[v].color == BLACK){
			if(V[u].d < V[v].d)
				e->type = FORWARD;
			else
				e->type = CROSS;
		}
		e = e->next;
	}
	V[u].color = BLACK;
	time++;
	V[u].f = time;
}

void Link_Graph::Print_Vertex_Time(){
	int i;
	for(i = 1; i <= n; i++){
	cout<<char('p'+i)<<':';
	cout<<V[i].d<<' '<<V[i].f<<endl;
	}
}

void Link_Graph::Print_Edge_Type(){
	int i;
	for(i = 1; i <= n; i++){
		Edge *e = V[i].head;
		while(e){
			cout<<char(e->start+'p')<<"->"<<char(e->end+'p')<<": ";
			switch (e->type){
				case TREE:
					cout<<"树边"<<endl;
					break;
				case BACK:
					cout<<"反向边"<<endl;
					break;
				case FORWARD:
					cout<<"正向边"<<endl;
					break;
				case CROSS:
					cout<<"交叉边"<<endl;
					break;
			}
			e = e->next;
		}
	}
}
