# Box API Automation
In 2023, NIH implemented a policy requiring all external collaborations to be re-approved every 90 days. This can be onerous for certain researchers who have potentially hundreds of such collaborations. They are notified via email, individually for each collaboration. There is no bulk way for a researcher to approve all collaborations and they can only be renewed within 6 days of expiration. 

This repository attempts to use the [Box API](https://developer.box.com/reference/) to automate renewing expiring collaborations.

To get started, use the conda environment provided
```
conda env create -f box.yml
conda activate box
```
The to run
```
python box_api_test.py
```
