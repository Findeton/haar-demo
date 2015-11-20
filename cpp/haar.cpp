#include <deque>
#include <cmath>
#include <iostream>
#include <tuple>

using namespace std;

void print(deque<double> d, bool end = false);
void print(deque<deque<double>> d);
pair<deque<double>,deque<double>> haar_level(const deque<double>& f);
deque<deque<double>> haar(deque<double> f);
deque<double> inverse_haar_level(const deque<double>& a, const deque<double>& d);
deque<double> inverse_haar(const deque<deque<double>>& h);

int main()
{
    deque<double> data = {4,6,10,12,8,6,5,5};
    print(data, true);
    auto res = haar(data);
    print(res);
    print(inverse_haar(res), true);
    return 0;
}

void print(deque<double> d, bool end)
{
    cout << "[ " ;
    for (auto i: d)
        cout << i << ", ";
    cout << " ] " << (end? "\n" : "");
    
}

void print(deque<deque<double>> d)
{
    cout << "[ ";
    for(auto i: d)
        print(i);
    cout << " ]" << endl;
}

pair<deque<double>,deque<double>> haar_level(const deque<double>& f)
{
    deque<double> a, d;
    static const double base = 1.0 / pow(2, 0.5);
    auto n = f.size() / 2;
    for (size_t i = 0; i < n; ++i)
    {
        a.push_back(base*(f[2*i] + f[2*i+1]));
        d.push_back(base*(f[2*i] - f[2*i+1]));
    }
    return make_pair(a, d);
}

deque<deque<double>> haar(deque<double> f)
{
    size_t n = log2(f.size());
    cout << "n " << n << endl;
    deque<double> A;
    size_t m = pow(2, n);
    for(size_t i = 0; i < m; ++i)
        A.push_back(f[i]);
    deque<deque<double>> res;
    while (A.size() > 1)
    {
        deque<double> D;
        tie(A, D) = haar_level(A);
        res.push_front(D);
    }
    res.push_front(A);
    return res;
}

deque<double> inverse_haar_level(const deque<double>& a, const deque<double>& d)
{
    static const double base = 1.0 / pow(2, 0.5);
    deque<double> res;
    for (size_t i = 0; i < a.size(); ++i)
    {
        res.push_back(base*(a[i] + d[i]));
        res.push_back(base*(a[i] - d[i]));
    }
    return res;
}

deque<double> inverse_haar(const deque<deque<double>>& h)
{
    auto an = h[0];
    for (size_t i = 1; i < h.size(); ++i)
        an = inverse_haar_level(an, h[i]);
    return an;
}