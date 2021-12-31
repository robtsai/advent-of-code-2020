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

template <typename T>
void print(vector<T> vec) {
	for (T i: vec) {
		cout << i << ' ';
	}
	cout << "\n" << endl;
}



int main() {
	ifstream myfile;
	myfile.open("input_files/problem10.txt");
	string mytext;

	vector<int> nums;

	while (getline (myfile, mytext)) {
		int num = stoi(mytext);
		nums.push_back(num);
	}

	sort(nums.begin(), nums.end());

	print(nums);

	int *largest = &nums.back();

	cout << *largest << endl;

	vector<long> numways(*largest+1, 0);

	numways[0] = 1;
	print(numways);

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

	cout << "the answer is " << numways.back() << endl;

}