#include<stdio.h>  
#include<string.h> 
int main(void)
{
    char origin[] = "minji";    //"minji\0" 이므로 size = 6;
    char dest1[20];
    char dest2[] = "abcdefghijklmnop";    //size = 17;
    char dest3[] = "STRNCPY_EXAMPLE";    //size = 16;
    char dest4[10];
 
    //case1 : 빈 배열에 전체를 복사할때
    strncpy(dest1, origin, sizeof(origin));  // minji
 
    //case2 : 꽉 차있는 배열에 전체를 복사할때
    strncpy(dest2, origin, sizeof(origin));  // minji
 
    //case3 : "STRNCPY_EXAMPLE"라고 꽉 차있는 배열에 일부(minji)만 복사할때
    strncpy(dest3, origin, 4);    // minjCPY_EXAMPLE
 
    //case4 : 빈 배열에 일부만 복사할때
    strncpy(dest4, origin, 4);    // minj
 
    printf("case1 : %s\n", dest1); // minji
    printf("case2 : %s\n", dest2); // minji
    printf("case3 : %s\n", dest3); // minjCPY_EXAMPLE
    printf("case4 : %s\n", dest4); // minj
    return 0;
}
