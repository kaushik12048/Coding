#include<bits/stdc++.h>
using namespace std;
#define MAX 10000
struct comp {
    bool operator() (const pair<int,int> &a, const pair<int,int> &b) {
        return a.second > b.second;
    }
};
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
map<string,int> mapp;
int main(){
   int m,n,i,j,u,v,w,src,dest,edges,testcases,t;
   inp(t);
   while(t--){
   inp(m);
   vector<pair<int,int> > vec[m+1];
   for(i=0;i<m;i++)
      vec[i+1].clear();
   mapp.clear();
   bool visited[m+1];
   char name[MAX],s[MAX],d[MAX];
   for(i=0;i<m;i++){
     scanf("%s",name);
     mapp[(string)(name)]=i+1;
     inp(edges);
     for(j=0;j<edges;j++){
     inp(v);
     inp(w);
     vec[i+1].push_back(make_pair(v,w));
    // vec[v].push_back(make_pair(i+1,w));
     }
   }
   inp(testcases);
   while(testcases--){
   scanf("%s",s);
   scanf("%s",d);
   src=mapp[(string)(s)];
   dest=mapp[(string)(d)];
   vector<int>dist(m+1,INT_MAX);
   memset(visited,0,sizeof(visited));
   dist[src]=0;
   priority_queue<pair<int,int>,vector<pair<int,int> >,comp> PQ;
   PQ.push(make_pair(src,0));
   while(PQ.size()>0){
   u=PQ.top().first;
   PQ.pop();
   if(u==dest)
      break;
   for(i=0;i<vec[u].size();i++){
       v=vec[u][i].first;
       w=vec[u][i].second;
       if(visited[v]==false && dist[u]+w<dist[v]){
          dist[v]=dist[u]+w;
          PQ.push(make_pair(v,dist[v]));
       }
   }
   visited[u]=true;
   }
   printf("%d\n",dist[dest]);
   }
   printf("\n");
   }
   return 0;
}
