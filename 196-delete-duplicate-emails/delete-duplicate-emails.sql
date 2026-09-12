DELETE p
FROM Person p
JOIN (
    SELECT MIN(id) AS min_id, email
    FROM Person
    GROUP BY email
) t
ON p.email = t.email
AND p.id <> t.min_id;

  