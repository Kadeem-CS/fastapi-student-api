CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    major VARCHAR(100),
    gpa FLOAT
);

INSERT INTO students (name, major, gpa)
VALUES
('Kadeem Collins', 'Computer Science', 3.6),
('Jane Doe', 'Business', 3.2);
