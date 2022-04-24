CREATE TABLE course_attendances(
	id INT,
	student_id INT,
	schedule_id INT,
	attend_dt DATE
);

CREATE TABLE Courses(
	id INT,
	name VARCHAR(100)
);

CREATE TABLE enrollments(
	id INT,
	student_id INT,
	schedule_id INT,
	academic_year VARCHAR(30),
	semester INT,
	enroll_dt DATE
);

CREATE TABLE schedules(
	id INT,
	course_id INT,
	lecturer_id INT,
	start_dt DATE,
	end_dt DATE,
	course_days VARCHAR(30)
);