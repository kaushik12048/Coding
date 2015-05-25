#include<bits/stdc++.h>
using namespace std;
int arr[1000005];
int main(){
	int t,i,x,temp,a,b,c,l;
	scanf("%d",&t);
	set<int> s[10];
	set<int>::iterator it,ok;
    for(i=0;i<t;i++){
    	scanf("%d",&arr[i]);
    	if(arr[i]%2==0) s[2].insert(i);
    	if(arr[i]%3==0) s[3].insert(i);
    	if(arr[i]%5==0) s[5].insert(i);
    }
    scanf("%d",&x);
    while(x--){
    	scanf("%d",&temp);
    	if(temp==1){
    		scanf("%d %d %d",&a,&b,&c);
    		a-=1;
    		b-=1;
    		ok=lower_bound(s[c].begin(),s[c].end(),a);
    		vector<int> vec;
    		for(it=ok;it!=s[c].end();it++){
    			if(*it>b) break;
    			arr[*it]/=c;
    			if(arr[*it]%c!=0) vec.push_back(*it);
    		}
    		for(i=0;i<vec.size();i++) s[c].erase(vec[i]);
    	}
    	if(temp==2){
    		scanf("%d %d",&a,&b);
    		a-=1;
    	if(arr[a]%2==0) s[2].erase(a);
    	if(arr[a]%3==0) s[3].erase(a);
    	if(arr[a]%5==0) s[5].erase(a);
    	
    	if(b%2==0) s[2].insert(a);
    	if(b%3==0) s[3].insert(a);
    	if(b%5==0) s[5].insert(a);
    	arr[a]=b;
    	}
    }
    for(i=0;i<t;i++)
        printf("%d ",arr[i]);
    printf("\n");
    return 0;
}
    
