#include<bits/stdc++.h>
using namespace std;
long long int binarysearch(long long int x,long long int arr[],long long int a)
{
  long long int low=0,high=a-1,mid;
  while(low<=high)
  {
     mid=(low+high)/2;
     if(arr[mid]==x)
        break;
     else if(arr[mid]>x)
        high=mid-1;
     else 
        low=mid+1;
   }
  if(arr[mid]==x){ while(arr[mid]==x) mid--;
    return (mid+1);}
  else
   return -1;
}    

int main()
{
  long long int i,a,b;
  scanf("%lld %lld",&a,&b);
  long long int arr[a];
  for(i=0;i<a;i++)
      scanf("%lld",&arr[i]);
  while(b--)
  {   long long int x;
      scanf("%lld",&x);
      printf("%lld\n",binarysearch(x,arr,a));
  }
  return 0;
}

