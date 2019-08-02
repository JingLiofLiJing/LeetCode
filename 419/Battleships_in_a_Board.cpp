#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
	int countBattleships(vector<vector<char>>& board) {
		int result = 0;
		bool flag = false;
		for (int i = 0; i < board.size(); ++i) {
			for (int j = 0; j < board[i].size(); ++j) {
				if (board[i][j] == 'X') {
					if (i == 0 && j == 0) { flag = true; }
					else if (i == 0 && j > 0 && board[i][j - 1] == '.') { flag = true; }
					else if (j == 0 && i > 0 && board[i - 1][j] == '.') { flag = true; }
					else if (i > 0 && j > 0 && board[i - 1][j] == '.' && board[i][j - 1] == '.') { flag = true; }
					if (flag) {
						++result;
						flag = false;
					}
				}
			}
		}
		return result;
	}
};

int main() {
	vector<vector<char>> board = { {'X','X', 'X'} };
	Solution a;
	cout << a.countBattleships(board) << endl;
};