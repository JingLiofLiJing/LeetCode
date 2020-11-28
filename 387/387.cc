#include <unordered_map>
#include <utility>
#include <algorithm>

class Solution {
public:
    int firstUniqChar(string s) {
        int a[26]={0};
        int len=s.length(),i;
        for(i=0;i<len;i++)
           ++a[s[i]-'a'];
        for(i=0;i<len;i++)
           if(a[s[i]-'a']==1)
             return i;
        return -1;
    }
};
