#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <typeinfo>
#include <unordered_map>

// cd "/Users/Tom/AdventOfCode-2024/Day1/" && g++ day1.cpp -o day1 && "/Users/Tom/AdventOfCode-2024/Day1/"day1

using namespace std;

void readDataIntoArray(const std::string &filename, int *array, int &size, int maxSize)
{
    std::ifstream inputFile(filename);
    if (!inputFile)
    {
        std::cerr << "Error: Could not open the file." << std::endl;
        return;
    }

    size = 0;
    int value;

    while (inputFile >> value && size < maxSize)
    {
        array[size++] = value;
    }

    if (size == maxSize && !inputFile.eof())
    {
        std::cerr << "Warning: File contains more data than the array can hold." << std::endl;
    }

    inputFile.close();
}

void recordFrequency(const vector<int> &arr, unordered_map<int, int> *frequencyMap)
{
    for (int num : arr)
    {
        (*frequencyMap)[num]++;
    }
}

int main()
{
    const int MAX_SIZE = 5000;
    int data[MAX_SIZE];
    int size;

    readDataIntoArray("./day1_data.txt", data, size, MAX_SIZE);

    vector<int> left;
    vector<int> right;

    for (int i = 0; i < size; ++i)
    {
        if (i % 2 == 0)
        {
            left.push_back(data[i]);
        }
        else
        {
            right.push_back(data[i]);
        }
    }

    sort(left.begin(), left.end());
    sort(right.begin(), right.end());

    int total = 0;
    int total2;

    unordered_map<int, int> frequencyMap;
    recordFrequency(right, &frequencyMap);

    for (int i = 0; i < size / 2; ++i)
    {
        total += abs(left[i] - right[i]);
        total2 += left[i] * frequencyMap[left[i]];
    }

    cout << "Part 1 Total: " << total << endl;
    cout << "Part 2 Total: " << total2 << endl;

    return 0;
}
