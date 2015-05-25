#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
//fibonacci function in log n from here: http://ronzii.wordpress.com/2011/07/09/using-matrix-exponentiation-to-calculated-nth-fibonacci-number/
long long int fibonacci(long long int n){
    long long fib[2][2]= {{1,1},{1,0}},ret[2][2]= {{1,0},{0,1}},tmp[2][2]= {{0,0},{0,0}};
    long long int i,j,k;
    while(n){
        if(n&1){
            memset(tmp,0,sizeof tmp);
            for(i=0; i<2; i++) for(j=0; j<2; j++) for(k=0; k<2; k++)
                 tmp[i][j]=(tmp[i][j]+ret[i][k]*fib[k][j])%mod;
            for(i=0; i<2; i++) for(j=0; j<2; j++) ret[i][j]=tmp[i][j];
        }
        memset(tmp,0,sizeof tmp);
        for(i=0; i<2; i++) for(j=0; j<2; j++) for(k=0; k<2; k++)
            tmp[i][j]=(tmp[i][j]+fib[i][k]*fib[k][j])%mod;
        for(i=0; i<2; i++) for(j=0; j<2; j++) fib[i][j]=tmp[i][j];
        n/=2;
    }
    return (ret[0][1]);
}
int main(){
	long long int t;
	scanf("%lld",&t);
//	printf("%lld\n",fibonacci(3));
	while(t--){
		long long int x,y;
		scanf("%lld %lld",&x,&y);
		//printf("%lld %lld\n",fibonacci(x+1),fibonacci(y+2));
		printf("%lld\n",(fibonacci(y+2)-fibonacci(x+1)+mod)%mod);
	}
	return 0;
}
