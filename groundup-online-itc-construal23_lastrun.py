#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.6),
    on Tue Feb 13 00:52:37 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'groundup-online-itc-construal23'  # from the Builder filename that created this script
expInfo = {u'participant': u'1', u'session': u'1', u'k_M': u'0.001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/benjaminsmith/GDrive/neural-construal-level/code/SmithAdaptConstrualITC/groundup-online-itc-construal23.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "beginRoutine"
beginRoutineClock = core.Clock()
tLoading = visual.TextStim(win=win, name='tLoading',
    text='.......................',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "fMRI_pause"
fMRI_pauseClock = core.Clock()
BeginMomentarily = visual.TextStim(win=win, name='BeginMomentarily',
    text='There are two sets of instructions in this task. \nThe first set of instructions relates to a categorization task.\nThere is a correct answer.\n\nThe second set of instructions is a money dilemma task. \nYour choices are entirely up to you. \nYour performance on the task will determine your payout, \nso you will need to pay close attention.\n\nThe tasks will be staggered.\nIn other words, you will see one of each at a time.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
tPressToContinue = visual.TextStim(win=win, name='tPressToContinue',
    text='Press 5 to continue.',
    font='Arial',
    pos=(0, -.9), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "rTaskInstructions"
rTaskInstructionsClock = core.Clock()
task_instructions = visual.TextStim(win=win, name='task_instructions',
    text='The game is starting.\n\nFor the money dilemma task, \nplease choose one of the two options on the screen.\n\nYou will have 5 seconds to make a decision.\n\nIf you are completing this in an fMRI scanner, \nplease remain as still as possible.\n\nPress 1 or 2 to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
debugtext = visual.TextStim(win=win, name='debugtext',
    text='default text',
    font='Arial',
    pos=(0, 0.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "rHowWhyTaskInstructions"
rHowWhyTaskInstructionsClock = core.Clock()
iHowWhyTaskInstructions = visual.ImageStim(
    win=win, name='iHowWhyTaskInstructions',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2.0,2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "rBlockInstructions"
rBlockInstructionsClock = core.Clock()
tBlockInstructions = visual.TextStim(win=win, name='tBlockInstructions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ITIfix"
ITIfixClock = core.Clock()
tFix = visual.TextStim(win=win, name='tFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "construal_trial"
construal_trialClock = core.Clock()
tConstrualQuestion = visual.TextStim(win=win, name='tConstrualQuestion',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
tConstrualAnswer = visual.TextStim(win=win, name='tConstrualAnswer',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);
yes1 = visual.TextStim(win=win, name='yes1',
    text='1\nYes',
    font='Arial',
    pos=(-0.3, -0.3), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0);
no2 = visual.TextStim(win=win, name='no2',
    text='2\nNo',
    font='Arial',
    pos=(0.3, -0.3), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "rTaskInterval"
rTaskIntervalClock = core.Clock()
tFixSimple = visual.TextStim(win=win, name='tFixSimple',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
iOption1Background = visual.ImageStim(
    win=win, name='iOption1Background',
    image='sin', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.4, 0.3),
    color=1.0, colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
iOption2Background = visual.ImageStim(
    win=win, name='iOption2Background',
    image='sin', mask=None,
    ori=0, pos=(0.5, 0), size=(0.4, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
delay1 = visual.TextStim(win=win, name='delay1',
    text='default text',
    font='Arial',
    pos=(-0.5, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);
delay2 = visual.TextStim(win=win, name='delay2',
    text='default text',
    font='Arial',
    pos=(0.5, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0);
amount1 = visual.TextStim(win=win, name='amount1',
    text='default text',
    font='Arial',
    pos=(-0.5, 0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0);
amount2 = visual.TextStim(win=win, name='amount2',
    text='default text',
    font='Arial',
    pos=(0.5, 0.05), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0);
divider = visual.TextStim(win=win, name='divider',
    text='|',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0);
tRespondTooSlow = visual.TextStim(win=win, name='tRespondTooSlow',
    text='Respond faster!',
    font='Arial',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-8.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "beginRoutine"-------
t = 0
beginRoutineClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
beginRoutineComponents = [tLoading]
for thisComponent in beginRoutineComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "beginRoutine"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = beginRoutineClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tLoading* updates
    if t >= 0.0 and tLoading.status == NOT_STARTED:
        # keep track of start time/frame for later
        tLoading.tStart = t
        tLoading.frameNStart = frameN  # exact frame index
        tLoading.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if tLoading.status == STARTED and t >= frameRemains:
        tLoading.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginRoutineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "beginRoutine"-------
for thisComponent in beginRoutineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "fMRI_pause"-------
t = 0
fMRI_pauseClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
resp_fMRI = event.BuilderKeyResponse()
# keep track of which components have finished
fMRI_pauseComponents = [BeginMomentarily, resp_fMRI, tPressToContinue]
for thisComponent in fMRI_pauseComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "fMRI_pause"-------
while continueRoutine:
    # get current time
    t = fMRI_pauseClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *BeginMomentarily* updates
    if t >= 0.0 and BeginMomentarily.status == NOT_STARTED:
        # keep track of start time/frame for later
        BeginMomentarily.tStart = t
        BeginMomentarily.frameNStart = frameN  # exact frame index
        BeginMomentarily.setAutoDraw(True)
    
    # *resp_fMRI* updates
    if t >= 0.0 and resp_fMRI.status == NOT_STARTED:
        # keep track of start time/frame for later
        resp_fMRI.tStart = t
        resp_fMRI.frameNStart = frameN  # exact frame index
        resp_fMRI.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(resp_fMRI.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if resp_fMRI.status == STARTED:
        theseKeys = event.getKeys(keyList=['5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            resp_fMRI.keys = theseKeys[-1]  # just the last key pressed
            resp_fMRI.rt = resp_fMRI.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *tPressToContinue* updates
    if ((expInfo['run'].toLowerCase().startsWith('p'))) and tPressToContinue.status == NOT_STARTED:
        # keep track of start time/frame for later
        tPressToContinue.tStart = t
        tPressToContinue.frameNStart = frameN  # exact frame index
        tPressToContinue.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fMRI_pauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fMRI_pause"-------
for thisComponent in fMRI_pauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if resp_fMRI.keys in ['', [], None]:  # No response was made
    resp_fMRI.keys=None
thisExp.addData('resp_fMRI.keys',resp_fMRI.keys)
if resp_fMRI.keys != None:  # we had a response
    thisExp.addData('resp_fMRI.rt', resp_fMRI.rt)
thisExp.nextEntry()
# the Routine "fMRI_pause" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
instructionLoop = data.TrialHandler(nReps=expInfo['run'].toLowerCase().startsWith('p'), method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blockcontrol.csv'),
    seed=None, name='instructionLoop')
thisExp.addLoop(instructionLoop)  # add the loop to the experiment
thisInstructionLoop = instructionLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstructionLoop.rgb)
if thisInstructionLoop != None:
    for paramName in thisInstructionLoop.keys():
        exec(paramName + '= thisInstructionLoop.' + paramName)

for thisInstructionLoop in instructionLoop:
    currentLoop = instructionLoop
    # abbreviate parameter names if possible (e.g. rgb = thisInstructionLoop.rgb)
    if thisInstructionLoop != None:
        for paramName in thisInstructionLoop.keys():
            exec(paramName + '= thisInstructionLoop.' + paramName)
    
    # ------Prepare to start Routine "rTaskInstructions"-------
    t = 0
    rTaskInstructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    debugtext.setText(' ')
    respTaskInstructions = event.BuilderKeyResponse()
    # keep track of which components have finished
    rTaskInstructionsComponents = [task_instructions, debugtext, respTaskInstructions]
    for thisComponent in rTaskInstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "rTaskInstructions"-------
    while continueRoutine:
        # get current time
        t = rTaskInstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *task_instructions* updates
        if t >= 0.0 and task_instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            task_instructions.tStart = t
            task_instructions.frameNStart = frameN  # exact frame index
            task_instructions.setAutoDraw(True)
        
        # *debugtext* updates
        if t >= 0.0 and debugtext.status == NOT_STARTED:
            # keep track of start time/frame for later
            debugtext.tStart = t
            debugtext.frameNStart = frameN  # exact frame index
            debugtext.setAutoDraw(True)
        
        # *respTaskInstructions* updates
        if t >= 0 and respTaskInstructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            respTaskInstructions.tStart = t
            respTaskInstructions.frameNStart = frameN  # exact frame index
            respTaskInstructions.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(respTaskInstructions.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if respTaskInstructions.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                respTaskInstructions.keys = theseKeys[-1]  # just the last key pressed
                respTaskInstructions.rt = respTaskInstructions.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rTaskInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rTaskInstructions"-------
    for thisComponent in rTaskInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if respTaskInstructions.keys in ['', [], None]:  # No response was made
        respTaskInstructions.keys=None
    instructionLoop.addData('respTaskInstructions.keys',respTaskInstructions.keys)
    if respTaskInstructions.keys != None:  # we had a response
        instructionLoop.addData('respTaskInstructions.rt', respTaskInstructions.rt)
    # the Routine "rTaskInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rHowWhyTaskInstructions"-------
    t = 0
    rHowWhyTaskInstructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    iHowWhyTaskInstructions.setImage('images/construal-stimuli/howwhytest_instructions.jpg')
    respHowWhyTaskInstructions = event.BuilderKeyResponse()
    # keep track of which components have finished
    rHowWhyTaskInstructionsComponents = [iHowWhyTaskInstructions, respHowWhyTaskInstructions]
    for thisComponent in rHowWhyTaskInstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "rHowWhyTaskInstructions"-------
    while continueRoutine:
        # get current time
        t = rHowWhyTaskInstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iHowWhyTaskInstructions* updates
        if t >= 0.0 and iHowWhyTaskInstructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            iHowWhyTaskInstructions.tStart = t
            iHowWhyTaskInstructions.frameNStart = frameN  # exact frame index
            iHowWhyTaskInstructions.setAutoDraw(True)
        
        # *respHowWhyTaskInstructions* updates
        if t >= 0.0 and respHowWhyTaskInstructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            respHowWhyTaskInstructions.tStart = t
            respHowWhyTaskInstructions.frameNStart = frameN  # exact frame index
            respHowWhyTaskInstructions.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(respHowWhyTaskInstructions.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if respHowWhyTaskInstructions.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                respHowWhyTaskInstructions.keys = theseKeys[-1]  # just the last key pressed
                respHowWhyTaskInstructions.rt = respHowWhyTaskInstructions.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rHowWhyTaskInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rHowWhyTaskInstructions"-------
    for thisComponent in rHowWhyTaskInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if respHowWhyTaskInstructions.keys in ['', [], None]:  # No response was made
        respHowWhyTaskInstructions.keys=None
    instructionLoop.addData('respHowWhyTaskInstructions.keys',respHowWhyTaskInstructions.keys)
    if respHowWhyTaskInstructions.keys != None:  # we had a response
        instructionLoop.addData('respHowWhyTaskInstructions.rt', respHowWhyTaskInstructions.rt)
    # the Routine "rHowWhyTaskInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed expInfo['run'].toLowerCase().startsWith('p') repeats of 'instructionLoop'


# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(('design_csv_files/'+expInfo['designDir']+'/metaloop_sub[participant]d[session]r[run].csv'.replace("[participant]",expInfo['participant']).replace("[session]",expInfo['session']).replace("[run]",expInfo['run']))),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock.keys():
        exec(paramName + '= thisBlock.' + paramName)

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
    
    # ------Prepare to start Routine "rBlockInstructions"-------
    t = 0
    rBlockInstructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    tBlockInstructions.setText(PreTaskInstructions.replaceAll("\\n","\n"))
    # keep track of which components have finished
    rBlockInstructionsComponents = [tBlockInstructions]
    for thisComponent in rBlockInstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "rBlockInstructions"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rBlockInstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *tBlockInstructions* updates
        if t >= 0 and tBlockInstructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            tBlockInstructions.tStart = t
            tBlockInstructions.frameNStart = frameN  # exact frame index
            tBlockInstructions.setAutoDraw(True)
        frameRemains = 0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if tBlockInstructions.status == STARTED and t >= frameRemains:
            tBlockInstructions.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rBlockInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rBlockInstructions"-------
    for thisComponent in rBlockInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    trials_set1 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions((LoopFile.replace("[participant]",expInfo['participant']).replace("[session]",expInfo['session']))),
        seed=None, name='trials_set1')
    thisExp.addLoop(trials_set1)  # add the loop to the experiment
    thisTrials_set1 = trials_set1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_set1.rgb)
    if thisTrials_set1 != None:
        for paramName in thisTrials_set1.keys():
            exec(paramName + '= thisTrials_set1.' + paramName)
    
    for thisTrials_set1 in trials_set1:
        currentLoop = trials_set1
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_set1.rgb)
        if thisTrials_set1 != None:
            for paramName in thisTrials_set1.keys():
                exec(paramName + '= thisTrials_set1.' + paramName)
        
        # ------Prepare to start Routine "ITIfix"-------
        t = 0
        ITIfixClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ITIfixComponents = [tFix]
        for thisComponent in ITIfixComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ITIfix"-------
        while continueRoutine:
            # get current time
            t = ITIfixClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tFix* updates
            if t >= 0 and tFix.status == NOT_STARTED:
                # keep track of start time/frame for later
                tFix.tStart = t
                tFix.frameNStart = frameN  # exact frame index
                tFix.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIfixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ITIfix"-------
        for thisComponent in ITIfixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "ITIfix" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "construal_trial"-------
        t = 0
        construal_trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        tConstrualQuestion.setText(Construal_QuestionText)
        tConstrualAnswer.setText(Construal_AnswerText)
        construal_resp = event.BuilderKeyResponse()
        # keep track of which components have finished
        construal_trialComponents = [tConstrualQuestion, tConstrualAnswer, construal_resp, yes1, no2]
        for thisComponent in construal_trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "construal_trial"-------
        while continueRoutine:
            # get current time
            t = construal_trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tConstrualQuestion* updates
            if t >= 0.0 and tConstrualQuestion.status == NOT_STARTED:
                # keep track of start time/frame for later
                tConstrualQuestion.tStart = t
                tConstrualQuestion.frameNStart = frameN  # exact frame index
                tConstrualQuestion.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if tConstrualQuestion.status == STARTED and t >= frameRemains:
                tConstrualQuestion.setAutoDraw(False)
            
            # *tConstrualAnswer* updates
            if t >= 1.75 and tConstrualAnswer.status == NOT_STARTED:
                # keep track of start time/frame for later
                tConstrualAnswer.tStart = t
                tConstrualAnswer.frameNStart = frameN  # exact frame index
                tConstrualAnswer.setAutoDraw(True)
            frameRemains = 1.75 + 2.25- win.monitorFramePeriod * 0.75  # most of one frame period left
            if tConstrualAnswer.status == STARTED and t >= frameRemains:
                tConstrualAnswer.setAutoDraw(False)
            
            # *construal_resp* updates
            if t >= 1.75 and construal_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                construal_resp.tStart = t
                construal_resp.frameNStart = frameN  # exact frame index
                construal_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(construal_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if construal_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if construal_resp.keys == []:  # then this was the first keypress
                        construal_resp.keys = theseKeys[0]  # just the first key pressed
                        construal_resp.rt = construal_resp.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
            
            # *yes1* updates
            if t >= 1.75 and yes1.status == NOT_STARTED:
                # keep track of start time/frame for later
                yes1.tStart = t
                yes1.frameNStart = frameN  # exact frame index
                yes1.setAutoDraw(True)
            frameRemains = 1.75 + 2.25- win.monitorFramePeriod * 0.75  # most of one frame period left
            if yes1.status == STARTED and t >= frameRemains:
                yes1.setAutoDraw(False)
            
            # *no2* updates
            if t >= 1.75 and no2.status == NOT_STARTED:
                # keep track of start time/frame for later
                no2.tStart = t
                no2.frameNStart = frameN  # exact frame index
                no2.setAutoDraw(True)
            frameRemains = 1.75 + 2.25- win.monitorFramePeriod * 0.75  # most of one frame period left
            if no2.status == STARTED and t >= frameRemains:
                no2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in construal_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "construal_trial"-------
        for thisComponent in construal_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if construal_resp.keys in ['', [], None]:  # No response was made
            construal_resp.keys=None
        trials_set1.addData('construal_resp.keys',construal_resp.keys)
        if construal_resp.keys != None:  # we had a response
            trials_set1.addData('construal_resp.rt', construal_resp.rt)
        # the Routine "construal_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "rTaskInterval"-------
        t = 0
        rTaskIntervalClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        rTaskIntervalComponents = [tFixSimple]
        for thisComponent in rTaskIntervalComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "rTaskInterval"-------
        while continueRoutine:
            # get current time
            t = rTaskIntervalClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tFixSimple* updates
            if t >= 0.0 and tFixSimple.status == NOT_STARTED:
                # keep track of start time/frame for later
                tFixSimple.tStart = t
                tFixSimple.frameNStart = frameN  # exact frame index
                tFixSimple.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rTaskIntervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rTaskInterval"-------
        for thisComponent in rTaskIntervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "rTaskInterval" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        iOption1Background.setColor([1,1,1], colorSpace='rgb')
        iOption1Background.setImage('images/redbg.png')
        iOption2Background.setImage('images/bluebg.png')
        delay1.setText(SSamount)
        delay2.setText(LLdelay)
        amount1.setText(SSamount)
        amount2.setText(LLamount)
        resp_trial = event.BuilderKeyResponse()
        # keep track of which components have finished
        trialComponents = [iOption1Background, iOption2Background, delay1, delay2, amount1, amount2, divider, resp_trial, tRespondTooSlow]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *iOption1Background* updates
            if t >= 0.0 and iOption1Background.status == NOT_STARTED:
                # keep track of start time/frame for later
                iOption1Background.tStart = t
                iOption1Background.frameNStart = frameN  # exact frame index
                iOption1Background.setAutoDraw(True)
            frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if iOption1Background.status == STARTED and t >= frameRemains:
                iOption1Background.setAutoDraw(False)
            
            # *iOption2Background* updates
            if t >= 0.0 and iOption2Background.status == NOT_STARTED:
                # keep track of start time/frame for later
                iOption2Background.tStart = t
                iOption2Background.frameNStart = frameN  # exact frame index
                iOption2Background.setAutoDraw(True)
            frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if iOption2Background.status == STARTED and t >= frameRemains:
                iOption2Background.setAutoDraw(False)
            
            # *delay1* updates
            if t >= 0.0 and delay1.status == NOT_STARTED:
                # keep track of start time/frame for later
                delay1.tStart = t
                delay1.frameNStart = frameN  # exact frame index
                delay1.setAutoDraw(True)
            frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if delay1.status == STARTED and t >= frameRemains:
                delay1.setAutoDraw(False)
            
            # *delay2* updates
            if t >= 0.0 and delay2.status == NOT_STARTED:
                # keep track of start time/frame for later
                delay2.tStart = t
                delay2.frameNStart = frameN  # exact frame index
                delay2.setAutoDraw(True)
            frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if delay2.status == STARTED and t >= frameRemains:
                delay2.setAutoDraw(False)
            
            # *amount1* updates
            if t >= 0.0 and amount1.status == NOT_STARTED:
                # keep track of start time/frame for later
                amount1.tStart = t
                amount1.frameNStart = frameN  # exact frame index
                amount1.setAutoDraw(True)
            frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if amount1.status == STARTED and t >= frameRemains:
                amount1.setAutoDraw(False)
            
            # *amount2* updates
            if t >= 0.0 and amount2.status == NOT_STARTED:
                # keep track of start time/frame for later
                amount2.tStart = t
                amount2.frameNStart = frameN  # exact frame index
                amount2.setAutoDraw(True)
            frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if amount2.status == STARTED and t >= frameRemains:
                amount2.setAutoDraw(False)
            
            # *divider* updates
            if t >= 0.0 and divider.status == NOT_STARTED:
                # keep track of start time/frame for later
                divider.tStart = t
                divider.frameNStart = frameN  # exact frame index
                divider.setAutoDraw(True)
            frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
            if divider.status == STARTED and t >= frameRemains:
                divider.setAutoDraw(False)
            
            # *resp_trial* updates
            if t >= 0.0 and resp_trial.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp_trial.tStart = t
                resp_trial.frameNStart = frameN  # exact frame index
                resp_trial.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(resp_trial.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if resp_trial.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if resp_trial.keys == []:  # then this was the first keypress
                        resp_trial.keys = theseKeys[0]  # just the first key pressed
                        resp_trial.rt = resp_trial.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
            
            # *tRespondTooSlow* updates
            if ((showRespondFasterWarning)) and tRespondTooSlow.status == NOT_STARTED:
                # keep track of start time/frame for later
                tRespondTooSlow.tStart = t
                tRespondTooSlow.frameNStart = frameN  # exact frame index
                tRespondTooSlow.setAutoDraw(True)
            if tRespondTooSlow.status == STARTED and t >= (tRespondTooSlow.tStart + 1.0):
                tRespondTooSlow.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if resp_trial.keys in ['', [], None]:  # No response was made
            resp_trial.keys=None
        trials_set1.addData('resp_trial.keys',resp_trial.keys)
        if resp_trial.keys != None:  # we had a response
            trials_set1.addData('resp_trial.rt', resp_trial.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_set1'
    
# completed 1 repeats of 'blocks'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
