#include<bits/stdc++.h>
using namespace std;
int main(){
  long long int i;
  vector<long long int> s;
  for(i=0;i<5;i++)
    s.push_back(i);
  vector<long long int>::iterator k;
  for(k=s.begin();k!=s.end();k++)
    printf("%lld\n",*k);
  return 0;
}
