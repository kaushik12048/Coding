#include<bits/stdc++.h>
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
int main(){
 long long int t;
 scanf("%lld",&t);
 while(t--){
 long long int n,p,ans=1,i;
 scanf("%lld %lld",&n,&p);
 if(n>=p)
    printf("0\n");
 else{
 for(i=p-1;i>=n+1;i--) // Wilson's theorem applied. (p-1)!%p=(p-1)%p 
    ans=(ans*i)%p;
 ans=mod(ans,p-2,p);   // Fermat's little theorem applied. (x^y)%y=x and (x^(y-1))%y=1; where x<y
 ans=(ans*(p-1))%p;
 printf("%lld\n",ans);
 }
 }
 return 0;
}
