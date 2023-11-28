# hl7_sample
#To Locate a specific Patient in the DB by patientID
SELECT * FROM results WHERE patient_id = 'patient_id';

#locate patients by the results flags with all their patientIDs 
SELECT DISTINCT patient_id FROM results WHERE result_flag = 'your_result_flag';
