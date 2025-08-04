#include <stdio.h>

int main() {
    int day;

    printf("Enter a number  to get the day of the week: ");
    scanf("%d", &day);

    for (int i = day; i <= day; i++) {  
        switch (i) 
		{
            case 1: printf("Monday\n");
			break;
            case 2: printf("Tuesday\n");
			break;
            case 3: printf("Wednesday\n");
			break;
            case 4: printf("Thursday\n");
			break;
            case 5: printf("Friday\n"); 
			break;
            default: printf("Invalid input");
        }
    }
    return 0;
}