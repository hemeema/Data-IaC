#!/bin/bash
#Turn off monitor to avoid multiple calls to this script
sudo systemctl stop nifi-custom-processors.path
sudo systemctl disable nifi-custom-processors.path
sudo rm /etc/systemd/system/nifi-custom-processors*
#Move custom processor
sudo mv /tmp/nifi-hana-custom-processor-2.0.jar /var/lib/nifi/work/nar/extensions/nifi-standard-nar-1.8.0.3.3.1.0-10.nar-unpacked/NAR-INF/bundled-dependencies/nifi-hana-custom-processor-2.0.jar
sudo chown -R nifi:hadoop /var/lib/nifi/work/nar/extensions/nifi-standard-nar-1.8.0.3.3.1.0-10.nar-unpacked/NAR-INF/bundled-dependencies/nifi-hana-custom-processor-2.0.jar
