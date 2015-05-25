#include<bits/stdc++.h>
using namespace std;
int findmin(int dist[],bool visited[],int n){
  int val=INT_MAX,index=0,i;
  for(i=0;i<n;i++)
    if(dist[i]<=val && visited[i]==false){
        val=dist[i];
        index=i;
    }
  return index;
}
int main()
{
   int t;
   scanf("%d",&t);
   while(t--){
   int m,n,a,b,c,dest;
   scanf("%d",&n);
   int grph[n][n];
   memset(grph,0,sizeof(grph));
   int i,j,src,u,v;
   scanf("%d",&m);
   while(m--){
     scanf("%d %d %d",&a,&b,&c);
     grph[a-1][b-1]=c;
   }
   scanf("%d %d",&src,&dest);
   src-=1;
   bool visited[n];
   memset(visited,false,sizeof(visited));
   int dist[n];
   for(i=0;i<n;i++)
      dist[i]=INT_MAX;
   dist[src]=0;
   for(i=0;i<n-1;i++){
     u=findmin(dist,visited,n);
     visited[u]=true;
     for(v=0;v<n;v++)
       if(grph[u][v]!=0 && visited[v]==false)
         dist[v]=min(dist[v],dist[u]+grph[u][v]);
     }
   if(dist[dest-1]==INT_MAX)
      printf("NO\n");
   else
      printf("%d\n",dist[dest-1]);
   }
   return 0;
}
