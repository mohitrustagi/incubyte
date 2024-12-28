DELETE FROM patients;
DELETE FROM doctors;
DELETE FROM locations;
DELETE FROM doctor_locations;
DELETE FROM doctor_schedules;

INSERT INTO patients(id, name) VALUES (0, 'patient-1');
INSERT INTO patients(id, name) VALUES (1, 'patient-2');


INSERT INTO doctors(id, first_name, last_name) VALUES (0, 'Jane', 'Wright');
INSERT INTO doctors(id, first_name, last_name) VALUES (1, 'Joseph', 'Lister');

INSERT INTO locations(id, address) VALUES (0, '1 Park St');
INSERT INTO locations(id, address) VALUES (1, '2 University Ave');

INSERT INTO doctor_locations(id, doctor_id, location_id) VALUES (0, 0, 0);
INSERT INTO doctor_locations(id, doctor_id, location_id) VALUES (1, 1, 0);
INSERT INTO doctor_locations(id, doctor_id, location_id) VALUES (2, 1, 1);


INSERT INTO doctor_schedules (id, doctor_id, location_id, day_of_the_week, start_time, end_time) VALUES
(0, 0, 0, 'Monday', '14:00', '16:00'),
(1, 0, 1, 'Tuesday', '14:00', '16:00'),
(2, 1, 1, 'Wednesday', '10:00', '12:00');
