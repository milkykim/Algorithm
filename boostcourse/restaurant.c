#include <cs50.h>
#include <stdio.h>
#include <string.h>

string get_menu(string d);

int main(void)
{
    string day = get_string("요일을 입력하세요: ");
    string menu = get_menu(day);

    printf("%s: %s\n", day, menu);
    
}

string get_menu(string d)
{
    string menu = "";

    if(strcmp(d, "월요일") == 0) {
        menu = "청국장";
    } else if (strcmp(d, "화요일") == 0) {
        menu = "비빔밥";
    } else if (strcmp(d, "수요일") == 0) {
        menu = "된장찌개";
    } else if (strcmp(d, "목요일") == 0) {
        menu = "칼국수";
    } else if (strcmp(d, "금요일") == 0) {
        menu = "냉면";
    } else if (strcmp(d, "토요일") == 0) {
        menu = "소불고기";
    } else if (strcmp(d, "일요일") == 0) {
        menu = "오삼불고기";
    } else {
        menu = "다시 시작하세요";
    }

    return menu;
}
