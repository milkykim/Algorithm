#include<stdio.h>
#include<string.h>
 
int main(void)
{
    char origin[] = "minji";    //"minji\0" 이므로 size = 6;
    char dest1[20];
    char dest2[5];
    char dest3[] = "STRCPY_EXAMPLE";    // size = 15;
 
    //case1 : 빈 배열에 전체를 복사할때
    strcpy(dest1, origin);
 
    //case2 : 내용이 들어있는 꽉 차있는 배열에 크기가 넘는 문자열을 복사할때
    //strcpy(dest2, origin);    //run time error
 
    //case3 : 내용이 들어있는 꽉 차있는 배열에 전체를 복사할때
    strcpy(dest3, origin);
 
    printf("case1 : %s\n", dest1);    // minji
    //printf("case2 : %s\n", dest2); //run time error
    printf("case3 : %s\n", dest3);    // minji

    dest3[5] = '_';    //'\0' -> '_'
    printf(" case3 after  : %s\n", dest3); // minji_EXAMPLE

    return 0;
}
