#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// cd "/Users/Tom/AdventOfCode-2024/Day1/" && g++ day1.c -o day1 && "/Users/Tom/AdventOfCode-2024/Day1/"day1

int FILESIZE = 6;

int loadFile(FILE **file)
{
    *file = fopen("./day1_data.txt", "r");
    if (*file == NULL)
    {
        perror("Unable to open file");
        return 1;
    }
    return 0;
}

int compare(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

int main()
{
    FILE *file;

    if (loadFile(&file) == 1)
    {
        perror("Loading Error");
        return 1;
    }

    char line[15];
    int left[FILESIZE];
    int right[FILESIZE];
    int i = 0;

    while (fgets(line, sizeof(line), file))
    {
        if (i >= FILESIZE)
        {
            printf("Too many lines in file, only processing first %d lines.\n", FILESIZE);
            break;
        }

        if (strlen(line) < 5)
        {
            printf("Line %d is too short.\n", i + 1);
            continue;
        }

        char left_char[5];
        char right_char[5];
        for (int k = 0; k < 5; k++)
        {
            left_char[k] = line[k];
        }
        for (int j = 7; j < 10; j++)
        {
            right_char[j] = line[j];
        }
        left[i] = atoi(left_char);
        printf("left[%d]: %d\n", i, left[i]);
        // right[i] = line[4] - 48;
        right[i] = atoi(right_char);
        i++;
    }

    for (i = 0; i < FILESIZE; i++)
    {
        printf("left[%d]: %d\n", i, left[i]);
    }

    qsort(left, FILESIZE, sizeof(int), compare); // from stdlib
    qsort(right, FILESIZE, sizeof(int), compare);

    int total = 0;

    for (int i = 0; i < FILESIZE; i++)
    {
        printf("left: %d - right: %d", left[i], right[i]);
        total += abs(left[i] - right[i]);
    }

    printf("Part 1 Solution: %d ", total);

    fclose(file);

    return 0;
}