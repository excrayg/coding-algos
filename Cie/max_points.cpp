// Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.


// time: from 5:54 to 6:10

struct Point {
 int x;
 int y;
 Point() : x(0), y(0) {}
 Point(int a, int b) : x(a), y(b) {}
};


int maxPoints(vector<Point>& points) {
    int n = points.size();
    if (n < 3) return n;
    int xi, yi, xj, yj; // (x,y) of i and (x,y) of j
    double k; // gradient of line(i,j)
    int res = 0, tmpres, same; // same represents for the points same to i
    for (int i = 0; i < n; ++i) {
        Point pi = points[i];
        xi = pi.x, yi = pi.y;
        int v = 0; // vertical lines containing i
        tmpres = 0, same = 1; // at first there's only one point same to i, that's itself
        unordered_map<double, int> count; // the count of line of the same gradient
        for (int j = i + 1; j < n; ++j) {
            Point pj = points[j];
            xj = pj.x, yj = pj.y;
            if (xj == xi && yj == yi) {
                ++same;
            } else if (xj == xi) {
                ++v;
                if (v > tmpres) tmpres = v;
            } else {
                k = (double)(yj - yi) / (xj - xi);
                if (count.find(k) == count.end()) count[k] = 1;
                else ++count[k];
                if (count[k] > tmpres) tmpres = count[k];
            }
        }
        tmpres += same;
        res = max(res, tmpres);
    }
    return res;
}
