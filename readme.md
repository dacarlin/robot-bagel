# Outline  

## Protein production

Transformation, growth (or grow from Kunkel glycerol stocks, workflow would be Kunkel, transform, selection plate, mail selection plate to Genscript, rec sequencing within 48 hours, grow appropriate clone)

Grow in triplicate (abstract away the idea of plates/wells?)

## Protein purification 

Lyse w/ BugBuster

Clarify supernatant 

Take off top half (pipet height will need to be set)

Apply to columns 

Wash columns 

Strongly advocating a column-based approach here! Will work a lot better than beads 

Elute 

Quantitate and run gel 

## Assay 

+ `kinetics.py` is the autoprotocol for the kinetic assay 
+ we will also want a thermal stability assay as well, easy, same as above except constant substrate concentration and extra thermal cycle step 

## Data analysis 

See `bagel-fitter` for automated data analysis of kinetic data 

See `bagel-thermostability` for automated analysis of thermal stability data 

