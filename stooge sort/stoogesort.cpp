/******************************************************
Program Name: stoogesort
Author: Christian Roccanova
Date: 4/12/2018
Description: reads data from file into an array and then sorts via stooge sort.  Sorted data is then output to stooge.out
******************************************************/

#include <iostream>
#include <fstream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::ifstream;
using std::ofstream;


void stoogeSort(int arr[], int front, int back)
{
	int temp;
	int third;
	int fore;
	int aft;

	//swaps first and last elements if first is larger
	if (arr[front] > arr[back])
	{
		temp = arr[front];
		arr[front] = arr[back];
		arr[back] = temp;
	}

	//recursively sorts remainder of the array in sets of 2/3
	if (back - front + 1 > 2)
	{
		third = (back - front + 1) / 3;
		fore = back - third;
		aft = front + third;

		//sorts first 2/3
		stoogeSort(arr, front, fore);

		//sorts back 2/3
		stoogeSort(arr, aft, back);

		//sorts first 2/3 again for confirmation
		stoogeSort(arr, front, fore);
	}

}

int main()
{
	int rowLen;
	int rowNum;
	int rowTotal = 0;
	int rowCount = 0;
	int numArr[100000];
	string rowString;
	ifstream dataFile;
	ofstream outFile("stooge.out");


	dataFile.open("data.txt");
	//counts number of rows in data file
	while (!dataFile.eof()) {
		getline(dataFile, rowString);
		rowTotal++;
	}

	dataFile.close();

	dataFile.open("data.txt");

	//cycles through each row individually
	for (int i = 0; i < rowTotal; i++)
	{

		dataFile >> rowLen;

		//fills initial array
		for (int j = 0; j < rowLen; j++)
		{
			dataFile >> numArr[j];
		}

		stoogeSort(numArr, 0, rowLen-1);

		//outputs sorted array to file
		for (int j = 0; j < rowLen; j++)
		{
			outFile << numArr[j] << " ";
		}


		outFile << endl;


	}
	outFile.close();
	dataFile.close();

	return 0;
}