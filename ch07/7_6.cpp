#include <iostream>
#include <ctime>
using namespace std;
struct IntervalType{
	int a;
	int b;
};

void Exchange(IntervalType interArry[],int i,int j){
	IntervalType tmpInterval = interArry[i];
	interArry[i] = interArry[j];
	interArry[j] = tmpInterval;
}

void Partition(IntervalType interArr[], int oBeg, int oEnd, int &preEnd, int &postBeg){
	IntervalType midInterval = interArr[oEnd];
	int i = oBeg - 1;
	int j = oEnd + 1;
	for(int k = oBeg; k < j && k < oEnd; k++){
		if(interArr[k].b < midInterval.a)
		{
			i++;
			Exchange(interArr, k, i);
		}
		else if(interArr[k].a > midInterval.b)
		{
			j--;
			Exchange(interArr, k, j);
			k--;
		}
		else
		{
			midInterval.a = max(midInterval.a, interArr[k].a);
			midInterval.b = min(midInterval.b, interArr[k].b);
		}
	}
	preEnd = i;
	postBeg = j;
	return;
}

void IntervalQuickSort(IntervalType interArr[], int iBeg, int iEnd){
	if(iBeg >= iEnd)
		return;
	int preEnd, postBeg;
	Partition(interArr, iBeg, iEnd, preEnd, postBeg);
	IntervalQuickSort(interArr, iBeg, preEnd);
	IntervalQuickSort(interArr, postBeg, iEnd);
	return ;
}


