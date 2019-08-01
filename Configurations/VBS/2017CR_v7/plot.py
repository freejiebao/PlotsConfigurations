# plot configuration



# groupPlot = {}
#
# Groups of samples to improve the plots (merge different sample during plot).
# If not defined, normal plots is used
#
Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=860

groupPlot['non-prompt']  = {
                  'nameHR' : 'non-Prompt',
                  'isSignal' : 0,
                  'color': Yellow,    # kYellow
                  'samples'  : ['Fake_lep']
              }


##Fake and prompt substraction
plot['Fake_lep']  = {
                  'color': Yellow,    # kYellow
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
              }

##Data

plot['DATA']  = {
                  'nameHR' : 'Data',
                  'color': 1 ,
                  'isSignal' : 0,
                  'isData'   : 1 ,
                  'isBlind'  : 1 ,
                  'scale'    : 1.0
              }



# additional options
legend['lumi'] = 'L = 41.5/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'
