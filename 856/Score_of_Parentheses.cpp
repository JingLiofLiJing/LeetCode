#include <iostream>
#include <stack>
#include <string>

int scoreOfParentheses(string S) {
  size_t size = S.size();
  size_t i = 0;
  std::stack<int> st;
  // 防止 "()()" 解析出现"11"的栈的情况没有聚合最后的结果，在最外面加入一层括号
  // 强制聚合，最后结果除2即可；空string情况下仍然可以有效解析不出错（1/2 = 0）
  st.emplace(-1);
  while (i <= size) {
    if (i < size && S[i] == '(') {
      st.emplace(-1);
    } else {
      bool flag = false;
      int sum = 0;
      int tmp;
      while ((tmp = st.top()) != -1) {
        flag = true;
        sum += tmp;
        st.pop();
      }
      // flag为false代表最近的括号内没有之前聚合过的数字，所以是1，如果有的话为值的两倍。
      st.top() = flag ? sum * 2 : 1;
    }
    i += 1;
  }
  // 返回栈顶结果，函数调用结束栈会自动析构。
  return st.top() / 2;
}

int main()
{
  using namespace std;
  std::string s{ "()()" };
  std:cout << scoreOfParentheses(s) << std::endl;
  return 0;
}
