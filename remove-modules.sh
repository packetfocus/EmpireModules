echo "Removing Files"
rm  /tools/Empire/data/module_source/credentials/tmp/Invoke-MassMimikatz.ps1
rm  /tools/Empire/lib/modules/credentials/mimikatz/Invoke-MassMimikatz.py
echo "Cleaning up local files"
rm Invoke-MassMimikatz.ps1
rm Invoke-MassMimikatz.py
rm /tmp/Invoke-MassMimikatz.ps1
rm /tmp/Invoke-MassMimikatz.py
echo "Finished."
