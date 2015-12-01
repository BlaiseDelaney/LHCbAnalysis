#include "TMath.h"
#include "TLorentzVector.h"

#include "Selection.h"

using namespace std;

Dst2D0pi::Selection::Selection(TString _name, Variables_Analysis *_v):
	Analyser(_name),
  v(_v)
{}

Dst2D0pi::Selection::~Selection(){}

bool Dst2D0pi::Selection::AnalyseEvent(){

  // -----------------------------------------------------------------------
  // do physics cuts here:
  //
  
  if ( ! v->Dst_L0HadronDecision_TOS             ||
       ! v->Dst_Hlt1CalibTrackingKPiDecision_TOS ||
       ! v->Dst_Hlt2CharmHadDstp2D0Pip_D02KmPip_LTUNBTurboDecision_TOS ) return false;
  
  if ( (v->Dst_M - v->D0_M) < 144.5 ) return false;
  if ( (v->Dst_M - v->D0_M) > 146.5 ) return false;
  
  if ( TMath::Abs( v->Dst_DIRA_OWNPV ) < 0.9999 ) return false;
  if ( v->D0_MINIPCHI2>9 ) return false;

	return true;
}
