# OpenStick on 4G Modem
We can turn a `Qualcomm 410` (MSM8916) based 4G modem into a portable Linux computer. Let's see how to do that.

* Read the related documentatio [here](https://openstick.org/getting-started/quickstart/)

> ⚠️ Warning: Use this at your own risk. We are not responsible for any damage.

## Installation Steps
You may check the full video for step by step process.

### Use EDL to backup

* We can boot into QDL (EDL) mode as show in the video. You can install the tool [edl](https://github.com/bkerler/edl#grab-files-and-install).

* Type in `edl` to check the board details.

* Perform a full backup. Do this from your required directory.

```bash
# backup the parition details
edl printgpt > gpt.txt

# backup the full data (may take more than 10 min)
edl rf full-emmc.bin

# backup individual partitions (this also takes some time)
mkdir calibration
edl rl calibration --genxm # stores all bin files under calibration folder
```

### Flash using the one-click installer
Keep the modem in `edl` mode and perform the following stpes.

* Download the [openstick-installer.zip](https://github.com/Basistiy/openstick-installer/releases) and unzip in your computer.

* Copy the entire `calibration` folder inside the extracted `openstick-installer` folder.

* Run the installer (you may skip the backp as we have done it already) > select your board and flash with `Debian`. That's it.

```bash
# on Linux
./run.sh

# on Windows
.\run.bat
```
