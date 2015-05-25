#include<bits/stdc++.h>
using namespace std;
long long int euler(long long int n){
	long long int i,ans=n;
	for(i=2;i<=sqrt(n);i++){
		if(n%i==0){
			ans-=ans/i;
			while(n%i==0) n/=i;
		}
	}
	if(n>1) ans-=ans/n;
	return ans;
}
int main(){
	long long int t;
	scanf("%lld",&t);
	while(t--){
		long long int x;
		scanf("%lld",&x);
		printf("%lld\n",euler(x));
	}
	return 0;
}
// Phi(p^k)=p^k-p^(k-1)
// Phi(p)=p-1 where p is a prime number
// Phi(a*b)=Phi(a)*Phi(b) where a and b are co-prime
// (p1^k1).(p2^k2)....(pm^km)=n
// n*(1-1/k1)*(1-1/k2)*....*(1-1/km)
