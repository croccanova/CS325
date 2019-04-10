/******************************************************
Program Name: insertsort
Author: Christian Roccanova
Date: 4/6/2018
Description: reads data from file into an array and then sorts via insertion sort.  Sorted data is then output to insert.out
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

//sorts array by comparing a number to those that come before it and swapping positions when necessarry
void insertSort(int arr[], int len)
{
	int temp;
	for (int i = 0; i < len; i++)
	{
		for (int j = i; j > 0; j--)
		{
			//swaps positions if a number is smaller than the one preceeding it
			if (arr[j] < arr[j-1])
			{
				temp = arr[j];
				arr[j] = arr[j-1];
				arr[j - 1] = temp;
			}
		}
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
	ofstream outFile ("insert.out");
	

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

		insertSort(numArr, rowLen);

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