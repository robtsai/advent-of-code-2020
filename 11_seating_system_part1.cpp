#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <tuple>
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::ifstream;
using std::sort;
using std::tuple;
using std::make_tuple;


struct Plane {
	int numrows;
	int rowwidth;
	char **seatrows;

	Plane(int nr, int rw) {
		numrows = nr;
		rowwidth = rw;

		seatrows = new char*[nr];
		for (int i=0; i < rowwidth; i++) {
			seatrows[i] = new char[rowwidth];
		}
	}

	// copy constructor
	Plane(int nr, int rw, Plane *otherplane) {
		numrows = nr;
		rowwidth = rw;

		seatrows = new char*[nr];
		for (int i=0; i < rowwidth; i++) {
			seatrows[i] = new char[rowwidth];
			for (int j=0; j < rowwidth; j++) {
				seatrows[i][j] = otherplane->seatrows[i][j];
			}
		}
	}

	void print_plane() {
		for (int i=0; i<numrows; i++) {
			for (int j=0; j<rowwidth; j++) {
				cout << seatrows[i][j];
			}
			cout << endl;
		}
	}

	int total_occ() {
		int total = 0;
		for (int i=0; i<numrows; i++) {
			for (int j=0; j<rowwidth; j++) {
				if (seatrows[i][j] == '#') {
					total++;
				}
			}
		}
		return total;
	}	
};


// helper function to print a tuple of any size
// https://en.cppreference.com/w/cpp/utility/tuple/tuple_cat
template<class Tuple, std::size_t N>
struct TuplePrinter {
    static void print(const Tuple& t) 
    {
        TuplePrinter<Tuple, N-1>::print(t);
        std::cout << ", " << std::get<N-1>(t);
    }
};
 
template<class Tuple>
struct TuplePrinter<Tuple, 1> {
    static void print(const Tuple& t) 
    {
        std::cout << std::get<0>(t);
    }
};
 
template<typename... Args, std::enable_if_t<sizeof...(Args) == 0, int> = 0>
void print(const std::tuple<Args...>& t)
{
    std::cout << "()\n";
}
 
template<typename... Args, std::enable_if_t<sizeof...(Args) != 0, int> = 0>
void print(const std::tuple<Args...>& t)
{
    std::cout << "(";
    TuplePrinter<decltype(t), sizeof...(Args)>::print(t);
    std::cout << ")\n";
}
// end helper function


typedef vector< tuple<int, int> > tuple_list;

void print_vec(tuple_list tl) {
	for (tuple<int, int> tii: tl) {
		print(tii);
	}
}


tuple_list adjacent(int r, int c, int numrows, int rowwidth) {
	// returns a tuple list of adjacent i,r to check
	tuple_list tl;
	for (int i=r-1; i<=r+1; i++) {
		for (int j=c-1; j<=c+1; j++) {
			if (i >=0 && i < numrows && j >= 0 and j < rowwidth and !(i==r && j==c)) {
				tl.push_back(make_tuple(i, j));
			}
		}
	}
	return tl;
}

int adj_occupied(int i, int j, Plane *p) {
	tuple_list adj = adjacent(i, j, p->numrows, p->rowwidth);
	int num_occupied = 0;
	for (tuple<int, int> tii: adj) {
		int checki = std::get<0>(tii);
		int checkj = std::get<1>(tii);
		char checkseat = p->seatrows[checki][checkj];
		if (checkseat == '#') {
			num_occupied++;
		}
	}
	return num_occupied;
}




void state_change(Plane *orig, Plane *nextp) {
	for (int i=0; i<orig->numrows; i++) {
		for (int j=0; j<orig->rowwidth; j++) {
			char seat = orig->seatrows[i][j];
			int num_adj = adj_occupied(i, j, orig);
			if (seat == 'L' && num_adj == 0) {
				nextp->seatrows[i][j] = '#';
			} else if (seat == '#' && num_adj >= 4) {
				nextp->seatrows[i][j] = 'L';
			} else {
				nextp->seatrows[i][j] = seat;
			}
		}
	}
}



string filename = "input_files/problem11.txt";


int main() {
	ifstream myfile;

	myfile.open(filename);	
	string firstline;
	getline(myfile, firstline);
	int rowwidth = firstline.length();
	cout << "The width of a row is " << rowwidth << endl;
	myfile.close();

	int numrows = 0;
	myfile.open(filename);	
	string mytext;
	while (getline (myfile, mytext)) {
		numrows++;
	}
	cout << "the number of rows is " << numrows << endl;
	myfile.close();


	Plane *plane = new Plane(numrows, rowwidth);


	// populate plane
	int i = 0;
	myfile.open(filename);	
	while (getline (myfile, mytext)) {
		for (int j=0; j<rowwidth; j++) {
			plane->seatrows[i][j] = mytext[j];
		}
		i++;
	}
	myfile.close();

	plane->print_plane();

	int num_steps = 0;


	Plane *currplane = plane;

	while (true) {
		int curr_occupied = currplane->total_occ();
		cout << "seats at step " << num_steps << " is " << curr_occupied << endl;
		num_steps++;
		Plane *nextplane = new Plane(numrows, rowwidth);
		state_change(currplane, nextplane);
		nextplane->print_plane();
		int next_occupied = nextplane->total_occ();
		cout << "seats at step " << num_steps << " is " << next_occupied << endl;
		if (curr_occupied == next_occupied) {
			cout << "no change in seats" << endl;
			cout << "the answer to part 1 is " << curr_occupied << endl;
			break;
		}
		delete currplane;
		currplane = nextplane;
	}

	

	return 0;
}