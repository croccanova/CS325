/******************************************************
Program Name: activity scheduler
Author: Christian Roccanova
Date: 4/28/2018
Description: Reads data from file into an array of and then sorts via insertion sort based on latest starting time.  
				Sorted data is then sent to a greedy algorithm to schedule the optimal amount of activities.
******************************************************/

#include <iostream>
#include <string>
#include <fstream>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::ofstream;
using std::ifstream;

//activity object containing its number, start time and finish time
class activity
{
public:

	int num;
	int start;
	int end;
};

//sorts activities by start time with the latest time being first
void insertSort(activity arr[], int len)
{
	activity temp;
	for (int i = 0; i < len; i++)
	{
		for (int j = i; j > 0; j--)
		{
			//swaps positions if a number is larger than the one preceeding it
			if (arr[j].start > arr[j - 1].start)
			{
				temp = arr[j];
				arr[j] = arr[j - 1];
				arr[j - 1] = temp;
			}
		}
	}
}

//selects activities by latest start time
void activitySelect(activity act[], int len)
{
	int count = 0;	
	activity order[10000];

	//activity with the latest start time will always be first
	order[0] = act[0];

	for (int i = 1; i < len; i++)
	{
		//adds activity to the final list if it's end time is compatible with (earlier than or equal to) the previous activitie's start time
		if (act[i].end <= order[count].start)
		{
			count++;
			order[count] = act[i];
			
		}
	}

	//print results
	cout << "Number of activities selected: " << count + 1 << endl;
	cout << "Order of activities: ";
	for (int i = count; i >= 0; i--)
	{
		cout << order[i].num << " ";
	}

	cout << endl << endl;
}



int main()
{
	int actNum;
	activity actArray[10000];
	ifstream dataFile;
	
	dataFile.open("act.txt");
	while (!dataFile.eof())
	{
		dataFile >> actNum;
		
		// fills object array with data
		for (int i = 0; i < actNum; i++)
		{
			dataFile >> actArray[i].num;
			dataFile >> actArray[i].start;
			dataFile >> actArray[i].end;
								
		}

		//sorts array
		insertSort(actArray, actNum);

		//schedules activities
		activitySelect(actArray, actNum);

	}
	
	
	return 0;
}