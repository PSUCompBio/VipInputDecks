mkdir collected_data
rm collected_data/*
for i in {301..972}
do
	echo "directory: scenario_$i"
	cp scenario_$i/viper3d_th_overpressure.txt collected_data/viper3d_th_overpressure_s$i.txt
done
