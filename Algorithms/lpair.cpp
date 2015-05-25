#include<bits/stdc++.h>
using namespace std;
#define MAX 100005
vector<pair<long long int,long long int > >k;
long long int arr[MAX];
long long int temp[MAX];
void inp(long long int &x)
{
register long long int c = getchar_unlocked();
x = 0;
for(;(c<48 || c>57);c = getchar_unlocked());
for(;c>47 && c<58;c = getchar_unlocked())
{
x = (x<<1) + (x<<3) + c - 48;
}
}
long long int merge(long long int arr[],long long int temp[],long long int a,long long int b,long long int c){
 long long int l,r,j,c1=0,i;
 l=a;
 r=b;
 j=a;
 while(l<=b-1 && r<=c){
  if(arr[l]<=arr[r])
     temp[j++]=arr[l++];
  else
  {  c1+=b-l;
     temp[j++]=arr[r++];  
  }
  }
  while(l<=b-1) temp[j++]=arr[l++];
  while(r<=c) temp[j++]=arr[r++];
  for(i=a;i<j;i++)
     arr[i]=temp[i];
  return c1;
  }
long long int invcount(long long int arr[],long long int temp[],long long int a,long long int b){
long long int c=0,mid;
 if(a<b){
 mid=(a+b)/2;
 c+=invcount(arr,temp,a,mid);
 c+=invcount(arr,temp,mid+1,b);
 c+=merge(arr,temp,a,mid+1,b);}
 return c;
}

int main()
{
  long long int a;
  inp(a);
  k.clear();
  long long int i,l,r;
 
  for(i=0;i<a;i++){
      inp(l);
      inp(r);
      k.push_back(make_pair(l,r));
  }
  sort(k.begin(),k.end());
  memset(arr,0,sizeof(arr));
  for(i=0;i<a;i++)
     arr[i]=k[i].second;
  printf("%lld\n",invcount(arr,temp,0,a-1));

  return 0;
}
