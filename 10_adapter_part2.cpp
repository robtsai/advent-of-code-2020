#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::ifstream;
using std::sort;

void print_vec(vector<int> vec) {
	for (int i: vec) {
		cout << i << ' ';
	}
	cout << "\n" << endl;
}


void print_long(vector<long> vec) {
	for (long i: vec) {
		cout << i << ' ';
	}
	cout << "\n" << endl;
}


int main() {
	ifstream myfile;
	myfile.open("input_files/problem10.txt");
	string mytext;

	vector<int> nums;

	int n = 0;

	while (getline (myfile, mytext)) {
		int num = stoi(mytext);
		nums.push_back(num);
		n++;
	}

	sort(nums.begin(), nums.end());

	print_vec(nums);

	int *largest = &nums.back();

	cout << *largest << endl;

	vector<long> numways(*largest+1, 0);

	numways[0] = 1;
	print_long(numways);

	for (int i: nums) {
		int less1 = i-1;
		int less2 = i-2;
		int less3 = i-3;
		long waystohere = 0;
		if (less1 >= 0) {
			waystohere += numways[less1];
		}
		if (less2 >= 0) {
			waystohere += numways[less2];
		}
		if (less3 >= 0) {
			waystohere += numways[less3];
		}
		numways[i] = waystohere;
		cout << i << " " << waystohere << endl;
	}


}