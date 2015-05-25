#include<bits/stdc++.h>
using namespace std;
unsigned long long int power(unsigned long long int a,unsigned long long int b)
{
 unsigned long long int c=1;

 while(b>0)
 {
   if(b%2==1)
    c=c*a;
   b=b>>1;
    a=a*a;
  }
  return c;
}
int main()
{
  unsigned long long int a,b;
  scanf("%llu %llu",&a,&b);
  printf("%llu\n",power(a,b));
  return 0;
}
