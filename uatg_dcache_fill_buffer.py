from yapsy.IPlugin import IPlugin
from ruamel.yaml import YAML
import uatg.regex_formats as rf
from typing import Dict, List
import re
import os
import random	

class uatg_cache_fillbuffer_01(IPlugin):
    """
    The test is used to fill the fill buffer. 
    It uses consecutive load operations to do so.
    """

    def __init__(self):

        super().__init__()

    def execute(self, core_yaml, isa_yaml):
 
        _dcache_dict = core_yaml['dcache_configuration']
        _dcache_en = _dcache_dict['instantiate']
        self._sets = _dcache_dict['sets']
        self._word_size = _dcache_dict['word_size']
        self._block_size = _dcache_dict['block_size']
        self._ways = _dcache_dict['ways']
        self._cache_size=self._sets*self._ways*self._block_size
        self._fb_size=_dcache_dict['fb_size']
        return True

    def generate_asm(self) -> List[Dict[str, str]]:
        """
        This method returns a string of the ASM file to be generated.

        This ASM file is written as the ASM file which will be run on the DUT.
        """
        asm_data = '\nrvtest_data:\n'

        for i in range (self._cache_size*4):
        	val=str(hex(int(random.uniform(0,self._cache_size*4)))[2:].zfill(8))    #for generating a random hex value
        	asm_data+=f"\t.word 0x{val}\n" 						#for naturally aligned 4-bytes or 32-bit comma separated words

	#clear the cache using fence
        asm='init:\n\tfence\n\tla t1, rvtest_data\t\n'  #load the address of rvtest_data into the t1 register
        
        #fills the cache	
        asm+='fillc:'
        for i in range(self._cache_size):
	        asm+=f'\n\tlw t0, 0(t1)\n\taddi t1, t1, {self._sets*self._block_size*self._word_size}\n'
        
        asm+='clearfb:'
        for i in range(70):
            asm+='\n\tnop\n'  #A series of 70 nops is done to clear the fill buffer.

        asm+='fillfb:'
        for i in range(self._fb_size+10):
            asm+=f'\n\taddi t1, t1, 32\n\tlw t0, 0(t1)\n'


        asm+='end:\n\tnop\n'


        return [{
            'asm_code': asm,
            'asm_data': asm_data,
            'asm_sig': '',
            'compile_macros': []
        }]

    def check_log(self, log_file_path, reports_dir):
        return None

    def generate_covergroups(self, config_file):
        return ''


        
