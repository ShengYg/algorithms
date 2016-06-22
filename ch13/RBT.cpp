//RedBlackTree

struct Tree *root = NULL;
void LEFT_ROTATE(struct Tree *T, struct Tree *x){
	struct Tree*y = x->right;
	x->right = y->left;
	if(y! = NULL&&y->left! = NULL){
		y->left->parent = x;
	}
	y->parent = x->parent;
	if(x->parent == NULL){
		root = y;
	}
	else if(x == x->parent->left){
	x->parent->left = y;
	}
	else x->parent->right = y;
	y->left = x;
	x->parent = y;
}

void RB_INSERT_INSERT_FIXUP(struct Tree *T,struct Tree *z){
	while (z->parent->color == RED){
	if (z->parent == z->parent->parent->left){
		struct Tree*y = z->parent->parent->right;
		if (y->color == RED){
			z->parent->color = BLACK;
			y->color = BLACK;
			z->parent->parent->color = RED;
			z = z->parent->parent;
		}
	else{
	if(z == z->parent->right){
		z = z->parent;
		LEFT_ROTATE(T,z);
	} 
	z->parent->color = BLACK;
	z->parent->parent->color = RED;
	RIGHT_ROTATE(T,z->parent->parent);
	}
}
else{
	struct Tree*y = z->parent->parent->left;
	if (y->color == RED){
		z->parent->color = BLACK;
		y->color = BLACK;
		z->parent->parent->color = RED;
		z = z->parent->parent;
	} 
	else{
		if(z == z->parent->left){
			z = z->parent;
			RIGHT_ROTATE(T,z);
		} 
		z->parent->color = BLACK;
		z->parent->parent->color = RED;
		LEFT_ROTATE(T,z->parent->parent);
	}
	root->color = BLACK;
}

void RB_INSERT(struct Tree *T,struct Tree *z){
	struct Tree*y = nil;
	struct Tree*x = root;
	while (x! = nil){
		y = x;
		if (z->key<x->key){
			x = x->left;
		}
		else x = x->right;
	}
	z->parent = y;
	if (y == nil){
		root = z;
	} 
	else if(z->key<y->key){
		y->left = z;
	}
	else y->right = z;
	z->left = nil;
	z->right = nil;
	z->color = RED;
	RB_INSERT_INSERT_FIXUP(T,z);
} 
