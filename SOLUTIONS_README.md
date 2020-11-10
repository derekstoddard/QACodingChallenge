# QA Coding Challenge

## Challenge 1. Test a static HTML page
Created and tested using Eclipse Version: 2020-06 (4.16.0)

Run test_challenges.py As Python unit-test

Requires requests library: https://requests.readthedocs.io/en/master/

	python -m pip install requests
	Version: requests==2.24.0
___
## Challenge 2. Test plan

1. Active positive data received

	1.a) Expect alert set to default (not sure, is it set as null?)
	1.b) Expect no alerts, no email notifications
	
2. System receives initial data signifying zero energy

	2.a) Expect Open alert trigger
	2.b) Expect email notification sent to user
	
3. System receives continued data signifying zero energy, Day 2+

	3.a) Expect Open alert trigger to remain
	3.b) Expect email notification to be sent out to user again, 2nd+ notification
	
4. User acknowledges email notification

	4.a) Expect Acknowledged alert status
	4.b) Expect no new email notification now that user has acknowledged alert email
	
5. System begins receiving data signifying positive energy Before user acknowledgement

	5.a) Expect Open alert status update to Closed
	5.b) Expect Closed alert trigger
	5.c) Expect email notification that alert is now Closed
	
6. System begins receiving data signifying positive energy After user acknowledgement

	6.a) Expect Acknowledged alert status update to Closed
	6.b) Expect Closed alert trigger
	6.c) Expect email notification that alert is now Closed
	
7. Zero generation alert received, but email is not proper

	7.a) Expect notification system error (send alert to backup email or some type of system admin?)
___
### Bonus

1. Sunrise - ping for location's sunrise time (alternatively, ping system setting for manually set Sunrise time)

	1.a) Sunrise time returned, expect zero-gen alert system to activate

2. Sunset - ping for location's sunset time (alternatively, ping system setting for manually set Sunset time)

	2.a) Sunset time returned, expect zero-gen alert system to deactivate
