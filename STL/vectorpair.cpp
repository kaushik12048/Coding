#include<bits/stdc++.h>
using namespace std;

int main()
{
  vector<pair< long long int,long long int> >ans;
  long long int t,s=0,m;
  scanf("%lld",&t);
  m=t;
  while(t--!=0)
   {
    long long int flag,score;
    cin>>flag>>score;
    if(flag==1)
      score-=(10*score)/100;
    else
      score+=(20*score)/100;
    ans.push_back(make_pair(score,s));
    s++;
   }
 sort(ans.begin(), ans.end());
  long long int i=0,j=1,sum=0;
  long long int arr[m];
  for(i=0;i<ans.size();i++)
   {   
         if(j==1)
         {arr[ans[i].second]=j; j+=1;}
           else
        { arr[ans[i].second]=j; j=j*2;}
        sum+=arr[ans[i].second]; 
  //printf("%lld %lld %lld\n",arr[ans[i].second],ans[i].second,sum);
   } 
  for(i=0;i<m;i++)
   printf("%lld\n",(arr[i]*100)/sum);
  return 0;
}
