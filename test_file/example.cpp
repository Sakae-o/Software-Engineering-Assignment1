#include <stdio.h>
int main(){
    int i=1;
	int jswitch=0;
	long f;
	switch(i){
		case 0:
		break;
		case 1:
			break;
		case 2:
			break;
		default:
			break;
	}
	switch(jswitch){
		case 0:
			break;
		case 1:
			break;
		default:
			break;
    }
	if(i<0){
		if(i<-1){}
		else{};
    }
	else if(i>0){
		if (i>2){}
		else if (i==2) {}
		else if (i>1) {}
		else {};
	}
	else{
		if(jswitch!=0){}
		else{} 
	}
	return 0;
}
