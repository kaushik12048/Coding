#include<bits/stdc++.h>
using namespace std;
int main(){
  long long int t;
  scanf("%lld",&t);
  while(t--){
  long long int h,m;
  double ans;
  scanf("%lld %lld",&h,&m);
  if(h>=24 || m>=60){
     printf("Invalid Time\n"); continue; }
  else{
     long long int a1=(h*60-11*m)/2;
     long long int a2=((h*60-11*m)%2);
     a1%=360;
     double ans=(double)(a1)+(double)(a2/2.0);
     if(ans<0.0){ 
         ans=ans*(-1); }
     if(ans>180.0)
         ans=360.0-ans;
     printf("%.1lf\n",ans);
     }
  }
  return 0;
}
