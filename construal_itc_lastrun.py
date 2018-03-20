#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.6),
    on Thu Feb  1 16:34:34 2018
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
expName = u'construal_itc'  # from the Builder filename that created this script
expInfo = {u'ntrials': u'60', u'participant': u'0', u'day': u'0', u'run_id': u'0'}
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
    originPath=u'/Users/benjaminsmith/GDrive/neural-construal-level/code/SmithAdaptConstrualITC/construal_itc.psyexp',
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
    monitor=u'testMonitor', color=u'grey', colorSpace='rgb',
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
    text='Get ready for the new block!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "itc_trial"
itc_trialClock = core.Clock()
left_feedback = visual.Rect(
    win=win, name='left_feedback',
    width=(0.35,0.25)[0], height=(0.35,0.25)[1],
    ori=0, pos=(-0.5, 0),
    lineWidth=5, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[1,1,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
right_feedback = visual.Rect(
    win=win, name='right_feedback',
    width=(0.35,0.25)[0], height=(0.35,0.25)[1],
    ori=0, pos=(0.5, 0),
    lineWidth=5, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
Choice2Background = visual.Rect(
    win=win, name='Choice2Background',
    width=(0.3, 0.2)[0], height=(0.3, 0.2)[1],
    ori=0, pos=(0.5, 0.0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0.5,0.5], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
Choice1Background = visual.Rect(
    win=win, name='Choice1Background',
    width=(0.3, 0.2)[0], height=(0.3, 0.2)[1],
    ori=0, pos=(-0.5, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0.5,0.5], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
Delay1 = visual.TextStim(win=win, name='Delay1',
    text='First Delay',
    font='Arial',
    pos=(-0.5,-0.05), height=0.1, wrapWidth=None, ori=1.0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-4.0);
Delay2 = visual.TextStim(win=win, name='Delay2',
    text='SecondDelay',
    font='Arial',
    pos=(0.5,-0.05), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
Amount1 = visual.TextStim(win=win, name='Amount1',
    text=u'amount1',
    font=u'Arial',
    pos=(-0.5, 0.05), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-6.0);
Amount2 = visual.TextStim(win=win, name='Amount2',
    text=u'amount2\n',
    font=u'Arial',
    pos=(0.5, 0.05), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-7.0);
from itclogic import *

salience_condition=choose_condition(expInfo['participant'] ,expInfo['run_id'],expInfo['day'])
itc_feedback_duration=0.5
debugger = visual.TextStim(win=win, name='debugger',
    text='This is the debugger readout.',
    font='Arial',
    pos=(0, 0.5), height=0.1, wrapWidth=None, ori=0, 
    color=[0.5,0.5,1], colorSpace='rgb', opacity=1,
    depth=-10.0);
no_response = visual.TextStim(win=win, name='no_response',
    text='Respond faster',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=-11.0);
middle_line = visual.Line(
    win=win, name='middle_line',
    start=(-(0.3,0)[0]/2.0, 0), end=(+(0.3,0)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=5, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)

# Initialize components for Routine "gap"
gapClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
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

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "blockstart"-------
    t = 0
    blockstartClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.100000)
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
        frameRemains = 0.0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
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
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=asarray(int(expInfo['ntrials'])), method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        # ------Prepare to start Routine "itc_trial"-------
        t = 0
        itc_trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        Delay1.setColor('white', colorSpace='rgb')
        Delay1.setOri(0)
        resp = event.BuilderKeyResponse()
        feedback_began=False
        testtextvar="this is set by a var!"
        response_timer=None
        next_ct_printout=1.5
        debugger.text=str(trials.thisN)
        
        def begin_feedback(feedback_obj):
            global response_timer
            global feedback_began
            feedback_began=True
            response_timer = core.CountdownTimer(itc_feedback_duration)
            feedback_obj.setAutoDraw(True)
            feedback_obj.status= STARTED
        # keep track of which components have finished
        itc_trialComponents = [left_feedback, right_feedback, Choice2Background, Choice1Background, Delay1, Delay2, Amount1, Amount2, resp, debugger, no_response, middle_line]
        for thisComponent in itc_trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "itc_trial"-------
        while continueRoutine:
            # get current time
            t = itc_trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *left_feedback* updates
            if ((False)) and left_feedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                left_feedback.tStart = t
                left_feedback.frameNStart = frameN  # exact frame index
                left_feedback.setAutoDraw(True)
            
            # *right_feedback* updates
            if ((False)) and right_feedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                right_feedback.tStart = t
                right_feedback.frameNStart = frameN  # exact frame index
                right_feedback.setAutoDraw(True)
            
            # *Choice2Background* updates
            if t >= 0.0 and Choice2Background.status == NOT_STARTED:
                # keep track of start time/frame for later
                Choice2Background.tStart = t
                Choice2Background.frameNStart = frameN  # exact frame index
                Choice2Background.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Choice2Background.status == STARTED and t >= frameRemains:
                Choice2Background.setAutoDraw(False)
            
            # *Choice1Background* updates
            if t >= 0.0 and Choice1Background.status == NOT_STARTED:
                # keep track of start time/frame for later
                Choice1Background.tStart = t
                Choice1Background.frameNStart = frameN  # exact frame index
                Choice1Background.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Choice1Background.status == STARTED and t >= frameRemains:
                Choice1Background.setAutoDraw(False)
            
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
                theseKeys = event.getKeys(keyList=['left', 'down', 'right'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    resp.keys = theseKeys[-1]  # just the last key pressed
                    resp.rt = resp.clock.getTime()
                    # was this 'correct'?
                    if (resp.keys == str('"left"')) or (resp.keys == '"left"'):
                        resp.corr = 1
                    else:
                        resp.corr = 0
            
            if resp.status == STARTED:
                if len(theseKeys)>0:
                    if 'left' in theseKeys:
                        fb_obj=left_feedback
                    elif 'right' in theseKeys:
                        fb_obj=right_feedback
                    else:
                        raise Exception("Unhandled response key: " + str(theseKeys))
                    
                    if feedback_began==False: #execute on the first frame after a response.
                        begin_feedback(fb_obj)
                        resp.status == FINISHED
            
            elif resp.status==FINISHED and feedback_began==False:
                #second trigger for ending trial; response time is ended.
                begin_feedback(no_response)
                #
            
            #execute on first frame after feedback begins
            if response_timer is not None:
                #print out the time left but only on multiples of 0.1
                if response_timer.getTime()<next_ct_printout:
                    next_ct_printout=next_ct_printout-0.1
                    debugger.text=str(round(response_timer.getTime(),1))
            
                if response_timer.getTime()<0:
                    break #force end of routine.
            
            # *debugger* updates
            if t >= 0.0 and debugger.status == NOT_STARTED:
                # keep track of start time/frame for later
                debugger.tStart = t
                debugger.frameNStart = frameN  # exact frame index
                debugger.setAutoDraw(True)
            
            # *no_response* updates
            if ((False)) and no_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                no_response.tStart = t
                no_response.frameNStart = frameN  # exact frame index
                no_response.setAutoDraw(True)
            
            # *middle_line* updates
            if t >= 0.0 and middle_line.status == NOT_STARTED:
                # keep track of start time/frame for later
                middle_line.tStart = t
                middle_line.frameNStart = frameN  # exact frame index
                middle_line.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if middle_line.status == STARTED and t >= frameRemains:
                middle_line.setAutoDraw(False)
            
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
            if str('"left"').lower() == 'none':
               resp.corr = 1  # correct non-response
            else:
               resp.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('resp.keys',resp.keys)
        trials.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            trials.addData('resp.rt', resp.rt)
        
        # the Routine "itc_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
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
        thisExp.nextEntry()
        
    # completed asarray(int(expInfo['ntrials'])) repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 2 repeats of 'blocks'

# get names of stimulus parameters
if blocks.trialList in ([], [None], None):
    params = []
else:
    params = blocks.trialList[0].keys()
# save data for this loop
blocks.saveAsExcel(filename + '.xlsx', sheetName='blocks',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

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
