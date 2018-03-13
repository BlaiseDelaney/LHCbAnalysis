#include "Utils.h"

#include "RunEngine.h"
#include "Variables_Analysis.h"
#include "Plotter.h"
#include "BuRejectionBDT.h"

using namespace std;
using namespace Utils;

int main(int argc, char **argv) {

  // create run engine
  RunEngine runner("Bc2DmunuAnalysis", argc, argv);

  // create the variables
  Bc2Dmunu::Variables_Analysis *v = new Bc2Dmunu::Variables_Analysis() ;

  // make the analysers
  Bc2Dmunu::Plotter   *plotter       = new Bc2Dmunu::Plotter   ( "Plotter", v );
  Bc2Dmunu::BuRejectionBDT *bdtTrain = new Bc2Dmunu::BuRejectionBDT( "BDT", v );
  bdtTrain->setTrainMode();


  // pass variables to runner
  runner.setVariables( v );

  // pass analysers to runner
  runner.addAnalyser( plotter );
  runner.addAnalyser( bdtTrain );

  // run
  runner.run();

  // clean up
  delete v;
  delete plotter;
  delete bdtTrain;

  return 0;

}

