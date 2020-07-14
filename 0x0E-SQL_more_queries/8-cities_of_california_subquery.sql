-- lists all the cities of California in the database hbtn_0d_usa
-- Another fucking comment
SELECT id, name FROM hbtn_0d_usa.cities
	WHERE state_id = (SELECT id FROM hbtn_0d_usa.states WHERE name = 'California')
	ORDER BY cities.id;
