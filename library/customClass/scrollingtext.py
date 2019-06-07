# This code was written by Alex Muhl-Richardson and Hayward Godwin with assistance from the team at SR Research
# This is a single custom class written for use in conjunction with an experiment created in SR Research's Experiment Builder (EB) and does NOT function independently
# 
# If you use this code, or a modified version, in published work, please cite: 
#	- Our JEP:Applied paper: Muhl-Richardson, A., Godwin, H. J., Garner, M., Hadwin, J. A., Liversedge, S. P., & Donnelly, N. (2018). Individual differences in search and monitoring for color targets in dynamic visual displays. Journal of Experimental Psychology: Applied, 24(4), 564-577. http://dx.doi.org/10.1037/xap0000155
#	- Our OSF project: Muhl-Richardson, A., Godwin, H. J., Garner, M., Hadwin, J. A., Liversedge, S. P., & Donnelly, N. (2019, May 9). Searching and Monitoring Dynamically Changing Visual Displays. Retrieved from osf.io/ahufd

#Import modules needed by Experiment Builder and the Eyelink 1000
import sreb
import sreb.graphics
import sreb.time
import pylink
import random

#Make a class for the creation of individual squares
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

#Make a class for handling the properties of targets and target-predictive distractors (but not other background stimuli)
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


