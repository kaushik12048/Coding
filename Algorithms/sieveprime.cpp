#include<bits/stdc++.h>
using namespace std;
#define MAX 100000
long long int arr[MAX];
void compute(long long int arr[],long long int j){
  long long int a=2;
  while((j*a)<=MAX){
   arr[j*a]=1;
   a++;
   }
}
void prefill(){
  long long int i;
  memset(arr,0,sizeof(arr));
  for(i=2;i<=MAX;i++){
   if(arr[i]==0){ 
   compute(arr,i); } }
}
int main()
{
  long long int t,i;
  prefill();
  scanf("%lld",&t);
  for(i=2;i<=t;i++) if(arr[i]==0) printf("%lld ",i);
  return 0;
}
