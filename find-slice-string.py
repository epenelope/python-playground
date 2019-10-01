#slices the number part of the string and converts it to a float before printing the output.

text = 'X-DSPAM-Confidence:    0.8475'
sp = text.find('0')
end = text.find('5')
num = text[sp:end+1]
print(float(num))

