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
#Import modules for managing display changes
import random

class CustomClassTemplate(sreb.EBObject):
	def __init__(self):
		sreb.EBObject.__init__(self)

		# BASE STUFF
		self.customResource = None;		# for EB integration
		self.displayScreenPath=''	# use to store the current screen path in the expt
		self.screen=None		# handle for the screen object
		self.finished = 0;		# variable used to check whether the trial has finished;
		self.resources = None
		self.displayMatrix = None
		self.masterDisplayMatrix = None

		# UNIQUE IDENTIFIER FOR EACH REFRESH
		self.uid = 0
		self.shouldChangeDisplay = False

		# DIMENSIONS
		#...of individual squares
		self.squareWidth = 18
		self.squareHeight = 18
		#...of the array of squares
		self.mosaicWidth = 882
		self.mosaicHeight = 630
		#...where should the array of squares start (from top left)
		self.mosaicStartX = 71
		self.mosaicStartY = 69

		# TEMPORAL DIMENSIONS
		#These parameters determine how long targets and distractors take to appear, how long they remain, and if they repeat
		#They do not specify exact times, but are rather parameters for creating noisy distributions that are used to produce variable timings (see below)
		self.timeBetweenObjectsMean = 1
		self.timeBetweenObjectsSD = 1
		self.repetitions = 3 # NUMBER OF TIMES TO SHOW EACH LOCATION
		self.objectLifetimeMean = 20
		self.objectLifetimeSD = 5

		# TRIAL INFO
		self.setsize = 0
		self.size = None
		self.objectLocs = None
		self.objectStatus = None
		#These variables interact with the temporal variables above to determine the behaviour of individual stimuli
		self.objectTimeToRise = None # CONTROLS THE SPEED AT WHICH THEY RISE FROM THE START OF THE DISPLAY
		self.objectTimeToMax = None # CONTROLS THE SPEED AT WHICH THEY HIT THEIR PEAK
		self.objectType = None
		self.objectLifetime = None
		self.objectTimeToFall = None
		self.objectCurrentHeat = None
		#Stops multiple targets occurring in the same place at the same time
		self.isOccupied = None

	#VARIOUS GET AND SET FUNCTIONS FOR INTERACTING WITH EXPERIMENT BUILDER
	# These two methods are used to read and set the extent of the display;
	# (measured in pixels);
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

	# Initialize the custom class graphics in Experiment Builder
	def initialize(self):
		self.screen=sreb.graphics.getScreenFromPath(self.getDisplayScreenPath())
		if self.screen is None:
			raise "EBScreen could not be accessed"

		self.resources = self.screen.getResources()

		for x in range(0, len(self.resources)-1):
			self.resources[x].setVisible(False)

		self.customResource = self.screen.createCustomResource(sreb.EBRectangle(0, 0 ,1024, 768),False,-2)
		self.customResource.setDrawMethodPointer(self.redraw)
		self.customResource.setShouldRedrawMethodPointer(self.shouldRedraw)
		self.lastRedrawDone=0
		self.uid = 0

	# Used to reset the trial status and set up all the variables that were initialized above
	def reset(self):
		self.lastRedrawDone=0
		self.finished = 0
		pylink.getEYELINK().sendMessage("RESET")
		self.uid = 0
		self.shouldChangeDisplay = True
		self.setsize = 0
		self.objectLocs = []
		self.size = []
		self.masterDisplayMatrix = [["UID", "X", "Y", "X_CURSOR", "Y_CURSOR", "COLOUR", "STATUS", "OBJECT_TYPE", "OBJECT_OWNER"]]
		self.objectStatus = []
		self.objectTimeToRise = []
		self.displayMatrix = []
		self.objectType = []
		self.objectLifetime = []
		self.objectTimeToFall = []
		self.objectCurrentHeat = []
		self.objectTimeToMax = []
		self.isOccupied = []
		uidCounter = 0 # GIVE FIVE SHIFTS OF THE DISPLAY TO LEAD IN
		x_target_start = self.mosaicStartX
		y_target_start = self.mosaicStartY
		time_counter = 0

		# OBJECT LOCATIONS
		for r in range(0, self.repetitions):

			objectTimeToRiseTemp = []

			#The ranges of these loops must be changed to match the number of stimuli specified during initialization
			for x in range(4, 45, 5):
				for y in range(2, 35, 5):
					# Set up basic properties of all stimuli
					self.objectLocs.append([x, y])
					self.setsize = self.setsize + 1
					self.objectStatus.append("PASSIVE")
					self.size.append(random.randint(0,2))
					time_counter = time_counter + uidCounter + random.normalvariate(self.timeBetweenObjectsMean, self.timeBetweenObjectsSD)
					objectTimeToRiseTemp.append(time_counter)
					newLifetime = random.normalvariate(self.objectLifetimeMean, self.objectLifetimeSD)
					self.objectLifetime.append(newLifetime)
					self.objectTimeToFall.append(time_counter + newLifetime)
					objectTypes = ["TARGET", "TARGET", "TARGET", "TARGET", "TARGET", "TARGET", "DISTRACTOR", "DISTRACTOR"]
					random.shuffle(objectTypes)
					self.objectType.append(objectTypes[0])
					self.objectTimeToMax.append(newLifetime / 2)
					self.objectCurrentHeat.append(4)

			random.shuffle(objectTimeToRiseTemp)
			self.objectTimeToRise.extend(objectTimeToRiseTemp)

		x_start = self.mosaicStartX
		y_start = self.mosaicStartY
		status = "NULL"

		for x in range(0, 50):
			x_cursor = x_start + (self.squareWidth*x)
			for y in range(0, 35):
				y_cursor = y_start + (self.squareHeight*y)
				i = random.randint(5,9)
				object_type = "NEUTRAL"
				self.displayMatrix.append([self.uid, x, y, x_cursor, y_cursor, i, status, object_type, "none"]) # FINAL NONE IS OWNERSHIP OF THIS CELL

		self.masterDisplayMatrix.extend(self.displayMatrix)

		#Prevents multiple targets from onsetting at same location at same time
		for j in range(0,(self.setsize/self.repetitions)): #Adds to list one boolean value for each target location - independent of number of repetitions/underlying targets at same locations
			self.isOccupied.append(False) 

	#This redraws the display to the screen with every update
	def redraw(self):

		# REDRAW AND UPDATE DISPLAY
		start = sreb.time.getCurrentTime()
		shouldUpdate = 100

		#With other values of shouldUpdate and variations of this if statement this can be used to make display refreshes less frequent
		if (shouldUpdate == 100):
			self.shouldChangeDisplay= True

		#This updates all stimulus timings using the parameters outlined during initialization and reset
		#Firstly the timing related properties are all updated
		if (self.shouldChangeDisplay == True):
			for j in range(0,self.setsize):

						self.objectTimeToRise[j] = self.objectTimeToRise[j] - 1

						# DECREASE TIME TO MAX
						if (self.objectStatus[j] == "ACTIVE"):
							self.objectTimeToMax[j] = self.objectTimeToMax[j] - 1
							self.isOccupied[self.objectLocs.index(self.objectLocs[j])] = True

						# NEUTRALISE IF PAST ITS TIME
						# IN DECLINE MEANS GETTING COOLER - OF COURSE THIS TERMINOLOGY HAS BEEN INSPIRED BY SMALL WORLD.
						if (self.objectTimeToRise[j]<=0 and self.objectStatus[j] == "ACTIVE" and self.objectTimeToFall[j] <=0):
							self.objectStatus[j] = "IN_DECLINE"

						if (self.objectTimeToRise[j]<=0 and self.objectStatus[j] == "PASSIVE" and (self.isOccupied[self.objectLocs.index(self.objectLocs[j])] == False)): # NOTE THIS ALSO PREVENTS OBJECTS WRITING OVER ONE ANOTHER
							self.objectStatus[j] = "ACTIVE"

							# WORK OUT ROW INDEX OF TARGET
							targetCell = self.determineCellRowIndexInMatrix(self.objectLocs[j][0], self.objectLocs[j][1])
							self.displayMatrix[targetCell][7]=self.objectType[j]
							self.displayMatrix[targetCell][8]= j

							# SET UP CELLS THAT NEIGHBOUR THE TARGET
							for x in range(-self.size[j], self.size[j]+1):
								for y in range(-self.size[j], self.size[j]+1):
									neighbourCell = self.determineCellRowIndexInMatrix(self.objectLocs[j][0]+x, self.objectLocs[j][1]+y)

									# THIS MEANS IT IGNORES THE TARGET SQUARE SO WON'T WRITE OVER IT
									if (self.displayMatrix[neighbourCell][7] != self.objectType[j]):
										self.displayMatrix[neighbourCell][7] = "OBJECT_NEIGHBOUR"
										self.displayMatrix[neighbourCell][8]= j
			
			#Secondly the colour properties of all stimuli are updated based on the timings
			
			# NEXT WE UPDATE THE CURRENT COLOURS FOR ALL CELLS IN THE MOSAIC
			target = self.customResource
			rowIndex = 0

			for x in range(0,self.mosaicWidth/self.squareWidth):
				for y in range(0,self.mosaicHeight/self.squareHeight):
					self.displayMatrix[rowIndex][0] = self.uid;

					if (self.displayMatrix[rowIndex][7]=="NEUTRAL"):
						upDown = random.randint(0,2)

						if (upDown == 1 and self.displayMatrix[rowIndex][5] - 1 >= 5):
							self.displayMatrix[rowIndex][5] = self.displayMatrix[rowIndex][5] - 1

						if (upDown == 0 and self.displayMatrix[rowIndex][5] + 1 <= 9):
							self.displayMatrix[rowIndex][5] = self.displayMatrix[rowIndex][5] + 1

					if (self.displayMatrix[rowIndex][7]=="TARGET" or self.displayMatrix[rowIndex][7]=="DISTRACTOR"):
						# KEEP AT MAX HEAT IF ALREADY AT MAX HEAT
						if (self.displayMatrix[rowIndex][5] != 0):
							# RANDOM HEAT CHANGE; BIASED UPWARDS SLIGHTLY
							upDown = random.randint(10,20)
							# CHECK IF IN DECLINE OR NOT
							currentObject = self.determineObjectIndexInObjectArray([x,y])

							if (self.objectStatus[currentObject] == "IN_DECLINE"):
								#TEMP BREAKAGE
								self.clearObject([x,y], rowIndex)

							# TARGETS CAN GO TO MAX HEAT, BUT THEY MUST TAKE THEIR TIME TO GET THERE.
							if (self.displayMatrix[rowIndex][7]=="TARGET" and self.objectStatus[currentObject] == "ACTIVE" and self.objectTimeToMax[currentObject] <= 0):

								if (upDown >= 10 and self.displayMatrix[rowIndex][5] - 1 > 0):
									self.displayMatrix[rowIndex][5] = self.displayMatrix[rowIndex][5] - 1

							# DISTRACTORS CANT GO TO MAX HEAT
							if (self.displayMatrix[rowIndex][7]=="DISTRACTOR" and self.objectStatus[currentObject] == "ACTIVE"):

								if (upDown >= 10 and self.displayMatrix[rowIndex][5] - 1 >= 2):
									self.displayMatrix[rowIndex][5] = self.displayMatrix[rowIndex][5] - 1

							# UPDATE CURRENT HEAT FOR REFERENCE
							self.objectCurrentHeat[currentObject] = self.displayMatrix[rowIndex][5]

							# NOW UPDATE THE MOUNTAIN REGIONS AROUND THE CENTRE
							# NEED TO DO THIS HERE OR TEMPORAL LOOP ISSUES HAPPEN
							for xSize in range((x - self.size[currentObject]), (self.size[currentObject] + x+1)):
								for ySize in range(-self.size[currentObject] + y, self.size[currentObject] + y+1):

									neighbourCell = self.determineCellRowIndexInMatrix(xSize, ySize)

									if (self.displayMatrix[neighbourCell][7] == "OBJECT_NEIGHBOUR"):
										xDistance = abs(xSize-x)
										yDistance = abs(ySize-y)
										distance = max([xDistance, yDistance])
										distance = distance + random.randint(0,2)

										if (self.objectCurrentHeat[currentObject] + distance <= 9):
											self.displayMatrix[neighbourCell][5] = self.objectCurrentHeat[currentObject] + distance

					# INCREMENT ROW INDEX
					rowIndex = rowIndex+1

			
			rowIndex = 0

			for x in range(0,self.mosaicWidth/self.squareWidth):
				for y in range(0,self.mosaicHeight/self.squareHeight):

					# FINALLY DRAW
					target.blitArea(self.resources[self.displayMatrix[rowIndex][5]],[self.displayMatrix[rowIndex][3],self.displayMatrix[rowIndex][4]], [0, 0, self.squareWidth, self.squareHeight])

					# INCREMENT ROW INDEX
					rowIndex = rowIndex+1

			self.shouldChangeDisplay = False
		#This outputs all display information through the Eyelink as messages to be recorded by the host computer
		#This generates large EDF files and can result in slow transfer of files back to the display PC
		end = sreb.time.getCurrentTime()
		pylink.getEYELINK().sendMessage("REFRESH_COMPLETE: " + str(self.uid) + str(end) + "; ")

		for s in range(0, self.setsize):

			outString = "OBJECT INFO;"
			outString = outString + str(s) + ';'
			outString = outString + str(self.size[s]) + ";"
			outString = outString +self.objectStatus[s]+ ";"
			outString = outString + str(self.objectLocs[s][0]) + ',' + str(self.objectLocs[s][1])+ ";"
			outString = outString + str(self.objectTimeToRise[s])+ ";"
			outString = outString + self.objectType[s]+ ";"
			outString = outString + str(self.objectLifetime[s])+ ";"
			outString = outString + str(self.objectTimeToFall[s])+ ";"
			outString = outString + str(self.objectCurrentHeat[s])+ ";"

			pylink.getEYELINK().sendMessage(outString)

		self.lastRedrawDone=end
		self.uid = self.uid + 1

	#This deals with clicks
	def handleResponse(self, positionX, positionY):

		coords = self.determineCellPosition(positionX, positionY)
		changedRowIndex = self.determineCellRowIndexInMatrix(coords[0], coords[1])

		targetClicked = None

		# ENFORCE A DISPLAY CHANGE
		self.shouldChangeDisplay = True

		targetClicked = self.clearObject(coords, changedRowIndex)

	#This handles target/distractor offsets and resets of other stimuli following clicks or timing out
	def clearObject(self, coords, changedRowIndex):

		targetClicked = False

		# FIRST UPDATE TARGET RELATED INFORMATION
		for j in range(0, self.setsize):

			# CHECK THE LOCATION
			if (self.objectStatus[j]!="CLEARED" and self.objectStatus[j]!="PASSIVE" and((self.objectLocs[j][0] - self.size[j]) <= coords[0] <= (self.objectLocs[j][0] + self.size[j])) and ((self.objectLocs[j][1] - self.size[j]) <= coords[1] <= (self.objectLocs[j][1] + self.size[j]) )):

				self.objectStatus[j] = "CLEARED"
				self.isOccupied[self.objectLocs.index(self.objectLocs[j])] = False

				if (self.objectType[j] == "TARGET"):
					targetClicked == True

				# SET UP CELLS THAT NEIGHBOUR THE TARGET
				for x in range(-self.size[j], self.size[j]+1):
					for y in range(-self.size[j], self.size[j]+1):

						# NOTE INCLUDES ZERO WHICH IS THE TARGET LOCATION
						newCell = self.determineCellRowIndexInMatrix(self.objectLocs[j][0]+x, self.objectLocs[j][1]+y)
						self.displayMatrix[newCell][7] = "NEUTRAL"

						# RESET TO DEFAULT RANDOMISATION THIS IS FOR TESTING PURPOSES TO ENSURE STUFF HAS RESPONDED
						self.displayMatrix[newCell][5] = random.randint(7,9)

	#Helper function for responses
	def determineObjectIndexInObjectArray(self, coords):

		row = 0

		# FIRST UPDATE TARGET RELATED INFORMATION
		for j in range(0, self.setsize):

			# IF THE CLICKED COORDS MATCH A TARGET
			if (coords[0] == self.objectLocs[j][0] and coords[1] == self.objectLocs[j][1] and (self.objectStatus[j]=="ACTIVE" or self.objectStatus[j]=="IN_DECLINE")):
				row = j

		return(row)
	#Helper function for responses
	def determineCellPosition(self, positionX, positionY):

		# CORRECT FOR WHITE SPACE
		positionX = positionX - self.mosaicStartX
		positionY = positionY - self.mosaicStartY

		# WORK OUT WHAT COLUMN WE ARE IN
		x = positionX / self.squareWidth
		y = positionY / self.squareHeight

		coords = []
		coords = [x,y]

		return coords
	#Helper function for responses
	def determineCellRowIndexInMatrix(self, x, y):
		row = (x *(self.mosaicHeight/self.squareHeight)) + y

		return row
	#Helper function for redrawing
	def shouldRedraw(self):
		# return True if you want the CustomResource to be redrawn
		#(by calling the DrawMethodPointer) and the screen updated
		# and display flipped
		# return False to indicate that no redraw is needed for the resource

		if self.screen.getLastUpdateRetraceTime() < sreb.time.getCurrentTime() and \
			self.lastRedrawDone < self.screen.getLastUpdateRetraceTime():
			return True
		return False

	def writeMatrix(self):

		mew = 1

