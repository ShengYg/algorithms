#include <iostream>
#include <queue>
using namespace std;

#define N 100
#define WHITE 0
#define GRAY 1
#define BLACK 2

queue<int> Q;
class Mat_Graph
{
public:
	int n;
	int color[N+1];
	int d[N+1];
	int Pie[N+1];
	int Map[N+1][N+1];

	Mat_Graph(int num):n(num){
		memset(Map, 0, sizeof(Map));
	}

	void AddDoubleEdge(int a, int b, int value = 1){
		AddSingleEdge(a, b, value);
		AddSingleEdge(b, a, value);
	}

	void AddSingleEdge(int start, int end, int value = 1){
		Map[start][end] = value;
	}

	void DeleteDoubleEdge(int a, int b){
		DeleteSingleEdge(a, b);
		DeleteSingleEdge(b, a);
	}

	void DeleteSingleEdge(int start, int end){
		Map[start][end] = 0;
	}

	void Print();

	Mat_Graph* Reverse();

	Mat_Graph* Square();

	bool Universal_Sink();

	void BFS(int s);

	void Print_Path(int s, int v);
};

void Mat_Graph::Print(){
	int i, j;
	for(i = 1; i <= n; i++){
		for(j = 1; j <= n; j++){
			cout<<Map[i][j]<<' ';
			cout<<endl;
		}
	}
}

Mat_Graph* Mat_Graph::Reverse(){
	int i, j;
	Mat_Graph *ret = new Mat_Graph(n);
	for(i = 1; i <= n; i++){
		for(j = 1; j <= n; j++)
			if(Map[i][j])
				ret->AddSingleEdge(j, i);
	}
	return ret;
}

Mat_Graph* Mat_Graph::Square(){
	int i, j, k;
	Mat_Graph *ret = new Mat_Graph(n);

	for(i = 1; i <= n; i++){
		for(j = 1; j <= n; j++){
			if(Map[i][j]){
				ret->AddSingleEdge(i, j);
				for(k = 1; k <= n; k++)
					if(Map[j][k])
						ret->AddSingleEdge(i, k);
			}
		}
	}
	return ret;
}

bool Mat_Graph::Universal_Sink(){
	int i = 1, j = 1;
	while(j <= n){
		if(Map[i][j] == 0)
			j++;
		else if(i == j){
			i++;
			j++;
		}
		else i = j;
	}

	if(i > n)
		return false;
	else{
		for(j = 1; j <= i-1; j++){
			if(Map[i][j] == 1)
				return false;
		}
		for(j = 1; j <= n; j++)
			if( i != j && Map[j][i] == 0)
				return false;
		return true;
	}
}

void Mat_Graph::BFS(int s){
	int u, v;
	for(u = 1; u <= n; u++){
		color[u] = WHITE;
		d[u] = 0x7fffffff;
		Pie[u] = 0;
	}
	color[s] = GRAY;
	d[s] = 0;
	Pie[s] = 0;
	while(!Q.empty())
		Q.pop();
	Q.push(s);
	while(!Q.empty())
	{
		u = Q.front();Q.pop();
		for(v = 1; v <= n; v++){
			if(Map[u][v] == 0)
				continue;
			if(color[v] == WHITE){
				color[v] = GRAY;
				d[v] = d[u] + 1;
				Pie[v] = u;
				Q.push(v);
			}
		}
		color[u] = BLACK;
	}
}

void Mat_Graph::Print_Path(int s, int v){
	BFS(s);
	if(v == s)
		cout << s<<' ';
	else{
		if(Pie[v] == 0)
			cout<<"no path from "<<s<<" to "<<v<<" exists."<<endl;
		else{
			Print_Path(s, Pie[v]);
			cout<<v<<' ';
		}
	}
}

