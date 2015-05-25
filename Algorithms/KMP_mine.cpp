#include<bits/stdc++.h>
using namespace std;
int arr[10000];
void pre(string a){
	int i,j,q,k=0;
	arr[0]=0;
	for(i=1;i<a.length();i++){
		while(k>0 && a[k]!=a[i])
		     k=arr[k-1];
		if(a[k]==a[i]) k+=1;
		arr[i]=k;
	}
}
void KMP(string a,string b){
	pre(a);
        int i,j,q,k=0,count=0,flag=0;
	for(i=0;i<b.length();i++){
		while(k>0 && a[k]!=b[i])
		    k=arr[k-1];
			k+=1;
			if(k==a.length()){
				printf("%d\n",i-a.length()+1);
				flag=1;
				i=i-a.length()+1;
				k=0;
		}
	}
	if(flag==0) printf("\n");
}
int main(){
	 int t;
	while(scanf("%d",&t)!=EOF){
		string a,b;
		cin>>a;
		cin>>b;
		KMP(a,b);
	}
	return 0;
}
