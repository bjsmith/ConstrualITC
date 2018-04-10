var CHOICE_SS="SS";//CHOICE_SS=1;
var CHOICE_LL="LL";//CHOICE_LL=2;
var SALIENCE_CONDITION_AMOUNT_SALIENT=0;
var SALIENCE_CONDITION_DELAY_SALIENT=1;
var SSonLorR_L="L";//SSonLorR_L=1;
var SSonLorR_R="R";//SSonLorR_R=2;
var condition_STANDARD = 1
var condition_DOMINANT = 2
var k_val=null;//the default k value is set at the start of the test.
var itc_feedback_duration = 1.0;
var itc_feedback_limit=5;
var construal_trial_maxlength=4.0;
var endBuffer=12.0;//leave 12 seconds at the end, and an extra 10 to allow for an additional trial.


showRespondFasterWarning=false;

var time_limit_reached = false;

//fix because we needed a "replaceAll" function that was compatible with python syntax
String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.replace(new RegExp(search.replace(/\\/g,'\\\\'), 'g'), replacement);
};

//BUG FIX
STARTED="";

function get_fMRI_time(){
	return (globalClock.getTime()-resp_fMRI.rt);
}

function get_delayLL(k_M,delaySS,amountSS,amountLL){
	//alert('delayll;' + delaySS + ',' + amountSS + ',' + delayLL + ',' + amountLL);
	return ((amountLL*((1+k_M*delaySS)/amountSS))-1)/k_M;
}

function get_amountSS(k_M,delaySS,delayLL,amountLL){
	//alert('amountss;' + delaySS + ',' + amountSS + ',' + delayLL + ',' + amountLL);
	return (amountLL/(1 + k_M*delayLL))*(1+k_M*delaySS);
}

function increment_k_m(choice,old_k_M){
	var k_M = null;
	if(choice==CHOICE_SS){
		k_M = old_k_M * Math.pow(10.0,(1/8));
	}else if (choice==CHOICE_LL){
		k_M = old_k_M * Math.pow(10.0,(-1/8));
	}else {
		alert("unknown choice type:" + choice)
	}
	return(k_M);
}


function on_construal_trialRoutineBegin(){
		trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['construal_trialUp']=get_fMRI_time();
}
function after_construal_trialRoutineEachFrame(){
	if(t>=construal_trial_maxlength || time_limit_reached==true){
		continueRoutine=false;
	}
	//record the timing for this.
}

function on_construal_trialRoutineEnd(){
		trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['construal_trialComplete']=get_fMRI_time();
}


//OK now, I think we need to work out what the data structure looks like
//until we do that it's difficult to code the behavior.
//function on_experiment_start(){}

