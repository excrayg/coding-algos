// Print all permutations of a string without recursion, you can use a stack

// time: from 7:26 to 8:15
#include "utils.h"
#include <utility>
#include <stack>
using std::stack;
using std::make_pair;
using std::pair;

vector<string> getp(string s) {
  int n = s.length();
  if (n == 0) return vector<string>();
  vector<string> res;
  bool fetch = false;
  stack<pair<int, int> > st;
  int i = 0, j = 0;
  int count = 1;
  for (int k = 1; k <= n; ++k) count *= k;
  while (res.size() < count) {
    if (fetch) { // we reached the end of last turn and now we fetch a pre status
      pair<int, int> ptmp = st.top();
      st.pop();
      std::swap(s[ptmp.first], s[ptmp.second]); // restore the pre exchange
      if (ptmp.second == n - 1) continue; // if this status can not go further, we continue fetch
      fetch = false;                      // else we can continue this status by move j to next position
      i = ptmp.first, j = ptmp.second + 1;
    } else {
      if (i == n - 1 && j == n - 1) { // if reach the end, save this string
        res.push_back(s);
        fetch = true; // the end of this turn and should pick a status from the stack
        continue;
      }
      std::swap(s[i], s[j]); // exchange the two
      st.push(make_pair(i, j)); // save the exchange status
      ++i;   // start to get the permutations from i + 1, i + 1
      j = i; // 
    }
  }
  return res;
}

int main() {
    print(getp("a"));
    print(getp("ab"));
    print(getp("abc"));
    print(getp("abcd"));
    
    return 0;
}