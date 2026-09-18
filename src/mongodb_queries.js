// Run these commands in mongosh after pipeline.py

use hospital_appointment_db

// 1. View all appointments
db.appointments.find().pretty()

// 2. Count total appointments
db.appointments.countDocuments()

// 3. Count appointments by status
db.appointments.aggregate([
  {$group: {_id: "$status", total: {$sum: 1}}}
])

// 4. Count appointments by department
db.appointments.aggregate([
  {$group: {_id: "$department", total: {$sum: 1}}},
  {$sort: {total: -1}}
])

// 5. Average lead time
db.appointments.aggregate([
  {$group: {_id: null, average_lead_time: {$avg: "$lead_time"}}}
])

// 6. No-show appointments
db.appointments.find(
  {status: "No-Show"},
  {appointment_id: 1, patient_name: 1, doctor_name: 1, lead_time: 1}
)

// 7. View collections
show collections
