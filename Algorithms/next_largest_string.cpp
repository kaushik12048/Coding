#include<bits/stdc++.h>
using namespace std;
void inp(int &x)
{
register int c = getchar_unlocked();
x = 0;
for(;(c<48 || c>57);c = getchar_unlocked());
for(;c>47 && c<58;c = getchar_unlocked())
{
x = (x<<1) + (x<<3) + c - 48;
}
}
int main(){
    int t;
    inp(t);
    while(t--){
       int x,i,m,pos=-1,c=0;
      inp(x);
      int arr[x];
      for(i=0;i<x;i++){
         inp(arr[i]);
         if(i==0) continue;
         if(arr[i-1]<arr[i])
            pos=i-1;
      }
      if(pos==-1){ printf("-1\n"); continue; }
      for(i=pos+1;i<x;i++){
        if((arr[pos]<arr[i]) && i>pos) c=i;
      }
      int k=arr[pos];
      arr[pos]=arr[c];
      arr[c]=k;
      for(i=0;i<=pos;i++)
          printf("%d",arr[i]);
      for(i=x-1;i>pos;i--)
          printf("%d",arr[i]);
      printf("\n");
   }
   return 0;
}


/* Find the largest index with a[k]<a[k+1], store it in k .. if not possible then no answer exists
   then find the largest index with a[k]<a[l] store it in l
   Print the string as usual except reverse the string from the end till kth index */
  // http://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
