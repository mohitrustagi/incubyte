-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS patients;
DROP TABLE IF EXISTS doctors;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS doctor_locations;
DROP TABLE IF EXISTS doctor_schedules;
DROP TABLE IF EXISTS doctor_appointments;

CREATE TABLE patients (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE doctors (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL
);

CREATE TABLE locations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  address TEXT NOT NULL
);

CREATE TABLE doctor_locations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  doctor_id INTEGER NOT NULL,
  location_id INTEGER NOT NULL,
  FOREIGN KEY (doctor_id) REFERENCES doctors (id),
  FOREIGN KEY (location_id) REFERENCES locations (id)
);


CREATE TABLE doctor_schedules (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  doctor_id INTEGER NOT NULL,
  location_id INTEGER NOT NULL,
  day_of_the_week VARCHAR(50) NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL
);  

CREATE TABLE doctor_appointments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  patient_id INTEGER NOT NULL,
  doctor_schedule_id INTEGER NOT NULL,
  appointment_datetime TIMESTAMP NOT NULL
);
