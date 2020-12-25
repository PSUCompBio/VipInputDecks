rm collected_data_4/*
for i in {1..162}
do
	echo "directory: scenario_$i"
	cp temp_output_files_4/scenario_$i/viper3d_th_overpressure.txt collected_data_4/viper3d_th_overpressure_front_right_six_s$i.txt
done
