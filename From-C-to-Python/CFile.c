#include <stdio.h>
#include <string.h>

#define MAX_STUDENTS 50
#define MAX_NAME 50

typedef struct {
    char name[MAX_NAME];
    float grades[3];
    char honors[20];
} Student;

float calculate_average(float grades[], int count) {
    float sum = 0;
    for (int i = 0; i < count; i++) sum += grades[i];
    return sum / count;
}

void assign_honors(Student *s) {
    float avg = calculate_average(s->grades, 3);
    if (avg >= 16.0)       strcpy(s->honors, "Excellent");
    else if (avg >= 14.0)  strcpy(s->honors, "Very Good");
    else if (avg >= 12.0)  strcpy(s->honors, "Good");
    else if (avg >= 10.0)  strcpy(s->honors, "Pass");
    else                   strcpy(s->honors, "Fail");
}

void display_student(Student s) {
    float avg = calculate_average(s.grades, 3);
    printf("%s — Average: %.2f — %s\n", s.name, avg, s.honors);
}

int main() {
    Student students[MAX_STUDENTS];
    int count = 0;

    // Manual data entry
    strcpy(students[0].name, "Alice");
    students[0].grades[0] = 17.5;
    students[0].grades[1] = 15.0;
    students[0].grades[2] = 18.0;
    assign_honors(&students[0]);
    count++;

    strcpy(students[1].name, "Bob");
    students[1].grades[0] = 9.0;
    students[1].grades[1] = 11.5;
    students[1].grades[2] = 8.0;
    assign_honors(&students[1]);
    count++;

    strcpy(students[2].name, "Charlie");
    students[2].grades[0] = 13.0;
    students[2].grades[1] = 12.5;
    students[2].grades[2] = 14.0;
    assign_honors(&students[2]);
    count++;

    // Display results
    printf("=== Results ===\n");
    for (int i = 0; i < count; i++) {
        display_student(students[i]);
    }

    // Top student
    int best = 0;
    for (int i = 1; i < count; i++) {
        if (calculate_average(students[i].grades, 3) >
            calculate_average(students[best].grades, 3)) {
            best = i;
        }
    }
    printf("\nTop student: %s\n", students[best].name);

    return 0;
}