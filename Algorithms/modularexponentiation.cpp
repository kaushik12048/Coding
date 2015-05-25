#include<bits/stdc++.h>
using namespace std;
long long int mod(long long int x,long long int y,long long int m){
  long long int ans=1;
   while(y>0)
   {
    if(y%2==1)
     ans=(ans*x)%m;
    y=y>>1;
    x=(x*x)%m;
   }
  return ans;
}
int main()
{
   long long int test;
  scanf("%lld",&test);
  while(test--)
  {
    long long int x,y,m,t;
   scanf("%lld %lld %lld",&x,&y,&m);
   printf("%lld\n",mod(x,y,m));
   }
  return 0;
}
