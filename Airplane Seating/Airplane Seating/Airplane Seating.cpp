#include "pch.h"
#include <iostream>
#include <string>
#include <iomanip>
#define NUMBER_ROWS 13
#define NUMBER_SEATS 6
using namespace std;
void init(char[][NUMBER_SEATS]);
void printPlane(char[][NUMBER_SEATS]);
void getSeatNum(char[][NUMBER_SEATS], int&, int&);
void checkSeat(char[][NUMBER_SEATS], int, int);
char getSeatYN();
int main()
{
	int row;
	int col;

	int i;
	int j;
	bool goodseat;
	char choice;
	char plane[NUMBER_ROWS][NUMBER_SEATS];
	init(plane);
	cout << "Welcome to Jessica's Plane Seating Service!" << endl;
	cout << endl;
	printPlane(plane);
	choice = getSeatYN();
	while (choice != 'N')
	{
		getSeatNum(plane, row, col);
		printPlane(plane);
		choice = getSeatYN();
	}
	return 0;
}
void checkSeat(char plane[][NUMBER_SEATS], int row, int col)
{
	if (plane[row - 1][col] != 'X')
	{
		plane[row - 1][col] = 'X';
		cout << "The seat is reserved for you\n";
	}
	else
	{
		cout << "Seat taken!" << endl;
	}
}
void init(char plane[][NUMBER_SEATS])
{
	int i, j;
	for (i = 0; i < NUMBER_ROWS; i++)
		for (j = 0; j < NUMBER_SEATS; j++)
			plane[i][j] = '*';

}
void getSeatNum(char plane[][NUMBER_SEATS], int& row, int& col)
{
	char ticket;
	char seat;
	int min, max;
	bool good = true;
	char Answer;
	do
	{
		good = true;
		cout << "Please Enter the type of Seat desired: " << endl;
		cout << "F = First Class " << '\n' << "B = Business Class " << '\n' << "E = Economy Class" << endl;
		cin >> ticket;
		ticket = toupper(ticket);
		switch (ticket)
		{
		case 'F':min = 1;
			max = 2;
			break;
		case 'E':
			min = 8;
			max = 13;
			break;

		case 'B': min = 3;
			max = 7;
			break;
		default: good = false;
			cout << "invalid seat type\n";
		}
	} while (!good);
	good = false;
	do
	{
		cout << "Please enter in the desired Row Number (" << min << "-" << max << "): " << endl;
		cin >> row;
		if (row < min || row > max)
		{
			cout << "This seat is not in the class you chose! Would you like to change your ticket?" << endl;
			cout << "Would you like to change your selection? (Y/N): ";
			cin >> Answer;
			if (Answer == 'Y' || Answer == 'y')
				good = true;
			if (row == 1 || row == 2)
				ticket = 'F';
			else if (row > 2 && row < 8)
				ticket = 'B';
			else
				ticket = 'E';
		
		}
		else
		{
			good = true;
		}
	}while (!good);
	good = false;
	do
	{
		cout << "Please enter in the desired Seat (A-F): " << endl;
		cin >> seat;

		col = tolower(seat) - 'a';
		if (col < 0 || col > 5)
			cout << "Invalid Seat\n";
		else if ((ticket == 'F') && (row > 2) || row < 1)
			cout << "Invalid Selction for First Class" << endl;
		else if ((ticket == 'B') && ((row <= 2) || (row > 7)))
			cout << "Invalid Selection for Business Class" << endl;
		else if ((ticket == 'E') && ((row < 8) || (row > 13)))
			cout << "Invalid Selection for Economy Class" << endl;
		else
			checkSeat(plane, row, col);
			good = true;
	} while (!good);
}
char getSeatYN()
{
	char choice;
	cout << "Would you like to make a selection? (Y/N): ";
	cin >> choice;

	choice = static_cast<char>(toupper(choice));
	return choice;
}
void printPlane(char plane[][NUMBER_SEATS])
{
	int i, j;
	cout << setw(11) << "A" << setw(5) << "B"
		<< setw(5) << "C" << setw(5) << "D"
		<< setw(5) << "E" << setw(5) << "F" << endl;
	cout << " " << endl;


	for (i = 0; i < NUMBER_ROWS; i++)
	{
		cout << "Row " << setw(2) << i + 1;
		for (j = 0; j < NUMBER_SEATS; j++)
			cout << setw(5) << plane[i][j];
		cout << endl;
	}

	cout << " " << endl;
	cout << "* -- available seat\n";
	cout << "X -- occupied seat\n\n";
	cout << "Rows 1 and 2 are for first class customers\n";
	cout << "Rows 3 through 7 are for business class passengers\n";
	cout << "Rows 8 through 13 are for economy class passengers\n\n";

}