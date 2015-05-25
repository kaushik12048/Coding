#include<bits/stdc++.h>
using namespace std;
long long int mul_inv(long long int a, long long int b)
{
long long int b0 = b, t, q;
long long int x0 = 0, x1 = 1;
if (b == 1) return 1;
while (a > 1) {
q = a / b;
t = b, b = a % b, a = t;
t = x0, x0 = x1 - q * x0, x1 = t;
}
if (x1 < 0) x1 += b0;
return x1;
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
 ans=mul_inv(ans,p);
 ans=(ans*(p-1))%p;
 printf("%lld\n",ans);
 }
 }
 return 0;
}
