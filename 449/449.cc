/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:
using Iter = std::vector<int32_t>::const_iterator;

	std::string ListToString(const std::vector<int32_t>& lst) {
		std::string res{"["};
		std::size_t sz = lst.size();
		for (std::size_t i = 0ul; i < sz; ++i) {
			if (i > 0ul) {
				res += ',';
			}
			res += std::to_string(lst[i]);
		}
		res += ']';
		return res;
	}

	std::vector<int32_t> StringToList(const std::string& text) {
		if (text.size() < 3ul) {
			return {};
		}
		std::size_t start = 1ul;
		std::vector<int32_t> res;
		const char* data = text.c_str();
		while (true) {
			auto pos = text.find(',', start);
			int32_t val = std::atoi(data + start);
			res.push_back(val);
			if (pos == std::string::npos) {
				break;
			}
			start = pos + 1;
		}
		return res;
	}
	
	void Insert(TreeNode* root, std::vector<int32_t>& res) {
		if (root) {
			res.push_back(root -> val);
			Insert(root->left, res);
			Insert(root->right, res);
		}
	}

	// Encodes a tree to a single string.
	string serialize(TreeNode* root) {
		std::vector<int32_t> res;
		Insert(root, res);
		return ListToString(res);
	}

	TreeNode* Trans(Iter a_beg, Iter a_end, Iter b_beg, Iter b_end) {
		if (a_beg == a_end) {
			return nullptr;
		}
		int32_t val = *a_beg;
		TreeNode* ret = new TreeNode(val);
		auto pos = std::find(b_beg, b_end, val);
		auto gap = pos - b_beg;
		Iter l1 = a_beg + 1, l2 = l1 + gap;
		ret->left = Trans(l1, l2, b_beg, pos);
		ret->right = Trans(l2, a_end, pos + 1, b_end);
		return ret;
	}

	// Decodes your encoded data to tree.
	TreeNode* deserialize(string data) {
		std::vector<int32_t> a = StringToList(data), b = a;
		std::sort(b.begin(), b.end());
		return Trans(a.begin(), a.end(), b.begin(), b.end());
	}
};

// Your Codec object will be instantiated and called as such:
// Codec* ser = new Codec();
// Codec* deser = new Codec();
// string tree = ser->serialize(root);
// TreeNode* ans = deser->deserialize(tree);
// return ans;
