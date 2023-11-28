import hl7apy
from hl7apy.parser import parse_message

def parse_hl7_message(message_string):
    message = parse_message(message_string)

    patient_id = message['PID'][0]['PID_3'][0]['CX_1'].value
    print(f"Patient ID: {patient_id}")

    for obr in message['OBR']:
        observed_date = obr['OBR_7'].value
        print(f"Observed Date: {observed_date}")

        for obx in obr['OBX']:
            result_name = obx['OBX_3']['CE_2'].value
            result_value = obx['OBX_5'].value
            result_units = obx['OBX_6']['CE_1'].value
            result_range = obx['OBX_7'].value
            result_flag = obx['OBX_8'].value

            print(f"Result Name: {result_name}")
            print(f"Result Value: {result_value}")
            print(f"Result Units: {result_units}")
            print(f"Result Range: {result_range}")
            print(f"Result Flag: {result_flag}")
            print('---')

# Replace with your HL7 ORU message
hl7_message = """
MSH|^~\&|NOVA^Prime+^V1.14.1057.0^PP1719210C^PRIME_PLUS_BUN_MODEL||||20220215083327.245||ORU^R01^ORU_R01|0215083327.245|P|2.5||||||UNICODE UTF-8
PID|1|fid:5821314|||Claw^Bear^||19860717|U||||||||||
PV1|1|U|||||1^Margolis^Dr.^Jeffrey|||||||||||||
SPM|1|||BLD|||||||P||||||20220215083128.000
OBR|1|||^^^^Full Panel^NOVABIO|||||||||||BLD|1^Margolis^Dr.^Jeffrey|||||||||F|||||||||
OBX|1|FT|^^^pH^pH^NOVABIO^M||7.415||7.310 to 7.410|H|||F|||20220215083128.000||||PP1719210C|20220215083128.000
OBX|2|FT|^^^pCO2^pCO2^NOVABIO^M||40.0|mmHg|41.0 to 51.0|L|||F|||20220215083128.000||||PP1719210C|20220215083128.000
OBX|3|FT|^^^Na^Na^NOVABIO^M||142.0|mmol/L|136.0 to 146.0|N|||F|||20220215083128.000||||PP1719210C|20220215083128.000
OBX|4|FT|^^^K^K^NOVABIO^M||3.86|mmol/L|3.50 to 5.10|N|||F|||20220215083128.000||||PP1719210C|20220215083128.000
OBX|5|FT|^^^Cl^Cl^NOVABIO^M||106.6|mmol/L|98.0 to 106.0|H|||F|||20220215083128.000||||PP1719210C|20220215083128.000
OBX|6|FT|^^^Ca^iCa^NOVABIO^M||1.25|mmol/L|1.09 to 1.35|N|||F|||20220215083128.000||||PP1719210C|20220215083128.000
OBX|7|FT|^^^Mg^iMg^NOVABIO^M||0.65|mmol/L|0.45 to 0.60|H|||F|||20220215083128.000||||PP1719210C|20220215083128.000
OBX|8|FT|^^^Glu^Glu^NOVABIO^M||89|mg/dL|65 to 95|N|||F|||20220215083128.000||||PP1719210C|20220215083128.000
OBX|9|FT|^^^Creat^Creat^NOVABIO^M||0.7|mg/dL|0.6 to 1.3|N|||F|||20220215083128.000||||PP1719210C|20220215083128.000
OBX|10|FT|^^^BUN^BUN^NOVABIO^M||15|mg/dL|7 to 18|N|||F|||20220215083128.000||||PP1719210C|20220215083128.000
OBX|11|FT|^^^TCO2^TCO2^NOVABIO^M||27.1|mmol/L|22.0 to 29.0|N|||F|||20220215083128.000||||PP1719210C|20220215083128.000
"""
parse_hl7_message(hl7_message)
