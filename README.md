# Box API Automation
In 2023, NIH implemented a policy requiring all external collaborations to be re-approved every 90 days. This can be onerous for certain researchers who have potentially hundreds of such collaborations. They are notified via email, individually for each collaboration. There is no bulk way for a researcher to approve all collaborations and they can only be renewed within 6 days of expiration. 

This repository attempts to use the [Box API](https://developer.box.com/reference/) to automate renewing expiring collaborations.

To get started, use the conda environment provided
```
conda env create -f box.yml
conda activate box
```

You will need to change the `CREDS_FILE` to point to a text file containing the correct creds. This file should have 3 lines. The first is the `client_id`, the second is the `client_secret`, and the third is the `access_token`.

Then to run
```
python box_api_test.py
```
