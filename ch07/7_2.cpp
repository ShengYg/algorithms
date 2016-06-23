#include <iostream> 
#include <time.h> 
using namespace std; 
int PARTITION(int A[], int p, int r){//T(n) = O(r-p)+O(r-p)+O(t-r+1) = O(r-p)
	int x = A[r]; 
	int i = p - 1, k = 0, t = r; 
	for (int j = p; j < r-1; j++){
		if(A[j] == x) { 
			if(A[j]! = A[r-1]){ 
				swap(A[j], A[r-1]); 
				r--; 
			} 
			else{ 
				j--;r--; 
			} 
		} 
	} 
	for (j = p; j<= r - 1; j++){ 
		if (A[j]<= x) { 
			i++; 
			swap(A[i], A[j]); 
		} 
	} 
	for (int h = 0; h < t - r + 1; h++){
		swap(A[i + h + 1], A[r + h]); 
	} 
	return i + 1; 
} 

int RANDOMIZED_PARTITION(int A[], int p, int r) { 
	srand( (unsigned)time( NULL ) ); 
	int i = rand() % (r - p + 1) + p, k = 0; 
	swap(A[r], A[i]); 
	return PARTITION(A, p, r, k); 
} 

void QUICKSORT(int A[], int p, int r) { 
	int k = 0; 
	if (p < r){ 
		int q = PARTITION(A, p, r, k);
		int t = q + k - 1; 
		QUICKSORT(A, p, q - 1);
		QUICKSORT(A, t + 1, r); 
	} 
} 


