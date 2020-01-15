from search.models import Lesson
from search.function.modify import get_data
data = get_data()
cnt = len(data[0])
for i in range(cnt):
    lesson = Lesson(
        name = data[0][i],
        teacher = data[1][i],
        capacity = data[2][i],
        classroom = data[3][i],
        supplement = data[4][i],
        collage = data[5][i],
        school = data[6][i],
        lesson_id = data[7][i],
        score = data[8][i],
        time = data[9][i],
        weeks = data[10][i]
    )
    lesson.save()
    print("Finished",i,'/',cnt)
