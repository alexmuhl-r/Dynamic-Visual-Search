# This code was written by Alex Muhl-Richardson and Hayward Godwin with assistance from the team at SR Research
# This is a single custom class written for use in conjunction with an experiment created in SR Research's Experiment Builder (EB) and does NOT function independently
# 
# If you use this code, or a modified version, in published work, please cite: 
#	- Our ACP paper: Muhl-Richardson, A., Cornes, K., Godwin, H. J., Garner, M., Hadwin, J. A., Liversedge, S. P. & Donnelly, N. (2018). Searching for Two Categories of Target in Dynamic Visual Displays Impairs Monitoring Ability. Applied Cognitive Psychology, 32(4), 440-449. https://doi.org/10.1002/acp.3416
#	- Our OSF project: Muhl-Richardson, A., Godwin, H. J., Garner, M., Hadwin, J. A., Liversedge, S. P., & Donnelly, N. (2019, May 9). Searching and Monitoring Dynamically Changing Visual Displays. Retrieved from osf.io/ahufd

import sreb
import sreb.graphics
import sreb.time
import pylink
import random

#v4.3 Changelog - Changed random background starting colours to be 5 through to 15 and not just 5 to 7 and 13 to 15.
#				- Not suitable for dual target trials - only self.cond == 0/s1
#				- Attempted to fix the lack of any 0 colour squares appearing
#				- Attempted to fix multiple colour updates in a single loop due to multiple if statements being met in each loop (see "updated == 0" condition)
#				- Also attempted to fix targets not clearing after going into decline from stray if statement

class SquareProp:
	""" Represents and manipulates properties of squares"""

	def __init__(self, id, Xlocation, Ylocation, Xjitter, Yjitter, colour, type, status):
		"""Notes on parameters"""

		self.id = id
		self.Xlocation = Xlocation
		self.Ylocation = Ylocation
		self.Xjitter = Xjitter
		self.Yjitter = Yjitter
		self.colour = colour
		self.status = status
		self.type = type

	def getID(self):
		return self.id
	def setID(self,s):
		self.id = s

	def getXlocation(self):
		return self.Xlocation
	def setXlocation(self,s):
		self.Xlocation = s
		
	def getYlocation(self):
		return self.Ylocation
	def setYlocation(self,s):
		self.Ylocation = s
		
	def getXjitter(self):
		return self.Xjitter
	def setXjitter(self,s):
		self.Xjitter = s
		
	def getYjitter(self):
		return self.Yjitter
	def setYjitter(self,s):
		self.Yjitter = s
		
	def getColour(self):
		return self.colour
	def setColour(self,s):
		self.colour = s

	def getType(self):
		return self.type
	def setType(self,s):
		self.type = s
		
	def getStatus(self):
		return self.status
	def setStatus(self,s):
		self.status = s
		
class StimProp:
	"""Generates the properties of stimuli - both targets and distractors"""
	
	def __init__(self, id, squareid, status, type, rise, life, fall, max, xcoord, ycoord, hot, size):
		
		self.stimid = id
		self.squareid = squareid
		self.status = status
		self.type = type
		self.objectCurrentHeat = 4
		self.xcoord = xcoord
		self.ycoord = ycoord
		self.stimsize = size
		
		self.hot = hot
		
		self.objectTimeToRise = rise
		self.objectLifetime = life
		self.objectTimeToFall = fall
		self.objectTimeToMax = max
		
		
	def getStimid(self):
		return self.stimid
	def setStimid(self,s):
		self.stimid = s
		
	def getSquareid(self):
		return self.squareid
	def setSquareid(self,s):
		self.squareid = s
		
	def getStimstatus(self):
		return self.status
	def setStimstatus(self,s):
		self.status = s
		
	def getObjectTimeToRise(self):
		return self.objectTimeToRise
	def setObjectTimeToRise(self,s):
		self.objectTimeToRise = s
		
	def getObjectLifetime(self):
		return self.objectLifetime
	def setObjectLifetime(self,s):
		self.objectLifetime = s
		
	def getObjectTimeToFall(self):
		return self.objectTimeToFall
	def setObjectTimeToFall(self,s):
		self.objectTimeToFall = s

	def getObjectCurrentHeat(self):
		return self.objectCurrentHeat
	def setObjectCurrentHeat(self,s):
		self.objectCurrentHeat = s

	def getObjectTimeToMax(self):
		return self.objectTimeToMax
	def setObjectTimeToMax(self,s):
		self.objectTimeToMax = s
		
	def getType(self):
		return self.type
	def setType(self,s):
		self.type = s
		
	def getXcoord(self):
		return self.xcoord
	def setXcoord(self,s):
		self.xcoord = s
		
	def getYcoord(self):
		return self.ycoord
	def setYcoord(self,s):
		self.ycoord = s
		
	def getHot(self):
		return self.hot
	def setHot(self,s):
		self.hot = s
		
	def getStimsize(self):
		return self.stimsize
	def setStimsize(self, s):
		self.stimsize = s
		
class numberProp:
	""" Represents and manipulates properties of squares"""

	def __init__(self, id, Xlocation, Ylocation, value, status, type, rise, life, fall, max):
		"""Notes on parameters"""

		self.id = id
		self.Xlocation = Xlocation
		self.Ylocation = Ylocation
		self.value = value
		self.type = type
		self.status = status

		self.numberTimeToRise = rise
		self.numberLifetime = life
		self.numberTimeToFall = fall
		self.numberTimeToMax = max

	def getID(self):
		return self.id
	def setID(self,s):
		self.id = s
		
	def getXlocation(self):
		return self.Xlocation
	def setXlocation(self,s):
		self.Xlocation = s
		
	def getYlocation(self):
		return self.Ylocation
	def setYlocation(self,s):
		self.Ylocation = s
		
	def getValue(self):
		return self.value
	def setValue(self, s):
		self.value = s
		
	def getNumberStatus(self):
		return self.status
	def setNumberStatus(self,s):
		self.status = s

	def getNumberTimeToRise(self):
		return self.numberTimeToRise
	def setNumberTimeToRise(self,s):
		self.numberTimeToRise = s
		
	def getNumberLifetime(self):
		return self.numberLifetime
	def setNumberLifetime(self,s):
		self.numberLifetime = s
		
	def getNumberTimeToFall(self):
		return self.numberTimeToFall
	def setNumberTimeToFall(self,s):
		self.numberTimeToFall = s

	def getNumberCurrentHeat(self):
		return self.numberCurrentHeat
	def setNumberCurrentHeat(self,s):
		self.numberCurrentHeat = s

	def getNumberTimeToMax(self):
		return self.numberTimeToMax
	def setNumberTimeToMax(self,s):
		self.numberTimeToMax = s
		
	def getNumberType(self):
		return self.type
	def setNumberType(self,s):
		self.type = s

