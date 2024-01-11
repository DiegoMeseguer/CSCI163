#include <iostream>
#include <vector>
using namespace std;

int fib(int f);
long double dfib(int n);

int main() {

	cout<<"Normal Fib"<<endl;
	cout<<fib(8)<<endl;
	cout<<fib(5)<<endl;
	cout<<fib(9)<<endl;


	cout<<"Dynamic Programming Fib"<<endl;
	cout<<dfib(0)<<endl;
	cout<<dfib(1)<<endl;
	cout<<dfib(2)<<endl;
	cout<<dfib(3)<<endl;
	cout<<dfib(4)<<endl;
	cout<<dfib(5)<<endl;
	cout<<dfib(6)<<endl;
	cout<<dfib(7)<<endl;
	cout<<dfib(8)<<endl;
	cout<<dfib(9)<<endl;
	cout<<dfib(50)<<endl;
	cout<<dfib(100)<<endl;


	return 0;
}


int fib(int f){
	if(f==1)
		return 1;
	else if(f==2)
		return 1;
	else
		return(fib(f-1)+fib(f-2));
}
long double dfib(int n) {

	//Formating stuff	
	cout.setf(ios::fixed);
	cout.precision(0);

	//Create vector to contain your table
	vector<long double> dtable;
	long double number;

	for (int i = 0; i < n + 1; ++i) {
		if(i == 0)
			dtable.push_back(0);
		else if(i == 1)
			dtable.push_back(1);
		else{
			number = dtable[i-1] + dtable[i-2];
			dtable.push_back(number);
		}
	}
	
	return(dtable[n]);
}

