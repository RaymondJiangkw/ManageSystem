# Developer Guide
## Denotation
### Time Interval
|id |    Time      |
|---|--------------|
| 1 |  8:00~9:50   |
| 2 | 10:10~12:00  |
| 3 | 12:10~14:00  |
| 4 | 14:10~16:00  |
| 5 | 16:20~18:10  |
| 6 | 19:00~20:50  |
| 7 | 21:00~21:50  |
## Models
### Lesson
* name: the name of lesson.
* teacher: the name of the teacher.
* capacity: the capacity of the class.
* classroom: indicate where the lesson is held.
* supplement: the additional information about this lesson.
* collage: indicate which collage this lesson belongs to.
* school: specify which school this lesson belongs to.
* lesson_id: indicate the id of the lesson.

### Class_time
* day: the representation of day
* time: the time interval
* system: the id of system
* lesson[Foreign Key]: related to the lesson
* interpretation: interpretation for the time

## Views
### index
* display all classes.
* Provide an input box to filter ideal classes.

### Detail
* Give details about a specific class.
