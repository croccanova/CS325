/******************************************************
Program Name: Making Change
Author: Christian Roccanova
Date: 4/20/2018
Description: Takes data from file and uses it to determine the minimum number of "coins" needed to add up to a given value.
******************************************************/
#include <limits.h>
#include <iostream>
#include <fstream>
#include <string>


using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::ifstream;
using std::ofstream;

// determines the lowest number of coins required to add up to value "val"
int makeChange(int coinArr[], int len, int val)
{
	// table[val] will hold final result
	int res[10000];
		
	res[0] = 0;

	// initialize table values to infinity
	for (int i = 1; i <= val; i++)
	{
		res[i] = INT_MAX;		
	}
		
	// compute minimum coins for all values 1 to val
	for (int i = 1; i <= val; i++)
	{
		// cycles through all coins smaller than i
		for (int j = 0; j < len; j++)
		{
			
			if (coinArr[j] <= i)
			{				
				if (res[i - coinArr[j]] + 1 < res[i])
				{
					res[i] = res[i - coinArr[j]] + 1;					
				}
			}
				
			
		}

		
	}
	
	return res[val];
}


int main()
{
	
	int rowLen;
	int rowNum;
	int setNum;
	int value;
	int minCoins;
	int rowTotal = 0;
	int rowCount = 0;
	int coinArr[10000];
	string rowString;
	ifstream dataFile;
	ofstream outFile("change.out");


	dataFile.open("amount.txt");
	//counts number of rows in data file
	while (!dataFile.eof()) {
		getline(dataFile, rowString);
		rowTotal++;		
	}
	
	dataFile.close();

	dataFile.open("amount.txt");
		
	//number of sets should be total rows / 2
	setNum = (rowTotal / 2);

	//cycles through each row individually
	for (int i = 0; i < setNum; i++)
	{
		dataFile >> rowLen;

		//fills initial array
		for (int j = 0; j < rowLen; j++)
		{
			dataFile >> coinArr[j];
			
		}
		

		//outputs initial array to file
		for (int j = 0; j < rowLen; j++)
		{
			outFile << coinArr[j] << " ";
		}
		
		dataFile >> value;

		outFile << endl << value << endl;

		//calls function to determine minimum number of coins and stores result
		minCoins = makeChange(coinArr, rowLen, value);
		
		outFile << minCoins << endl;

		outFile << endl;
		
	}
	outFile.close();
	dataFile.close();
	
	return 0;
	
}
