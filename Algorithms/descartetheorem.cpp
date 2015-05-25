#include<bits/stdc++.h>
using namespace std;
// Descartes theorem (k1+k2+k3+k4)^2=2*(k1^2+k2^2+k3^2+k4^2)
// k4=k1+k2+k3+2*rootof(k1.k2+k2.k3+k3.k1); 
// where k=1/r
int main()
{
  double x,y,z;
  long long int t;
  scanf("%lld",&t);
  while(t--){
  long long int a,b,c;
  scanf("%lld %lld %lld",&a,&b,&c);
  x=1.0/a;
  y=1.0/b;
  z=1.0/c;
  double ans=x+y+z+2*sqrt(x*y+y*z+x*z);
  printf("%.6lf\n",1.0/ans);
  }
  return 0;
}
