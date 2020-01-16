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
* score: indicate the score given after finishing this lesson.
* time: indicate when the lesson is held in the specific week.
* weeks: indicate which weeks the lesson is held.

## Views
### index
* display all classes.
* Provide an input box to filter ideal classes.
  * Regulations:
    * '[]' to indicate some ambiguous searching.
      * ',' to list different items at the same position (enumeration).
      * '-':
        * '0-9' means {0,1,2,3,4,5,6,7,8,9}
        * 'a-z' means {a, b, c, d, ... , x, y, z}
        * 'A-Z' means {A, B, C, D, ... , X, Y, Z}
    * ';' to indicate different candidates
    * '{}' to indicate precise matching.
* feature: In the Address-Blank bar, there are two slashes. The first element indicates how many items are there in one page. The second element indicates the index of this page.
### Detail
* Give details about a specific class.

## Function
### get_data
* get data from the web page from BJTU.
### read_from_csv(path,school)
* get data from a specific file.
* Customs:
  * use ';' to denote another item.
  * use ',' to denote different property inside a item.
