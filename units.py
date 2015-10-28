"""
Measurement units
"""

__all__ = [
        'capacity_units',
        'time_units'
          ]

capacity_units = {'Tbps': 10**12,        'Gbps': 10**9,      'Mbps': 10**6,      
                  'Kbps': 1000,          'kbps': 1000,       'bps': 1,
                  'Tbit/s': 10**12,      'Gbit/s': 10**9,    'Mbit/s': 10**6,    
                  'Kbit/s': 1000,        'kbit/s': 1000,     'bit/s': 1,
                  'Tb': 10**12,          'Gb': 10**9,        'Mb': 10**6,        
                  'Kb': 1000,            'kb': 1000,         'b': 1,
                  'TBps': 8*(10**12),    'GBps': 8*(10**9),  'MBps': 8*(10**6),  
                  'KBps': 8000,          'kBps': 8000,       'Bps': 8,
                  'TB/s': 8*(10**12),    'GB/s': 8*(10**9),  'MB/s': 8*(10**6),  
                  'KB/s': 8000,          'kB/s': 8000,       'B/s': 8,
                  'TB': 8*(10**12),      'GB': 8*(10**9),    'MB': 8*(10**6),    
                  'KB': 8000,            'kB': 8000,         'B': 8
                  }


time_units = {'minutes': 60*10**3,      'minute': 60*10**3,
              'min': 60*10**3,          'm': 60*10**3,
              'seconds': 10**3,         'second': 10**3,
              'sec': 10**3,             's': 10**3,
              'milliseconds': 1,        'millisecond': 1,
              'millisec': 1,            'ms': 1,
              'microseconds': 0.001,    'microsecond': 0.001,
              'microsec': 0.001,        'us': 0.001,
              'nanoseconds': 0.000001,  'nanosecond': 0.000001,
              'nanosec': 0.000001,      'ns': 0.000001
              }

