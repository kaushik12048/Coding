#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	scanf("%d",&t);
	while(t--){
		string a,b;
		cin>>a;
		cin>>b;
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		if(a.compare(b)==0)
		   printf("YES\n");
		else
		   printf("NO\n");
	}
	return 0;
}
