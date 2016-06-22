//Binary Search Tree

#include <iostream>
using namespace std;
#define LEN sizeof(struct Tree)
struct Tree{
	int key;
	struct Tree *lchild;
	struct Tree *rchild;
};

void create(struct Tree *p){
	p = new struct Tree [LEN];
	cout << "input key" << endl;
	cin >> p->key;
	static i = 0;
	if (p->key! = 0){
		create(&p->lchild);
		create(&p->rchild);
	}
}

void PreOderTraverse(struct Tree *p){//递归实现
	if (p->key){
	cout << p->key << " ";
	PreOderTraverse(p->lchild);
	PreOderTraverse(p->rchild);
	}
}

void PreOderTraverse(struct Tree *root){//C++STL实现
	if (root == NULL) return; 
	stack<struct Tree *>s; 
	s.push(root);
	while (!s.empty()) { 
		struct Tree *p=s.top();
		cout << p->key <<" ";
		s.pop();
		if (p->rchild->key != 0){
			s.push(p->rchild); 
		}
		if (p->lchild->key != 0){
			s.push(p->lchild);
		}
	}
	cout << endl;
}
void InOderTraverse(struct Tree *p){//利用父节点,重写create函数
	if(!p->key)
		return;
	struct Tree *x = NULL;
	while(1){
		if(x != p->lchild){
			while(p->lchild->key){
			p = p->lchild;
			}
		}
		cout << p->key << " ";
		if(p->rchild->key){
			p = p->rchild;
			continue;
		}
		do{
			x = p;
			p = p->parent;
			if(!p)
			return;
		}while(x == p->rchild);
	}
}
void InOderTraverse(struct Tree *p){
	if (p->key){ 
	InOderTraverse(p->lchild);
	cout << p->key <<" ";
	InOderTraverse(p->rchild);
	}
} 
void BackOderTraverse(struct Tree *p){
	if (p->key){
	BackOderTraverse(p->lchild);
	BackOderTraverse(p->rchild);
	cout << p->key << " ";
	}
}

void TREE_INSERT(struct Tree *root,struct Tree *z){
	struct Tree *y = NULL;
	struct Tree *x = root;
	while (x->key != NULL){
		y = x;
		if (z->key < x->key)
			x = x->lchild;
		else x = x->rchild;
	}
	z->parent = y;
	if (y->key == NULL){
		root = z;
	} 
	else if(z->key < y->key){
		y->lchild = z;
	}
	else y->rchild = z;
	z->lchild = new struct Tree[LEN];
	z->rchild = new struct Tree[LEN];
	z->lchild->key = z->rchild->key = 0;
}

void TRANSPLANT(struct Tree *root, struct Tree *u, struct Tree *v){
	if (u->parent->key == NULL){
		root = v;
	} 
	else if(u == u->parent->lchild){
		u->parent->lchild = v;
	}
	else u->parent->rchild = v;
	if (v->key != NULL){
		v->parent = u->parent;
	}
}

void TREE_DELETE(struct Tree *root,struct Tree *z)
{
	if (z->lchild->key == NULL){
		TRANSPLANT(root, z, z->rchild);
	}
	else if (z->rchild->key == NULL){
		TRANSPLANT(root, z, z->lchild);
	}
	else{
		struct Tree *y = TREE_MINIMUM(z->rchild);
		if (y->parent != z){
			TRANSPLANT(root, y, y->rchild);
			y->rchild = z->rchild;
			y->rchild->parent = y;
		}
		TRANSPLANT(root, z, y);
		y->lchild = z->lchild;
		y->lchild->parent = y;
	}
}

void main(){
	struct Tree *p=NULL;
	create(&p);
	cout <<"先序遍历："<<endl;
	PreOderTraverse(p);
	cout <<endl;
	cout <<"中序遍历："<<endl;
	InOderTraverse(p);
	cout <<endl;
	cout <<"后序遍历："<<endl;
	BackOderTraverse(p);
	cout <<endl;
}
