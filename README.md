# hl7_sample
#To Locate a specific Patient in the DB by patientID
SELECT * FROM results WHERE patient_id = 'patient_id';

#locate patients by the results flags with all their patientIDs 
SELECT DISTINCT patient_id FROM results WHERE result_flag = 'your_result_flag';

#Locate patients by Normal results
SELECT * FROM results WHERE result_flag = '' OR result_flag = 'N';

#Locate patients with Abnormal values 
SELECT * FROM results Where result_flag NOT LIKE '%N%' OR results_flag is NOT NULL;
