import csv
aux=['Others',0,0,0];
data_input_file =input("name of the source csv file?")
data_output_file =input("name of the target csv file?")
outfile = open (data_output_file, 'w')
with open(data_input_file, 'r') as csvfile:
    filereader = csv.reader(csvfile)
    for row in filereader: 
        if (row[1] == 'Renewed'):
            outfile.write ('Registrar,Renewed,Eligible for Renewal, % Renewals\n');
        else:
            if (int(row[1]) > 1000) :
                aux2 =(str(row[0])+','+str(row[1])+','+str(row[2])+','+str(row[3]));
                outfile.write('%s\n' % (aux2));
            else:
                aux[1]=aux[1]+int(row[1]);
                aux[2]=aux[2]+int(row[2]);
aux[3]=aux[1]/aux[2]*100;
aux2 =str(str(aux[0])+','+str(aux[1])+','+str(aux[2])+','+str(aux[3])+'%');
print (aux2);
outfile.write('%s\n' % (aux2));	   
	
