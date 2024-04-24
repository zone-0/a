#include <stdio.h>
#include <omp.h>

#define N 100
#define NUM_PROCESSORS 4

int main()
{

    int arr[N];
    arr[0] = 1;
    for (int i = 0; i < 100; i++)
    {
        arr[i] = i + 1;
    }

    int BLOCK = (N / NUM_PROCESSORS);

    int sum = 0;
    int pre[NUM_PROCESSORS];

    for (int i = 0; i < NUM_PROCESSORS; i++)
    {
        pre[i] = 0;
    }

#pragma omp parallel num_threads(NUM_PROCESSORS)
    {
        int thread_id = omp_get_thread_num();
        int start = thread_id * BLOCK;
        int end = (thread_id + 1) * BLOCK;

        // range and calulcagte sum ..
    }

    return 0;
}


#include<omp.h>
#include<stdio.h>

#pragma omp parallel num_threads(NUM_PROCESSORS)
