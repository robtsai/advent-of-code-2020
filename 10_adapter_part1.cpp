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

	// add charging outlet to front
	nums.insert(nums.begin(), 0);

	print_vec(nums);


	int i = 1;

	int jolt_diff1 = 0;;
	int jolt_diff3 = 0;;

	while (i < nums.size()) {
		int diff = nums[i] - nums[i-1];
		if (diff == 1) {
			jolt_diff1 += 1;
		} else if (diff == 3) {
			jolt_diff3 += 1;
		}
		i++;
	}

	// add 3 jolt diff at end
	jolt_diff3 += 1;

	cout << jolt_diff1 << endl;
	cout << jolt_diff3 << endl;
	cout << "Answer to part 1 " << jolt_diff1 * jolt_diff3 << endl;
}