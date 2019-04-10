/******************************************************
Program Name: mergesort
Author: Christian Roccanova
Date: 4/6/2018
Description: reads data from file into an array and then sorts via merge sort.  Sorted data is then output to merge.out
******************************************************/

#include<iostream>
#include <fstream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::ifstream;
using std::ofstream;

//compares values and stores them in a temporary array in sorted order to be copied over the original array at the end
void merge(int *arr, int low, int mid, int high)
{
	int indexA = low;
	int indexB = mid + 1;
	int indexC = low;
	int temp[100000];	//temporary array holds sorted values

	//compares elements and adds the lower to the temporary array
	while (indexA <= mid && indexB <= high)
	{
		if (arr[indexA] < arr[indexB])
		{
			temp[indexC] = arr[indexA];
			indexA++;
			indexC++;
					
		}
		else
		{
			temp[indexC] = arr[indexB];
			indexB++;
			indexC++;
		}
	}

	while (indexA <= mid)
	{
		temp[indexC] = arr[indexA];
		indexA++;
		indexC++;
	}

	while (indexB <= mid)
	{
		temp[indexC] = arr[indexB];
		indexB++;
		indexC++;
	}

	//copies sorted temporary array into original array
	for (int i = low; i < indexC; i++)
	{
		arr[i] = temp[i];
	}
}

//sorts array by breaking down the input array and then calling merge() to put it back together in sorted order
void mergeSort(int *arr, int low, int high)
{
	//if array size is greater than 0, recursively calls mergeSort
	if (low < high)
	{
		//sets midpoint
		int mid = low + (high - low) / 2;

		mergeSort(arr, low, mid);
		mergeSort(arr, mid + 1, high);
		merge(arr, low, mid, high);

	}
}

int main()
{
	int rowLen;
	int rowTotal = 0;
	int rowCount = 0;
	int numArr[100000];
	string rowString;
	ifstream dataFile;
	ofstream outFile("merge.out");

	
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

		mergeSort(numArr, 0, rowLen-1);

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