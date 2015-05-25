#include<bits/stdc++.h>
using namespace std;
int gcd(int a,int b)
{
  if(b==0)
     return a;
  else
     return gcd(b,a%b);
}
int numfactors(int n){
  int ans=0,i;
  for(i=1;i<=sqrt(n);i++){
     if(n%i==0 && i*i!=n)
         ans+=2;
     else if(i*i==n)
         ans+=1;
  }
  return ans;
}
int main(){
  int t;
  scanf("%d",&t);
  while(t--){
  int x,y,ans,i,sum=0;
  scanf("%d %d",&x,&y);
  if(x>y)
    ans=gcd(x,y);
  else
    ans=gcd(y,x);
  printf("%d\n",numfactors(ans));
  }
  return 0;
}
