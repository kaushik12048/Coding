#include<bits/stdc++.h>
using namespace std;
int main(){
  long long int t;
  scanf("%lld",&t);
  while(t--){
   long long int n,i;
   double k=0.0;
   scanf("%lld",&n);
   for(i=1;i<=n;i++)
     k+=(double)(n/(double)i);
   printf("%.2lf\n",k);
  } 
  return 0;
}
