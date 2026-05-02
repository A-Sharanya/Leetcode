class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        traverse(root, res);
        return res;
    }

private:
    void traverse(TreeNode* node, vector<int>& res) {
        if (!node) return;
        
        traverse(node->left, res);
        traverse(node->right, res);
        res.push_back(node->val);
    }
};