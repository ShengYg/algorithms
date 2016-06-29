#include <iostream>
#include <queue>
using namespace std;

#define N 100
#define WHITE 0
#define GRAY 1
#define BLACK 2

queue<int> Q;
struct Vertex;
struct Edge{
	int start;
	int end;
	int value;
	Edge *next;
	Edge(int s, int e, int v):start(s),end(e),value(v),next(NULL){}
};

struct Vertex{
	int color;
	int d;
	int Pie;
	Edge *head;
	Vertex():head(NULL), color(WHITE), d(0x7fffffff), Pie(0){};
};

class Link_Graph{
public:
	int n;
	Vertex *V;
	Link_Graph(int num):n(num){
		V = new Vertex[n+1];
	}
	~Link_Graph(){
		delete []V;
	}
	void AddSingleEdge(int start, int end, int value = 1){
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
	void DeleteDoubleEdge(int a, int b){
		DeleteSingleEdge(a, b);
		DeleteSingleEdge(b, a);
	}
	void OutDegree();
	void InDegree();
	void Print();
	Link_Graph* Reverse();
	Link_Graph* Square();
	void BFS(int s);
	void Print_Path(int s, int v);
};

void Link_Graph::OutDegree(){
	int i, cnt = 0;
	Edge *e;
	for(i = 1; i <= n; i++){
		cnt = 0;
		e = V[i].head;
		while(e){
			cnt++;
			e = e->next;
		}
		cout<<"顶点"<<i<<"的出度为"<<cnt<<endl;
	}
}

void Link_Graph::InDegree(){
	int ret[N+1] = {0}, i;
	Edge *e;
	for(i = 1; i <= n; i++){
		e = V[i].head;
		while(e){
			ret[e->end]++;
			e = e->next;
		}
	}
	for(i = 1; i <= n; i++)
		cout<<"顶点"<<i<<"的入度为"<<ret[i]<<endl;
}

void Link_Graph::Print(){
	int i;
	Edge *e;
	for(i = 1; i <= n; i++){
		cout<<i;
		e = V[i].head;
		while(e){
			cout<<"->"<<e->end;
			e = e->next;
		}
		cout<<endl;
	}
}

Link_Graph* Link_Graph::Reverse(){
	Link_Graph *ret = new Link_Graph(n);
	int i;
	for(i = 1; i <= n; i++){
		Edge *e = V[i].head;
		while(e){
			ret->AddSingleEdge(e->end, e->start);
			e = e->next;
		}
	}
	return ret; 
}

Link_Graph* Link_Graph::Square()
{
	int i;
	Link_Graph *ret = new Link_Graph(n);
	for(i = 1; i <= n; i++){
		Edge *e = V[i].head, *e2;
		while(e){
			ret->AddSingleEdge(e->start, e->end);
			e2 = V[e->end].head;
			while(e2){
				ret->AddSingleEdge(e->start, e2->end);
				e2 = e2->next;
			}
		e = e->next;
		} 
	}
	return ret;
}

void Link_Graph::BFS(int s){
	int i;
	for(i = 1; i <= n; i++){
		V[i].color = WHITE;
		V[i].d = 0x7fffffff;
		V[i].Pie = 0;
	}
	V[s].color = GRAY;
	V[s].d = 0;
	V[s].Pie = 0;
	while(!Q.empty())
		Q.pop();
	Q.push(s);
	while(!Q.empty()){
		int u, v;
		u = Q.front();
		Q.pop();
		Edge *e = V[u].head;
		while(e){
			v = e->end;
			if(V[v].color == WHITE){
				V[v].color = GRAY;
				V[v].d = V[u].d + 1;
				V[v].Pie = u;
				Q.push(v);
			}
			e = e->next;
		}
		V[u].color = BLACK;
	}
}

void Link_Graph::Print_Path(int s, int v)
{
	BFS(s);
	if(v == s)
		cout<<s<<' ';
	else{
		if(V[v].Pie == 0)
			cout<<"no path from "<<s<<" to "<<v<<" exists.";
		else{
			Print_Path(s, V[v].Pie);
			cout<<v<<' ';
		}
	}
}