trialRoutine_end_t=null;
var trialFeedbackReceived=false;
var startingK = null;
var trial_choiceUp=null;
function after_trialRoutineBegin(){
	itc_trial_response_obtained=false;
	
	//BUG FIX
	STARTED=psychoJS.STARTED;
	
	//load the k value if it hasn't been already
	if(k_val==null){
		k_val = [expInfo['k_val']*1,expInfo['k_val']*1];
	}
	startingK=k_val[parseInt(salienceCondition)];//[salienceCondition];
	//alert(delaySS + ',' + amountSS + ',' + delayLL + ',' + amountLL);
	if(salienceCondition==SALIENCE_CONDITION_AMOUNT_SALIENT){
		SSamount=get_amountSS(k_val[parseInt(salienceCondition)],SSdelay,LLdelay,LLamount);
	}else if (salienceCondition==SALIENCE_CONDITION_DELAY_SALIENT){
	//SSamount,LLamount,Condition,Choice,SSdelay,LLdelay
		//alert('calling delayll;' + SSdelay + ',' + SSamount + ',' + LLdelay + ',' + LLamount);
		LLdelay=get_delayLL(k_val[parseInt(salienceCondition)],SSdelay,SSamount,LLamount);
	}
	
	//now that we've calculated these, if this is a Dominated condition
	//then we bring back the LL fixed value to match the SS fixed value
	if (Condition==condition_DOMINANT){
		if(salienceCondition==SALIENCE_CONDITION_AMOUNT_SALIENT){
			LLdelay=SSdelay;
		}else if (salienceCondition==SALIENCE_CONDITION_DELAY_SALIENT){
			LLamount=SSamount;
		}
	}
	
	//work out which item to put on which side.
	
	if(SSonLorR==SSonLorR_L){
		tSSdelay=delay1;
		tLLdelay=delay2;
		tSSamount=amount1;
		tLLamount=amount2;
		//set the colors
        iOption1Background.setImage(psychoJS.resourceManager.getResource('images/redbg.png'));
        iOption2Background.setImage(psychoJS.resourceManager.getResource('images/bluebg.png'));
        //iOption1SelectedBg.setImage(psychoJS.resourceManager.getResource('images/red-highlight-bg.png'));
        //iOption2SelectedBg.setImage(psychoJS.resourceManager.getResource('images/blue-highlight-bg.png'));
	}else if (SSonLorR==SSonLorR_R){
		tSSdelay=delay2;
		tLLdelay=delay1;
		tSSamount=amount2;
		tLLamount=amount1;	
		//set the colors
        iOption1Background.setImage(psychoJS.resourceManager.getResource('images/bluebg.png'));
        iOption2Background.setImage(psychoJS.resourceManager.getResource('images/redbg.png'));
        //iOption1SelectedBg.setImage(psychoJS.resourceManager.getResource('images/blue-highlight-bg.png'));
        //iOption2SelectedBg.setImage(psychoJS.resourceManager.getResource('images/red-highlight-bg.png'));

	}
	

	//put the text in the boxes.
	tSSdelay.setText(Math.round(SSdelay,0) + " days");
    tLLdelay.setText(Math.round(LLdelay,0) + " days");
    tSSamount.setText("$" + parseFloat(SSamount).toFixed(2));
    tLLamount.setText("$" + parseFloat(LLamount).toFixed(2));
    
    //reset the "respond faster" label.
	showRespondFasterWarning=false;

    trialRoutine_end_t=6;
    if (time_limit_reached==true){
	    trialRoutine_end_t=0;//truncate back down to zero because we want to finish off!
    }
    
    trialFeedbackReceived=false;    
    trial_choiceUp = get_fMRI_time();

}

function BeginMomentarily_getText(){

	if (expInfo['run'].toLowerCase().startsWith('p')){
		return ("There are two sets of instructions in this task.\n"+
			"The first set of instructions relates to a categorization task.\n"+
			"There is a correct answer.\n\n"+
			"The second set of instructions is a money dilemma task.\n"+
			"Your choices are entirely up to you.\n"+
			"Your performance on the task will determine your payout,\n"+
			"so you will need to pay close attention.\n\n"+
			"The tasks will be staggered.\n"+
			"In other words, you will see one of each at a time.");
	}else{
		return ("This is the How/Why and Money Choice task\nthat you have played before.");
	}
}


