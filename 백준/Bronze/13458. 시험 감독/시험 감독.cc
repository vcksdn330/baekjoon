#include <iostream>
#include <vector>
using namespace std;

int main() {
    long long n, b, c;
    long ct, ans = 0;
    cin >> n;
    vector<int> stu(n);

    for (int i = 0; i < n; i++)
    {
        cin >> stu[i];
    }
    cin >> b >> c;

    for (int q = 0; q < n; q++)
    {
        stu[q] -= b;
        ct = 1;        
        if(stu[q] > 0)
        {
            ct += stu[q] / c;
            if (stu[q] % c != 0) ct ++;
        }
        ans += ct;
    }
    cout << ans << endl;
    return 0;
}