#Test
def test_HDL_analysis():
	from cholesterol_analysis import HDL_analysis
	answer = DHL_analysis(80)
	expected = "Normal"
	assert answer == expected