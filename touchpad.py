#!/usr/bin/python3
import os
import time
#xinput list

touchpad_word = "Touchpad"
len_with_touchpad = 4
touchpad_enabled = True

def get_id(text: str) -> int:
	text = text.split('\t')
	for did in text:
		if "id=" in did:
			return did[3:]
	return -1

def get_touchpad_id(arr) -> int:
	touchpad_id = -1
	for string in str_list:
		if touchpad_word in string:
			touchpad_id = get_id(string)
	return touchpad_id

while True:
	data = os.popen("xinput list")
	str_list = data.read().split("\n")
	data.close()
	cut_index = -1
	
	for i, string in enumerate(str_list):
		if "Virtual core keyboard" in string:
			cut_index = i
			break

	str_list = str_list[:cut_index]
	
	
	if len(str_list) != len_with_touchpad and touchpad_enabled:
		touchpad_id = get_touchpad_id(str_list)
		os.system(f"xinput set-prop {touchpad_id} \"Device Enabled\" 0")
		touchpad_enabled = False

	elif len(str_list) == len_with_touchpad and not touchpad_enabled:
		touchpad_id = get_touchpad_id(str_list)
		os.system(f"xinput set-prop {touchpad_id} \"Device Enabled\" 1")
		touchpad_enabled = True
		
	time.sleep(1)
