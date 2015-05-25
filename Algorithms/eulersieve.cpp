#include<bits/stdc++.h>
using namespace std;
#define MAX  1000001
long long int arr[MAX],temp[MAX],eulersieve[MAX];
void prime(long long int arr[],long long int i,long long int n)
{
  long long int a=2;
  while(a*i<=n)
  {
     arr[a*i]=1;
     a++;
   }
}
long long int sieve(long long int s){
 long long int i;
 memset(arr,0,sizeof(arr));
 memset(temp,0,sizeof(temp));
 arr[0]=1;
 arr[1]=1;
 for(i=2;i<=(MAX);i++)
 {
    if(arr[i]==0){
    temp[s++]=i; 
    prime(arr,i,MAX);
    }  
   }
  return s;
}
void euler(long long int n){
	long long int i,j;
	 for(i=0;i<=n;i++)
	    eulersieve[i]=i;
	 for(i=2;i<=n;i++){
	 	if(arr[i]==0)
	 	 for(j=i;j<=n;j+=i)
	 	   eulersieve[j]-=eulersieve[j]/i;
	 }
}
int main()
{
  long long int s=0,i,t;
  s=sieve(s);
  euler(1000000);
  scanf("%lld",&t);
  while(t--){
  	long long int x;
  	scanf("%lld",&x);
  	printf("%lld\n",eulersieve[x]);
    }  
	return 0;
}
