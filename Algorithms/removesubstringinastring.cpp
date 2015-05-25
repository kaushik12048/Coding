#include<bits/stdc++.h>
using namespace std;
int main(){
	long long int t;
	while(scanf("%lld",&t)!=EOF){
		string s,x;
		cin>>s;
		while(t--){
			cin>>x;
		   string::size_type done = 0;
           while( std::string::npos != (done = s.find(x, done) ) ){s.erase(done,x.length());;}
			  
		}
		if(s.length()==0) printf("0\n");
		else
		cout<<s<<endl;   
	}
	return 0;
}
