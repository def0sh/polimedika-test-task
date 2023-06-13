Проект выполнялся на Ubuntu 22.04.
Стек:
-FastApi
-Postgres

### Часть 1: База данных

#### 1.1 ER-диаграмма:
![eruniv](https://github.com/def0sh/polimedika-test-task/assets/74783488/4027fcaf-70c4-4529-82c3-8ac4accd79c3)
#### 1.2 Создание таблиц
```sql
CREATE TABLE student (
    id SERIAL NOT NULL, 
    name VARCHAR(25) NOT NULL,
    group_id INTEGER NOT NULL,
    surname VARCHAR(25) NOT NULL,
    phone VARCHAR(15),
    course_number INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(group_id) REFERENCES group(id)
);


CREATE TABLE teacher (
    id SERIAL NOT NULL, 
    department_id INTEGER NOT NULL, 
    name VARCHAR NOT NULL, 
    surname VARCHAR(25) NOT NULL, 
    phone VARCHAR(15), 
    PRIMARY KEY (id), 
    FOREIGN KEY(department_id) REFERENCES department(id)
);


CREATE TABLE course (
  id SERIAL PRIMARY KEY,
  course_name VARCHAR(100),
  department_id INTEGER REFERENCES department(id)
);


CREATE TABLE group (
    id SERIAL NOT NULL, 
    department_id INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(department_id) REFERENCES department(id),
    
);


CREATE TABLE department (
    id SERIAL NOT NULL, 
    faculty_id INTEGER NOT NULL, 
    dep_name VARCHAR NOT NULL,
    PRIMARY KEY (id), 
    FOREIGN KEY (faculty_id) REFERENCES faculty(id),
    PRIMARY KEY (id)
);


CREATE TABLE grade (
  grade_id SERIAL PRIMARY KEY,
  student_id INTEGER REFERENCES student(id),
  course_id INTEGER REFERENCES course(id),
  grade INTEGER NOT NULL
);


CREATE TABLE faculty (
    id SERIAL NOT NULL, 
    fac_number VARCHAR NOT NULL, 
    fac_name VARCHAR NOT NULL, 
    PRIMARY KEY (id)
);


CREATE TABLE exam (
    id SERIAL NOT NULL, 
    name VARCHAR NOT NULL, 
    PRIMARY KEY (id)
);


CREATE TABLE building (
    id SERIAL NOT NULL, 
    department_id INTEGER,
    number INTEGER NOT NULL,
    address VARCHAR NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(department_id) REFERENCES department(id)
);


CREATE TABLE semester (
    id SERIAL NOT NULL,
    curriculum_id INTEGER NOT NULL, 
    start_date DATE NOT NULL, 
    end_date DATE NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(curriculum_id) REFERENCES curriculums(id)
);


CREATE TABLE schedule (
  schedule_id SERIAL PRIMARY KEY,
  course_id INTEGER REFERENCES course(id),
  teacher_id INTEGER REFERENCES teacher(id),
  building_id INTEGER REFERENCES building(id),
  classroom_id INTEGER REFERENCES classroom(id),
  semester_id INTEGER REFERENCES semester(id),
  day_of_week INTEGER,
  start_time TIME,
  end_time TIME
);


CREATE TABLE classroom (
  id SERIAL PRIMARY KEY,
  building_id INTEGER REFERENCES building(id),
  room_number INTEGER
);


CREATE TABLE homework (
  id SERIAL PRIMARY KEY,
  course_id INTEGER REFERENCES course(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  description TEXT
);


CREATE TABLE course_program (
  id SERIAL PRIMARY KEY,
  course_id INTEGER REFERENCES course(id),
  description TEXT
);


CREATE TABLE curriculum (
  curriculum_id SERIAL PRIMARY KEY,
  course_id INTEGER REFERENCES course(id),
  semester_id INTEGER REFERENCES semester(id)
);


CREATE TABLE homework_course (
  homework_id INTEGER REFERENCES homework(id),
  course_id INTEGER REFERENCES course(id),
  PRIMARY KEY (homework_id, course_id)
);


CREATE TABLE student_course (
  id SERIAL PRIMARY KEY,
  student_id INTEGER REFERENCES student(id),
  course_id INTEGER REFERENCES course(id)
);
```

### Часть 2: SQL запросы



Выбрать всех студентов, обучающихся на курсе "Математика"
```sql
SELECT s.student_id, s.student_name
FROM Student s
JOIN Student_Group sg ON s.student_id = sg.student_id
JOIN Group g ON sg.group_id = g.group_id
JOIN Course c ON g.course_id = c.course_id
WHERE c.course_name = 'Математика';
```

Обновить оценку студента по курсу
```sql
UPDATE grade
SET grade = 2
WHERE student_id = 1 AND course_id = 6;
```

Выбрать всех преподавателей, которые преподают в здании №3
```sql
SELECT teacher.id, teacher.name
FROM teacher
JOIN schedule ON teacher.id = schedule.id
JOIN building ON schedule.building_id = building.id
WHERE building.number = 3;
```

Удалить задание для самостоятельной работы, которое было создано более года назад
```sql
DELETE FROM homework
WHERE created_at < CURRENT_TIMESTAMP - INTERVAL '1 year';
```

Добавить новый семестр в учебный год.
```sql
INSERT INTO semester (curriculum_id, "start_date", "end_date")
VALUES (5, '2023-01-07', '2017-25-12');
```

### Часть 3: FastAPI

#### Установка:
1. Клонировать проект
2. Создать файл .env в корневой директории проекта
3. poetry install

````
DB_USER=
DB_PASS=
DB_HOST=
DB_PORT=
DB_NAME=
````

``` 
4. uvicorn src.main:app --reload
```

#### Через docker:

Выполнить команды
````
sudo docker build . -t app:latest
sudo docker run -d -p 8000:8000 app
sudo docker logs <log>
````











