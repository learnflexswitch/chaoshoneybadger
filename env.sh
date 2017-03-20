if [ -z "$PYTHONPATH" ]; 
then
	 export PYTHONPATH=$SR_CODE_BASE/snaproute/src/flexSdk/py/:$SR_CODE_BASE/snaproute/src/test/tests/:$SR_CODE_BASE/snaproute/src/test/utils/:$SR_CODE_BASE/snaproute/src/test/setups/:$SR_CODE_BASE/snaproute/src/test/base/:$SR_CODE_BASE/snaproute/src/chaosmonkey/setups/:$SR_CODE_BASE/snaproute/src/chaosmonkey/base/
else 
	 export PYTHONPATH=$PYTHONPATH:$SR_CODE_BASE/snaproute/src/flexSdk/py/:$SR_CODE_BASE/snaproute/src/test/tests/:$SR_CODE_BASE/snaproute/src/test/utils/:$SR_CODE_BASE/snaproute/src/test/setups/:$SR_CODE_BASE/snaproute/src/test/base/:$SR_CODE_BASE/snaproute/src/chaosmonkey/setups/:$SR_CODE_BASE/snaproute/src/chaosmonkey/base/
fi;
