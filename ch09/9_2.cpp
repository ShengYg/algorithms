#include <iostream>
#include <time.h>
using namespace std;
const n = 8;
int PARTITION(int A[], int p, int r);

int RANDOM(int p, int r){
	int t = rand()%(r - p + 1) + p;
	return t;
}

int RANDOMIZED_PARTITION(int A[], int p, int r){
	int i = RANDOM(p, r);
	swap(A[r], A[i]);
	return PARTITION(A, p, r);
}

int PARTITION(int A[], int p, int r){
	int x = A[r];
	int i = p - 1;
	for (int j = p; j <= r-1; j++){
		if (A[j] <= x){
			i++;
			swap(A[i] ,A[j]);
		}
	}
	swap(A[i + 1] ,A[r]);
	return i + 1;
}

int RANDOMIZED_SELECT(int A[], int p, int r, int i){
	if (p == r){
		return A[p];
	}
	int q = RANDOMIZED_PARTITION(A, p, r);
	int k = q - p + 1;
	if (i == k){
		return A[q];
	}
	else if(i < k){
		return RANDOMIZED_SELECT(A, p, q - 1, i);
	}
	else 
		return RANDOMIZED_SELECT(A, q + 1, r, i - k);
}

void main(){
	//int A[n] = {43,11,29,82,0,89};
	int A[n] = {0};
	srand( (unsigned)time( NULL ) );
	for (int i = 0; i < n; i++){
		A[i] = rand()%100;
		cout << A[i] << " ";
	}
	cout << endl;
	cout << RANDOMIZED_SELECT(A, 0, 7, 2) << endl;
}
