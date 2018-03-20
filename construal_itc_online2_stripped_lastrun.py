#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.6),
    on Fri Feb  2 18:23:33 2018
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
expName = u'construal_itc_online2_stripped'  # from the Builder filename that created this script
expInfo = {u'participant': u'0', u'ntrials': u'60', u'kval': u'0.001', u'day': u'0', u'run_id': u'0'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/benjaminsmith/GDrive/neural-construal-level/code/SmithAdaptConstrualITC/construal_itc_online2_stripped.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='grey', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "blockstart"
blockstartClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='The game is starting.\n\nPlease choose one of the two options on the screen.\n\nYou will have 5 seconds to make a decision.\n\nPlease remain as still as possible.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "itc_trial"
itc_trialClock = core.Clock()
ImgChoice2Background = visual.ImageStim(
    win=win, name='ImgChoice2Background',
    image=u'images/bluebg.png', mask=None,
    ori=0, pos=(0.5, 0), size=(0.3, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ImgChoice1Background = visual.ImageStim(
    win=win, name='ImgChoice1Background',
    image='sin', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.3, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Delay1 = visual.TextStim(win=win, name='Delay1',
    text='default text',
    font=u'Arial',
    pos=(-0.5,-0.05), height=0.1, wrapWidth=None, ori=1.0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-2.0);
Delay2 = visual.TextStim(win=win, name='Delay2',
    text='default text',
    font=u'Arial',
    pos=(0.5,-0.05), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0);
Amount1 = visual.TextStim(win=win, name='Amount1',
    text='default text',
    font=u'Arial',
    pos=(-0.5, 0.05), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);
Amount2 = visual.TextStim(win=win, name='Amount2',
    text='default text',
    font=u'Arial',
    pos=(0.5, 0.05), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0);
text_middle_line = visual.TextStim(win=win, name='text_middle_line',
    text=u'|',
    font=u'Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-7.0);

# Initialize components for Routine "gap"
gapClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "block2intro"
block2introClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=u"We'll show you another block now.\n\nbe good!",
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText = visual.TextStim(win=win, name='thanksText',
    text='This is the end of the experiment.\n\nThanks!',
    font='arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "blockstart"-------
t = 0
blockstartClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
blockstartComponents = [text]
for thisComponent in blockstartComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "blockstart"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blockstartClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blockstartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blockstart"-------
for thisComponent in blockstartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "itc_trial"-------
t = 0
itc_trialClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.500000)
# update component parameters for each repeat
ImgChoice1Background.setImage(u'images/redbg.png')
Delay1.setColor(u'white', colorSpace='rgb')
Delay1.setText(u'SSdelay')
Delay1.setOri(0)
Delay2.setText(u'LLdelay')
Amount1.setText(u'SSamount')
Amount2.setText(u'LLamount')
resp = event.BuilderKeyResponse()
# keep track of which components have finished
itc_trialComponents = [ImgChoice2Background, ImgChoice1Background, Delay1, Delay2, Amount1, Amount2, resp, text_middle_line]
for thisComponent in itc_trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "itc_trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = itc_trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ImgChoice2Background* updates
    if t >= 0.0 and ImgChoice2Background.status == NOT_STARTED:
        # keep track of start time/frame for later
        ImgChoice2Background.tStart = t
        ImgChoice2Background.frameNStart = frameN  # exact frame index
        ImgChoice2Background.setAutoDraw(True)
    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ImgChoice2Background.status == STARTED and t >= frameRemains:
        ImgChoice2Background.setAutoDraw(False)
    
    # *ImgChoice1Background* updates
    if t >= 0.0 and ImgChoice1Background.status == NOT_STARTED:
        # keep track of start time/frame for later
        ImgChoice1Background.tStart = t
        ImgChoice1Background.frameNStart = frameN  # exact frame index
        ImgChoice1Background.setAutoDraw(True)
    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ImgChoice1Background.status == STARTED and t >= frameRemains:
        ImgChoice1Background.setAutoDraw(False)
    
    # *Delay1* updates
    if t >= 0.0 and Delay1.status == NOT_STARTED:
        # keep track of start time/frame for later
        Delay1.tStart = t
        Delay1.frameNStart = frameN  # exact frame index
        Delay1.setAutoDraw(True)
    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if Delay1.status == STARTED and t >= frameRemains:
        Delay1.setAutoDraw(False)
    
    # *Delay2* updates
    if t >= 0.0 and Delay2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Delay2.tStart = t
        Delay2.frameNStart = frameN  # exact frame index
        Delay2.setAutoDraw(True)
    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if Delay2.status == STARTED and t >= frameRemains:
        Delay2.setAutoDraw(False)
    
    # *Amount1* updates
    if t >= 0.0 and Amount1.status == NOT_STARTED:
        # keep track of start time/frame for later
        Amount1.tStart = t
        Amount1.frameNStart = frameN  # exact frame index
        Amount1.setAutoDraw(True)
    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if Amount1.status == STARTED and t >= frameRemains:
        Amount1.setAutoDraw(False)
    
    # *Amount2* updates
    if t >= 0.0 and Amount2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Amount2.tStart = t
        Amount2.frameNStart = frameN  # exact frame index
        Amount2.setAutoDraw(True)
    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if Amount2.status == STARTED and t >= frameRemains:
        Amount2.setAutoDraw(False)
    
    # *resp* updates
    if t >= 0 and resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        resp.tStart = t
        resp.frameNStart = frameN  # exact frame index
        resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if resp.status == STARTED and t >= frameRemains:
        resp.status = STOPPED
    if resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            if resp.keys == []:  # then this was the first keypress
                resp.keys = theseKeys[0]  # just the first key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str('"1"')) or (resp.keys == '"1"'):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
    
    # *text_middle_line* updates
    if t >= 0.0 and text_middle_line.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_middle_line.tStart = t
        text_middle_line.frameNStart = frameN  # exact frame index
        text_middle_line.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_middle_line.status == STARTED and t >= frameRemains:
        text_middle_line.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in itc_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "itc_trial"-------
for thisComponent in itc_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if resp.keys in ['', [], None]:  # No response was made
    resp.keys=None
    # was no response the correct answer?!
    if str('"1"').lower() == 'none':
       resp.corr = 1  # correct non-response
    else:
       resp.corr = 0  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('resp.keys',resp.keys)
thisExp.addData('resp.corr', resp.corr)
if resp.keys != None:  # we had a response
    thisExp.addData('resp.rt', resp.rt)
thisExp.nextEntry()

# ------Prepare to start Routine "gap"-------
t = 0
gapClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
gapComponents = [text_2]
for thisComponent in gapComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "gap"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = gapClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_2.status == STARTED and t >= frameRemains:
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in gapComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "gap"-------
for thisComponent in gapComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "block2intro"-------
t = 0
block2introClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
block2introComponents = [text_3]
for thisComponent in block2introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "block2intro"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = block2introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_3.status == STARTED and t >= frameRemains:
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block2introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "block2intro"-------
for thisComponent in block2introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if t >= 0.0 and thanksText.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanksText.tStart = t
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if thanksText.status == STARTED and t >= frameRemains:
        thanksText.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
