#include<bits/stdc++.h>
using namespace std;
#define SIZE 86029000
#define MAX (int)(SIZE-3)/2
int prime[MAX+1];                                                   //array that stores the primes up to sqrt(SIZE)
bitset<MAX+1> bset;                                                  //auxiliary bitset used to make the sieve
void sieve()
{
    int i,j;
    for(i=0;i*i<=SIZE;i++)                                           //we only have to get primes up to sqrt(SIZE)
        if(!bset.test(i))
             for(j=i+1;(2*j+1)*(2*i+3)<=SIZE;j++)
                  bset.set(((2*j+1)*(2*i+3)-3)/2);                   //setting all non-primes
    prime[0]=2;                                                     //store the first prime (that is 2)
    for(i=1,j=0;j<MAX+1;j++)
       if(!bset.test(j))
          prime[i++]=2*j+3;                                        //store the remaining odd primes    
}
int main()
{
  long long int t,i;
  sieve();
  scanf("%lld",&t);
  while(t--){
  long long int x;
  scanf("%lld",&x);
  printf("%d\n",prime[x-1]);
  }
  return 0;
}
