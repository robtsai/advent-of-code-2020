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



int adj_occupied(int i, int j, Plane *p) {
	int num_occupied = 0;

	// up
	for (int r=i-1; r >= 0; r--) {
		char checkseat = p->seatrows[r][j];
		if (checkseat == '#') {
			num_occupied++;
			break;
		} else if (checkseat == 'L') {
			break;
		}
	}

	// down
	for (int r=i+1; r < p->numrows; r++) {
		char checkseat = p->seatrows[r][j];
		if (checkseat == '#') {
			num_occupied++;
			break;
		} else if (checkseat == 'L') {
			break;
		}
	}		
	
	// left
	for (int c=j-1; c >= 0; c--) {
		char checkseat = p->seatrows[i][c];
		if (checkseat == '#') {
			num_occupied++;
			break;
		} else if (checkseat == 'L') {
			break;
		}
	}		

	// right
	for (int c=j+1; c < p->rowwidth; c++) {
		char checkseat = p->seatrows[i][c];
		if (checkseat == '#') {
			num_occupied++;
			break;
		} else if (checkseat == 'L') {
			break;
		}
	}		

	// up left
	int r = i-1;
	int c = j-1;

	while (r >= 0 && c >= 0) {
		char checkseat = p->seatrows[r][c];
		if (checkseat == '#') {
			num_occupied++;
			break;
		} else if (checkseat == 'L') {
			break;
		} else {
			r--;
			c--;
		}
	}			

	// up right
	r = i-1;
	c = j+1;

	while (r >= 0 && c < p->rowwidth) {
		char checkseat = p->seatrows[r][c];
		if (checkseat == '#') {
			num_occupied++;
			break;
		} else if (checkseat == 'L') {
			break;
		} else {
			r--;
			c++;
		}
	}

	// down left
	r = i+1;
	c = j-1;

	while (r < p->numrows && c >= 0) {
		char checkseat = p->seatrows[r][c];
		if (checkseat == '#') {
			num_occupied++;
			break;
		} else if (checkseat == 'L') {
			break;
		} else {
			r++;
			c--;
		}
	}

	// down right
	r = i+1;
	c = j+1;

	while (r < p->numrows && c < p->rowwidth) {
		char checkseat = p->seatrows[r][c];
		if (checkseat == '#') {
			num_occupied++;
			break;
		} else if (checkseat == 'L') {
			break;
		} else {
			r++;
			c++;
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
			} else if (seat == '#' && num_adj >= 5) {
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
			cout << "the answer to part 2 is " << curr_occupied << endl;
			break;
		}
		delete currplane;
		currplane = nextplane;
	}

	

	return 0;
}