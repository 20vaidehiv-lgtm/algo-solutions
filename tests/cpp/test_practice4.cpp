#include <cassert>

#define main solution_main
#include "../../solutions/cpp/practice4.cpp"
#undef main

int main() {
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->right = new TreeNode(7);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);

    TreeNode* inv = invertTree(root);
    assert(inv->val == 4);
    assert(inv->left->val == 7);
    assert(inv->right->val == 2);
    assert(inv->right->left->val == 3);
    assert(inv->right->right->val == 1);
    assert(invertTree(nullptr) == nullptr);
    return 0;
}

