INSERT OR IGNORE INTO activities (name, description, schedule, max_participants) VALUES
    ('Chess Club', 'Learn strategies and compete in chess tournaments', 'Fridays, 3:30 PM - 5:00 PM', 12),
    ('Programming Class', 'Learn programming fundamentals and build software projects', 'Tuesdays and Thursdays, 3:30 PM - 4:30 PM', 20),
    ('Gym Class', 'Physical education and sports activities', 'Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM', 30),
    ('Soccer Team', 'Join the school soccer team and compete in matches', 'Tuesdays and Thursdays, 4:00 PM - 5:30 PM', 22),
    ('Basketball Team', 'Practice and play basketball with the school team', 'Wednesdays and Fridays, 3:30 PM - 5:00 PM', 15),
    ('Art Club', 'Explore your creativity through painting and drawing', 'Thursdays, 3:30 PM - 5:00 PM', 15),
    ('Drama Club', 'Act, direct, and produce plays and performances', 'Mondays and Wednesdays, 4:00 PM - 5:30 PM', 20),
    ('Math Club', 'Solve challenging problems and participate in math competitions', 'Tuesdays, 3:30 PM - 4:30 PM', 10),
    ('Debate Team', 'Develop public speaking and argumentation skills', 'Fridays, 4:00 PM - 5:30 PM', 12);

INSERT OR IGNORE INTO students (email, name, grade_level) VALUES
    ('michael@mergington.edu', 'Michael', '11'),
    ('daniel@mergington.edu', 'Daniel', '11'),
    ('emma@mergington.edu', 'Emma', '10'),
    ('sophia@mergington.edu', 'Sophia', '10'),
    ('john@mergington.edu', 'John', '12'),
    ('olivia@mergington.edu', 'Olivia', '12'),
    ('liam@mergington.edu', 'Liam', '11'),
    ('noah@mergington.edu', 'Noah', '11'),
    ('ava@mergington.edu', 'Ava', '10'),
    ('mia@mergington.edu', 'Mia', '10'),
    ('amelia@mergington.edu', 'Amelia', '9'),
    ('harper@mergington.edu', 'Harper', '9'),
    ('ella@mergington.edu', 'Ella', '10'),
    ('scarlett@mergington.edu', 'Scarlett', '10'),
    ('james@mergington.edu', 'James', '12'),
    ('benjamin@mergington.edu', 'Benjamin', '12'),
    ('charlotte@mergington.edu', 'Charlotte', '11'),
    ('henry@mergington.edu', 'Henry', '11');

INSERT OR IGNORE INTO activity_registrations (activity_id, student_id)
SELECT a.id, s.id
FROM activities a
JOIN students s ON s.email IN ('michael@mergington.edu', 'daniel@mergington.edu')
WHERE a.name = 'Chess Club';

INSERT OR IGNORE INTO activity_registrations (activity_id, student_id)
SELECT a.id, s.id
FROM activities a
JOIN students s ON s.email IN ('emma@mergington.edu', 'sophia@mergington.edu')
WHERE a.name = 'Programming Class';

INSERT OR IGNORE INTO activity_registrations (activity_id, student_id)
SELECT a.id, s.id
FROM activities a
JOIN students s ON s.email IN ('john@mergington.edu', 'olivia@mergington.edu')
WHERE a.name = 'Gym Class';

INSERT OR IGNORE INTO activity_registrations (activity_id, student_id)
SELECT a.id, s.id
FROM activities a
JOIN students s ON s.email IN ('liam@mergington.edu', 'noah@mergington.edu')
WHERE a.name = 'Soccer Team';

INSERT OR IGNORE INTO activity_registrations (activity_id, student_id)
SELECT a.id, s.id
FROM activities a
JOIN students s ON s.email IN ('ava@mergington.edu', 'mia@mergington.edu')
WHERE a.name = 'Basketball Team';

INSERT OR IGNORE INTO activity_registrations (activity_id, student_id)
SELECT a.id, s.id
FROM activities a
JOIN students s ON s.email IN ('amelia@mergington.edu', 'harper@mergington.edu')
WHERE a.name = 'Art Club';

INSERT OR IGNORE INTO activity_registrations (activity_id, student_id)
SELECT a.id, s.id
FROM activities a
JOIN students s ON s.email IN ('ella@mergington.edu', 'scarlett@mergington.edu')
WHERE a.name = 'Drama Club';

INSERT OR IGNORE INTO activity_registrations (activity_id, student_id)
SELECT a.id, s.id
FROM activities a
JOIN students s ON s.email IN ('james@mergington.edu', 'benjamin@mergington.edu')
WHERE a.name = 'Math Club';

INSERT OR IGNORE INTO activity_registrations (activity_id, student_id)
SELECT a.id, s.id
FROM activities a
JOIN students s ON s.email IN ('charlotte@mergington.edu', 'henry@mergington.edu')
WHERE a.name = 'Debate Team';
