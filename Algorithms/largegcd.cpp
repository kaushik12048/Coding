#include<bits/stdc++.h>
using namespace std;
long long int gcd(long long int a,long long int b)
{
  if(b==0)
     return a;
  else
     return gcd(b,a%b);
}
int main()
{
  long long int t;
  scanf("%lld",&t);
  while(t--)
  {
   long long int a,b,i,rem=0,s=0;
   string k;
   scanf("%llu",&a);
   cin>>k;
   if(a==0)
      cout<<k<<endl;
   else{
   for(i=0;i<k.length();i++)
   {  
     if(s==0)
       rem=((long long int)(k[i])-48)%a;
     else
       rem=(rem*10+((long long int)(k[i])-48))%a;
    // printf("%lld ",rem);
      s++;
   }
   printf("%llu\n",gcd(a,rem));
  }
  }
  return 0;
}
