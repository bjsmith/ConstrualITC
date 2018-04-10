var CHOICE_SS=1;
var CHOICE_LL=2;
function get_delayLL(k_M,delaySS,amountSS,amountLL){
	return ((amountLL*((1+k_M*delaySS)/amountSS))-1)/k_M;
}

function get_amountSS(k_M,delaySS,delayLL,amountLL){
	return (amountL/(1 + k_M*delayL))*(1+k_M*delayS);
}

function increment_k_m(choice,old_k_M){
	if(choice==CHOICE_SS){
		k_M = old_k_M * 10^(1/8);
	}else if (choice==CHOICE_LL){
		k_M = old_k_M * 10^(-1/8);
	}else {
		alert("unknown choice type)")
	}
	return(k_M)
}

//OK now, I think we need to work out what the data structure looks like
//until we do that it's difficult to code the behavior.

//for now we can wo


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