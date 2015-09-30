// # Question:
// # The awards committee had planned to give n research grants this year, out of a its total yearly budget.
// # However, the budget was reduced to b dollars. The committee members has decided to affect the minimal number of highest grants, by applying a maximum cap c on all grants: every grant that was planned to be higher than c will now be c dollars.
// # Help the committee to choose the right value of c that would make the total sum of grants equal to the new budget.
// # Given an array of grants g and a new budget b, explain and code an efficient method to find the cap c.
// # Analyze the time and space complexity of your solution.

// time: from 19:13 to

#include "utils.h"
#include <algorithm>
using std::sort;

int getC(vector<int> &g, int b) {
    int n = g.size();
    if (n == 0) return 0;
    int total = 0;
    for (int j = 0; j < n; ++j) total += g[j];
    int dif = total - b;
    if (dif <= 0) return g[n - 1];
    int sub = 0;
    sort(g.begin(), g.end());
    // first find proper index that would be lower than b
    int i = n - 2;
    for (i = n - 2; i >= 0; --i) {
        sub += (g[i + 1] - g[i]) * (n - i - 1);
        if (sub >= dif) break;
    }
    // when we reduce the max grant to g[i], the total now is less than b
    if (sub == dif) return g[i];
    int res = g[i];
    // try to find the best max grant
    while (sub > dif) {
        sub -= (n - i - 1);
        ++res;
    }
    return res;
}


int main() {
    
    vector<int> g;
    g.push_back(3);
    g.push_back(1);
    g.push_back(5);
    g.push_back(4);
    g.push_back(7);
    g.push_back(9);
    //total 29
    // budget 28:8, 27:7, 25:6, 23:5, 20:4, 6:1
    cout << getC(g, 28) << endl;
    cout << getC(g, 27) << endl;
    cout << getC(g, 25) << endl;
    cout << getC(g, 23) << endl;
    cout << getC(g, 20) << endl;
    cout << getC(g, 6) << endl;
    return 0;
}
