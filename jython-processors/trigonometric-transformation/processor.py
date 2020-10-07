#Packages import
import math

#Parameters import :
periodic_column = params.get('periodic_column')
min_value = params.get('min_value')
max_value = params.get('max_value')
feature_period = math.fabs(min_value) + math.fabs(max_value)

#Production code :
def process(row):
    
    x = row[periodic_column]
    
    try:
        x = float(x)
        
        if x < 0 :
            x = feature_period + x
            
        arg_val = math.pi/2.0-(math.pi*x)/(feature_period/2.0)
        cos_val = math.cos(arg_val)
        sin_val = math.sin(arg_val)
        tan_val = math.tan(arg_val)
        log_message = None
        
    except TypeError as t:
        log_message = "TypeError : {0}".format(str(t.args))
        arg_val, cos_val, sin_val, tan_val  = None, None, None, None
    
    except ValueError as v:
        log_message = "ValueError : {0}".format(str(v.args))
        arg_val, cos_val, sin_val, tan_val  = None, None, None, None
    
    except Exception as e:
        if min_value == max_value : 
            log_message = "ERROR : Minimum and Maximum values must be different."
        else:
            log_message = "ERROR : "+str(e)
        arg_val, cos_val, sin_val, tan_val  = None, None, None, None
        
    row["{0}_arg".format(periodic_column)] = arg_val
    row["{0}_cos".format(periodic_column)] = cos_val
    row["{0}_sin".format(periodic_column)] = sin_val
    row["{0}_tan".format(periodic_column)] = tan_val
    row["log_message"] = log_message
    
    return row