#include <stdlib.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int NUMBER_OF_GRADES = 9; // 학점 등급의 개수
const int SCORES[NUMBER_OF_GRADES] = {95, 90, 85, 80, 75, 70, 65, 60, 0}; // 점수 배열
const char *GRADES[NUMBER_OF_GRADES] = {"A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"}; // 학점 등급 포인터 배열

char* calculateGrade(int score); // 실제 학점을 계산하는 함수

int main(void)
{
    printf("학점 프로그램\n");
    printf("종료를 원하면 \"999\" 입력\n");
    printf("[학점 테이블]\n");
    printf("점수 : 95   90   85   80   75   70   65   60   0\n");
    printf("학점  : A+   A    B+   B    C+   C    D+   D   F\n");

    while(1){

        int score = get_int("성적을 입력하세요 (0~100)  :  ");

        // 999점이면 종료
        if(score==999) {
            printf("학점 프로그램을 종료합니다.\n");
            return 0;
        }

        // 0~100 범위의 점수가 입력되면 학점 계산 함수 호출
        if(score >= 0 && score <= 100) {
            char *grade = calculateGrade(score);
            printf("학점은 %s 입니다.\n", grade);
        } else {
            printf("** %d 성적을 올바르게 입력하세요. 범위는 0 ~ 100 입니다.\n", score);
        } 
    }
}

char* calculateGrade(int score){
    char* grade;
    grade = malloc(2); // 명시적으로 2bytes memory를 allocation, sandbox에서 실행하려면 이렇게해야함

    for(int i = 0; i < NUMBER_OF_GRADES; i++) {
        // 학점의 배열 끝까지 반복을 하며,
        // 입력된 점수가 해당 배열 위치 점수 이상이 된다면, 해당 위치에 맞는 학점을 grade에 대입
        if(score >= SCORES[i]) {
            //grade = malloc(sizeof(char) * strlen(GRADES[i]));
            strcpy(grade, GRADES[i]);
            break;
        }
    }

    return grade;
}