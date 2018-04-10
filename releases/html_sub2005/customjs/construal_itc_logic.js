var CHOICE_SS=1;
var CHOICE_LL=2;
var SALIENCE_CONDITION_AMOUNT_SALIENT=0;
var SALIENCE_CONDITION_DELAY_SALIENT=1;
var SSonLorR_L=1;
var SSonLorR_R=2;
var condition_STANDARD = 1
var condition_DOMINANT = 2
var k_val=null;//the default k value is set at the start of the test.
var itc_feedback_duration = 1.0;
var itc_feedback_limit=5;

var construal_trial_maxlength=4.0

showRespondFasterWarning=false;
//these are obsolete. Can be removed after next main screen compile.
//option_1_chosen=false;
//option_2_chosen=false;


//fix because we needed a "replaceAll" function that was compatible with python syntax
String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.replace(new RegExp(search.replace(/\\/g,'\\\\'), 'g'), replacement);
};

//BUG FIX
STARTED="";

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
		trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['construal_trialUp']=rTaskInstructionsClock.getTime();
}
function after_construal_trialRoutineEachFrame(){
	if(t>=construal_trial_maxlength){
		continueRoutine=false;
	}
	//record the timing for this.
}

function on_construal_trialRoutineEnd(){
		trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['construal_trialComplete']=rTaskInstructionsClock.getTime();
}


//OK now, I think we need to work out what the data structure looks like
//until we do that it's difficult to code the behavior.
//function on_experiment_start(){}

trialRoutine_end_t=null;
var trialFeedbackReceived=false;
var startingK = null;
var trial_choiceUp=null;
function after_trialRoutineBegin(){
	
	//BUG FIX
	STARTED=psychoJS.STARTED;
	
	//load the k value if it hasn't been already
	if(k_val==null){
		k_val = expInfo['k_val']*1
	}
	startingK=k_val;
	//alert(delaySS + ',' + amountSS + ',' + delayLL + ',' + amountLL);
	if(salienceCondition==SALIENCE_CONDITION_AMOUNT_SALIENT){
		SSamount=get_amountSS(k_val,SSdelay,LLdelay,LLamount);
	}else if (salienceCondition==SALIENCE_CONDITION_DELAY_SALIENT){
	//SSamount,LLamount,Condition,Choice,SSdelay,LLdelay
		//alert('calling delayll;' + SSdelay + ',' + SSamount + ',' + LLdelay + ',' + LLamount);
		LLdelay=get_delayLL(k_val,SSdelay,SSamount,LLamount);
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
	
	if(SSonLorR==1){
		tSSdelay=delay1;
		tLLdelay=delay2;
		tSSamount=amount1;
		tLLamount=amount2;
		//set the colors
        iOption1Background.setImage(psychoJS.resourceManager.getResource('images/redbg.png'));
        iOption2Background.setImage(psychoJS.resourceManager.getResource('images/bluebg.png'));
        //iOption1SelectedBg.setImage(psychoJS.resourceManager.getResource('images/red-highlight-bg.png'));
        //iOption2SelectedBg.setImage(psychoJS.resourceManager.getResource('images/blue-highlight-bg.png'));
	}else if (SSonLorR==2){
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
	

	
	tSSdelay.setText(Math.round(SSdelay,0) + " days");
    tLLdelay.setText(Math.round(LLdelay,0) + " days");
    tSSamount.setText("$" + parseFloat(SSamount).toFixed(2));
    tLLamount.setText("$" + parseFloat(LLamount).toFixed(2));
    
    //reset the "respond faster" label.
	showRespondFasterWarning=false;

    trialRoutine_end_t=6;
    
    trialFeedbackReceived=false;    
    trial_choiceUp = rTaskInstructionsClock.getTime();

}


function after_TrialRoutineEachFrame(){
		//function within function!!!
		function saveTrialValues(){
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['startingK']=startingK;
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['endingK']=endingK;
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['RT']=t;
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['choiceMade']=rTaskInstructionsClock.getTime();
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['choiceUp']=trial_choiceUp;
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['Choice']=trial_choice;
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['LLdelay']=LLdelay;
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['SSamount']=SSamount;
			trials_set1.trialList[trials_set1.nTotal-trials_set1.nRemaining]['SSonLorR']=SSonLorR;
			endingK=k_val;
		}
	//this is called every single screen frame.	
	if (theseKeys.length > 0 & t<itc_feedback_limit) {  // at least one key was pressed
		



		var trial_choice = null;
		
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
		//saveTrialValues();
		
		//recalculate k value, but only if we're not in a dominated condition.
		if (Condition==condition_STANDARD){
			k_val = increment_k_m(trial_choice,k_val);
		}
	}else if (theseKeys.length > 0 & t>=itc_feedback_limit){
		//a key was pressed but after the time limit; ignore the keypress!
		theseKeys=[]
		resp_trial.keys=[]
	}
	
	if(trial_choice!=null){
		//we have a choice; collect values!
		saveTrialValues();
	}

	


	//bring forward the end of the routine; we just need long enough to display feedback.	
	if(t>=trialRoutine_end_t){
		//this is the end! put anything involving ending the trial here.
		if (trialFeedbackReceived==false){
		//we reached here without getting feedback; save the trial values
			saveTrialValues();
		}
		continueRoutine=false;



		//trials_set1.addData('startingK',startingK);
		//trials_set1.addData('endingK',endingK);
		//trials_set1.trialListaddData('endingK'
		//resp_trial.rt
	}
	
	
	
	if(t>=itc_feedback_limit){
		//show the 'too slow' item.
		showRespondFasterWarning=true;
	}
	

        
	
}
function on_routine_end(choice){
	k_val = increment_k_m(choice,k_val)
}

function after_ITIfixRoutineEachFrame(){
	if(t>=ITI){
		continueRoutine=false;
	}
}

function after_rTaskIntervalRoutineEachFrame(){
	if(t>=ITI){
		continueRoutine=false;
	}
}


function run_replace_default_expInfo(){
	expInfo = {'participant':'', 'session':'1','run':'1',
	'designDir':'fmri_v120180206203544',
	'k_val':0.01};

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