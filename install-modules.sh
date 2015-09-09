wget https://raw.githubusercontent.com/packetfocus/EmpireModules/master/Invoke-MassMimikatz.ps1 > /tmp/Invoke-MassMimikatz.ps1
wget https://raw.githubusercontent.com/packetfocus/EmpireModules/master/Invoke-MassMimikatz.py > /tmp/Invoke-MassMimikatz.py
echo "Moving into Empire Directories"
cp  /tmp/Invoke-MassMimikatz.ps1 /tools/Empire/data/module_source/credentials/
cp   /tmp/Invoke-MassMimikatz.py /tools/Empire/lib/modules/credentials/mimikatz/
echo "Cleaning up"
rm Invoke-MassMimikatz.ps1
rm Invoke-MassMimikatz.py
echo "Finished."
