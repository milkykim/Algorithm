#include <stdio.h>
#include <stdlib.h> //랜덤함수 호출

void Swap(int arr[], int a, int b) // a,b 스왑 함수 
{
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}
int Partition(int arr[], int left, int right)
{
    int pivot = arr[left]; // 피벗의 위치는 가장 왼쪽에서 시작
    int low = left + 1;
    int high = right;

    while (low <= high) // 교차되기 전까지 반복한다 
    {
        while (low <= right && pivot >= arr[low]) // 피벗보다 큰 값을 찾는 과정 
        {
            low++; // low를 오른쪽으로 이동 
        }
        while (high >= (left+1)  && pivot <= arr[high]) // 피벗보다 작은 값을 찾는 과정 
        {
            high--; // high를 왼쪽으로 이동
        }
        if (low <= high)// 교차되지 않은 상태이면 스왑 과정 실행 
        {
            Swap(arr, low, high); //low와 high를 스왑 
        }
    }
    Swap(arr, left, high); // 피벗과 high가 가리키는 대상을 교환 
    return high;  // 옮겨진 피벗의 위치정보를 반환 

}
 

void QuickSort(int arr[], int left, int right)
{
    if (left <= right)
    {
        int pivot = Partition(arr, left, right); // 둘로 나누어서
        QuickSort(arr, left, pivot - 1); // 왼쪽 영역을 정렬한다.
        QuickSort(arr, pivot + 1, right); // 오른쪽 영역을 정렬한다.
    }
}

// 두 배열의 동일 인덱스에 있는 원소가 같은지 확인하는 함수 
int array_element_of_index_equal(int a[], int b[], int size) { 
    int i; 
    for(i=0; i<size; i++) {
        if( a[i]!=b[i] ) {// 동일한 index의 a, b 원소가 다르면 
            return 0; // miss match
        } 
    }
    
    return 1; // otherwise. 
}

//메인함수
int main()
{
    int n,i,ret;

    // 숫자 쌍을 서로 다른 배열로 선언
    int test1[5] = { 1, 2, 3, 4, 5 };
    int test2[5] = { 5, 4, 3, 2, 1 };
    
    // 각자 퀵 정렬을 진행(평균 nlogn의 시간복잡도를 가짐)
    QuickSort(test1,0,4);
    QuickSort(test2,0,4);
    
    // 배열의 인덱스와 원소 내용을 서로 비교하는 함수
    ret = array_element_of_index_equal(test1, test2, 5); 
    
    if(ret == 1) {
        printf("True\n"); 
    } else {
        printf("False\n");
    }

    return 0;
}
