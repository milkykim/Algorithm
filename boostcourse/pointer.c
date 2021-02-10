#include <stdio.h>

// C언어의 자료형에는 string이 존재하지 않는다. 포인터를 사용해야한다.
int main(void)
{
    char *s = "EMMA";
    printf("%p\n", s);  //s는 EMMA문자열의 첫 번째 문자의 주소를 출력하게 됨 -> 0x42b15a
    
    printf("%p\n", &s[0]);  //0x42b15a
    printf("%p\n", &s[1]);  //0x42b15b
    printf("%p\n", &s[2]);  //0x42b15c
    printf("%p\n", &s[3]);  //0x42b15d

    printf("%c\n", *s);  // E
    printf("%c\n", *(s+1));  // M
    printf("%c\n", *(s+2));  // M
    printf("%c\n", *(s+3));  // A
}
