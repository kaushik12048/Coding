#include<bits/stdc++.h>
using namespace std;
int main()
{
  long long int a,b;
  while(1){
  long long int i,j;
  scanf("%lld %lld",&a,&b);
  if(a==0 && b==0)
     break;
  long long int arr[b],val[b],dp[a+1],m;
  memset(dp,0,sizeof(dp));
  for(i=0;i<b;i++)
     scanf("%lld %lld",&arr[i],&val[i]);
  for(i=0;i<b;i++)
     for(j=a;j>=arr[i];j--)
         dp[j]=max(dp[j],dp[j-arr[i]]+val[i]);
  m=a;
  while(dp[m]==dp[a])
       m--;
  printf("%lld %lld\n",m+1,dp[a]);
  }
  return 0;
}
