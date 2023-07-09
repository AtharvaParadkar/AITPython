//Atharva Paradkar 2201144

const mysql = require('mysql');

const connection = mysql.createConnection({
  host: '127.0.0.1',
  user: 'root',
  password: '',
  database: 'student records'
});

connection.connect((error) => {
  if (error) {
    console.error('Error connecting to the database: ', error);
    return;
  }

  console.log('Connected to the database.');

  const students = [
    { name: 'Atharva Paradkar', rollno: 123, age: 23, grade: 'A' },
    { name: 'Ashutosh Saoji', rollno: 142, age: 22, grade: 'B' },
    { name: 'Rohit Savale', rollno: 152, age: 18, grade: 'C+' }
  ];

  connection.query('INSERT INTO student (name, rollno, age, grade) VALUES ?', [students.map(student => [student.name, student.rollno, student.age, student.grade])], (error, result) => {
    if (error) {
      console.error('Error inserting records: ', error);
      return;
    }

    console.log('Records inserted successfully.');

    console.log(result);

    connection.end((error) => {
      if (error) {
        console.error('Error closing the database connection: ', error);
      }

      console.log('Database connection closed.');
    });
  });
});
