#include <iostream>
using namespace std;
void swap(int& a, int& b)
{
	int t = a;
	a=b;
	b=t;
}
int main()
{
	int n;
	cin>>n;
	int noc,nonc,now;
	noc = n;
	nonc = n/3;
	now = n%3;
	noc=noc+nonc;
	while(true)
	{
		nonc=(nonc+now)/3;
		now=nonc%3;
		noc=noc+nonc;
		if(nonc == 0){break;}
	}
	cout<<noc;
}