class CustomClassTemplate(sreb.EBObject):
	def __init__(self):
		sreb.EBObject.__init__(self)
		
		#Participant and trial basics
		self.ppt_id = ""
		self.cond = ""
		self.prevalence = ""
		self.numberCondition = ""
		self.practice = 0
		self.layout = 0

		#Clear targets/distractors after time
		self.clearing = True
		#Multiple targets display simulataneously
		self.multiple = False
		#Target absent trials
		self.absentTrials = False
		#Have more than one simultaneous number distractor
		self.multipleNumberDistractors = False
				
		#Determines the target colours - can be a value between 0 and 15
		self.rotation = None
		self.numberRotation = None
		
		self.numberTargets = 0 
		
		self.mouseLocation = []
		
		#Feedback noise
		self.whichNoise = 2

		# BASE STUFF
		self.customResource = None;
		self.displayScreenPath=''	# use to store the current screen path in the expt
		self.screen=None		# handle for the screen object
		self.finished = 0		# variable used to check whether the trial has finished;

		self.resources = []
		self.displayMatrix = []
		self.masterDisplayMatrix = []
		self.stimMatrix = []
		self.numberMatrix = []

		# UNIQUE IDENTIFIER FOR EACH REFRESH
		self.uid = 0
		self.rid = 0
		self.shouldChangeDisplay = False
		self.shouldChangeNumbers = False
		self.firstNumBlit = False

		# DIMENSIONS
		self.squareWidth = 18
		self.squareHeight = 18
		
		self.regionWidth = 68
		self.regionHeight = 68

		self.mosaicWidth = 408
		self.mosaicHeight = 272

		self.mosaicStartX = 308
		self.mosaicStartY = 248
		self.numberSquaresX = 6
		self.numberSquaresY = 4
		
		self.numberWidth = 34
		self.numberHeight = 50
		
		
		self.numberObjects = 24
		self.numberStimuli = 4
		
		self.xLocations = []
		self.yLocations = []
		
		# TEMPORAL DIMENSIONS
		self.timeBetweenObjectsMean = 18
		self.timeBetweenObjectsSD = 3
		self.repetitions = 1 # NUMBER OF TIMES TO SHOW EACH LOCATION
		self.objectLifetimeMean = 30
		self.objectLifetimeSD = 1
				
		self.timeBetweenObjectsMeanNumber = 15
		self.timeBetweenObjectsSDNumber = 2
		self.objectLifetimeMeanNumber = 30
		self.objectLifetimeSDNumber = 1

		self.redrawSpeed = 83
		
		# TRIAL INFO
		self.setsize = 0
		self.size = None
		self.objectLocs = None
		self.objectStatus = None
		self.objectTimeToRise = None # CONTROSL THE SPEED AT WHICH THEY RISE FROM THE START OF THE DISPLAY
		self.objectTimeToMax = None # CONTROLS THE SPEED AT WHICH THEY HIT THEIR PEAK
		self.objectType = None
		self.objectLifetime = None
		self.objectTimeToFall = None
		self.objectCurrentHeat = None
		self.isOccupied = []
		self.isOccupiedNumber = []
		self.isFinished = None
		
		self.numberXLocations = [104, 104, 855, 855]
		self.numberYLocations = [78, 594, 78, 594] 
		
		self.targetLocations = []
		
		self.targetCurrentlyVisible = None #USED TO ENSURE THAT ONLY ONE TARGET IS VISIBLE AT ANY ONE TIME
		
		self.numberTargetCurrentlyVisible = None
		self.numberDistractorCurrentlyVisible = None
		
		self.numberTargetOnsets = 0
		
		self.numberTrials = 0
		
		self.objectTimesToRise = []
		
		self.numberTargetsClicked = 0
		
		self.t1 = None
		self.t2 = None
		self.tNumber = None
		
	def setBasics (self, ppt_id, cond, prev, practice, numCond, layout):
		
		self.ppt_id = ppt_id
		self.cond = cond
		self.prevalence = prev
		self.practice = int(practice)
		self.numberCondition = numCond
		self.layout = layout
		
	def setMouseLocation(self, s):
		self.mouseLocation = s
	def getMouseLocation(self):
		return self.mouseLocation
		

		
	# These two methods are used to read and set the extent of the RSVP display;
	# (measured in pixels for the characters displayed);
	def getDisplayExtent(self):
		return self.displayExtent
	def setDisplayExtent(self,s):
		self.displayExtent=s

	# These two methods are used to read and set the trial status;
	def getFinished(self):
		return self.finished
	def setFinished(self,s):
		self.finished=s

	# These two methods are used to read and set the screen path;
	def getDisplayScreenPath(self):
		return self.displayScreenPath
	def setDisplayScreenPath(self,s):
		self.displayScreenPath=s
		
	def getNumberTrials(self):
		return self.numberTrials
	def setNumberTrials(self,s):
		self.numberTrials = s
		
	def getNumberTargetsClicked(self):
		return self.numberTargetsClicked
	def getNumberTargetOnsets(self):
		return self.numberTargetOnsets
		
	def getTargetOne(self):
		return self.t1
	def getTargetTwo(self):
		return self.t2
	def getTargetNumber(self):
		return self.tNumber
		
	def getTargetOnsets(self):
		return self.numberTargetOnsets
	def getTargetsClicked(self):
		return self.numberTargetsClicked
		
	def getTrials(self):
		return self.numberTrials
				
	def getNoise(self):
		return int(self.whichNoise)
		
	# Initialize the custom class graphics.
	def initialize(self):
	
		if self.layout == 0:
			self.mosaicStartX = 308
			self.mosaicStartY = 248
			
			#Temp changes here!!!!!!!!!
			self.numberXLocations = [468, 468, 522, 522]
			self.numberYLocations = [324, 394, 324, 394]
			
		if self.layout == 1:
			self.mosaicStartX = 84
			self.mosaicStartY = 248
			
			self.numberXLocations = [707, 707, 761, 761]
			self.numberYLocations = [324, 394, 324, 394] 
			
			pylink.getEYELINK().sendMessage("ColoursLeftNumbersRight")
			
		if self.layout == 2:
			self.mosaicStartX = 547
			self.mosaicStartY = 248
			
			self.numberXLocations = [244, 244, 298, 298]
			self.numberYLocations = [324, 394, 324, 394]

			pylink.getEYELINK().sendMessage("ColoursRightNumbersLeft")

		if self.layout == 3:
			self.mosaicStartX = 84
			self.mosaicStartY = 248
			
			self.numberXLocations = [244, 244, 298, 298]
			self.numberYLocations = [324, 394, 324, 394]
			
			pylink.getEYELINK().sendMessage("ColoursLeftNumbersLeft")
			
		if self.layout == 4:
			self.mosaicStartX = 547
			self.mosaicStartY = 248
			
			self.numberXLocations = [707, 707, 761, 761]
			self.numberYLocations = [324, 394, 324, 394] 
			
			pylink.getEYELINK().sendMessage("ColoursRightNumbersRight")
		
		self.screen=sreb.graphics.getScreenFromPath(self.getDisplayScreenPath())
		if self.screen is None:
			raise "EBScreen could not be accessed"

		self.resources = self.screen.getResources()

		for x in range(0, len(self.resources)-1):
			self.resources[x].setVisible(False)
			#print(dir(self.resources[x])) debugging

		self.customResource = self.screen.createCustomResource(sreb.EBRectangle(0, 0 ,1024, 768),False,-2)
		self.customResource.setDrawMethodPointer(self.redraw)
		self.customResource.setShouldRedrawMethodPointer(self.shouldRedraw)

		self.lastRedrawDone=0
		self.uid = 0
		
		self.displayMatrix = []
		self.stimMatrix = []
		self.isOccupied = []
		self.isOccupiedNumber = []
		
		if self.absentTrials == True:
			self.numberTargets = 0
			
		if self.absentTrials == False:
			self.numberTargets = self.numberStimuli

		if int(self.ppt_id) < 16:
			self.rotation = int(self.ppt_id)
			
		if int(self.ppt_id) > 15:
			self.rotation = int(self.ppt_id) - 16
			
		if int(self.ppt_id) > 31:
			self.rotation = int(self.ppt_id) - 32
			
		if int(self.ppt_id) > 47:
			self.rotation = int(self.ppt_id) - 48
			
		if self.rotation % 2 == 0:
			self.t1 = 2
		if self.rotation % 2 == 1:
			self.t1 = 10
			
		if self.rotation <= 5:
			self.t2 = self.rotation+10
		if self.rotation >= 6:
			self.t2 = self.rotation-6
			
		if int(self.ppt_id) < 10:
			self.numberRotation = int(self.ppt_id)
			
		if int(self.ppt_id) > 9:
			self.numberRotation = int(self.ppt_id) - 10
			
		if int(self.ppt_id) > 19:
			self.numberRotation = int(self.ppt_id) - 20
			
		if int(self.ppt_id) > 29:
			self.numberRotation = int(self.ppt_id) - 30
			
		if self.numberRotation < 8:
			self.tNumber = self.numberRotation + 18
		 
		if self.numberRotation > 7:
			self.tNumber = self.numberRotation + 8
			
	#Used to set event structure
	def trialStructure(self):
		
		#Do this once at the start of the block
		self.trialArray = []
		
		#Set prevalence level
		
		#Set to 50% - half of trials will have at least one target appear - (18? trial block)
		if int(self.prevalence) == 1:
			for i in range (0, 2):
				self.trialArray.append([0,0])
				self.trialArray.append([1,0])
				self.trialArray.append([2,0])
				self.trialArray.append([0,1])
				self.trialArray.append([1,1])
				self.trialArray.append([2,1])
				self.trialArray.append([0,2])
				self.trialArray.append([1,2])
				self.trialArray.append([2,2])
				
		#OLD - Set to 5.55556% - one eighteenth of trials will have at least one target appear - 
		#if int(self.prevalence) == 0:
		#	for i in range (0, 68):
		#		self.trialArray.append(0)
		#	for i in range (0, 2):
		#		self.trialArray.append(1)
		#		self.trialArray.append(2)
				
		#Set to 66% - two thirds of trials will have at least one target - (3 trial practice block)
		if self.practice == 1:
			self.trialArray = []
			self.trialArray.append([0,0])
			self.trialArray.append([1,0])
			self.trialArray.append([0,1])
		
		random.shuffle(self.trialArray)
		
		
	# Used to reset the trial status
	def reset(self):
	
		### - Added these two lines
		self.displayMatrix = []
		self.stimMatrix = []
		self.isOccupied = []
		self.isOccupiedNumber = []
		self.numberMatrix = []
		
		self.lastRedrawDone=0
		self.finished = 0
		self.uid = 0
		self.rid = 0
		self.shouldChangeDisplay = True
		self.firstNumBlit = True
		
		self.setsize = 1
		
		uidCounter = 0
		
		x_target_start = self.mosaicStartX
		y_target_start = self.mosaicStartY
		time_counter = 0
		time_counter_number = 0
		
		#Do this at the start of each trial
		newObjectTypes = []
		newNumberTypes = []

		self.colourTargetsInTrial = self.trialArray[self.numberTrials][0]
		self.numberTargetsInTrial = self.trialArray[self.numberTrials][1]

		if self.colourTargetsInTrial == 0:
			newObjectTypes = ["DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR"]
		if self.colourTargetsInTrial == 1:
			newObjectTypes = ["TARGET", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR"]
		if self.colourTargetsInTrial == 2:
			newObjectTypes = ["TARGET", "TARGET", "DISTRACTOR", "DISTRACTOR"]
			
		if self.numberTargetsInTrial == 0:
			newNumberTypes = ["DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "NEUTRAL"]
		if self.numberTargetsInTrial == 1:
			newNumberTypes = ["TARGET", "DISTRACTOR", "DISTRACTOR", "NEUTRAL"]
		if self.numberTargetsInTrial == 2:
			newNumberTypes = ["TARGET", "TARGET", "DISTRACTOR", "NEUTRAL"]
				
		random.shuffle(newObjectTypes)
		random.shuffle(newNumberTypes)
		

		for x in range (0, 4):

			for y in range (0, 6):

				self.xLocations.append((y*self.regionWidth)+x_target_start)
				self.yLocations.append((x*self.regionHeight)+y_target_start)
				
				
		#for y in range (1, 4, 2):
			
			#for x in range (1, 6, 2):
				
					#templocations = [x,y]
					
					#self.targetLocations.append(templocations)
					
		self.targetLocations.append([1,1])
		self.targetLocations.append([1,3])
		self.targetLocations.append([5,1])
		self.targetLocations.append([5,3])
		
		for j in range(0, self.numberObjects):
				
			xJitterAmount = random.randint(5,36)
			yJitterAmount = random.randint(5,36)
				
			#Create a square of class SquareProp with an ID, a base X location, a base Y location, random x jitter, random y jitter, a random medium heat, set to PASSIVE and NEUTRAL type and NEUTRAL status
			square = SquareProp(j, self.xLocations[j], self.yLocations[j], xJitterAmount, yJitterAmount, random.choice([5,6,7,8,9,10,11,12,13,14,15]), "NEUTRAL", "NEUTRAL") 
				
			self.displayMatrix.append(square)
			
		numberTimeToRiseTemp = []
			
		for n in range (0, 4):
		
			time_counter_number = uidCounter + (random.normalvariate(self.timeBetweenObjectsMeanNumber, self.timeBetweenObjectsSDNumber)) + time_counter_number
			numberTimeToRiseTemp.append(time_counter_number)
				
			newLifetimeNumber = (random.normalvariate(self.objectLifetimeMeanNumber, self.objectLifetimeSDNumber))
			timeToFallNumber = newLifetimeNumber # + time_counter
		
			number = numberProp(n, self.numberXLocations[n], self.numberYLocations[n], random.choice([21,22,23,24,25]), "PASSIVE", newNumberTypes[n], 0, newLifetimeNumber, timeToFallNumber, newLifetimeNumber/2)
			
			self.numberMatrix.append(number)
						

		for j in range (0, 4):
			
			random.shuffle(numberTimeToRiseTemp)
				
			self.numberMatrix[j].setNumberTimeToRise(numberTimeToRiseTemp[0])
			self.numberMatrix[j].setNumberTimeToFall(self.numberMatrix[j].getNumberTimeToFall()+numberTimeToRiseTemp[0])
			
		for r in range (0, self.repetitions):
		
			objectTimeToRiseTemp = []
				
			for j in range (0, self.numberStimuli):
			
				self.setsize = self.setsize + 1
				
				targetJitterX = random.randint(-1,0)
				targetJitterY = random.randint(-1,0)
				
				hotOrCold = []
				
				if int(self.cond) == 0:
					hotOrCold = [True, True]
					
				if int(self.cond) == 1:
					hotOrCold = [False, False]
					
				if int(self.cond) == 2:
					hotOrCold = [True, False]
					
				random.shuffle(hotOrCold)
				
				time_counter = uidCounter + (random.normalvariate(self.timeBetweenObjectsMean, self.timeBetweenObjectsSD)) + time_counter
				objectTimeToRiseTemp.append(time_counter)
				
				newLifetime = (random.normalvariate(self.objectLifetimeMean, self.objectLifetimeSD))
				timeToFall = newLifetime # + time_counter

				#Will the non-unique object ID cause problems - maybe make it unique and use (r*j)?
				
				#Could get overlap with random locations (same location for multiple stimuli) - but also, a non-unique ID provides a basis for checking of self.isOccupied to function
				#Create a stimulus of class StimProp with a non-unique ID, a random corresponding square ID, PASSIVE status, a shuffled type, a time to rise, a lifetime, a time to fall and a time to max + a random x coordinate and random y coordinate + and a random True or False (hot or cold) and a size
				stim = StimProp(j, 0, "PASSIVE", newObjectTypes[j], 0, newLifetime, timeToFall, newLifetime/2, self.targetLocations[j][0]+targetJitterX, self.targetLocations[j][1]+targetJitterY, hotOrCold[0], random.randint(0,0))
				
				self.stimMatrix.append(stim)
				
				#print(time_counter)
				
			#Shuffle times to rise so that they don't all pop up in order from left to right
			for j in range (0, self.numberStimuli):
			
				random.shuffle(objectTimeToRiseTemp)
				
				self.stimMatrix[j].setObjectTimeToRise(objectTimeToRiseTemp[0])
				self.stimMatrix[j].setObjectTimeToFall(self.stimMatrix[j].getObjectTimeToFall()+objectTimeToRiseTemp[0])
			
		#Match up targets/distractors from the stimMatrix to the corresponding squares in the displayMatrix so their colour can be controlled correctly.
		for j in range(0, self.numberObjects):
			
			for r in range (0, self.numberStimuli):
			
				coords = self.determineBroadCellPosition(self.displayMatrix[j].getXlocation(), self.displayMatrix[j].getYlocation())
			
				if self.stimMatrix[r].getXcoord() == coords[0] and self.stimMatrix[r].getYcoord() == coords[1]:
				
					self.displayMatrix[j].setType(self.stimMatrix[r].getType())
					self.displayMatrix[j].setStatus(self.stimMatrix[r].getStimstatus())

		for j in range(0,self.numberStimuli): #Adds to list one boolean value for each target location - independent of number of repetitions/underlying targets at same locations

			self.isOccupied.append(False)
			
			if j < 4:
				self.isOccupiedNumber.append(False)
			
		self.targetCurrentlyVisible = False
		self.numberTargetCurrentlyVisible = False
		self.numberDistractorCurrentlyVisible = False
		
		self.numberTrials = self.numberTrials + 1
		
	def setTrue(self):
		self.shouldChangeDisplay = True
		
		
	def sendJitterMessages(self):
	
		#Send one off messages with the jitter values for the entire display
		
		xJitterList = ""
		yJitterList = ""
		
		for j in range (0, self.numberObjects):
		
			xJitterList = xJitterList + str(self.displayMatrix[j].getXjitter())+";"
			yJitterList = yJitterList + str(self.displayMatrix[j].getYjitter())+";"
			
		#self.xJitterList = ''.join(self.xJitterList)
		#self.yJitterList = ''.join(self.yJitterList)

		numberXmessages = len(xJitterList)/128
		numberYmessages = len(yJitterList)/128
		
		pylink.getEYELINK().sendMessage("X JITTER LIST")
		
		for x in range (0,numberXmessages+1):
			pylink.getEYELINK().sendMessage(str(xJitterList[x*128:(x*128)+128]))
			
		pylink.getEYELINK().sendMessage("Y JITTER LIST")
		
		for x in range (0,numberYmessages+1):
			pylink.getEYELINK().sendMessage(str(yJitterList[x*128:(x*128)+128]))
			
		xStimList = ""
		yStimList = ""
		
		for j in range (0, self.numberStimuli):
		
			xStimList = xStimList + str(self.stimMatrix[j].getXcoord())+";"
			yStimList = yStimList + str(self.stimMatrix[j].getYcoord())+";"
			
		numberXmessages = len(xJitterList)/128
		numberYmessages = len(yJitterList)/128
		
		pylink.getEYELINK().sendMessage("X STIM LIST")
		
		for x in range (0,numberXmessages+1):
			pylink.getEYELINK().sendMessage(str(xStimList[x*128:(x*128)+128]))
			
		pylink.getEYELINK().sendMessage("Y STIM LIST")
		
		for x in range (0,numberYmessages+1):
			pylink.getEYELINK().sendMessage(str(yStimList[x*128:(x*128)+128]))
			
	def redraw(self):
				
		start = sreb.time.getCurrentTime()

		shouldUpdate = random.randint(self.redrawSpeed,100)
		
		#pylink.getEYELINK().sendMessage(str(self.mouseLocation))
		
		if (shouldUpdate == 100):
			self.shouldChangeDisplay= True

		if (self.shouldChangeDisplay == True):
		
			#DO THIS FOR COLOURS AND NUMBERS WHEN j IS LESS THAN 4
		
			self.rid = self.rid + 1
		
			#Set as fixed number for now (was self.setsize) - but perhaps use self.numberStimuli instead
			for j in range (0, self.numberStimuli):
		
				#Reduce the time to rise
				self.stimMatrix[j].setObjectTimeToRise(self.stimMatrix[j].getObjectTimeToRise()-random.random())
				
				if j < 4:
					self.numberMatrix[j].setNumberTimeToRise(self.numberMatrix[j].getNumberTimeToRise()-random.random())
			
				#Reduce time to max
				if self.stimMatrix[j].getStimstatus() == "ACTIVE":
					self.stimMatrix[j].setObjectTimeToMax(self.stimMatrix[j].getObjectTimeToMax()-random.random())
					self.stimMatrix[j].setObjectTimeToFall(self.stimMatrix[j].getObjectTimeToFall()-random.random())
					
				if j < 4 and self.numberMatrix[j].getNumberStatus() == "ACTIVE":
					self.numberMatrix[j].setNumberTimeToMax(self.numberMatrix[j].getNumberTimeToMax()-random.random())
					self.numberMatrix[j].setNumberTimeToFall(self.numberMatrix[j].getNumberTimeToFall()-random.random())
					
				#If past its time then cool it off - I'm not sure slow decline has actually been implemented yet
				if self.stimMatrix[j].getObjectTimeToRise() <= 0 and self.stimMatrix[j].getStimstatus() == "ACTIVE" and self.stimMatrix[j].getObjectTimeToFall()+self.stimMatrix[j].getObjectTimeToMax() <= 0:
			
					self.stimMatrix[j].setStimstatus("IN_DECLINE")
					
				if self.numberMatrix[j].getNumberTimeToRise() <= 0 and self.numberMatrix[j].getNumberStatus() == "ACTIVE" and self.numberMatrix[j].getNumberTimeToFall()+self.numberMatrix[j].getNumberTimeToMax() <= 0 and j < 4:
			
					self.numberMatrix[j].setNumberStatus("IN_DECLINE")
						
				#If ready (and location not already occupied) make active - I don't know if the ownership bit is necessary in the new version ##
				#Ownership bit definitely not necessary
				if self.stimMatrix[j].getObjectTimeToRise() <= 0 and self.stimMatrix[j].getStimstatus() == "PASSIVE" and self.isOccupied[j] == False and self.stimMatrix[j].getType() == "DISTRACTOR":
			
					self.stimMatrix[j].setStimstatus("ACTIVE")
					self.isOccupied[j] = True
					#print("DISTRACTOR ONSET")
					
					
				if self.numberMatrix[j].getNumberTimeToRise() <= 0 and self.numberMatrix[j].getNumberStatus() == "PASSIVE" and self.isOccupiedNumber[j] == False and self.numberMatrix[j].getNumberType() == "DISTRACTOR" and j < 4 and self.numberDistractorCurrentlyVisible == False:
			
					self.numberMatrix[j].setNumberStatus("ACTIVE")
					self.isOccupiedNumber[j] = True
					
					if self.multipleNumberDistractors == False:
						self.numberDistractorCurrentlyVisible = True
					#print("DISTRACTOR ONSET")
				
				#Seriously, what the fuck was the point of the last part of this if statement?!
				#I think it was a really dumb way of making sure there were target absent trials...
				if self.stimMatrix[j].getObjectTimeToRise() <= 0 and self.stimMatrix[j].getStimstatus() == "PASSIVE" and self.isOccupied[j] == False and self.stimMatrix[j].getType() == "TARGET" and self.targetCurrentlyVisible == False: #and self.numberTargetOnsets < self.numberTargets:
			
					self.stimMatrix[j].setStimstatus("ACTIVE")
					self.isOccupied[j] = True
					self.numberTargetOnsets = self.numberTargetOnsets + 1
					#print("TARGET ONSET")
					
					if self.multiple == False:
						self.targetCurrentlyVisible = True
					
				if self.numberMatrix[j].getNumberTimeToRise() <= 0 and self.numberMatrix[j].getNumberStatus() == "PASSIVE" and self.isOccupiedNumber[j] == False and self.numberMatrix[j].getNumberType() == "TARGET" and self.numberTargetCurrentlyVisible == False and j < 4:
			
					self.numberMatrix[j].setNumberStatus("ACTIVE")
					self.isOccupiedNumber[j] = True
					#print("TARGET ONSET")
					
					if self.multiple == False:
						self.numberTargetCurrentlyVisible = True
						
					
					
				# SET UP CELLS THAT NEIGHBOUR THE TARGET
					#for x in range(-self.stimMatrix[j].getStimsize(), self.stimMatrix[j].getStimsize()+1):

						#for y in range(-self.stimMatrix[j].getStimsize(), self.stimMatrix[j].getStimsize()+1):

							#neighbourCell = self.determineBroadCellRowIndexInMatrix(self.stimMatrix[j].getXcoord()+x, self.stimMatrix[j].getYcoord()+y)

							# THIS MEANS IT IGNORES THE TARGET SQUARE SO WON'T WRITE OVER IT
							#if (self.displayMatrix[neighbourCell].getType() != self.stimMatrix[j].getType()):
								#self.displayMatrix[neighbourCell].setType("OBJECT_NEIGHBOUR")
								#This final line appears to be for ownership so is almost certainly redundant
								#self.displayMatrix[neighbourCell][8] = j
								
			#Sends a number of messages that are sliced to 128 characters long
			#These include refresh ID at the start
			#Colour information for all squares
			#Status and type for all stimuli (targets/distractors)

			self.messageString = ""

			#Begin every series of messages with the refresh ID
			self.messageString = self.messageString + "R_ID" + str(self.rid) + ";"

			for o in range (0, self.numberObjects):
				
				self.messageString = self.messageString + str(self.displayMatrix[o].getColour()) + ";"
			
			self.numberMessages = len(self.messageString)/128
				
			for m in range (0, self.numberMessages+1):

				pylink.getEYELINK().sendMessage(str(self.messageString[m*128:(m*128)+128]))
				
			self.messageTwo = ""
				
			for s in range (0, self.numberStimuli):
			
				if self.stimMatrix[s].getStimstatus() == "PASSIVE":
					self.messageTwo = self.messageTwo + "P" + ";"
				if self.stimMatrix[s].getStimstatus() == "ACTIVE":
					self.messageTwo = self.messageTwo + "A" + ";"
				if self.stimMatrix[s].getStimstatus() == "IN_DECLINE":
					self.messageTwo = self.messageTwo + "I" + ";"
				if self.stimMatrix[s].getStimstatus() == "CLEARED":
					self.messageTwo = self.messageTwo + "C" + ";"
					
			for s in range (0, self.numberStimuli):
			
				if self.stimMatrix[s].getType() == "TARGET":
					self.messageTwo = self.messageTwo + "T" + ";"
				if self.stimMatrix[s].getType() == "DISTRACTOR":
					self.messageTwo = self.messageTwo + "D" + ";"
					
			self.numberMessagesOne = len(self.messageTwo)/128
				
			for m in range (0, self.numberMessagesOne+1):

				pylink.getEYELINK().sendMessage(str(self.messageTwo[m*128:(m*128)+128]))
				
			self.messageThree = "num;"
			
			for s in range (0,4):
				self.messageThree = self.messageThree + str(self.numberMatrix[s].getValue()) + ";"
				
				if self.numberMatrix[s].getNumberStatus() == "PASSIVE":
					self.messageThree = self.messageThree + "P" + ";"
				if self.numberMatrix[s].getNumberStatus() == "ACTIVE":
					self.messageThree = self.messageThree + "A" + ";"
				if self.numberMatrix[s].getNumberStatus() == "IN_DECLINE":
					self.messageThree = self.messageThree + "I" + ";"
				if self.numberMatrix[s].getNumberStatus() == "CLEARED":
					self.messageThree = self.messageThree + "C" + ";"
				if self.numberMatrix[s].getNumberType() == "TARGET":
					self.messageThree = self.messageThree + "T" + ";"
				if self.numberMatrix[s].getNumberType() == "DISTRACTOR":
					self.messageThree = self.messageThree + "D" + ";"
				if self.numberMatrix[s].getNumberType() == "NEUTRAL":
					self.messageThree = self.messageThree + "N" + ";"
					
			self.numberMessagesTwo = len(self.messageThree)/128
				
			for m in range (0, self.numberMessagesTwo+1):

				pylink.getEYELINK().sendMessage(str(self.messageThree[m*128:(m*128)+128]))
				
				
			#Now to do the colours of all cells in the display
			
			target = self.customResource
			rowIndex = 0
		
			for y in range (0, 4):
		
				for x in range (0, 6):
					
					if self.displayMatrix[rowIndex].getType() == "NEUTRAL" and int(self.cond) == 0 or self.displayMatrix[rowIndex].getStatus() == "CLEARED" and int(self.cond) == 0:
				
						upDown = random.randint(0,5)
						
						updated = 0
					
						#Keep neutral background squares varying between the middle heat levels
						if (upDown == 1 and 5 <= self.displayMatrix[rowIndex].getColour() <= 15 and self.displayMatrix[rowIndex].getColour() - 1 >= 5) and updated == 0:
							self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() - 1)
							updated = 1
						if (upDown == 0 and 5 <= self.displayMatrix[rowIndex].getColour() <= 15 and self.displayMatrix[rowIndex].getColour() + 1 <= 15) and updated == 0:
							self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() + 1)
							updated = 1
							
						
					if (self.displayMatrix[rowIndex].getType() =="TARGET" or self.displayMatrix[rowIndex].getType() =="DISTRACTOR"):
						
						currentObject = self.determineStimLocation(x,y)
						
						self.displayMatrix[rowIndex].setStatus(self.stimMatrix[currentObject].getStimstatus())
						
						if self.stimMatrix[currentObject].getStimstatus() == "PASSIVE":
						
							upDown = random.randint(0,5)
							
							updated = 0
					
							#Keep passive stim squares varying between the middle heat levels
							if (upDown == 1 and 5 <= self.displayMatrix[rowIndex].getColour() <= 15 and self.displayMatrix[rowIndex].getColour() - 1 >= 5) and updated == 0:
								self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() - 1)
								updated = 1
							if (upDown == 0 and 5 <= self.displayMatrix[rowIndex].getColour() <= 15 and self.displayMatrix[rowIndex].getColour() + 1 <= 15) and updated == 0:
								self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() + 1)
								updated = 1
						
						
						#If it is a hot target - do this loop for temperature control
						if self.stimMatrix[currentObject].getHot() == True:
				
						
							upDown = random.randint(1,10)
					
							if upDown >= 8 and self.stimMatrix[currentObject].getStimstatus() == "IN_DECLINE" and self.clearing == True:
					
								self.clearObject([x,y],rowIndex)
					
							#Targets can go to max heat
							if self.displayMatrix[rowIndex].getType() == "TARGET" and self.stimMatrix[currentObject].getStimstatus() == "ACTIVE" and self.stimMatrix[currentObject].getObjectTimeToMax() <= 0:
					
								updated = 0
					
								if (upDown >= 8 and 2 < self.displayMatrix[rowIndex].getColour() <= 9 and self.displayMatrix[rowIndex].getColour() - 1 >= 2) and updated == 0:
									self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() - 1)
									updated = 1
										
								#Extra if statements for looping colour round the end of the scale
								if upDown >=8 and 10 <= self.displayMatrix[rowIndex].getColour() <= 15 and self.displayMatrix[rowIndex].getColour() + 1 <= 15 and updated == 0:
									self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() + 1)
									updated = 1
									
								if upDown >=8 and self.displayMatrix[rowIndex].getColour() == 15 and updated == 0:
									self.displayMatrix[rowIndex].setColour(0)
									updated = 1

								if (upDown >=8 and self.displayMatrix[rowIndex].getColour() < 2 and self.displayMatrix[rowIndex].getColour() + 1 <= 2) and updated == 0:
									self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() + 1)
									updated = 1
								
							if self.displayMatrix[rowIndex].getType() == "TARGET" and self.stimMatrix[currentObject].getStimstatus() == "ACTIVE" and self.stimMatrix[currentObject].getObjectTimeToMax() > 0:
								
								upDownTwo = 0 #random.randint(0,1)
								
								updated = 0

								if (upDown >=8 and upDownTwo == 0 and 2 < self.displayMatrix[rowIndex].getColour() <= 9	 and self.displayMatrix[rowIndex].getColour() - 1 >= 3) and updated == 0:
									self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() - 1)
									updated = 1
									
								#Extra if statements for looping colour round the end of the scale
								if upDown >=8 and 10 <= self.displayMatrix[rowIndex].getColour() <= 15 and self.displayMatrix[rowIndex].getColour() + 1 <= 15 and updated == 0:
									self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() + 1)
									updated = 1
									
								if upDown >=8 and self.displayMatrix[rowIndex].getColour() == 15 and updated == 0:
									self.displayMatrix[rowIndex].setColour(0)
									updated = 1
										
								if (upDown >=8 and upDownTwo == 0 and self.displayMatrix[rowIndex].getColour() < 2 and self.displayMatrix[rowIndex].getColour() + 1 <= 1) and updated == 0:
									self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() + 1)
									updated = 1
								
							#Distractors cannot go to max heat but can go up
							if self.displayMatrix[rowIndex].getType()=="DISTRACTOR" and self.stimMatrix[currentObject].getStimstatus() == "ACTIVE":
							
								upDownTwo = 0 #random.randint(0,1)
								
								updated = 0

								if (upDown >=8 and upDownTwo == 0 and 2 < self.displayMatrix[rowIndex].getColour() <= 9	 and self.displayMatrix[rowIndex].getColour() - 1 >= 3) and updated == 0:
									self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() - 1)
									updated = 1
									
								#Extra if statements for looping colour round the end of the scale
								if upDown >=8 and 10 <= self.displayMatrix[rowIndex].getColour() <= 15 and self.displayMatrix[rowIndex].getColour() + 1 <= 15 and updated == 0:
									self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() + 1)
									updated = 1

								if upDown >=8 and self.displayMatrix[rowIndex].getColour() == 15 and updated == 0:
									self.displayMatrix[rowIndex].setColour(0)
									updated = 1
										
								if (upDown >=8 and upDownTwo == 0 and self.displayMatrix[rowIndex].getColour() < 2 and self.displayMatrix[rowIndex].getColour() + 1 <= 1) and updated == 0:
									self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() + 1)
									updated = 1
									
								#Some distractors only get to within two steps of the target colour
								#if (upDown >= 5 and upDownTwo == 1 and self.displayMatrix[rowIndex].getColour() > 2 and self.displayMatrix[rowIndex].getColour() - 1 >= 4):
									#self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() - 1)
										
								#if (upDown >= 5 and upDownTwo == 1 and self.displayMatrix[rowIndex].getColour() < 2 and self.displayMatrix[rowIndex].getColour() + 1 <= 0):
										#self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() + 1)
										
							# NOW UPDATE THE MOUNTAIN REGIONS AROUND THE CENTRE
							# NEED TO DO THIS HERE OR TEMPORAL LOOP ISSUES HAPPEN

							#for xSize in range((x - self.stimMatrix[currentObject].getStimsize()), (self.stimMatrix[currentObject].getStimsize() + x+1)):

								#for ySize in range(-self.stimMatrix[currentObject].getStimsize() + y, self.stimMatrix[currentObject].getStimsize() + y+1):

									#neighbourCell = self.determineBroadCellRowIndexInMatrix(xSize, ySize)

									#if (self.displayMatrix[neighbourCell].getType()  == "OBJECT_NEIGHBOUR"):

										#xDistance = abs(xSize-x)
										#yDistance = abs(ySize-y)

										#distance = max([xDistance, yDistance])

										#distance = distance + random.randint(0,2)

										#if (self.displayMatrix[rowIndex].getColour() + distance <= 9):

											#self.displayMatrix[neighbourCell].setColour(self.displayMatrix[rowIndex].getColour() + distance)
									
						#If it is a cold target - do this loop for temperature control
						#Cold targets redundant for prevalence experiments
						if self.stimMatrix[currentObject].getHot() == False:
						
							nothing = 0
				
							#if (self.displayMatrix[rowIndex].getColour() != 10):
					
								#upDown = random.randint(1,10)
						
								#if self.stimMatrix[currentObject].getStimstatus() == "IN_DECLINE" and self.clearing == True:
								
										#self.clearObject([x,y],rowIndex)
										
								#Targets can go to max heat
								#if self.displayMatrix[rowIndex].getType() == "TARGET" and self.stimMatrix[currentObject].getStimstatus() == "ACTIVE" and self.stimMatrix[currentObject].getObjectTimeToMax() <= 0:
						
									#if (upDown >=9 and self.displayMatrix[rowIndex].getColour() > 10 and self.displayMatrix[rowIndex].getColour() - 1 >= 10):
										#self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() - 1)
											
									#if (upDown >=9 and self.displayMatrix[rowIndex].getColour() < 10 and self.displayMatrix[rowIndex].getColour() + 1 <= 10):
										#self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() + 1)
									
								#Distractors cannot go to max heat
								#if self.displayMatrix[rowIndex].getType()=="DISTRACTOR" and self.stimMatrix[currentObject].getStimstatus() == "ACTIVE":
								
									#upDownTwo = 0 #random.randint(0,1)

									#if (upDown >=9 and upDownTwo == 0 and self.displayMatrix[rowIndex].getColour() > 10 and self.displayMatrix[rowIndex].getColour() - 1 >= 11):
										#self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() - 1)
											
									#if (upDown >=9 and upDownTwo == 0 and self.displayMatrix[rowIndex].getColour() < 10 and self.displayMatrix[rowIndex].getColour() + 1 <= 9):
											#self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() + 1)
										
									#Some distractors only get to within two steps of the target colour
									#if (upDown >= 5 and upDownTwo == 1 and self.displayMatrix[rowIndex].getColour() > 10 and self.displayMatrix[rowIndex].getColour() - 1 >= 12):
										#self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() - 1)
											
									#if (upDown >= 5 and upDownTwo == 1 and self.displayMatrix[rowIndex].getColour() < 10 and self.displayMatrix[rowIndex].getColour() + 1 <= 8):
											#self.displayMatrix[rowIndex].setColour(self.displayMatrix[rowIndex].getColour() + 1)
								 
								#NOW UPDATE THE MOUNTAIN REGIONS AROUND THE CENTRE
								# NEED TO DO THIS HERE OR TEMPORAL LOOP ISSUES HAPPEN

								#for xSize in range((x - self.stimMatrix[currentObject].getStimsize()), (self.stimMatrix[currentObject].getStimsize() + x+1)):

									#for ySize in range(-self.stimMatrix[currentObject].getStimsize() + y, self.stimMatrix[currentObject].getStimsize() + y+1):

										#neighbourCell = self.determineBroadCellRowIndexInMatrix(xSize, ySize)

										#if (self.displayMatrix[neighbourCell].getType()  == "OBJECT_NEIGHBOUR"):

											#xDistance = abs(xSize-x)
											#yDistance = abs(ySize-y)

											#distance = max([xDistance, yDistance])

											#distance = distance + random.randint(0,2)

											#if (self.displayMatrix[rowIndex].getColour() + distance <= 9):

												#self.displayMatrix[neighbourCell].setColour(self.displayMatrix[rowIndex].getColour() + distance)
					rowIndex = rowIndex+1
					
			for r in range (0, 4):
		
				if (self.numberMatrix[r].getNumberType() == "NEUTRAL" or self.numberMatrix[r].getNumberStatus() == "CLEARED"):
			
					upDown = random.randint(0,5)
					
					updated = 0
				
					#Keep neutral background squares varying between the middle heat levels
					if (upDown == 0 and 21 <= self.numberMatrix[r].getValue() <= 25 and self.numberMatrix[r].getValue() - 1 >= 21) and updated == 0:
						self.numberMatrix[r].setValue(self.numberMatrix[r].getValue() - 1)
						updated = 1
					if (upDown == 1 and 21 <= self.numberMatrix[r].getValue() <= 25 and self.numberMatrix[r].getValue() + 1 <= 25) and updated == 0:
						self.numberMatrix[r].setValue(self.numberMatrix[r].getValue() + 1)
						updated = 1
						
					
				if (self.numberMatrix[r].getNumberType() =="TARGET" or self.numberMatrix[r].getNumberType() =="DISTRACTOR"):
					
					self.numberMatrix[r].setNumberStatus(self.numberMatrix[r].getNumberStatus())
					
					if (self.numberMatrix[r].getNumberStatus() == "PASSIVE" or self.numberMatrix[r].getNumberStatus() == "NEUTRAL"):
					
						upDown = random.randint(0,5)
						
						updated = 0
				
						#Keep passive stim squares varying between the middle heat levels
						if (upDown == 0 and 21 <= self.numberMatrix[r].getValue() <= 25 and self.numberMatrix[r].getValue() - 1 >= 21) and updated == 0:
							self.numberMatrix[r].setValue(self.numberMatrix[r].getValue() - 1)
							updated = 1
						if (upDown == 1 and 21 <= self.numberMatrix[r].getValue() <= 25 and self.numberMatrix[r].getValue() + 1 <= 25) and updated == 0:
							self.numberMatrix[r].setValue(self.numberMatrix[r].getValue() + 1)
							updated = 1
					
					upDown = random.randint(1,10)
			
					if upDown >= 8 and self.numberMatrix[r].getNumberStatus() == "IN_DECLINE" and self.clearing == True:
			
						self.clearNumber(r)
			
					#Targets can go to max heat
					if self.numberMatrix[r].getNumberType() == "TARGET" and self.numberMatrix[r].getNumberStatus() == "ACTIVE" and self.numberMatrix[r].getNumberTimeToMax() <= 0:
			
						updated = 0
			
						if (upDown >= 8 and 18 < self.numberMatrix[r].getValue() <= 22 and self.numberMatrix[r].getValue() - 1 >= 18) and updated == 0:
							self.numberMatrix[r].setValue(self.numberMatrix[r].getValue() - 1)
							updated = 1
								
						#Extra if statements for looping colour round the end of the scale
						if upDown >=8 and 23 <= self.numberMatrix[r].getValue() <= 25 and self.numberMatrix[r].getValue() + 1 <= 25 and updated == 0:
							self.numberMatrix[r].setValue(self.numberMatrix[r].getValue() + 1)
							updated = 1
							
						if upDown >=8 and self.numberMatrix[r].getValue() == 25 and updated == 0:
							self.numberMatrix[r].setValue(16)
							updated = 1

						if (upDown >=8 and self.numberMatrix[r].getValue() < 18 and self.numberMatrix[r].getValue() + 1 <= 18) and updated == 0:
							self.numberMatrix[r].setValue(self.numberMatrix[r].getValue() + 1)
							updated = 1
						
					if self.numberMatrix[r].getNumberType() == "TARGET" and self.numberMatrix[r].getNumberStatus() == "ACTIVE" and self.numberMatrix[r].getNumberTimeToMax() > 0:
						
						upDownTwo = 0 #random.randint(0,1)
						
						updated = 0

						if (upDown >= 8 and 18 < self.numberMatrix[r].getValue() <= 22 and self.numberMatrix[r].getValue() - 1 > 18) and updated == 0:
							self.numberMatrix[r].setValue(self.numberMatrix[r].getValue() - 1)
							updated = 1
								
						#Extra if statements for looping colour round the end of the scale
						if upDown >=8 and 23 <= self.numberMatrix[r].getValue() <= 25 and self.numberMatrix[r].getValue() + 1 <= 25 and updated == 0:
							self.numberMatrix[r].setValue(self.numberMatrix[r].getValue() + 1)
							updated = 1
							
						if upDown >=8 and self.numberMatrix[r].getValue() == 25 and updated == 0:
							self.numberMatrix[r].setValue(16)
							updated = 1

						if (upDown >=8 and self.numberMatrix[r].getValue() < 18 and self.numberMatrix[r].getValue() + 1 < 18) and updated == 0:
							self.numberMatrix[r].setValue(self.numberMatrix[r].getValue() + 1)
							updated = 1
						
					#Distractors cannot go to max heat but can go up
					if self.numberMatrix[r].getNumberType()=="DISTRACTOR" and self.numberMatrix[r].getNumberStatus() == "ACTIVE":
					
						upDownTwo = 0 #random.randint(0,1)
						
						updated = 0

						if (upDown >= 8 and 18 < self.numberMatrix[r].getValue() <= 22 and self.numberMatrix[r].getValue() - 1 > 18) and updated == 0:
							self.numberMatrix[r].setValue(self.numberMatrix[r].getValue() - 1)
							updated = 1
								
						#Extra if statements for looping colour round the end of the scale
						if upDown >=8 and 23 <= self.numberMatrix[r].getValue() <= 25 and self.numberMatrix[r].getValue() + 1 <= 25 and updated == 0:
							self.numberMatrix[r].setValue(self.numberMatrix[r].getValue() + 1)
							updated = 1
							
						if upDown >=8 and self.numberMatrix[r].getValue() == 25 and updated == 0:
							self.numberMatrix[r].setValue(16)
							updated = 1

						if (upDown >=8 and self.numberMatrix[r].getValue() < 18 and self.numberMatrix[r].getValue() + 1 < 18) and updated == 0:
							self.numberMatrix[r].setValue(self.numberMatrix[r].getValue() + 1)
							updated = 1
						
			# Apparently: WE DO ALL THE ABOVE AGAIN BECAUSE OF TEMPORAL LOOP ISSUES
			rowIndex = 0
							
			for x in range (0, self.numberSquaresX):
		
				for y in range (0, self.numberSquaresY):
				
					if rowIndex in [0,1,2,3,4,5,6,7,10,11,12,13,16,17,18,19,20,21,22,23]:
				
						# Blitting - I don't know what arguments target.blitArea takes or what the structure of self.resources is
						#Looks like resources is colour, x cursor, y cursor...
						
						trueColour = []
						
						if self.rotation in [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]:
							trueColour = self.displayMatrix[rowIndex].getColour()
							
						if self.rotation in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41]:
							if 0 <= self.displayMatrix[rowIndex].getColour() <= 7:
								trueColour = self.displayMatrix[rowIndex].getColour() + 8
							if 8 <= self.displayMatrix[rowIndex].getColour() <= 15:
								trueColour = self.displayMatrix[rowIndex].getColour() - 8
								
						target.blitArea(self.resources[trueColour],[self.displayMatrix[rowIndex].getXlocation()+self.displayMatrix[rowIndex].getXjitter(),self.displayMatrix[rowIndex].getYlocation()+self.displayMatrix[rowIndex].getYjitter()],[0, 0, self.squareWidth, self.squareHeight])

						# INCREMENT ROW INDEX
						rowIndex = rowIndex+1
						
					#If one of the middle four squares (behind the numbers) do not draw
					if rowIndex in [8,9,14,15]:
						
						rowIndex = rowIndex+1
					
			blitmsg = "BLITTING_ARRAY_" + str(self.rid)
				
			pylink.getEYELINK().sendMessage(blitmsg)
						
		#if self.firstNumBlit == True:
			
			#for n in range (0, 4):
				
				#trueValue = self.numberMatrix[n].getValue() + self.numberRotation
				
				#if 26 <= trueValue <= 35:
					#trueValue = trueValue-10
				#if 36 <= trueValue <= 45:
					#trueValue = trueValue-20
				#if 46 <= trueValue <= 55:
					#trueValue = trueValue-30
				#if 56 <= trueValue <= 65:
					#trueValue = trueValue-40
				
				#self.customResource.blitArea(self.resources[trueValue],[self.numberMatrix[n].getXlocation(),self.numberMatrix[n].getYlocation()],[0, 0, self.numberWidth, self.numberHeight])
				#self.firstNumBlit = False
			
		for n in range (0, 4):
		
			trueValue = [] 
					
			if 16 <= self.numberMatrix[n].getValue() + self.numberRotation <= 25:
				trueValue = self.numberMatrix[n].getValue() + self.numberRotation
			if 26 <= self.numberMatrix[n].getValue() + self.numberRotation <= 35:
				trueValue = self.numberMatrix[n].getValue() + self.numberRotation - 10
			if 36 <= self.numberMatrix[n].getValue() + self.numberRotation <= 45:
				trueValue = self.numberMatrix[n].getValue() + self.numberRotation - 20
			if 46 <= self.numberMatrix[n].getValue() + self.numberRotation <= 55:
				trueValue = self.numberMatrix[n].getValue() + self.numberRotation - 30
			if 56 <= self.numberMatrix[n].getValue() + self.numberRotation <= 65:
				trueValue = self.numberMatrix[n].getValue() + self.numberRotation - 40
				
			print('T_',trueValue)			
					
			self.customResource.blitArea(self.resources[trueValue],[self.numberMatrix[n].getXlocation(),self.numberMatrix[n].getYlocation()],[0, 0, self.numberWidth, self.numberHeight])

		blitmsg = "BLITTING_NUMBERS_" + str(self.rid)
		pylink.getEYELINK().sendMessage(blitmsg)
						
		end = sreb.time.getCurrentTime()

		self.lastRedrawDone=end
		self.uid = self.uid + 1
		
		self.shouldChangeDisplay = False
		
	###################Additional supporting methods below#####################
		
	def determineStimLocation(self, x, y):
	
		location = 0
		
		for j in range (0, self.numberStimuli):
		
			if x == self.stimMatrix[j].getXcoord() and y == self.stimMatrix[j].getYcoord():
						
				location = j
				
		return(location)
		
	def determineBroadCellPosition(self, positionX, positionY):

		# CORRECT FOR WHITE SPACE
		positionX = positionX - self.mosaicStartX
		positionY = positionY - self.mosaicStartY

		# WORK OUT WHAT COLUMN WE ARE IN
		x = positionX / self.regionWidth
		y = positionY / self.regionHeight

		coords = []

		# IGNORE GUTTERS
		#if x!= 6 and x!=13 and y!=7:
		coords = [x,y]

		return coords
		
	def determineBroadCellRowIndexInMatrix(self, x, y):
		#row = (x *(self.mosaicWidth/self.squareWidth)) + y
		row = 0
		xlocation = (x*self.regionWidth)+self.mosaicStartX
		ylocation = (y*self.regionHeight)+self.mosaicStartY
		
		for j in range (0, self.numberObjects):
		
			if self.displayMatrix[j].getXlocation() == xlocation and self.displayMatrix[j].getYlocation() == ylocation:
			
				row = j

		return row
		
	def handleResponse(self, positionX, positionY):

		#print("response!!")

		coords = self.determineBroadCellPosition(positionX, positionY)
		changedRowIndex = self.determineBroadCellRowIndexInMatrix(coords[0], coords[1])

		#print(self.objectStatus)
		#print(coords)
		#print(changedRowIndex)

		targetClicked = None

		# ONLY PROCEED IF THEY HIT A TARGET
		# if (self.displayMatrix[changedRowIndex][5] < 2 ):
		# ENFORCE A DISPLAY CHANGE
		self.shouldChangeDisplay = True

		#print("COORDS CLICKED " + str(coords[0]) + "," + str(coords[1]))
		pylink.getEYELINK().sendMessage(str("COORDS CLICKED, " + str(coords[0]) + "," + str(coords[1])))
		
		if self.displayMatrix[changedRowIndex].getColour() != 2: #or self.displayMatrix[changedRowIndex].getColour() != 10: 
				
			self.whichNoise = 0
			#print("WRONGNOISE")
			
		if self.displayMatrix[changedRowIndex].getColour() == 2: #or self.displayMatrix[changedRowIndex].getColour() == 10:
				
			self.whichNoise = 1
			#print("CORRECTNOISE")
				
		targetClicked = self.clearObject(coords, changedRowIndex)

		#return(targetClicked)
		
	def handleNumberResponse(self):
	
		pylink.getEYELINK().sendMessage("NUMRESP;" + str(self.numberMatrix[0].getValue()) + ";" + str(self.numberMatrix[1].getValue()) + ";" + str(self.numberMatrix[2].getValue()) + ";" + str(self.numberMatrix[3].getValue()))
		
		if self.numberMatrix[0].getValue() != 18 and self.numberMatrix[1].getValue() != 18 and self.numberMatrix[2].getValue() != 18 and self.numberMatrix[3].getValue() != 18:
			self.whichNoise = 0
			print("SOMETHING HAS GONE WRONG")
			print(self.numberMatrix[0].getValue())
			print(self.numberMatrix[1].getValue())
			print(self.numberMatrix[2].getValue())
			print(self.numberMatrix[3].getValue())
			print(self.numberRotation)
			if 16 <= self.numberMatrix[0].getValue() <= 20:
				self.clearNumber(0)
			if 16 <= self.numberMatrix[1].getValue() <= 20:
				self.clearNumber(1)
			if 16 <= self.numberMatrix[2].getValue() <= 20:
				self.clearNumber(2)
			if 16 <= self.numberMatrix[3].getValue() <= 20:
				self.clearNumber(3)
				
		if self.numberMatrix[0].getValue()== 18:
			self.whichNoise = 1
			self.clearNumber(0)
			
		if self.numberMatrix[1].getValue()== 18:
			self.whichNoise = 1
			self.clearNumber(1)
			
		if self.numberMatrix[2].getValue()== 18:
			self.whichNoise = 1
			self.clearNumber(2)
			
		if self.numberMatrix[3].getValue()== 18:
			self.whichNoise = 1
			self.clearNumber(3)
			
	def clearNumber(self, id):
	
		responseMade = False
				
		j = id
				
		if self.numberMatrix[j].getNumberStatus()!="CLEARED" and self.numberMatrix[j].getNumberStatus()!="PASSIVE":
			self.numberMatrix[j].setNumberStatus("CLEARED")
			self.numberMatrix[j].setValue(random.choice([21,22,23,24,25]))
			
			self.isOccupiedNumber[j] = False
			self.numberTargetCurrentlyVisible = False
			self.numberDistractorCurrentlyVisible = False
		
	def clearObject(self, coords, changedRowIndex):

		targetClicked = False

		# FIRST UPDATE TARGET RELATED INFORMATION
		for j in range(0, self.numberStimuli):

			# CHECK THE LOCATION
			if self.stimMatrix[j].getStimstatus()!="CLEARED" and self.stimMatrix[j].getStimstatus()!="PASSIVE" and self.stimMatrix[j].getXcoord() == coords[0] and self.stimMatrix[j].getYcoord() == coords[1]:
				
				self.stimMatrix[j].setStimstatus("CLEARED")
				self.displayMatrix[changedRowIndex].setType("NEUTRAL")
				self.displayMatrix[changedRowIndex].setColour(random.choice([5,6,7,8,9,10,11,12,13,14,15]))
				
				self.isOccupied[j] = False
				
				if (self.stimMatrix[j].getType() == "TARGET"):
					targetClicked == True
					self.targetCurrentlyVisible = False
					self.stimMatrix[j].setStimstatus("CLEARED")
					#print("TARGET CLEARED")
					self.numberTargetsClicked = self.numberTargetsClicked + 1
					
		#Deal with the clicking of background squares too 
		for j in range (0, self.numberObjects):
		
			if self.displayMatrix[j].getType() != "CLEARED" and self.displayMatrix[j].getType != "TARGET" and self.displayMatrix[j].getType != "DISTRACTOR" and ((self.displayMatrix[j].getXlocation()-self.mosaicStartX)/60) == coords [0] and ((self.displayMatrix[j].getYlocation()-self.mosaicStartY)/60) == coords [1]:
			
				self.displayMatrix[j].setColour(random.choice([5,6,7,8,9,10,11,12,13,14,15]))
				
				# SET UP CELLS THAT NEIGHBOUR THE TARGET
				#for x in range(-self.size[j], self.size[j]+1):

					#for y in range(-self.size[j], self.size[j]+1):

						# NOTE INCLUDES ZERO WHICH IS THE TARGET LOCATION
						#newCell = self.determineBroadCellRowIndexInMatrix(self.objectLocs[j][0]+x, self.objectLocs[j][1]+y)

						#self.displayMatrix[newCell][7] = "NEUTRAL"

						# RESET TO DEFAULT RANDOMISATION THIS IS FOR TESTING PURPOSES TO ENSURE STUFF HAS RESPONDED
						
						#self.displayMatrix[newCell][5] = random.randint(7,9)
						
		return(targetClicked)
		
	def shouldRedraw(self):
		# return True if you want the CustomResource to be redrawn
		#(by calling the DrawMethodPointer) and the screen updated
		# and display flipped
		# return False to indicate that no redraw is needed for the resource

		if self.screen.getLastUpdateRetraceTime() < sreb.time.getCurrentTime() and \
			self.lastRedrawDone < self.screen.getLastUpdateRetraceTime():
			return True
		return False
		
	def clearAll(self):
	
		rowIndex = 0
	
		for y in range (0, 4):
		
			for x in range (0, 6):
				
				if (self.displayMatrix[rowIndex].getType() =="TARGET" or self.displayMatrix[rowIndex].getType() =="DISTRACTOR"):
				
					self.clearObject([x,y],rowIndex)
		
				rowIndex = rowIndex+1
		
		for j in range (0, 4):
			self.numberMatrix[j].setNumberStatus("CLEARED")
			self.numberMatrix[j].setValue(random.choice([21,22,23,24,25]))
			
			self.isOccupiedNumber[j] = False
			self.numberTargetCurrentlyVisible = True
			self.numberDistractorCurrentlyVisible = True
		
		
	def writeMatrix(self):
	
		test = 1
		
