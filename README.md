# Chromite_bug_bounty_Cache_test
This repository contains the python scripts to generate RISC-V Assembly for testing the Cache subsystem in the Chromite Core by InCore Semiconductors.

This repository can be initialised as a submodule in chromite_uatg_tests.

## Test Description
- Fill the cache completely based on the size mentioned in the core64.yaml input.
- Try to fill the fill-buffer completely.
- Perform cache line thrashing
- Perform cache set thrashing
- Perform all possible types of load/store access (byte, hword, word, dword)
- Perform a load/store hit in the RAMS
- Perform a load/store hit in the Fill-buffer
- Perform an I/O operation
- Perform a store-to-load forwarding scenario from the store-buffer
- Perform a replacement on all sets.
- Check if fence and fence.iwork properly
- Check if performance counters are correctly incremented.
- Check to see if we can perform simultaneous io and cached ops

## File Structure
```
.
├── README.md -- Describes the Repo.
├── uatg_dcache_fill_fence_fencei.py -- Generates ASM to fill the Data Cache by performing consecutive stores at different address locations and check fence and fencei working.
├── uatg_dcache_fill_buffer.py -- Generates ASM to fill the Data Buffer by performing consecutive stores at different address locations.
├── uatg_dcache_fill_cache.py -- Generates ASM to fill the Data Cache by performing consecutive loads at different address locations.
```

## Code Description

#### uatg_dcache_fill_fence_fencei.py
- Perform a `fence` operation. 
- Load some data using numerous store operations to fill up the cache.
- Perform a `fence.i` operation.
#### uatg_dcache_fill_buffer.py
- Perform a `fence` operation. 
- Load some data using numerous store operations to fill up the cache.
- Clear the buffer
- Load some data into the buffer
#### uatg_dcache_fill_cache.py
- Perform a `fence` operation. 
- Load some data using numerous store operations to fill up the cache.

## Contributors
Pruthvi Raj S <<bharathd7900@gmail.com>>,
Bharadwaj D <<pruthvirajs@pesu.pes.edu>>

## Attribution
Ayush Mukherjee <<ayushrex007@gmail.com>>, Tejas Raj G R <<tejasraj40@gmail.com>>
