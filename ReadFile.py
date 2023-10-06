# File: ReadFile.py

# Description: Converts the provided data file into a .csv file

# Name: Fidel C. Otero

# UT EID: fco229

# Date: Fri. 09/22/2023

import sys

def write_col_names(csv_file_name):
    s = ''
    s = s + 'HR' + ','
    s = s + 'Name' + ','
    s = s + 'DM' + ','
    s = s + 'HD' + ','
    s = s + 'SAO' + ','
    s = s + 'FK5' + ','
    s = s + 'IRflag' + ','
    s = s + 'r_IRflag' + ','
    s = s + 'Multiple' + ','
    s = s + 'ADS' + ','
    s = s + 'ADScomp' + ','
    s = s + 'VarID' + ','
    s = s + 'RAh1900' + ','
    s = s + 'RAm1900' + ','
    s = s + 'RAs1900' + ','
    s = s + 'DE-1900' + ','
    s = s + 'DEd1900' + ','
    s = s + 'DEm1900' + ','
    s = s + 'DEs1900' + ','
    s = s + 'RAh' + ','
    s = s + 'RAm' + ','
    s = s + 'RAs' + ','
    s = s + 'DE-' + ','
    s = s + 'DEd' + ','
    s = s + 'DEm' + ','
    s = s + 'DEs' + ','
    s = s + 'GLON' + ','
    s = s + 'GLAT' + ','
    s = s + 'Vmag' + ','
    s = s + 'n_Vmag' + ','
    s = s + 'u_Vmag' + ','
    s = s + 'B-V' + ','
    s = s + 'u_B-V' + ','
    s = s + 'U-B' + ','
    s = s + 'u_U-B' + ','
    s = s + 'R-I' + ','
    s = s + 'n_R-I' + ','
    s = s + 'SpType' + ','
    s = s + 'n_SpType' + ','
    s = s + 'pmRA' + ','
    s = s + 'pmDE' + ','
    s = s + 'n_Parallax' + ','
    s = s + 'Parallax' + ','
    s = s + 'RadVel' + ','
    s = s + 'n_RadVel' + ','
    s = s + 'l_RotVel' + ','
    s = s + 'RotVel' + ','
    s = s + 'u_RotVel' + ','
    s = s + 'Dmag' + ','
    s = s + 'Sep' + ','
    s = s + 'MultID' + ','
    s = s + 'MultCnt' + ','
    s = s + 'NoteFlag'
    csv_file_name.write(f'{s}\n')

def dat_to_csv(dat_file_name, csv_file_name):
    with open(dat_file_name, 'r') as infile_dat:
        with open(csv_file_name, 'w') as infile_csv:
            write_col_names(csv_file_name=infile_csv)
            for line in infile_dat:
                tmp = line.replace(',', ' ')
                tmp = tmp.ljust(198)
                s = ''
                s = s + tmp[0:4] + ','
                s = s + tmp[4:14] + ','
                s = s + tmp[14:25] + ','
                s = s + tmp[25:31] + ','
                s = s + tmp[31:37] + ','
                s = s + tmp[37:41] + ','
                s = s + tmp[41] + ','   
                s = s + tmp[42] + ','    
                s = s + tmp[43] + ','
                s = s + tmp[44:49] + ','
                s = s + tmp[49:51] + ','   
                s = s + tmp[51:60] + ','
                s = s + tmp[60:62] + ','
                s = s + tmp[62:64] + ','   
                s = s + tmp[64:68] + ','
                s = s + tmp[68] + ','
                s = s + tmp[69:71] + ','
                s = s + tmp[71:73] + ','
                s = s + tmp[73:75] + ','
                s = s + tmp[75:77] + ','
                s = s + tmp[77:79] + ','                                                     
                s = s + tmp[79:83] + ','
                s = s + tmp[83] + ','
                s = s + tmp[84:86] + ','
                s = s + tmp[86:88] + ','
                s = s + tmp[88:90] + ','
                s = s + tmp[90:96] + ','
                s = s + tmp[96:102] + ','
                s = s + tmp[102:107] + ','
                s = s + tmp[107] + ','
                s = s + tmp[108] + ','
                s = s + tmp[109:114] + ','
                s = s + tmp[114] + ','
                s = s + tmp[115:120] + ','
                s = s + tmp[120] + ','
                s = s + tmp[121:126] + ','
                s = s + tmp[126] + ','
                s = s + tmp[127:147] + ','
                s = s + tmp[147] + ','
                s = s + tmp[148:154] + ','
                s = s + tmp[154:160] + ','
                s = s + tmp[160] + ','
                s = s + tmp[161:166] + ','
                s = s + tmp[166:170] + ','
                s = s + tmp[170:174] + ','
                s = s + tmp[174:176] + ','
                s = s + tmp[176:179] + ','
                s = s + tmp[179] + ','
                s = s + tmp[180:184] + ','
                s = s + tmp[184:190] + ','
                s = s + tmp[190:194] + ','
                s = s + tmp[194:196] + ','
                s = s + tmp[196]
                infile_csv.write(f'{s}\n')
        infile_csv.close()
    infile_dat.close()

def main():
    dat_file = input('Enter the .dat file to be converted to a .csv file: ')
    csv_file = input('Enter the name of the .csv file you want to create: ')
    dat_to_csv(dat_file, csv_file)

if __name__ == "__main__":
    main()