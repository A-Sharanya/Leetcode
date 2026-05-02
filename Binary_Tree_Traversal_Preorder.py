class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        traverse(root, res);
        return res;
    }

private:
    void traverse(TreeNode* node, vector<int>& res) {
        if (!node) return;
        
        res.push_back(node->val);
        traverse(node->left, res);
        traverse(node->right, res);
    }
};