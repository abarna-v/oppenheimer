TESTED ENVIRONMENTS:
--------------------
	1) OS: MacOS
	2) Browser: Chrome
	3) Editor: Eclipse IDE

PRE-REQUISITES:
---------------
	1) Latest Java Should be installed [JAVA 8 UPDATE 321]
	2) Latest Python(2.7.x) or Python(3.x) with pip should be available.
	3) Chrome Browser should be in latest version (100.x.x).
	   3.1) If not respective ChromeDriver should be download and copied to utils folder location.

INSTALLATION STEPS:
-------------------
	1) Copy the auto_bot folder from Git Repository to your Computer (using Download or git clone options)
		a) https://github.com/abarna-v/oppenheimer/
	2) Install the Dependency pip(package) Files
		a) Go the ~/oppenheimer/
		b) Execute : python utils/install_setup.py
	3) Copy the Oppenheimer Proj into the utils direcory.
		a) Go the ~/oppenheimer/utils/
		b) git clone https://github.com/auronsiow/oppenheimer-project-dev.git
		c) Make sure the OppenheimerProjectDev.jar are present in the "~/oppenheimer/utils/" location.

TEST_SUITE.robot
-----------------
	1) SUITE_SETUP
		1.1)	Execute Oppenheimer Project JAR
		1.2)	Verify the Process is running
	2) TEST CASES
		TC_1)	INSERT SINGLE PERSON RECORD
		TC_2)	INSERT MULTIPLE PERSON RECORD
		TC_3)	UPLOAD CSV FILE TO PORTAL
		TC_4)	CALCULATE AMOUNT OF TAX RELIEF
		TC_5)	DISPENSE TAX RELIEF TO WORKING CLASS HEROES
	3) SUITE CLEANUP
		3.1)	Kill all the running Process
		3.2)	Close All Browsers

ROBOT SUITE:
------------
	1)	Go the framework copied Directory : ~/oppenheimerProj/
	2)	Execute the following command:
		$  robot --loglevel DEBUG --timestampoutputs --outputdir logs/ test_scripts/testSuite.robot


EXECUTION_LOGS:
---------------

		iAbarnaV-MacBook-Pro:oppenheimerProj iAbarnaV$ robot --loglevel DEBUG --timestampoutputs --outputdir logs/ tests/testSuite.robot
		Command: /Users/iabarnav/tools/red-workaround/python -m robot.run --listener 	/var/folders/t6/cppytr0906ngmdddzyqdbfq40000gp/T/RobotTempDir13121175446785765543/TestRunnerAgent.py:55086 --argumentfile /var/folders/t6/cppytr0906ngmdddzyqdbfq40000gp/T/RobotTempDir13121175446785765543/args_a4728901.arg/Users/iabarnav/eclipse-workspace/oppenheimerProj
		Suite Executor: Robot Framework 4.1.3 (Python 2.7.18 on darwin)

		oppenheimerProj.Tests.testSuite                                               
		==============================================================================
		TC_1: INSERT SINGLE PERSON RECORD :: INSERT SINGLE RECORD OF A WOR... | PASS |
		\------------------------------------------------------------------------------
		TC_2: INSERT MULTIPLE PERSON RECORD :: INSERT SINGLE RECORD OF A W... | PASS |
		\------------------------------------------------------------------------------
		TC_3: UPLOAD CSV FILE TO PORTAL :: INSERT SINGLE RECORD OF A WORKI... | PASS |
		\------------------------------------------------------------------------------
		TC_4: CALCULATE AMOUNT OF TAX RELIEF :: CALCULATE TAX RELIEF FOR A... | PASS |
		\------------------------------------------------------------------------------
		TC_5: DISPENSE TAX RELIEF TO WORKING CLASS HEROES :: DISPENSE THE ... | PASS |
		\------------------------------------------------------------------------------
		Cleaning the Oppenheimer Project !!!

		oppenheimerProj.Tests.testSuite                                       | PASS |
		5 tests, 5 passed, 0 failed
		\==============================================================================
		oppenheimerProj.Tests                                                 | PASS |
		5 tests, 5 passed, 0 failed
		\==============================================================================
		oppenheimerProj                                                       | PASS |
		5 tests, 5 passed, 0 failed
		\==============================================================================
		Output:  /Users/iabarnav/eclipse-workspace/oppenheimerProj/output.xml
		Log:     /Users/iabarnav/eclipse-workspace/oppenheimerProj/log.html
		Report:  /Users/iabarnav/eclipse-workspace/oppenheimerProj/report.html 

