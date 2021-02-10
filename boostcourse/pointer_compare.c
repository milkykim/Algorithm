#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // 사용자로부터 s와 t 두 개의 문자열 입력받아 저장
    string s = get_string("s: ");
    string t = get_string("t: ");

    // 두 문자열을 비교 (각 문자들을 비교)
    if (s == t)  //string은 이렇게 비교하면 주소값을 비교하기 때문에, 다르다는 결과값이 나온다.
    {
        printf("Same\n");
    } 
    else
    {
        printf("Different\n");
    }
}