function after_TrialRoutineEachFrame(){
		//function within function!!!
		//this is run after subject response but before the feedback has fully been shown.
		function saveTrialValuesAndWrapUp(){
			endingK=k_val[parseInt(salienceCondition)];
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['startingK']=startingK;
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['endingK']=endingK;
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['RT']=t;
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['choiceMade']=get_fMRI_time();
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['choiceUp']=trial_choiceUp;
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['Choice']=trial_choice;
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['LLdelay']=LLdelay;
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['SSamount']=SSamount;
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['SSonLorR']=SSonLorR;
			if (get_fMRI_time()>(expInfo['total_time_limit']-endBuffer)){
				//trials_set1.finished=true;
				//blocks.finished=true;
				time_limit_reached=true;

			}

		}
	//this is called every single screen frame.	
	if (theseKeys.length > 0 & t<itc_feedback_limit  & itc_trial_response_obtained==false) {  // at least one key was pressed
		var trial_choice = null;
		itc_trial_response_obtained= true;
		
		firstResp=theseKeys[0];
        if (firstResp=='1'){
			//fb_obj=iOption1SelectedBg

			//got to re-set the text to assert it.
			amount1.setText(amount1.text);
			delay1.setText(delay1.text);
			//option_1_chosen=true;
			if (SSonLorR==SSonLorR_L){
				iOption1Background.setImage(psychoJS.resourceManager.getResource('images/red-highlight-bg.png'));
				trial_choice = CHOICE_SS;
				trialFeedbackReceived=true;
			}
			if (SSonLorR==SSonLorR_R){
				iOption1Background.setImage(psychoJS.resourceManager.getResource('images/blue-highlight-bg.png'));
				trial_choice = CHOICE_LL;
				trialFeedbackReceived=true;
				//alert('trial_choice:' + trial_choice);
			}



        }else if (firstResp=='2'){
			iOption2Background.setImage(psychoJS.resourceManager.getResource('images/blue-highlight-bg.png'));
			amount2.setText(amount2.text);
			delay2.setText(delay2.text);
			//fb_obj=iOption2SelectedBg
			//option_2_chosen=true;
			if (SSonLorR==SSonLorR_L){
				iOption2Background.setImage(psychoJS.resourceManager.getResource('images/blue-highlight-bg.png'));
				trial_choice = CHOICE_LL;
				trialFeedbackReceived=true;
			}
			if (SSonLorR==SSonLorR_R){
				iOption2Background.setImage(psychoJS.resourceManager.getResource('images/red-highlight-bg.png'));
				trial_choice = CHOICE_SS;
				trialFeedbackReceived=true;
			}
        }


		trialRoutine_end_t = t+itc_feedback_duration;
		//saveTrialValuesAndWrapUp();
		
		//recalculate k value, but only if we're not in a dominated condition.
		if (Condition==condition_STANDARD){
			k_val[parseInt(salienceCondition)] = increment_k_m(trial_choice,k_val[parseInt(salienceCondition)]);
		}
	}else if (theseKeys.length > 0 & t>=itc_feedback_limit){
		//a key was pressed but after the time limit; ignore the keypress!
		theseKeys=[]
		resp_trial.keys=[]
	}
	
	if(trial_choice!=null){
		//we have a choice; collect values!
		saveTrialValuesAndWrapUp();
	}



	//bring forward the end of the routine; we just need long enough to display feedback.	
	if(t>=trialRoutine_end_t){
		//this is the end! put anything involving ending the trial here.
		if (trialFeedbackReceived==false){
		//we reached here without getting feedback; save the trial values
			saveTrialValuesAndWrapUp();
		}
		continueRoutine=false;



		//trials_set1.addData('startingK',startingK);
		//trials_set1.addData('endingK',endingK);
		//trials_set1.trialListaddData('endingK'
		//resp_trial.rt
	}
	
	
	
	if(t>=itc_feedback_limit & itc_trial_response_obtained==false){
		//show the 'too slow' item.
		showRespondFasterWarning=true;
	}
	

        
	
}
//THIS SEEMS TO BE DEFUNCT AND NOT CALLED.
function on_routine_end(choice){
	k_val[parseInt(salienceCondition)] = increment_k_m(choice,k_val[parseInt(salienceCondition)]);
	console.log(total_time_limit);
	console.log(get_fMRI_time());
	//we're reaching the time limit, need to end.
}

function after_ITIfixRoutineEachFrame(){
	if(t>=ITI || time_limit_reached==true){
		continueRoutine=false;
	}
}

function after_rTaskIntervalRoutineEachFrame(){
	if(t>=TaskInterval || time_limit_reached==true){
		continueRoutine=false;
	}
}


function ITIFix_begin(){
	//continueRoutine=false;
	//tITIFix_begin_code.status=psychoJS.NOT_STARTED;
	//tITIFix_begin_code.duration=5;
	return("");
}

function on_rTaskIntervalFrame(){
	//continueRoutine=false;
	return("");
}


function run_replace_default_expInfo(){
	expInfo = {'participant':'', 'session':'','run':'',
	'k_val':0.01,
	'designDir':'fMRI_xxx',
	'total_time_limit':'395'
};
	document.getElementById('fps').style.display="none";

	return expInfo;
}


