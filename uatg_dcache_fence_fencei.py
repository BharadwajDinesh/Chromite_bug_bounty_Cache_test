from yapsy.IPlugin import IPlugin
from ruamel.yaml import YAML
import uatg.regex_formats as rf
from typing import Dict, List
import re
import os
import random	

class uatg_cache_dcache_fill_buffer(IPlugin):
    
    def __init__(self):
        super().__init__()

    def execute(self, core_yaml, isa_yaml):
        _dcache_dict = core_yaml['dcache_config']
        _dcache_en = _dcache_dict['instantiate']
        self._sets = _dcache_dict['sets']
        self._word_size = _dcache_dict['word_size']
        self._block_size = _dcache_dict['block_size']
        self._ways = _dcache_dict['ways']
        self._cache_size=_dcache_dict['cache_size']
        self._fb_size=_dcache_dict['fb_size']
        return True
    
    def check_log(self, log_file_path, reports_dir):
        return None
    
    def generate_covergroups(self, config_file):
        ''
    
    def generate_asm(self) -> List[Dict[str, str]]:
    
        asm_data = '\nrvtest_data:\n'

        for i in range (self._cache_size*4):
        	asm_data+=f"\t.word 0x{str(hex(random.randrange(16**8))[2:]).zfill(8)}\n"
            
        asm='\n\tfence\n'
        asm+='\n\tla t1,rvtest_data\t\n'
        
        for i in range(self._cache_size):
	        asm+=f'\n\tlw t0, 0(t1)\n\tli a1, {self._sets*self._block_size*self._word_size}\n\taddi t1, t1, a1\n'
        
        asm+='end:\t\n\tnop\n'
        
        asm+='\n\tfence.i\n'

        # compile macros for the test
        compile_macros=[]
        
        # return asm_code and sig_code
        test_dict.append({
            'asm_code': asm,
            'asm_data': asm_data,
            'asm_sig': '',
            'compile_macros': compile_macros
        })
        
        return test_dict