#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n; // n입력
    vector<int> t(n + 1);
    vector<int> p(n + 1);
    vector<int> dp(n + 2, 0); // 최대 수익을 저장하는 DP 배열

    for (int i = 1; i <= n; i++)
    {
        cin >> t[i] >> p[i];
    }

    for (int i = 1; i <= n; i++)
    {
        if (i + t[i] <= n+1) 
        {
            dp[i + t[i]] = max(dp[i + t[i]], dp[i] + p[i]);
        }

        dp[i + 1] = max(dp[i + 1], dp[i]);
    }
    
    cout << dp[n+1] << endl;

    return 0;
}