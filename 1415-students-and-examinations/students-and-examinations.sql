SELECT t.student_id, t.student_name, t.subject_name, IF(attended_exams is NULL, 0, attended_exams) as attended_exams
FROM (
    SELECT *
    FROM Students
    JOIN Subjects 
) t
LEFT JOIN (
    SELECT student_id, subject_name, COUNT(subject_name) AS attended_exams   
    FROM Examinations
    GROUP BY student_id, subject_name
) e
ON t.student_id = e.student_id 
AND t.subject_name = e.subject_name  
ORDER BY t.student_id, t.subject_name