function after_scheduleInstantiation(){
// 	if this is a practice run
// 	if (expInfo['run'].toLowerCase().startsWith('p')){
// 		instruction_loop.nReps=1;
// 	}else{
// 		fMRI_start_loop.nReps=1;
// 	}
// 	//

}


function tGetWarningText(){
	thisExp.save();
	if (expInfo['run'].toLowerCase().startsWith('p')){
		return ("Please pass the computer back to the experimenter.\nTo the experimenter: Press Spacebar to conclude.")
	}else{
		return ("(To the experimenter: press Spacebar to conclude)")
	}
}
// 
// function flowScheduler_insert_infront_of(previous_item_name,currentItem){
// 	t_to_insert=null;
// 	for (t = 0; t<flowScheduler.taskList.length;t++){
// 		if (flowScheduler.taskList[t].name==previous_item_name) t_to_insert=t;
// 	}
// 	flowScheduler.taskList.splice(t_to_insert+1,0,
// 	flowScheduler.argsList.splice(t_to_insert+1,0,undefined)
// }

//  if salienceCondition==0;
//         amountL=M(i,c_LLamount);
//         delayS = 3;
//         delayL = 90;
//         amountS = (amountL/(1 + k_M*delayL))*(1+k_M*delayS);
//         %dominated condition
//         if M(i,c_Condition) == 2;
//             delayL=delayS;
//         end
//     elseif salienceCondition==1;
//         delayS=M(i,c_SSdelay);
//         %fixed amounts, vary delay
//         amountS=25;
//         amountL=30;
//         delayL = ((amountL*((1+k_M*delayS)/amountS))-1)/k_M;
//     end


//this is straight from the psychojs/data.js library
//kind of naughty to change it here but Eustace has very specific ideas about how he wants the filename
//and this is the place to change it.

psychoJS.data.ExperimentHandler.prototype.save = function(attribs) {
	// prepare session information:
	var session = {};
//	session['experimentName'] = this.extraInfo['expName'];
	session['participantName'] = "participant" + this.extraInfo['participant'];
	session['sessionName'] = "session" + expInfo['session'];
	session['sessionDate'] = "run" + expInfo['run'];
//	session['sessionName'] = this.extraInfo['session'];
//	session['sessionDate'] = this.extraInfo['date'];
	for (property in psychoJS._IP)
		if (psychoJS._IP.hasOwnProperty(property)) {
			session[property] = "CITC";
		}

	// prepare the csv file:
	var csv = "";

	// (a) build the header:
	var header = this._trialsKeys;
	for (var l = 0; l < this._loops.length; l++) {
		var loop = this._loops[l];
		// add headers for condition columns
		if (typeof(loop.thisTrial) != 'undefined') {
			for (a in loop.thisTrial) header.push(a);
		}
		var loopAttributes = this.getLoopAttributes(loop);
		for (a in loopAttributes) {
			if (loopAttributes.hasOwnProperty(a)) header.push(a);
		}
	}
	for (a in this.extraInfo) {
		if (this.extraInfo.hasOwnProperty(a))
			header.push(a);
	}
	for (var h = 0; h < header.length; h++) {
		if (h > 0)
			csv = csv + ', ';
		csv = csv + header[h];
	}
	csv = csv + '\n';

	// (b) build the records:
	for (var r = 0; r < this._trialsData.length; r++) {
		for (var h = 0; h < header.length; h++) {
			if (h > 0) csv = csv + ', ';
			// leave 'undefined' values blank in the data file
			if (typeof(this._trialsData[r][header[h]]) != 'undefined') csv = csv + this._trialsData[r][header[h]];
		}
		csv = csv + '\n';
	}


	// upload data to the experiment server:
	if (this.saveTo === 'EXPERIMENT_SERVER') {
		psychoJS.resourceManager.EXPUploadData(session, 'RESULT', csv);
	}
	// upload data to OSF via the experiment server:
	else if (this.saveTo === 'OSF_VIA_EXPERIMENT_SERVER') {
		psychoJS.resourceManager.OSFEXPUploadData(session, 'RESULT', csv);
	}
	// save data to a local excel file:
	else if (this.saveTo === 'LOCAL_EXCEL') {
		// TODO
	}
}
