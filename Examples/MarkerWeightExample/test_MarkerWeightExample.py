

def test(anytest):
    macro = [[anytest.load_macro('Main.any')]]
    
    outputlist = anytest.app.start_macro(macro)
    
    anytest.check_output_log(outputlist)  
    
    