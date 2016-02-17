from autoprotocol.util import make_dottable_dict

def bagel_assay(protocol, refs, params):
    refs = make_dottable_dict(refs)
    params = make_dottable_dict(params)

    if params.make_substrate:
        #thaw substrate tube
        protocol.incubate(refs.substrate, "ambient", params.thaw_time)

        # make substrate plate (might be useful to just make 144 of these,
        # freeze them, and have them ready, rather than storing frozen substrate
        protocol.distribute(refs.hepes.wells_from(0,7).set_volume('1000:microliter'),
            refs.substrate_plate.wells_from("B1", 84), "75:microliter",
            allow_carryover=True)
        protocol.distribute(refs.substrate.well(0),
            refs.substrate_plate.wells_from(0,12), '100:microliter',
            allow_carryover=True)
        
        # serial dilution
        for row in [0, 12, 24, 36, 48]:
            protocol.transfer(
                refs.substrate_plate.wells_from(row, 12),
                refs.substrate_plate.wells_from(row+12, 12),
                '25:microliter',
                mix_after=True,
                mix_vol="75:microliter",
                repetitions=2,
                flowrate="150:microliter/second")

        protocol.transfer(
            refs.substrate_plate.wells_from('F1', 12), refs.trash.wells_from('A1', 12),
            '25:microliter')

        # reference reads for later
        protocol.absorbance('substrate_plate',
            refs.substrate_plate.wells_from(0, 96), '420:nanometer', 'bg1')
        protocol.absorbance('substrate_plate',
            refs.substrate_plate.wells_from(0, 96), '420:nanometer', 'bg2')

    else:
        #thaw a pre-made 96-well substrate plate
        protocol.incubate('substrate_plate', 'ambient', '15:minute')

    #aliquot mutants
    for i,mutant in enumerate(params.mutants):
        protocol.distribute(mutant, refs.enzyme.wells_from(i*24, 24,
            columnwise=True), "25:microliter")

    # initiate reaction
    # how long will this take?
    # ideally < 100 s
    #protocol.transfer(
    #    refs.substrate_plate.all_wells(),
    #    refs.enzyme.all_wells(),
    #    '25:microliter',
    #    mix_after=True,
    #    mix_vol="25:microliter",
    #    repetitions=2, )
    protocol.stamp( substrate_plate, enzyme, '75:microliter' )
    
    # 20 reads
    for i in range(1,21):
        protocol.absorbance('enzyme', refs.enzyme.all_wells(),
            '420:nanometer', 'data%s' % i)
        protocol.incubate('enzyme', 'ambient', '30:second')


if __name__ == '__main__':
    from autoprotocol.harness import run
    run(bagel_assay)

