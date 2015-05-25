#include<bits/stdc++.h>
using namespace std;
int main()
{
  int a,i,m=0,ans=-999;
  scanf("%d",&a);
  int arr[a];
  for(i=0;i<a;i++)
  { scanf("%d",&arr[i]);
    m=max(0,m+arr[i]);
    ans=max(ans,m);
   }
  printf("%d\n",ans);
  return 0;
}