class CustomClassTemplate(sreb.EBObject):
	def __init__(self):
		sreb.EBObject.__init__(self)
		
		#Participant and trial basics
		self.ppt_id = ""
		self.cond = ""
		self.prevalence = ""
		self.practice = 0

		#Clear targets/distractors after time
		self.clearing = True
		#Multiple targets display simulataneously
		self.multiple = False
		#Target absent trials
		self.absentTrials = False
				
		#Determines the target colours - can be a value between 0 and 15
		self.rotation = None
		
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

		# UNIQUE IDENTIFIER FOR EACH REFRESH
		self.uid = 0
		self.rid = 0
		self.shouldChangeDisplay = False

		# DIMENSIONS
		self.squareWidth = 18
		self.squareHeight = 18
		
		self.regionWidth = 68
		self.regionHeight = 68

		self.mosaicWidth = 816
		self.mosaicHeight = 612

		self.mosaicStartX = 104
		self.mosaicStartY = 78
		self.numberSquaresX = 12
		self.numberSquaresY = 9
		
		
		self.numberObjects = 108
		self.numberStimuli = 12
		
		self.xLocations = []
		self.yLocations = []
		
		# TEMPORAL DIMENSIONS
		self.timeBetweenObjectsMean = 9
		self.timeBetweenObjectsSD = 1
		self.repetitions = 1 # NUMBER OF TIMES TO SHOW EACH LOCATION
		self.objectLifetimeMean = 27
		self.objectLifetimeSD = 1

		self.redrawSpeed = 90
		
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
		self.isFinished = None
		
		self.targetLocations = []
		
		self.targetCurrentlyVisible = None #USED TO ENSURE THAT ONLY ONE TARGET IS VISIBLE AT ANY ONE TIME
		
		self.numberTargetOnsets = 0
		
		self.numberTrials = 0
		
		self.objectTimesToRise = []
		
		self.numberTargetsClicked = 0
		
		self.t1 = None
		self.t2 = None
		
	def setBasics (self, ppt_id, cond, prev, practice):
		self.ppt_id = ppt_id
		self.cond = cond
		self.prevalence = prev
		self.practice = int(practice)
		
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
		
	def getTargetOnsets(self):
		return self.numberTargetOnsets
	def getTargetsClicked(self):
		return self.numberTargetsClicked
		
	def getTrials(self):
		return self.numberTrials
				
	def getNoise(self):
		return self.whichNoise
		
	# Initialize the custom class graphics.
	def initialize(self):
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
			
		if self.rotation <= 13:
			self.t1 = self.rotation+2
		if self.rotation >= 14:
			self.t1 = self.rotation-14
			
		if self.rotation <= 5:
			self.t2 = self.rotation+10
		if self.rotation >= 6:
			self.t2 = self.rotation-6
			
	#Used to set event structure
	def trialStructure(self):
		
		#Do this once at the start of the block
		self.trialArray = []
		
		#Set prevalence level
		
		#Set to 66% - two thirds of trials will have at least one target appear - (72 trial block)
		if int(self.prevalence) == 1:
			for i in range (0, 20):
				self.trialArray.append(0)
			for i in range (0, 10):
				self.trialArray.append(1)
				self.trialArray.append(2)
		
		#Set to 5.55556% - one eighteenth of trials will have at least one target appear - (72 trial block)
		if int(self.prevalence) == 0:
			for i in range (0, 68):
				self.trialArray.append(0)
			for i in range (0, 2):
				self.trialArray.append(1)
				self.trialArray.append(2)
				
		#Set to 66% - two thirds of trials will have at least one target - (3 trial practice block)
		if self.practice == 1:
			self.trialArray = []
			self.trialArray.append(0)
			self.trialArray.append(1)
			self.trialArray.append(2)
		
		random.shuffle(self.trialArray)
		
		
	# Used to reset the trial status
	def reset(self):
	
		### - Added these two lines
		self.displayMatrix = []
		self.stimMatrix = []
		self.isOccupied = []
		
		self.lastRedrawDone=0
		self.finished = 0
		self.uid = 0
		self.rid = 0
		self.shouldChangeDisplay = True
		
		self.setsize = 1
		
		uidCounter = 0
		
		x_target_start = self.mosaicStartX
		y_target_start = self.mosaicStartY
		time_counter = 0
		
		#Do this at the start of each trial
		newObjectTypes = []

		self.targetsInTrial = self.trialArray[self.numberTrials]

		if self.targetsInTrial == 0:
			newObjectTypes = ["DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR"]
		if self.targetsInTrial == 1:
			newObjectTypes = ["TARGET", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR"]
		if self.targetsInTrial == 2:
			newObjectTypes = ["TARGET", "TARGET", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR", "DISTRACTOR"]
				
		random.shuffle(newObjectTypes)
		
		for x in range (0, 9):

			for y in range (0, 12):

				self.xLocations.append((y*self.regionWidth)+x_target_start)
				self.yLocations.append((x*self.regionHeight)+y_target_start)
				
		for y in range (1, 9, 3):
			
			for x in range (1, 12, 3):
				
					templocations = [x,y]
					
					self.targetLocations.append(templocations)
					
		
		for j in range(0, self.numberObjects):
				
			xJitterAmount = random.randint(5,36)
			yJitterAmount = random.randint(5,36)
				
			#Create a square of class SquareProp with an ID, a base X location, a base Y location, random x jitter, random y jitter, a random medium heat, set to PASSIVE and NEUTRAL type and NEUTRAL status
			square = SquareProp(j, self.xLocations[j], self.yLocations[j], xJitterAmount, yJitterAmount, random.choice([5,6,7,8,9,10,11,12,13,14,15]), "NEUTRAL", "NEUTRAL") 
				
			self.displayMatrix.append(square)

		for r in range (0, self.repetitions):
		
			objectTimeToRiseTemp = []
				
			for j in range (0, self.numberStimuli):
			
				self.setsize = self.setsize + 1
				
				targetJitter = random.randint(-1,1)
				
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
				stim = StimProp(j, 0, "PASSIVE", newObjectTypes[j], 0, newLifetime, timeToFall, newLifetime/2, self.targetLocations[j][0]+targetJitter, self.targetLocations[j][1]+targetJitter, hotOrCold[0], random.randint(0,0))
				
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
			
		self.targetCurrentlyVisible = False
		
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
			
			self.rid = self.rid + 1
		
			#Set as fixed number for now (was self.setsize) - but perhaps use self.numberStimuli instead
			for j in range (0, self.numberStimuli):
		
				#Reduce the time to rise
				self.stimMatrix[j].setObjectTimeToRise(self.stimMatrix[j].getObjectTimeToRise()-random.random())
			
				#Reduce time to max
				if self.stimMatrix[j].getStimstatus() == "ACTIVE":
					self.stimMatrix[j].setObjectTimeToMax(self.stimMatrix[j].getObjectTimeToMax()-random.random())
					self.stimMatrix[j].setObjectTimeToFall(self.stimMatrix[j].getObjectTimeToFall()-random.random())
					
				#If past its time then cool it off - I'm not sure slow decline has actually been implemented yet
				if self.stimMatrix[j].getObjectTimeToRise() <= 0 and self.stimMatrix[j].getStimstatus() == "ACTIVE" and self.stimMatrix[j].getObjectTimeToFall()+self.stimMatrix[j].getObjectTimeToMax() <= 0:
			
					self.stimMatrix[j].setStimstatus("IN_DECLINE")
						
				#If ready (and location not already occupied) make active - I don't know if the ownership bit is necessary in the new version ##
				#Ownership bit definitely not necessary
				if self.stimMatrix[j].getObjectTimeToRise() <= 0 and self.stimMatrix[j].getStimstatus() == "PASSIVE" and self.isOccupied[j] == False and self.stimMatrix[j].getType() == "DISTRACTOR":
			
					self.stimMatrix[j].setStimstatus("ACTIVE")
					self.isOccupied[j] = True
					#print("DISTRACTOR ONSET")
				
				#Seriously, what the fuck was the point of the last part of this if statement?!
				#I think it was a really dumb way of making sure there were target absent trials...
				if self.stimMatrix[j].getObjectTimeToRise() <= 0 and self.stimMatrix[j].getStimstatus() == "PASSIVE" and self.isOccupied[j] == False and self.stimMatrix[j].getType() == "TARGET" and self.targetCurrentlyVisible == False:
			
					self.stimMatrix[j].setStimstatus("ACTIVE")
					self.isOccupied[j] = True
					#print("TARGET ONSET")
					
					if self.multiple == False:
						self.targetCurrentlyVisible = True
					
								
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
							
			#Now to do the colours of all cells in the display
			
			target = self.customResource
			rowIndex = 0
		
			for y in range (0, 9):
		
				for x in range (0, 12):
					
					if self.displayMatrix[rowIndex].getType() == "NEUTRAL" and int(self.cond) == 0 or self.displayMatrix[rowIndex].getStatus() == "CLEARED" and int(self.cond) == 0:
				
						upDown = random.randint(0,5)
						
						updated = 0
					
						#Keep neutral background squares varying between the middle heat levels - random change to a new colour that is not the same colour or a colour one step away
						if upDown == 1 and updated == 0:
							tempColourList = [5,6,7,8,9,10,11,12,13,14,15]
							tempColourList = [x for x in tempColourList if x is not self.displayMatrix[rowIndex].getColour() and x is not self.displayMatrix[rowIndex].getColour() + 1 and x is not self.displayMatrix[rowIndex].getColour() - 1]
							self.displayMatrix[rowIndex].setColour(random.choice(tempColourList))
							updated = 1
						
					if (self.displayMatrix[rowIndex].getType() =="TARGET" or self.displayMatrix[rowIndex].getType() =="DISTRACTOR"):
						
						currentObject = self.determineStimLocation(x,y)
						
						self.displayMatrix[rowIndex].setStatus(self.stimMatrix[currentObject].getStimstatus())
						
						if self.stimMatrix[currentObject].getStimstatus() == "PASSIVE":
						
							upDown = random.randint(0,5)
							
							updated = 0
					
							#Keep passive stim squares varying between the middle heat levels
							if upDown == 1 and updated == 0:
								tempColourList = [5,6,7,8,9,10,11,12,13,14,15]
								tempColourList = [x for x in tempColourList if x is not self.displayMatrix[rowIndex].getColour() and x is not self.displayMatrix[rowIndex].getColour() + 1 and x is not self.displayMatrix[rowIndex].getColour() - 1]
								self.displayMatrix[rowIndex].setColour(random.choice(tempColourList))
								updated = 1
						
						#If it is a hot target - do this loop for temperature control
						if self.stimMatrix[currentObject].getHot() == True:
				
							upDown = random.randint(1,10)
							targetDecider = random.randint(1,10)
					
							if upDown >= 8 and self.stimMatrix[currentObject].getStimstatus() == "IN_DECLINE" and self.clearing == True:
					
								self.clearObject([x,y],rowIndex)
					
							#Targets can go to max heat
							if self.displayMatrix[rowIndex].getType() == "TARGET" and self.stimMatrix[currentObject].getStimstatus() == "ACTIVE" and self.stimMatrix[currentObject].getObjectTimeToMax() <= 0:
					
								updated = 0
					
								if upDown >= 8 and self.displayMatrix[rowIndex].getColour() != 2 and updated == 0:
									#Allow to vary between any non-target colour for a while
									tempColourList = [5,6,7,8,9,10,11,12,13,14,15]
									tempColourList = [x for x in tempColourList if x is not self.displayMatrix[rowIndex].getColour() and x is not self.displayMatrix[rowIndex].getColour() + 1 and x is not self.displayMatrix[rowIndex].getColour() - 1]
									self.displayMatrix[rowIndex].setColour(random.choice(tempColourList))
									updated = 1
								
								#One in ten chance of being set to target colour
								if targetDecider <= 6 and 4 > self.displayMatrix[rowIndex].getColour() > 0 and updated == 0:
									self.displayMatrix[rowIndex].setColour(2)
									self.numberTargetOnsets = self.numberTargetOnsets + 1
									updated = 1
									
								if 6 <= upDown <= 7 and self.displayMatrix[rowIndex].getColour() != 2 and updated == 0:
									tempColourList = [0,1,3,4]
									tempColourList = [x for x in tempColourList if x is not self.displayMatrix[rowIndex].getColour() and x is not self.displayMatrix[rowIndex].getColour() + 1 and x is not self.displayMatrix[rowIndex].getColour() - 1]
									self.displayMatrix[rowIndex].setColour(random.choice(tempColourList))
									updated = 1
										
								
							if self.displayMatrix[rowIndex].getType() == "TARGET" and self.stimMatrix[currentObject].getStimstatus() == "ACTIVE" and self.stimMatrix[currentObject].getObjectTimeToMax() > 0:
								
								upDownTwo = 0 #random.randint(0,1)
								
								updated = 0

								if upDown >=8 and upDownTwo == 0 and updated == 0:
									tempColourList = [5,6,7,8,9,10,11,12,13,14,15]
									tempColourList = [x for x in tempColourList if x is not self.displayMatrix[rowIndex].getColour() and x is not self.displayMatrix[rowIndex].getColour() + 1 and x is not self.displayMatrix[rowIndex].getColour() - 1]
									self.displayMatrix[rowIndex].setColour(random.choice(tempColourList))
									updated = 1
									
								if upDown <= 2 and self.displayMatrix[rowIndex].getColour() != 2 and updated == 0:
									tempColourList = [0,1,3,4]
									tempColourList = [x for x in tempColourList if x is not self.displayMatrix[rowIndex].getColour() and x is not self.displayMatrix[rowIndex].getColour() + 1 and x is not self.displayMatrix[rowIndex].getColour() - 1]
									self.displayMatrix[rowIndex].setColour(random.choice(tempColourList))
									updated = 1
									
								
							#Distractors cannot go to max heat but can go up
							if self.displayMatrix[rowIndex].getType()=="DISTRACTOR" and self.stimMatrix[currentObject].getStimstatus() == "ACTIVE":
							
								upDownTwo = 0 #random.randint(0,1)
								
								updated = 0

								if upDown >=8 and upDownTwo == 0 and self.displayMatrix[rowIndex].getColour() != 1 and self.displayMatrix[rowIndex].getColour() != 3 and updated == 0:
									tempColourList = [0,4,5,6,7,8,9,10,11,12,13,14,15]
									tempColourList = [x for x in tempColourList if x is not self.displayMatrix[rowIndex].getColour() and x is not self.displayMatrix[rowIndex].getColour() + 1 and x is not self.displayMatrix[rowIndex].getColour() - 1]
									self.displayMatrix[rowIndex].setColour(random.choice(tempColourList))
									updated = 1
									
								if upDown <= 2 and self.displayMatrix[rowIndex].getColour() > 4 and updated == 0:
									tempColourList = [0,1,3,4]
									tempColourList = [x for x in tempColourList if x is not self.displayMatrix[rowIndex].getColour() and x is not self.displayMatrix[rowIndex].getColour() + 1 and x is not self.displayMatrix[rowIndex].getColour() - 1]
									self.displayMatrix[rowIndex].setColour(random.choice(tempColourList))
									updated = 1

						#Cold targets redundant for current experiment
						if self.stimMatrix[currentObject].getHot() == False:
						
							nothing = 0

					rowIndex = rowIndex+1
						
			# Apparently: WE DO ALL THE ABOVE AGAIN BECAUSE OF TEMPORAL LOOP ISSUES
			rowIndex = 0
							
			for x in range (0, self.numberSquaresX):
		
				for y in range (0, self.numberSquaresY):
				
					# Blitting - I don't know what arguments target.blitArea takes or what the structure of self.resources is
					#Looks like resources is colour, x cursor, y cursor...
					
					trueColour = self.displayMatrix[rowIndex].getColour() + self.rotation
					
					if trueColour > 15:
						trueColour = trueColour-16
					
					target.blitArea(self.resources[trueColour],[self.displayMatrix[rowIndex].getXlocation()+self.displayMatrix[rowIndex].getXjitter(),self.displayMatrix[rowIndex].getYlocation()+self.displayMatrix[rowIndex].getYjitter()],[0, 0, self.squareWidth, self.squareHeight])

					# INCREMENT ROW INDEX
					rowIndex = rowIndex+1
			
			blitmsg = "BLITTING" + str(self.rid)
			
			pylink.getEYELINK().sendMessage(blitmsg)
						
		self.shouldChangeDisplay = False
		
		pylink.getEYELINK().sendMessage("NUM_T_ONSETS;" + str(self.numberTargetOnsets))
			
		end = sreb.time.getCurrentTime()

		self.lastRedrawDone=end
		self.uid = self.uid + 1
		
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
		
		if self.displayMatrix[changedRowIndex].getColour() != 2  or self.displayMatrix[changedRowIndex].getColour() != 10: 
				
			self.whichNoise = 0
			#print("WRONGNOISE")
			
		if self.displayMatrix[changedRowIndex].getColour() == 2 or self.displayMatrix[changedRowIndex].getColour() == 10:
				
			self.whichNoise = 1
			#print("CORRECTNOISE")
				
		targetClicked = self.clearObject(coords, changedRowIndex)

		#return(targetClicked)

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
					targetClicked = True
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
	
		for y in range (0, 9):
		
			for x in range (0, 12):
				
				if (self.displayMatrix[rowIndex].getType() =="TARGET" or self.displayMatrix[rowIndex].getType() =="DISTRACTOR"):
				
					self.clearObject([x,y],rowIndex)
		
				rowIndex = rowIndex+1
		
	def writeMatrix(self):
	
		test = 1
		
