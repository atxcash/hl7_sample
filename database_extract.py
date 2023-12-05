# MySQL credentials
user="your_username"
password="your_password"
database="your_database"

# Importing datetime module
from datetime import datetime

# Directory with HL7 files
dir="/path/to/your/directory"

# Process each file in the directory
for file in $dir/*.hl7
do
  echo "Processing $file"

  # Run the Python program and save the output
  output=$(python parse_hl7.py "$file")

  # Extract the fields from the output
  patient_id=$(echo "$output" | grep "Patient ID" | cut -d' ' -f3)
  observed_date=$(echo "$output" | grep "Observed Date" | cut -d' ' -f3)
  result_name=$(echo "$output" | grep "Result Name" | cut -d' ' -f3)
  result_value=$(echo "$output" | grep "Result Value" | cut -d' ' -f3)
  result_units=$(echo "$output" | grep "Result Units" | cut -d' ' -f3)
  result_range=$(echo "$output" | grep "Result Range" | cut -d' ' -f3)
  result_flag=$(echo "$output" | grep "Result Flag" | cut -d' ' -f3)

  # Insert the results into the MySQL database
  # Adding create date to the INSERT statement
  create_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  mysql -u$user -p$password $database -e "INSERT INTO results (patient_id, observed_date, result_name, result_value, result_units, result_range, result_flag) VALUES ('$patient_id', '$observed_date', '$result_name', '$result_value', '$result_units', '$result_range', '$result_flag');"
done

# Run a query to display the results
mysql -u$user -p$password $database -e "SELECT * FROM results;"
