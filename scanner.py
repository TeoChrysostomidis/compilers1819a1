"""
Sample script to test ad-hoc scanning by table drive.
This accepts a number with optional decimal part [0-9]+(\.[0-9]+)?

NOTE: suitable for optional matches
"""

def getchar(text,pos):
	""" returns char category at position `pos` of `text`,
	or None if out of bounds """
	
	if pos<0 or pos>=len(text): return None
	
	c = text[pos]
	
	# **Σημείο #3**: Προαιρετικά, προσθέστε τις δικές σας ομαδοποιήσεις
	
	return c	# anything else
	


def scan(text,transitions,accepts):
	""" scans `text` while transitions exist in
	'transitions'. After that, if in a state belonging to
	`accepts`, it returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 's0'
	# memory for last seen accepting states
	last_token = None
	last_pos = None
	
	
	while True:
		
		c = getchar(text,pos)	# get next char (category)
		
		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char
			
			# remember if current state is accepting
			if state in accepts:
				last_token = accepts[state]
				last_pos = pos
			
		else:	# no transition found

			if last_token is not None:	# if an accepting state already met
				return last_token,last_pos
			
			# else, no accepting state met yet
			return 'ERROR_TOKEN',pos
			
	
# **Σημείο #1**: Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων
transitions = { 'S0': { 'DIG0':'S1','DIG1':'S1','DIG2':'S2','DIG3':'S2' },
       		'S1': { 'DIG0':'S3','DIG1':'S3','DIG2':'S3','DIG3':'S3','DIG4':'S3','DIG5':'S3','DIG6':'S3','DIG7':'S3','DIG8':'S3','DIG9':'S3' },
       		'S2': { 'DIG0':'S3','DIG1':'S3','DIG2':'S3','DIG3':'S3','DIG4':'S3','DIG5':'S3' },
       		'S3': { 'DIG0':'S4' },
	        'S4': { 'DIG0':'S5','DIG1':'S5','DIG2':'S5','DIG3':'S5','DIG4':'S5','DIG5':'S5','DIG6':'S5','DIG7':'S5','DIG8':'S5','DIG9':'S5' },
	        'S5': { 'DIG0':'S6','DIG1':'S6','DIG2':'S6','DIG3':'S6','DIG4':'S6','DIG5':'S6','DIG6':'S6','DIG7':'S6','DIG8':'S6','DIG9':'S6' },
	        'S6': { 'G':'S9','K':'S7','M':'S11' },
	        'S7': { 'T':'S8'},
	        'S9': { 'DIG0':'S10','DIG1':'S10','DIG2':'S10','DIG3':'S10','DIG4':'S10','DIG5':'S10','DIG6':'S10','DIG7':'S10','DIG8':'S10','DIG9':'S10' },
	        'S10': { 'DIG0':'S6','DIG1':'S6','DIG2':'S6','DIG3':'S6','DIG4':'S6','DIG5':'S6','DIG6':'S6','DIG7':'S6','DIG8':'S6','DIG9':'S6' },
	        'S11': { 'P':'S12'},
	        'S12': { 'S':'S8'}
     	      } 

# **Σημείο #2**: Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής
accepts = { 'S8':'WIND_TOKEN'
     	  }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:		# i.e. len(text)>0
	# get next token and position after last char recognized
	token,pos = scan(text,transitions,accepts)
	if token=='ERROR_TOKEN':
		print('unrecognized input at position',pos,'of',text)
		break
	print("token:",token,"text:",text[:pos])
	# new text for next scan
	text = text[pos:]
	
